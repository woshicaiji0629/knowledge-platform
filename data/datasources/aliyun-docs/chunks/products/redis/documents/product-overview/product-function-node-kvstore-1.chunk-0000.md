| 功能集 | 功能 | 功能描述 | 参考文档 |
| --- | --- | --- | --- |
| 架构 | 主从版本 | 1 个主节点、1 个从节点的标准架构。 | [标准版-双副本](standard-master-replica-instances.md) |
| 读写分离 | 支持开启读写分离功能，1 个主节点、1~9 个只读节点（可随时调整）。 | [读写分离版](read-or-write-splitting-instances-1.md) |  |
| 集群版 | 支持原生 Redis Cluster 架构与代理模式集群架构，分片数量为 2~256 分片，分片规格为 1 GB~64 GB，整体容量可达 2 GB~16 TB。 | [集群版](cluster-master-replica-instances.md) |  |
| 单副本 | 仅单个节点，价格为主从版本的 50%，不支持备份与恢复，不保障数据可靠性，无 SLA 保障，仅适合纯缓存场景。 | [标准版-单副本](https://help.aliyun.com/zh/document_detail/52685.html) |  |
| 规格与架构变更 | 升配 | 升级配置，包括扩大分片容量，增加分片数量。 | [变更实例配置](../user-guide/change-the-configurations-of-an-instance.md) |
| 降配 | 降低配置，包括降低分片容量，减少分片数量。 | [变更实例配置](../user-guide/change-the-configurations-of-an-instance.md) |  |
| 跨架构变配 | 支持在单副本、主从、读写分离、集群架构之间相互变配，且无需修改业务代码。 | [变更实例配置](../user-guide/change-the-configurations-of-an-instance.md) |  |
| 版本兼容性 | 兼容 Redis4.0、5.0、6.0、7.0 | 支持 Redis 4.0、5.0、6.0 与 7.0 版本。 | [Redis](../support/new-features-of-apsaradb-for-redis.md) [大版本新特性与兼容性](../support/new-features-of-apsaradb-for-redis.md) |
| 兼容 Memcache | 兼容 Memcache API。 | [什么是云数据库 Memcache 版](https://help.aliyun.com/zh/memcache/product-overview/product-overview) |  |
| 安全能力 | 支持命令动态屏蔽 | 支持动态
