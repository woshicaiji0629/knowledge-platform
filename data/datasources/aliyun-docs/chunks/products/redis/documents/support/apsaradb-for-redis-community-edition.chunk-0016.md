| 安全加固 | 增强稳定性。 |
| 6.0.1.23 | LOW | 2022-09-20 | 功能优化 | 审计日志新增记录过期删除事件。 审计日志不再记录 PING、AUTH、SELECT 等非写命令。 |
| 6.0.1.22 | LOW | 2022-09-13 | 功能优化 | 优化集群架构实例连接数耗尽后的处理方式。 |
| 6.0.1.21 | LOW | 2022-08-30 | 功能优化 | 优化集群架构实例的启动流程。 |
| 6.0.1.20 | LOW | 2022-06-28 | 功能优化 | 修复 ZUNIONSTORE 和 ZINTERSTORE 等命令在集群代理模式下报错的问题。 |
| 6.0.1.19 | LOW | 2022-06-22 | 功能优化 | 优化延迟统计直方图，详情请参见 [时延洞察](../user-guide/latency-insights.md) 。 |
| 安全加固 | 升级、优化集群架构增、删节点流程，详情请参见 [调整集群分片数](../user-guide/adjust-the-number-of-cluster-shards.md) 。 |  |  |  |
| 6.0.1.18 | LOW | 2022-05-17 | 功能优化 | 删除 INFO 命令返回的 Errorstats - Selected 字段。 |
| 6.0.1.17 | LOW | 2022-05-10 | 功能优化 | 集群架构支持 MOVE 命令。 |
| 6.0.1.16 | MEDIUM | 2022-04-25 | 安全加固 | 优化升级集群架构增、删节点流程，增强稳定性。 |
| 6.0.1.15 | LOW | 2022-03-24 | 新特性 | 支持延时统计直方图（Latency），详情请参见 [时延洞察](../user-guide/latency-insights.md) 。 支持 INFO 命令返回 Errorstats（Redis 错误统计）信息。 |
| 6.0.1.14 | LOW | 2022-02-21 | 功能优化 | 支持 READONLY、READWRITE 命令，详情请参见 [Redis](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md) [开源版命令支持](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md) 。 |
| 6.0.1.13 | LOW | 2022-01-14 | 功能优化 | 增加 DB 元数据监控项：占用内存。 优
