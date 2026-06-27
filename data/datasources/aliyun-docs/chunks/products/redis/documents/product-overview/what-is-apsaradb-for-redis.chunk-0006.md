## 常见问题
Tair与Redis是什么关系？
云数据库 Tair（兼容 Redis）是完全兼容Redis协议的云原生高性能内存数据库。任何兼容Redis的客户端均可与云数据库 Tair（兼容 Redis）建立连接，从而进行数据存储及相应操作。
同时，Tair（企业版）版是强化版Redis服务，提供超高性能、超高性价比等一系列选择，更多信息请参见[Tair（企业版）与](comparison-between-apsaradb-for-redis-enhanced-edition-and-apsaradb-for-redis-community-edition.md)[Redis](comparison-between-apsaradb-for-redis-enhanced-edition-and-apsaradb-for-redis-community-edition.md)[开源版特性对比](comparison-between-apsaradb-for-redis-enhanced-edition-and-apsaradb-for-redis-community-edition.md)。
Tair兼容Redis哪些版本？
Tair（企业版）[内存型](dram-based-instances.md)（兼容Redis 7.0）：完全兼容Redis7.0版本及以下版本接口，额外支持Tair扩展数据结构。
Tair（企业版）[内存型](dram-based-instances.md)（兼容Redis 6.0）：完全兼容Redis6.2版本及以下版本接口，额外支持Tair扩展数据结构。
Tair（企业版）[内存型](dram-based-instances.md)（兼容Redis 5.0）：完全兼容Redis5.0版本及以下版本接口，额外支持Tair扩展数据结构。
Tair（企业版）[持久内存型](persistent-memory-optimized-instances-1.md)：兼容Redis6.0版本及以下版本接口，部分限制请参见[Tair（企业版）命令支持与限制](../developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
Tair（企业版）[磁盘型](essd-based-instances-1.md)：兼容Redis6.0版本及以下版本接口，部分限制请参见[Tair（企业版）命令支持与限制](../developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
Redis开源版：可选择7.0、6.
