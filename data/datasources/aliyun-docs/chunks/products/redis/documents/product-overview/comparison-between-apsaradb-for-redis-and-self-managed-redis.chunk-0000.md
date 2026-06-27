| 对比项 | 云数据库 Tair（兼容 Redis） | 自建 Redis |
| --- | --- | --- |
| 安全防护 | 事前防护： VPC 网络隔离。 [白名单控制访问](../getting-started/step-2-configure-whitelists.md) 。 [自定义账号与权限](../user-guide/create-and-manage-database-accounts.md) 。 | 事前防护： 需自行构建网络安全体系，成本高，难度大。 Redis 的默认访问配置存在安全漏洞，可能导致 Redis 数据泄露。 无账号鉴权体系。 |
| 事中保护： [TLS](../user-guide/enable-tls-encryption.md) [加密](../user-guide/enable-tls-encryption.md) 。 | 事中保护：需要自行通过第三方工具实现 SSL 加密访问。 |  |
| 事后审计： [审计日志](../user-guide/view-audit-logs.md) 。 | 事后审计：无审计功能。 |  |
| 备份恢复 | Tair（企业版） [内存型](dram-based-instances.md) 支持数据闪回功能，可以恢复指定时间点的数据。更多信息，请参见 [通过数据闪回按时间点恢复数据](../user-guide/use-data-flashback-to-restore-data-by-point-in-time.md) 。 | 仅支持一次性全量恢复。 |
| 运维管理 | 支持十余组监控指标，最小监控粒度为 5 秒。更多信息，请参见 [监控指标说明](../user-guide/metrics.md) 。 支持 [报警设置](../user-guide/alert-settings.md) 。 可根据需求创建多种架构的实例，支持变配到其它架构和规格。 提供基于快照的大 key 分析功能，精度高，无性能损耗。更多信息，请参见 [离线全量](../user-guide/offline-key-analysis.md) [Key](../user-guide/offline-key-analysis.md) [分析](../user-guide/offline-key-analysis.md) 。 | 需使用管理方式复杂的第三方监控工具实现服务监控。 改变规格或架构的操作复杂，且需要停止服务。 支持基于采样的大 key 分析，统计粗糙，精度较低。 |
| 部署和扩容 | 即时开通，弹性扩容。 | 需要自行完成采购硬件、机房托管、部署机器等工作，周期较长，且需要自行维护节点关系。 |
| 高可用 | [单可用区高可用方案](disaster-recovery.md) 。
