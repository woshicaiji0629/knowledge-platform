configure-whitelists.md) [ECS](../getting-started/step-2-configure-whitelists.md) [安全组设置白名单](../getting-started/step-2-configure-whitelists.md) 。 |
| 0.3.8 | HIGH | 2020-07-14 | 功能优化 | 开放 CLIENT UNBLOCK 子命令。 |
| 缺陷修复 | 修复在迁移 slot（槽）时解析 expire（过期时间）不正确的问题。 订正审计日志中的 latency 标记位，避免其在主备审计日志中混淆。 |  |  |  |
| 0.3.7 | HIGH | 2020-06-17 | 缺陷修复 | 修复直连模式下返回 IP 地址不可达的问题。 |
| 0.3.6 | LOW | 2020-06-09 | 新特性 | INFO 命令返回值中， Replication 部分支持展示 role 信息（例如 role:master ），可兼容 Redisson 客户端在部分场景下对该信息的调用。 |
| 0.3.5 | LOW | 2020-06-05 | 新特性 | 支持对读写命令 QPS 的统计，更多信息，请参见 [查看性能监控](../user-guide/view-monitoring-data.md) 。 |
| 0.3.4 | HIGH | 2020-04-08 | 缺陷修复 | 修复热点 Key 在被执行逐出时可能出现的崩溃问题。 修复关闭审计日志时因 UAF（Use-After-Free）导致的崩溃问题。 |
| 0.3.1 | HIGH | 2020-02-20 | 新特性 | 支持审计日志功能，为您提供日志的查询、在线分析、导出等功能，更多信息，请参见 [审计日志](../user-guide/enable-the-new-audit-log-feature.md) 。 支持直连模式，客户端通过直连地址可绕过代理，连接方式类似连接原生 Redis 集群，可降低链路开销，进一步提升 Redis 服务的响应速度。更多信息，请参见 [开通直连访问](../user-guide/enable-the-direct-connection-mode.md) 。 支持在 [专有网络](../user-guide/enable-password-free-access.md) [VPC](../user-guide/enable-password-free-access.md) [免密访问](../user-guide/enable-password-free-access.md) 的场景下，申请公网连接地址。 增加 INFO 命令中关于 oom_err_count 的统计场景：即 max
