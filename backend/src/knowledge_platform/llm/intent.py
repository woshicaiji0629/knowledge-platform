from dataclasses import dataclass
from enum import StrEnum


class Intent(StrEnum):
    DOC_QA = "doc_qa"
    TROUBLESHOOTING = "troubleshooting"
    HOW_TO = "how_to"
    GENERAL = "general"


@dataclass(frozen=True)
class IntentResult:
    intent: Intent
    confidence: float
    reason: str


class RuleBasedIntentClassifier:
    def classify(self, message: str) -> IntentResult:
        normalized_message = message.strip().lower()
        if any(keyword in normalized_message for keyword in ["报错", "错误", "失败", "error", "fail"]):
            return IntentResult(intent=Intent.TROUBLESHOOTING, confidence=0.72, reason="matched troubleshooting keyword")
        if any(keyword in normalized_message for keyword in ["怎么", "如何", "步骤", "how to"]):
            return IntentResult(intent=Intent.HOW_TO, confidence=0.68, reason="matched how-to keyword")
        if any(keyword in normalized_message for keyword in ["文档", "api", "配置", "参数", "aliyun", "阿里云"]):
            return IntentResult(intent=Intent.DOC_QA, confidence=0.64, reason="matched documentation keyword")
        return IntentResult(intent=Intent.GENERAL, confidence=0.5, reason="fallback intent")
