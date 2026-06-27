### 集群架构

| 实例架构 | 架构图 | 适用场景 |
| --- | --- | --- |
| [集群架构](cluster-master-replica-instances.md) 每个分片均采用主备（master-replica）多节点架构。 |  | 数据量较大的场景。 QPS 压力较大的场景。 吞吐密集型应用场景。 |
| [集群架构（开启读写分离）](read-or-write-splitting-instances-1.md) 每个分片均采用读写分离架构。 |  | 适用读请求流量超过主节点性能上限时，通过增加只读节点来提升实例的读性能。 |
| [集群架构（单节点）](cluster-master-replica-instances.md) 每个分片均采用单节点（副本）架构。 |  | 无数据可靠性要求的纯缓存场景。 数据量较大的场景。 QPS 压力较大的场景。 吞吐密集型应用场景。 |
