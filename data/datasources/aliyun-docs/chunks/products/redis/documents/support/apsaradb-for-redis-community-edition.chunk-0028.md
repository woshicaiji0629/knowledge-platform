ree-access.md) [VPC](../user-guide/enable-password-free-access.md) [免密访问](../user-guide/enable-password-free-access.md) 的场景下，申请公网连接地址的操作。 |
| 1.8.0 | HIGH | 2020-01-16 | 新特性 | 支持实时热点 Key 统计，帮助您快速发现实例中的热点 Key，更多信息，请参见 [Top Key](../user-guide/use-the-real-time-key-statistics-feature.md) [统计](../user-guide/use-the-real-time-key-statistics-feature.md) 。 |
| 缺陷修复 | 修复在 [直连访问](../user-guide/enable-the-direct-connection-mode.md) 场景下， INFO 命令的返回信息可包含 cluster_enabled 信息，使某些 SDK 能够正确地自协商至集群模式。 |  |  |  |
| 1.7.1 | MEDIUM | 2019-11-20 | 新特性 | 支持在读写分离实例的只读节点中执行只读的 lua 脚本。 支持直连模式，客户端通过直连地址可绕过代理，像连接原生 Redis 集群一样连接阿里云 Redis 集群，可降低链路开销，进一步提升 Redis 服务的响应速度。更多信息，请参见 [开通直连访问](../user-guide/enable-the-direct-connection-mode.md) 。 INFO 命令的返回信息中， Memory 部分中增加对 lua 脚本内存量的统计。 |
| 功能优化 | 优化审计日志的对内存使用。 |  |  |  |
| 1.5.8 | HIGH | 2019-09-23 | 缺陷修复 | 修复旧版全球多活链路中，双向同步时 SETEX 的原子性被破坏的问题。 |
| 1.5.6 | HIGH | 2019-08-28 | 新特性 | 审计日志支持记录 latency 事件。 |
| 缺陷修复 | 修复客户端发起的 KEYS 、 FLUSHALL 、 FLUSHDB 等命令引发的慢请求可能引起主备切换的问题。 |  |  |  |
| 1.5.4 | LOW | 2019-07-08 | 新特性 | 支持审计日志功能，为您提供日志的查询、在线分析、导出等功能，更多信息，请参见 [审计日志](../user-guide/enable-the-new-audit-log-feature.md) 。 支持对整个事件循环的 latency 记录，帮助您了解引擎的状态。 |
| 1.5.2 | HIGH | 201
