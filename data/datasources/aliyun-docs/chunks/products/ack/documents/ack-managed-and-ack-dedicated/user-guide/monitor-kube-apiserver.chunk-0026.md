### 准入Webhook时延
情况说明

| 正常情况 | 异常情况 | 说明 |
| --- | --- | --- |
| 准入 Webhook 时延 小于 0.5s。 | 持续出现 准入 Webhook 时延 大于 0.5s。 | Webhook 响应慢会影响 API Server 的响应时延。 |

推荐解决方案
排查Webhook日志等信息，判断是否符合预期。如果不需要某个Webhook，请卸载。
