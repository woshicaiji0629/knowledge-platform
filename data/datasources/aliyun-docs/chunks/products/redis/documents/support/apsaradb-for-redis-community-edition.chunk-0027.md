力，避免可能出现的长时间停顿问题。 |
| 1.9.0 | LOW | 2021-02-22 | 新特性 | 当返回 illegal address 错误消息时，Redis 会将当前客户端的 IP 地址包含在错误消息中。您可以根据提示，为 Redis 实例设置正确的 IP 白名单。 |
| 1.8.8 | HIGH | 2020-09-25 | 缺陷修复 | 修复 CLUSTER NODES 命令返回值与开源协议不一致的问题，即槽（slot）间以空格分隔，避免客户端解析错误。 |
| 1.8.7 | LOW | 2020-07-20 | 新特性 | 支持 ECS 安全组功能，通过为 Redis 实例绑定 ECS 所属安全组的方式实现快速授权（无需手动填写 ECS 的 IP 地址），可提升运维的便捷性。更多信息，请参见 [通过](../getting-started/step-2-configure-whitelists.md) [ECS](../getting-started/step-2-configure-whitelists.md) [安全组设置白名单](../getting-started/step-2-configure-whitelists.md) 。 |
| 1.8.6 | HIGH | 2020-07-14 | 缺陷修复 | 订正审计日志中的 latency 标记位，避免其在主备审计日志中混淆。 |
| 1.8.5 | LOW | 2020-06-09 | 新特性 | INFO 命令返回值中， Replication 部分支持展示 role 信息（例如 role:master ），可兼容 Redisson 客户端在部分场景下对该信息的调用。 |
| 1.8.4 | LOW | 2020-06-05 | 新特性 | 支持对读写命令 QPS 的统计，更多信息，请参见 [查看性能监控](../user-guide/view-monitoring-data.md) 。 |
| 1.8.3 | HIGH | 2020-04-08 | 缺陷修复 | 修复热点 Key 在被执行逐出时可能出现的崩溃问题。 修复关闭审计日志时因 UAF（Use-After-Free）导致的崩溃问题。 |
| 1.8.1 | LOW | 2020-02-20 | 新特性 | 支持在已开启 [专有网络](../user-guide/enable-password-free-access.md) [VPC](../user-guide/enable-password-free-access.md) [免密访问](../user-guide/enable-password-free-access.md) 的场景下，申请公网连接地址的操作。 |
| 1.8.0 | HIGH | 202
