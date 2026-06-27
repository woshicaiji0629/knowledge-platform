[VPC](../user-guide/enable-password-free-access.md) [免密访问](../user-guide/enable-password-free-access.md) 的场景下，申请公网连接地址。 增加 INFO 命令中关于 oom_err_count 的统计场景：即 maxmemory 数据量超过设定值时会被计入。 |
| 缺陷修复 | 修复当 RPOPLPUSH 命令的 source 和 destination 相同时，在执行过程中因触发了过期机制导致的崩溃问题。 修复专有网络 VPC 免密模式下权限验证错误的问题。 |  |  |  |
| 0.2.0 | LOW | 2020-01-17 | 新特性 | 支持实时热点 Key 统计，帮助您快速发现实例中的热点 Key，更多信息，请参见 [Top Key](../user-guide/use-the-real-time-key-statistics-feature.md) [统计](../user-guide/use-the-real-time-key-statistics-feature.md) 。 |
| 0.1.2 | LOW | 2019-11-26 | 新特性 | 支持在 [读写分离](../product-overview/read-or-write-splitting-instances-1.md) 实例的只读节点中执行只读的 lua 脚本。 |
| 0.1.2 之前 | 不涉及 | 不涉及 | 不涉及 | 5.0 版本下的早期小版本，建议升级至最新的小版本。 |
