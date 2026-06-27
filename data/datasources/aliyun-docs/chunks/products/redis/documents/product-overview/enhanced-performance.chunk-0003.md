## 性能说明

| 架构 | 性能说明 |
| --- | --- |
| [标准架构](standard-master-replica-instances.md) | 实例整体的性能与实例规格表中对应的性能一致。 |
| [集群架构直连模式](cluster-master-replica-instances.md) [集群架构代理模式](cluster-master-replica-instances.md) [读写分离功能](read-or-write-splitting-instances-1.md) | 实例整体的性能 = 分片规格的性能 * 分片数。 说明 集群架构代理模式实例的带宽上限为 20Gbps(2.5GB/s)，而最大连接数的计算规则取决于 Proxy 节点数，与分片数无关，上限为 50 万。 例如实例具备 4 个分片，分片的规格均为 tair.rdb.with.proxy.1g ，每个分片的性能为： CPU 核数：4 工作核+3 后台核。 带宽：768 Mbps（96 MB/s）。 连接数：30,000。 那么，该实例的整体性能即为： CPU 核数：28 核。 带宽：3,072 Mbps（384 MB/s）。 分片最大连接数为：120,000。 Proxy 最大连接数为：480,000（以该连接数为准）。 |
