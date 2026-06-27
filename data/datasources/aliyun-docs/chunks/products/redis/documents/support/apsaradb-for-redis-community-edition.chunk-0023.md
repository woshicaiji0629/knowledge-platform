| 2021-08-05 | 缺陷修复 | 修复集群实例开通直连的场景下，变配存在概率失败的问题。 |
| 0.5.4 | MEDIUM | 2021-07-27 | 功能更新 | 增强稳定性。 |
| 0.5.3 | MEDIUM | 2021-07-21 | 功能更新 | 优化数据迁移完成后删除源端数据的流程，增强数据可靠性。 简化数据迁移的增量数据同步流程。 |
| 0.5.2 | HIGH | 2021-04-26 | 安全加固 | 主要解决社区 Lua JIT 的安全性漏洞。 |
| 新特性 | 优化槽（slot）的迁移能力，云盘版实例可基于此实现无损扩缩容。 支持大 Key（big key）实时统计。 支持通过公网获取虚拟 IP（VIP）地址，为使用直连地址用户提供更好的支持。 |  |  |  |
| 0.5.0 | MEDIUM | 2021-03-25 | 新特性 | 支持槽（slot）的无感迁移能力。 |
| 功能优化 | 增强在处理大量异步客户端请求场景下的稳定性。 |  |  |  |
| 0.4.0 | MEDIUM | 2021-03-09 | 新特性 | 支持大 Key（big key）实时统计。 支持 CONFIG RESETSTAT 命令。 当返回 illegal address 错误消息时，Redis 会将当前客户端的 IP 地址包含在错误消息中。您可以根据提示，为 Redis 实例设置正确的 IP 白名单。 图 1. IP 地址提示 r-bp xxx .redis.rds.aliyuncs.com:6379> auth (error) ERR illegal address: 172.16.xxx:39136 |
| 功能优化 | 优化实例健康检查能力，提升在磁盘抖动场景下的主备切换速度。 |  |  |  |
| 0.3.10 | HIGH | 2020-09-25 | 缺陷修复 | 修复 CLUSTER NODES 命令返回值与开源协议不一致的问题，即槽（slot）间以空格分隔，避免客户端解析错误。 |
| 0.3.9 | LOW | 2020-07-20 | 新特性 | 支持 ECS 安全组功能，通过为 Redis 实例绑定 ECS 所属安全组的方式实现快速授权（无需手动填写 ECS 的 IP 地址），可提升运维的便捷性。更多信息，请参见 [通过](../getting-started/step-2-configure-whitelists.md) [ECS](../getting-started/step-2-configure-whitelists.md) [安全组设置白名单](../getting-started/step-2-configure-whitelists.md) 。 |
| 0.3.8 | HI
