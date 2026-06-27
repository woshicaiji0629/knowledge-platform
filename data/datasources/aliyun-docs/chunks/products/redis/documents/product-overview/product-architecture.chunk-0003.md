### 标准（未启用集群）架构

| 实例架构 | 架构图 | 适用场景 |
| --- | --- | --- |
| [标准架构](standard-master-replica-instances.md) 采用主备（master-replica）双节点架构，提供高可用切换。 |  | Redis 作为持久化数据存储使用的业务。 单个 Redis 性能压力可控的场景。 数据量较少的场景。 |
| [标准架构（开启读写分离）](read-or-write-splitting-instances-1.md) 由代理服务器（Proxy servers）、主备（master-replica）节点组成。 |  | 读取请求 QPS 压力较大的场景。 Redis 作为持久化数据存储使用的业务场景。 |
| [标准架构（单节点）](standard-master-replica-instances.md) 采用单节点架构。 |  | 无数据可靠性要求的纯缓存场景。 单个 Redis 性能压力可控的场景。 数据量较少的场景。 |
