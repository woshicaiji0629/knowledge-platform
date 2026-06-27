from pathlib import Path

import pytest

from knowledge_platform.scripts.evaluate_rag import EvalResult, load_eval_cases, markdown_report


def test_load_eval_cases(tmp_path: Path) -> None:
    questions_path = tmp_path / "questions.jsonl"
    questions_path.write_text(
        '{"id":"ecs-sizing","product":"ECS","question":"ECS 怎么选型？","tags":["compute"]}\n',
        encoding="utf-8",
    )

    cases = load_eval_cases(questions_path)

    assert len(cases) == 1
    assert cases[0].id == "ecs-sizing"
    assert cases[0].question == "ECS 怎么选型？"
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
    assert "根据业务负载选择实例规格。" in report
    assert "实例规格选型方法" in report
