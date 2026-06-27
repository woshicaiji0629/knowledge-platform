应对流量高峰。 | [开启带宽弹性伸缩](../user-guide/enable-bandwidth-auto-scaling.md) |
| 开启/关闭自动扩容 | 当内存平均使用率达到阈值后会自动升级 Redis 实例的规格，帮助您快速弹性适配业务高峰，规避内存溢出的风险。 | [开启自动扩容](../user-guide/enable-automatic-scale-up.md) |  |
| 无感扩缩容 | 实例扩容过程可实现客户端无感知、不闪断、无只读状态，满足随时弹性资源伸缩需求。 | [Tair](imperceptible-scaling.md) [集群无感扩缩容介绍](imperceptible-scaling.md) |  |
| 性能优化 | 代理查询缓存 | 支持代理查询缓存（Proxy Query Cache）功能，启用后，代理节点会缓存热点 Key 对应的请求和查询结果。 | [通过](../user-guide/use-read-write-splitting-to-mitigate-issues-caused-by-hotkeys.md) [Proxy Query Cache](../user-guide/use-read-write-splitting-to-mitigate-issues-caused-by-hotkeys.md) [优化热点](../user-guide/use-read-write-splitting-to-mitigate-issues-caused-by-hotkeys.md) [Key](../user-guide/use-read-write-splitting-to-mitigate-issues-caused-by-hotkeys.md) [问题](../user-guide/use-read-write-splitting-to-mitigate-issues-caused-by-hotkeys.md) |
| 日志管理 | 审计日志 | 支持开通、查询、下载审计日志。 | [审计日志](../audit-logs.md) |
| 查询慢日志 | 支持查询数据节点、代理节点慢日志。 | [查询慢日志](../user-guide/view-slow-logs.md) |  |
| 查询运行日志 | 支持查询实例的运行日志。 | [查询运行日志](../user-guide/view-active-logs.md) |  |
| 事件管理 | 修改运维事件计划时间 | 支持在可运维时间执行运维计划，支持修改可运维时间点。 | [修改运维事件计划切换时间](../developer-reference/api-r-kvstore-2015-01-01-modifyactiveoperatio
