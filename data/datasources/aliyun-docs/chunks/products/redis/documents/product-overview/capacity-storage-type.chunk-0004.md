## 性能说明

| 架构 | 性能说明 |
| --- | --- |
| [标准架构](standard-master-replica-instances.md) | 实例整体的性能与实例规格表中对应的性能一致。 |
| [集群架构直连模式](cluster-master-replica-instances.md) [集群架构代理模式](cluster-master-replica-instances.md) | 实例整体的性能 = 分片规格的性能 * 分片数。 说明 集群架构代理模式实例的带宽上限为 20Gbps(2.5GB/s)，而最大连接数的计算规则取决于 Proxy 节点数，与分片数无关，上限为 50 万。 例如实例具备 4 个分片，分片规格为 tair.localssd.c1m8.xlarge ，每个分片的性能为： CPU 核数：4 核 内存：32 GB SSD 容量：640 GB 连接数：60,000 带宽：1,500 Mbps（187.5 MB/s） 那么，该实例的整体性能即为： CPU 核数：16 核 内存：128 GB SSD 容量：2,560 GB 分片最大连接数为：240,000 Proxy 最大连接数为：480,000（以该连接数为准）。 带宽：6,000 Mbps（750 MB/s） |
