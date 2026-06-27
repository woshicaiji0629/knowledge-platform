## Redis开源版

| 实例规格文档 | 简介 |
| --- | --- |
| [Redis](instance-types-of-cloud-native-community-edition-instances.md) [开源版云原生版](instance-types-of-cloud-native-community-edition-instances.md) | 标准架构：内存容量上限可达 64 GB，支持约 100,000 QPS。 读写分离架构：内存容量上限可达 64 GB，支持约 600,000 QPS。 集群架构：内存容量上限可达 16,384 GB（64 GB*256 分片数），实例整体的性能= 分片数 * 各分片的规格对应的性能。 |
| [Redis](instance-types-of-classic-community-edition-instances.md) [开源版经典版](instance-types-of-classic-community-edition-instances.md) | 标准架构（多副本）：主备（master-replica）架构的 Redis 实例。内存容量上限可达 64 GB，支持约 80,000 QPS（参考值）。 标准架构（单副本）：单节点的 Redis 实例。内存容量上限可达 32 GB，支持约 80,000 QPS（参考值）。 集群架构（双副本）：每个数据分片都是主备（master-replica）架构。内存容量上限可达 4,096 GB（16 GB*256 分片数），支持约 25,600,000 QPS（参考值）。 集群架构（单副本）：每个数据分片都是单节点架构。内存容量上限可达 2,048 GB（16 GB*128 分片数），支持约 12,800,000 QPS（参考值）。 读写分离架构：由一个主备架构的主节点、一个或多个只读副本组成的 Redis 实例。内存容量上限可达 64 GB，支持约 600,000 QPS。 |
| 早期已停售规格 | 云数据库 Tair（兼容 Redis） 的部分规格已停止新购，但这些规格的已购实例仍可正常使用。您可以在 [早期已停售规格](retired-instance-types.md) 中查看这些规格的连接数限制、带宽、QPS 参考值等信息。 |
