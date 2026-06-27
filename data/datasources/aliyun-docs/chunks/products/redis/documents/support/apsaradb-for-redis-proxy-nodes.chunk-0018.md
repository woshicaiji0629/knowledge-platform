om/zh/dms/product-overview/what-is-dms#task-1919582) 连接失败的问题。 修复订阅 __keyspace@0__ 时，未指定 Key 导致的崩溃问题。 |
| 6.4.5 | LOW | 2020-09-27 | 新特性 | 增加对部分内部命令的支持。 |
| 6.4.3 | HIGH | 2020-09-25 | 功能优化 | 针对 Jedis 客户端中 pipeline 的特殊实现进行了适配，优化连接限制的释放计算，Jedis 连接示例，请参见 [客户端程序连接教程](../user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance.md) 。 |
| 缺陷修复 | 修复 BZPOPMIN 和 XREAD 命令错误记录了慢日志的问题，更多信息，请参见 [查询慢日志](../user-guide/view-slow-logs.md) 。 |  |  |  |
| 6.4.2 | HIGH | 2020-09-09 | 缺陷修复 | 修复空闲连接默认 1 分钟后被断开的问题。 |
| 6.4.1 | MEDIUM | 2020-08-25 | 新特性 | 新增 Timeout 配置，空闲的客户端连接会被自动断开。 支持统计只读节点上的慢日志信息，即 SLOWLOG 命令会发送至所有 Master 节点和只读节点。更多信息，请参见 [查询慢日志](../user-guide/view-slow-logs.md) 。 |
| 功能优化 | 优化了 Pub/Sub 和 Monitor 连接的内存使用，避免因内存碎片引起的内存快速上涨。 提升了 Proxy 节点处理新连接的能力。 |  |  |  |
| 6.4.0 | HIGH | 2020-08-18 | 缺陷修复 | 修复 ConfigServer 在完成配置前调用 stat 导致的崩溃问题。 |
