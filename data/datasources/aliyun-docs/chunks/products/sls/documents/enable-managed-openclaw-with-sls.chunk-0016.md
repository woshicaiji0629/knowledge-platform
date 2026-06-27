戳，用于时间窗口过滤、排序与告警范围界定 |

Runtime 日志— 记录网关与各子系统的运行状态，是排障与系统健康分析的数据基础。
说明
选择OpenClaw-运行时日志卡片并参考[步骤一：日志接入（以 Session 日志为例）](enable-managed-openclaw-with-sls.md)进行接入。

| 字段路径 | 类型 | 审计分析用途 |
| --- | --- | --- |
| _meta.logLevelName | text | 日志级别（TRACE / DEBUG / INFO / WARN / ERROR / FATAL），聚焦 ERROR 与 FATAL 做异常排查 |
| _meta.path | text | 源码文件路径与行号，精确关联代码位置，便于堆栈分析 |
| 数字键 "0" | object（JSON） | 结构化上下文，通常包含 subsystem 字段（如 gateway / channels / telegram / plugins ） |
| 数字键 "1" 及后续 | text | 日志消息正文与堆栈内容，支持全文检索与关键字匹配 |
