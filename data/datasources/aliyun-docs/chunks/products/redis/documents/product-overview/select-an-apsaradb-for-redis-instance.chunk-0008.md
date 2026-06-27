oper-reference/overview-3.md)[命令支持概览](../developer-reference/overview-3.md)和[设置参数](../user-guide/modify-the-values-of-parameters-for-an-instance.md)。
产品类型简介如下表：

| 对比项 | Redis 开源版 | Tair（企业版） |  |  |
| --- | --- | --- | --- | --- |
| [部署模式](comparison-between-tair-instances-that-cloud-native-and-classic.md) | 云原生（推荐） 经典 | 云原生 |  |  |
| 存储介质 | 内存 | [内存型](dram-based-instances.md) | [持久内存型](persistent-memory-optimized-instances-1.md) | [磁盘型](essd-based-instances-1.md) |
| 兼容 Redis 版本 | 5.0、6.0、7.0 | 5.0、6.0、7.0 | 6.0 | 6.0 |
| 性能 | 100%（基准） | 300% | 90% | 最高 60% |
| 特点 | 云上开源 Redis 服务。 | 提供丰富的自研 [扩展数据结构](../developer-reference/extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md) ，帮助您精简代码并提高业务整体性能。 支持企业级特性： [按时间点恢复数据](../user-guide/use-data-flashback-to-restore-data-by-point-in-time.md) 、代理查询缓存、 [全球多活](../user-guide/overview-of-global-distributed-cache-for-tair.md) 等。 支持高级加密： [TLS](../user-guide/enable-tls-encryption.md) [加密连接](../user-guide/enable-tls-encryption.md) 、 [透明数据加密](../user-guide/enable-tde.md) [TDE](../user-guide/enable-tde.md) 等。 | 高性价比：成本对比 Redis 开源版最高可降低 30%。 更高可靠性：同步持久化，每个写操作在主节点持久化成功之后返回。 | 数据通过磁盘持久化存储，内存用于请求加速。 |
| 适用场景参考 | 开源 Redis 场景。 | 对请求的响应时间要求极高场景，如视频直播、在线教育，在线游戏，RTA 等。 千万级 QPS 使用缓存场景，如在线购物、社交网络等。 | 海量数据下追求性价比和数据可靠性的场景，如物联网。 | 需要大存储空间且访问性能较高的温冷数据存储，且以成本作为首要考虑因素的场景，如文件存储的索引、历史消息的长期存储等。 |
