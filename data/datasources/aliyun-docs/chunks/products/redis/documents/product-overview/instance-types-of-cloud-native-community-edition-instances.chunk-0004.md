## 性能说明

| 架构 | 性能说明 |
| --- | --- |
| [标准架构](standard-master-replica-instances.md) | 实例整体的性能与实例规格表中对应的性能一致。 |
| [集群架构直连模式](cluster-master-replica-instances.md) [集群架构代理模式](cluster-master-replica-instances.md) [读写分离功能](read-or-write-splitting-instances-1.md) | 实例整体的性能 = 分片规格的性能 * 分片数。 说明 集群架构代理模式实例的带宽上限为 20Gbps(2.5GB/s)，而最大连接数的计算规则取决于 Proxy 节点数，与分片数无关，上限为 50 万。 例如实例具备 4 个分片，分片的规格为 redis.shard.with.proxy.small.ce，每个分片的性能为： CPU 核数：2 工作核+1 后台核。 带宽：384 Mbps（48 MB/s）。 最大连接数：10,000。 QPS 参考值：100,000。 那么，该实例的整体性能即为： CPU 核数：12 核。 带宽：1,536 Mbps（192 MB/s）。 分片最大连接数为：40,000。 Proxy 最大连接数为：360,000（以该连接数为准）。 QPS 参考值：400,000。 |
