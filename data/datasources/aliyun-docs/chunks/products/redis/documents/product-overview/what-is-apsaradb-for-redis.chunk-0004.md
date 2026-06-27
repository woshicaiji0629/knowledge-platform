s-compatible-edition.md) | Tair Serverless KV 实例为分布式集群架构，具备自动扩缩容以及按实际用量计费的能力。高峰时自动扩容保障业务平稳，低峰时自动缩容节省成本。全程自动化无缝伸缩，业务无感知，能够显著降低运维的复杂度。 |

支持灵活的多种部署架构，能够满足不同的业务场景。

| 架构类型 | 说明 |
| --- | --- |
| [标准版-单副本](https://help.aliyun.com/zh/document_detail/52685.html#concept-fx3-jrg-tdb) | 适用于纯缓存场景，支持单节点集群弹性变配，满足高 QPS（Queries per Second）场景，提供超高性价比。 |
| [标准架构](standard-master-replica-instances.md) | 系统工作时主节点（Master）和副本（Replica）数据实时同步，若主节点发生故障，系统会快速将业务切换至备节点，全程自动且对业务无影响，保障服务高可用性。 |
| [集群版-单副本](https://help.aliyun.com/zh/document_detail/59201.html#concept-ydy-g24-tdb) | 单副本集群版实例采用集群架构，每个分片服务器采用单副本模式。适用于纯缓存类业务或者 QPS 压力较大的业务场景。 |
| [集群架构](cluster-master-replica-instances.md) | 集群（Cluster）实例采用分布式架构，每个数据分片都支持主备切换（master-replica），能够自动进行容灾切换和故障迁移，保障服务高可用。同时提供多种规格，您可以根据业务压力选择对应规格，还可以随着业务的发展自由变配规格。集群版支持两种连接模式： [代理模式（推荐）](cluster-master-replica-instances.md) ：提供智能的连接管理，降低应用开发成本。 [直连模式](cluster-master-replica-instances.md) ：客户端绕过代理服务器直接访问后端数据分片，可降低网络开销和服务响应时间，适用于对 Redis 响应速度要求极高的业务。 |
| [读写分离功能](read-or-write-splitting-instances-1.md) | 读写分离实例通过主备（Master-Replica）架构实现高可用，主节点挂载只读副本（Read Replica）实现数据复制，支持读性能线性扩展。 只读副本可以有效缓解热点 Key 带来的性能问题，适合高读写比的业务场景。 读写分离实例有两种版本。 读写分离（ 云原生 版）：只读节点均从主节点同步数据，为星型复制架构，支持自定义只读节点数量（集群架构每分片 1 ~ 4 个，标准架构 1 ~ 9 个），适合超大规模高读写比的业务场景。 读写分离（ 经典 版，已停售）：只读节点采取链式复制架构，支持配置 1 个、3 个、5 个只读节点。 |
