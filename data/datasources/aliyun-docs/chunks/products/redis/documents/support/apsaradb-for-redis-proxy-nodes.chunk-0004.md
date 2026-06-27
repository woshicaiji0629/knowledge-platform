| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 7.1.6 | MEDIUM | 2026-01-24 | 功能优化 | 支持 bf.scandump 命令。 |
| 缺陷修复 | 修改向量全局索引功能在 db 节点访问失败时可能导致的异常。 |  |  |  |
| 7.1.5 | MEDIUM | 2025-12-09 | 功能优化 | 监控项支持 P95、P99 RT。 支持 wait 命令（proxy 直接返回命令中 numreplicas 参数值）。 |
| 缺陷修复 | 修复私有连接池功能开启后有小概率异常的问题。 |  |  |  |
| 7.1.3 | MEDIUM | 2025-10-27 | 功能优化 | 新增 subscribe_route_ronode_enabled 参数配置，支持订阅命令路由至只读节点。 在读写分离架构中，启用此配置后， SUBSCRIBE 、 SSUBSCRIBE 和 PSUBSCRIBE 命令可以被路由到只读节点。 开启此功能后， __keyevent@ 和 __keyspace@ 等键空间通知频道也可能被路由到只读节点。 如需将特定会话的所有请求（包括订阅）强制路由到主节点，可以使用 AUTH <user>:<password>:master 命令进行认证。 优化低 QPS 场景下审计日志的源 IP 被错误记录为 Proxy 实例地址的问题。 |
| 7.0.21 | MEDIUM | 2025-07-29 | 功能优化 | CLIENT LIST 命令新增返回以下统计项： tot-net-in ：表示该连接的总入流量。 tot-net-out ：表示该连接的总出流量。 tot-cmds ：表示该连接的总请求数。 Redis 7.0 实例的 INFO 、 IINFO 命令支持 Latencystats 模块（Section）统计信息。 |
| 缺陷修复 | 修复在使用 Vecotr 命令后，实例规格变更可能失败的问题。 Redis cluster 语法兼容模式支持 CLUSTER COUNTKEYSINSLOT 和 CLUSTER GETKEYSINSLOT 子命令。 |  |  |  |
| 7.0.20 | LOW | 2025-07-04 | 功能优化 | 支持 XSETID 命令的可选参数。 |
| 7.0.19 | MEDIUM | 2025-06-04 | 缺陷修复 | 修复部分 Vecotr 请求在客户端断连时可能导致异常的问题。 修复 XGROUP、XINFO、OBJECT HELP 等无 Key 命令导致异常的问题。 |
| 7.0.18 | MEDIUM | 2025-04-02 | 功能优化 | 修复
