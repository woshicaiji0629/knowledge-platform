## 架构介绍
Tair Serverless KVRedis兼容版实例为分布式集群架构，兼容Redis开源版6.0，更多信息请参见[Redis](commands-supported-by-tair-serverless-kv-instances.md)[兼容版命令支持](commands-supported-by-tair-serverless-kv-instances.md)。以下为架构图和组件说明。

| 组件 | 说明 |
| --- | --- |
| 数据分片（Partition） | 一个实例由多分片构成，分片间的数据分布与 Redis Cluster 兼容（SLOT）。每个数据分片均为一主多备（分别部署在不同机器上）的高可用架构。备节点的数量至少为 1。 |
| 高可用服务（HA） | 主节点（Master）发生故障后，系统会自动在 30 秒内切换至备节点（Replica），以保证服务高可用和数据高可靠。 |
