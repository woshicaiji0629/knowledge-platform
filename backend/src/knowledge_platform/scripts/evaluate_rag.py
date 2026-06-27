import argparse
import asyncio
import json
import time
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Literal, cast

from knowledge_platform.embeddings.dashscope import DashScopeEmbeddingProvider, dashscope_config_from_env
from knowledge_platform.llm.answer import (
    AnswerGenerationRequest,
    AnswerGeneratorProtocol,
    DashScopeAnswerGenerator,
    SkeletonAnswerGenerator,
    dashscope_chat_config_from_env,
)
from knowledge_platform.services.retrieval_service import QdrantRetrievalService, RetrievalContext
from knowledge_platform.sessions.models import Citation
from knowledge_platform.vectorstores.qdrant import QdrantConfig, QdrantVectorStore


@dataclass(frozen=True)
class EvalCase:
    id: str
    question: str
    product: str = ""
    product_filter: str = ""
    tags: list[str] | None = None


@dataclass(frozen=True)
class EvalResult:
    id: str
    question: str
    product: str
    product_filter: str
    tags: list[str]
    answer: str
    citations: list[dict[str, str | float]]
    context_chars: int
    duration_ms: int
    target_product_citations: int = 0
    off_product_citations: int = 0
    interface_reference_citations: int = 0
    top_score: float = 0.0
    avg_score: float = 0.0
    quality_warnings: list[str] | None = None
    error: str = ""


@dataclass(frozen=True)
class CitationQuality:
    target_product_citations: int
    off_product_citations: int
    interface_reference_citations: int
    top_score: float
    avg_score: float
    warnings: list[str]


INTERFACE_REFERENCE_PATTERNS = [
    "api-reference",
    "developer-reference",
    "sdk-reference",
    "openapi",
    "list-of-operations",
    "api参考",
    "sdk参考",
    "接口调用",
]

DEFAULT_LOW_SCORE_THRESHOLD = 0.55


def main() -> None:
    asyncio.run(_main_async())


async def _main_async() -> None:
    args = _parse_args()
    cases = load_eval_cases(Path(args.questions_path))
    if args.limit is not None:
        cases = cases[: args.limit]

    retrieval_service = QdrantRetrievalService(
        embedding_provider=DashScopeEmbeddingProvider(config=dashscope_config_from_env()),
        vector_store=QdrantVectorStore(
            config=QdrantConfig(
                endpoint=args.qdrant_endpoint,
                collection_name=args.collection,
                timeout_seconds=args.qdrant_timeout_seconds,
            )
        ),
        default_limit=args.top_k,
        context_max_chars=args.context_max_chars,
    )
    answer_generator = _answer_generator(args.answer_provider)

    semaphore = asyncio.Semaphore(args.concurrency)
    tasks = [
        _evaluate_case(
            case=case,
            retrieval_service=retrieval_service,
            answer_generator=answer_generator,
            semaphore=semaphore,
            low_score_threshold=args.low_score_threshold,
        )
        for case in cases
    ]
    results: list[EvalResult] = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
        status = "ERROR" if result.error else "OK"
        print(f"{status} {result.id} citations={len(result.citations)} duration_ms={result.duration_ms}")

    results.sort(key=lambda result: _case_order(cases, result.id))
    report_jsonl_path = _output_path(args.report_jsonl, suffix=".jsonl")
    report_markdown_path = _output_path(args.report_markdown, suffix=".md")
    write_jsonl_report(report_jsonl_path, results)
    write_markdown_report(report_markdown_path, results)
    print(f"jsonl_report: {report_jsonl_path}")
    print(f"markdown_report: {report_markdown_path}")


def load_eval_cases(path: Path) -> list[EvalCase]:
    cases: list[EvalCase] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        raw_case = json.loads(line)
        if not isinstance(raw_case, dict):
            raise ValueError(f"Eval case line {line_number} must be a JSON object")
        case_data = cast(dict[object, object], raw_case)
        case_id = case_data.get("id")
        question = case_data.get("question")
        product = case_data.get("product", "")
        product_filter = case_data.get("product_filter", "")
        tags = case_data.get("tags")
        if not isinstance(case_id, str) or not case_id:
            raise ValueError(f"Eval case line {line_number} missing string id")
        if not isinstance(question, str) or not question:
            raise ValueError(f"Eval case line {line_number} missing string question")
        if not isinstance(product, str):
            raise ValueError(f"Eval case line {line_number} product must be a string")
        if not isinstance(product_filter, str):
            raise ValueError(f"Eval case line {line_number} product_filter must be a string")
        if tags is not None and (
            not isinstance(tags, list) or any(not isinstance(tag, str) for tag in cast(list[object], tags))
        ):
            raise ValueError(f"Eval case line {line_number} tags must be a string list")
        cases.append(
            EvalCase(
                id=case_id,
                question=question,
                product=product,
                product_filter=product_filter,
                tags=cast(list[str] | None, tags),
            )
        )
    return cases


