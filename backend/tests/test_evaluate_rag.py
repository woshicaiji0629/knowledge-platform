from pathlib import Path

import pytest

from knowledge_platform.scripts.evaluate_rag import (
    EvalResult,
    evaluate_citation_quality,
    load_eval_cases,
    markdown_report,
)


def test_load_eval_cases(tmp_path: Path) -> None:
    questions_path = tmp_path / "questions.jsonl"
    questions_path.write_text(
        (
            '{"id":"ecs-sizing","product":"ECS","product_filter":"ecs",'
            '"question":"ECS 怎么选型？","tags":["compute"]}\n'
        ),
        encoding="utf-8",
    )

    cases = load_eval_cases(questions_path)

    assert len(cases) == 1
    assert cases[0].id == "ecs-sizing"
    assert cases[0].question == "ECS 怎么选型？"
    assert cases[0].product_filter == "ecs"
    assert cases[0].tags == ["compute"]


def test_load_eval_cases_rejects_missing_question(tmp_path: Path) -> None:
    questions_path = tmp_path / "questions.jsonl"
    questions_path.write_text('{"id":"bad"}\n', encoding="utf-8")

    with pytest.raises(ValueError, match="missing string question"):
        load_eval_cases(questions_path)


def test_markdown_report_includes_answers_and_citations() -> None:
    report = markdown_report(
        [
            EvalResult(
                id="ecs-sizing",
                question="ECS 怎么选型？",
                product="ECS",
                product_filter="ecs",
                tags=["compute"],
                answer="根据业务负载选择实例规格。",
                citations=[
                    {
                        "title": "实例规格选型方法",
                        "url": "https://help.aliyun.com/ecs",
                        "source": "aliyun_docs",
                        "score": 0.9,
                    }
                ],
                context_chars=100,
                duration_ms=123,
            )
        ]
    )

    assert "# RAG Evaluation Report" in report
    assert "product_filter: ecs" in report
    assert "根据业务负载选择实例规格。" in report
    assert "实例规格选型方法" in report
    assert "## Quality Summary" in report
    assert "| ecs-sizing | ecs | 1 | 0 | 0 | 0 | 0.0000 | 0.0000 | - |" in report


def test_evaluate_citation_quality_counts_target_product_citations() -> None:
    quality = evaluate_citation_quality(
        citations=[
            {
                "title": "什么是 ECS",
                "url": "https://help.aliyun.com/zh/ecs/product-overview",
                "source": "aliyun_docs",
                "score": 0.8,
            },
            {
                "title": "ECS 计费",
                "url": "https://help.aliyun.com/zh/ecs/billing",
                "source": "aliyun_docs",
                "score": 0.7,
            },
        ],
        product_filter="ecs",
    )

    assert quality.target_product_citations == 2
    assert quality.off_product_citations == 0
    assert quality.top_score == 0.8
    assert quality.avg_score == 0.75
    assert quality.warnings == []


def test_evaluate_citation_quality_warns_for_off_product_and_interface_reference() -> None:
    quality = evaluate_citation_quality(
        citations=[
            {
                "title": "API参考",
                "url": "https://help.aliyun.com/zh/rds/developer-reference/api-create",
                "source": "aliyun_docs",
                "score": 0.4,
            }
        ],
        product_filter="ecs",
        low_score_threshold=0.55,
    )

    assert quality.target_product_citations == 0
    assert quality.off_product_citations == 1
    assert quality.interface_reference_citations == 1
    assert quality.warnings == ["off_product_citations", "interface_reference_citations", "low_top_score"]
