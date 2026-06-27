兼容Redis6.0版本及以下版本接口，部分限制请参见[Tair（企业版）命令支持与限制](../developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
Redis开源版：可选择7.0、6.0、5.0或4.0，完全兼容社区大版本并向下兼容。
Tair兼容Redis哪些命令和操作？
云数据库 Tair（兼容 Redis）兼容支持绝大部分开源Redis的命令和操作，仅禁用了个别命令。具体请参见：
[Redis](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)
[Tair（企业版）命令支持与限制](../developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)
[Tair Serverless KV](commands-supported-by-tair-serverless-kv-instances.md)[命令支持](commands-supported-by-tair-serverless-kv-instances.md)
Tair是否有CPU、带宽和连接数等限制？
是的。云数据库 Tair（兼容 Redis）实例的CPU处理能力、网络带宽和最大连接数主要由实例类型和架构（集群、非集群等）决定。在相同类型和架构下，实例规格的主要差异体现在内存容量上，而其他性能指标仅存在轻微变化。您可以在[实例规格](overview-4.md)查看每个规格的具体性能。
Tair支持数据持久化吗？
支持。云数据库 Tair（兼容 Redis）采用内存加硬盘的方式存储数据，通过AOF和RDB[持久化策略](../user-guide/backup-and-restoration-solutions.md)将Tair数据保存到硬盘中。
Tair支持修改配置参数吗？
支持，更多信息请参见[设置参数](../user-guide/modify-the-values-of-parameters-for-an-instance.md)。
该文章对您有帮助吗？
反馈