def write_jsonl_report(path: Path, results: list[EvalResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(asdict(result), ensure_ascii=False) for result in results]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_markdown_report(path: Path, results: list[EvalResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown_report(results), encoding="utf-8")


def markdown_report(results: list[EvalResult]) -> str:
    success_count = sum(1 for result in results if not result.error)
    lines = [
        "# RAG Evaluation Report",
        "",
        f"- cases: {len(results)}",
        f"- succeeded: {success_count}",
        f"- failed: {len(results) - success_count}",
        "",
        "## Quality Summary",
        "",
        "| case | product_filter | citations | target | off_product | interface_refs | "
        "top_score | avg_score | warnings |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for result in results:
        warnings = ", ".join(result.quality_warnings or []) or "-"
        lines.append(
            "| "
            f"{result.id} | "
            f"{result.product_filter or '-'} | "
            f"{len(result.citations)} | "
            f"{result.target_product_citations} | "
            f"{result.off_product_citations} | "
            f"{result.interface_reference_citations} | "
            f"{result.top_score:.4f} | "
            f"{result.avg_score:.4f} | "
            f"{warnings} |"
        )
    lines.append("")
    for result in results:
        lines.extend(
            [
                f"## {result.id}",
                "",
                f"- product: {result.product or '-'}",
                f"- product_filter: {result.product_filter or '-'}",
                f"- question: {result.question}",
                f"- duration_ms: {result.duration_ms}",
                f"- context_chars: {result.context_chars}",
                f"- citations: {len(result.citations)}",
                "",
            ]
        )
        if result.error:
            lines.extend(["**Error**", "", result.error, ""])
            continue
        lines.extend(["**Answer**", "", result.answer, "", "**Citations**", ""])
        for index, citation in enumerate(result.citations, start=1):
            title = citation.get("title", "")
            url = citation.get("url", "")
            score = citation.get("score", 0.0)
            lines.append(f"{index}. {title} ({score}) {url}")
        lines.append("")
    return "\n".join(lines)


async def _evaluate_case(
    case: EvalCase,
    retrieval_service: QdrantRetrievalService,
    answer_generator: AnswerGeneratorProtocol,
    semaphore: asyncio.Semaphore,
    low_score_threshold: float,
) -> EvalResult:
    async with semaphore:
        started_at = time.perf_counter()
        try:
            retrieval_context = await retrieval_service.retrieve(
                query=case.question,
                product_filter=case.product_filter or None,
            )
            answer = await answer_generator.generate(
                AnswerGenerationRequest(
                    question=case.question,
                    context_text=retrieval_context.context_text,
                    citations=retrieval_context.citations,
                )
            )
            return _success_result(
                case=case,
                retrieval_context=retrieval_context,
                answer=answer,
                duration_ms=_duration_ms(started_at),
                low_score_threshold=low_score_threshold,
            )
        except Exception as error:
            return EvalResult(
                id=case.id,
                question=case.question,
                product=case.product,
                product_filter=case.product_filter,
                tags=case.tags or [],
                answer="",
                citations=[],
                context_chars=0,
                duration_ms=_duration_ms(started_at),
                quality_warnings=["error"],
                error=str(error),
            )


def _success_result(
    case: EvalCase,
    retrieval_context: RetrievalContext,
    answer: str,
    duration_ms: int,
    low_score_threshold: float,
) -> EvalResult:
    citations = [_citation_dict(citation) for citation in retrieval_context.citations]
    citation_quality = evaluate_citation_quality(
        citations=citations,
        product_filter=case.product_filter,
        low_score_threshold=low_score_threshold,
    )
    return EvalResult(
        id=case.id,
        question=case.question,
        product=case.product,
        product_filter=case.product_filter,
        tags=case.tags or [],
        answer=answer,
        citations=citations,
        context_chars=len(retrieval_context.context_text),
        duration_ms=duration_ms,
        target_product_citations=citation_quality.target_product_citations,
        off_product_citations=citation_quality.off_product_citations,
        interface_reference_citations=citation_quality.interface_reference_citations,
        top_score=citation_quality.top_score,
        avg_score=citation_quality.avg_score,
        quality_warnings=citation_quality.warnings,
    )


def _citation_dict(citation: Citation) -> dict[str, str | float]:
    return {
        "title": citation.title,
        "url": citation.url,
        "source": citation.source,
        "score": citation.score,
    }


def evaluate_citation_quality(
    citations: list[dict[str, str | float]],
    product_filter: str,
    low_score_threshold: float = DEFAULT_LOW_SCORE_THRESHOLD,
) -> CitationQuality:
    scores = [_citation_score(citation) for citation in citations]
    top_score = max(scores, default=0.0)
    avg_score = round(sum(scores) / len(scores), 6) if scores else 0.0
    target_product_citations = sum(1 for citation in citations if _is_target_product_citation(citation, product_filter))
    off_product_citations = len(citations) - target_product_citations if product_filter else 0
    interface_reference_citations = sum(1 for citation in citations if _is_interface_reference_citation(citation))

    warnings: list[str] = []
    if not citations:
        warnings.append("no_citations")
    if off_product_citations > 0:
        warnings.append("off_product_citations")
    if interface_reference_citations > 0:
        warnings.append("interface_reference_citations")
    if citations and top_score < low_score_threshold:
        warnings.append("low_top_score")

    return CitationQuality(
        target_product_citations=target_product_citations,
        off_product_citations=off_product_citations,
        interface_reference_citations=interface_reference_citations,
        top_score=round(top_score, 6),
        avg_score=avg_score,
        warnings=warnings,
    )


def _is_target_product_citation(citation: dict[str, str | float], product_filter: str) -> bool:
    if not product_filter:
        return False
    url = str(citation.get("url", "")).lower()
    return f"/zh/{product_filter.lower()}/" in url


def _is_interface_reference_citation(citation: dict[str, str | float]) -> bool:
    text = " ".join(str(citation.get(key, "")) for key in ("title", "url")).lower()
    return any(pattern in text for pattern in INTERFACE_REFERENCE_PATTERNS)


def _citation_score(citation: dict[str, str | float]) -> float:
    score = citation.get("score", 0.0)
    if isinstance(score, int | float):
        return float(score)
    return 0.0


def _answer_generator(provider: Literal["dashscope", "skeleton"]) -> AnswerGeneratorProtocol:
    if provider == "dashscope":
        return DashScopeAnswerGenerator(config=dashscope_chat_config_from_env())
    return SkeletonAnswerGenerator()


def _parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[4]
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    default_report_root = repo_root / "runtime-data" / "evals" / timestamp
    parser = argparse.ArgumentParser(description="Evaluate RAG answers for Aliyun product-oriented questions.")
    parser.add_argument(
        "--questions-path",
        default=str(repo_root / "backend" / "evals" / "aliyun_product_questions.jsonl"),
        help="JSONL eval cases. Each line must include id and question.",
    )
    parser.add_argument("--collection", default="aliyun_docs_product_v1", help="Qdrant collection name.")
    parser.add_argument("--qdrant-endpoint", default="http://localhost:6333", help="Qdrant HTTP endpoint.")
    parser.add_argument("--qdrant-timeout-seconds", type=float, default=30.0, help="Qdrant request timeout.")
    parser.add_argument("--top-k", type=int, default=5, help="Retrieval result count per question.")
    parser.add_argument("--context-max-chars", type=int, default=6000, help="Max retrieved context characters.")
    parser.add_argument("--concurrency", type=int, default=2, help="Concurrent eval cases.")
    parser.add_argument("--limit", type=int, default=None, help="Optional maximum eval cases.")
    parser.add_argument(
        "--answer-provider",
        choices=["dashscope", "skeleton"],
        default="dashscope",
        help="Use skeleton to evaluate retrieval without paid answer generation.",
    )
    parser.add_argument(
        "--low-score-threshold",
        type=float,
        default=DEFAULT_LOW_SCORE_THRESHOLD,
        help="Warn when a case has citations but the top retrieval score is below this threshold.",
    )
    parser.add_argument("--report-jsonl", default=str(default_report_root / "results.jsonl"), help="JSONL report path.")
    parser.add_argument(
        "--report-markdown",
        default=str(default_report_root / "report.md"),
        help="Markdown report path.",
    )
    return parser.parse_args()


def _case_order(cases: list[EvalCase], case_id: str) -> int:
    for index, case in enumerate(cases):
        if case.id == case_id:
            return index
    return len(cases)


def _output_path(value: str, suffix: str) -> Path:
    path = Path(value)
    if path.suffix != suffix:
        raise ValueError(f"Report path must end with {suffix}: {path}")
    return path


def _duration_ms(started_at: float) -> int:
    return round((time.perf_counter() - started_at) * 1000)


if __name__ == "__main__":
    main()
