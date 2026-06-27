求预建索引，用户无需额外配置即可直接查询。以下两类日志构成了自定义分析的核心数据源：
Session 日志— 记录 Agent 的完整业务行为，是安全审计与成本分析的主要依据。即在[步骤一：日志接入（以 Session 日志为例）](enable-managed-openclaw-with-sls.md)中接入的日志。

| 字段路径 | 类型 | 审计分析用途 |
| --- | --- | --- |
| __tag__:__session_id__ | text | 会话唯一标识，按会话隔离与聚合的关键字段 |
| type | text | 条目类型： session （会话元数据）/ message （对话消息）/ compaction （上下文压缩摘要），过滤出可审计的对话记录 |
| message.role | text | 消息角色： user （用户输入）/ assistant （模型响应）/ toolResult （工具返回），定位行为主体 |
| message.content | text | 消息正文，涵盖用户输入、模型输出与工具参数/返回值，支撑注入检测、敏感数据匹配与全文检索 |
| message.provider message.model | text | 模型提供方与模型名称，用于成本分析与按模型维度的行为统计 |
| message.usage.totalTokens message.usage.cost.total | long / double | Token 用量与估算成本，用于异常消耗检测与会话级成本排序 |
| message.stopReason | text | 响应终止原因： stop （正常结束）、 toolUse （触发工具调用，下一条通常为 toolResult）、 error / aborted / timeout （异常终止），筛选异常会话的关键字段 |
| message.toolName message.isError | text / bool | 工具调用名称与执行状态，配合 toolResult 角色做工具级审计 |
| id 、 parentId | text | 条目 ID 与父 ID，用于构建对话树、还原消息顺序； session 类型条目的 id 即为 sessionId |
| timestamp | text | 事件时间戳，用于时间窗口过滤、排序与告警范围界定 |

Runtime 日志— 记录网关与各子系统的运行状态，是排障与系统健康分析的数据基础。
说明
选择OpenClaw-运行时日志卡片并参考[步骤一：日志接入（以 Session 日志为例）](enable-managed-openclaw-with-sls.md)进行接入。
