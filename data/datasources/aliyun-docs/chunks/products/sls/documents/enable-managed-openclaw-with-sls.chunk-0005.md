### 可观测三支柱在 AI Agent 下的映射
可观测性建立在Logs + Metrics + Traces三支柱之上，在 OpenClaw 场景下，三者与数据源的对应关系及各自要回答的核心问题如下：

| 支柱 | OpenClaw 数据源 | 回答的核心问题 |
| --- | --- | --- |
| Logs（Session 审计日志） | ~/.openclaw/agents/<id>/sessions/*.jsonl | Agent 做了什么 ？调用了哪些工具？消耗了多少 Token、多少成本？ |
| Logs（应用运行日志） | /tmp/openclaw/openclaw-YYYY-MM-DD.log | 系统 哪里出了问题 ？Webhook 失败、认证被拒、网关异常？ |
| Metrics | diagnostics-otel 插件 OTLP 输出 | 当前 成本与延迟是否正常？有无会话卡死、异常重试？ |
| Traces | diagnostics-otel 插件 OTLP 输出 | 单条消息从接收到完整响应 经历了哪些步骤 ？调用链如何串起？ |

三支柱缺一不可：仅有 Metrics 无法回答“谁、因何”导致成本飙升；仅有 Session 日志无法从全局感知系统健康与异常拐点；仅有应用运行日志则看不到 Agent 的业务行为与工具调用序列。三者协同才能同时支撑安全审计、成本管控与运维排障。
