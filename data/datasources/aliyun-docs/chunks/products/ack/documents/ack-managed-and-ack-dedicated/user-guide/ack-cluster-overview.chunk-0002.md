| 比较项 | ACK 托管集群 | ACK 专有集群 |  |
| --- | --- | --- | --- |
| Pro 版 | 基础版 |  |  |
| 集群规模 | 单账号最多 100 个集群。 单集群默认支持最大 5000 个 Worker 节点，可通过 [配额平台](https://quotas.console.aliyun.com/products/csk/quotas) 申请提高配额。 | 单账号最多 2 个集群。 单集群默认支持最大 10 个 Worker 节点，不支持提高配额。 | 单账号最多 100 个集群。 单集群默认支持最大 5000 个 Worker 节点，可通过 [配额平台](https://quotas.console.aliyun.com/products/csk/quotas) 申请提高配额。 |
| 托管范围 | 支持开启 [Auto Mode](ack-cluster-overview.md) [模式](ack-cluster-overview.md) ： 开启：仅需进行简单的规划配置即可创建集群，集群控制面和关键组件全托管，并默认创建一个 Auto Mode 节点池。 不开启：集群控制面全托管，Worker 节点由您自行运维。 支持 [预设控制面](ack-pro-provisioned-control-plane.md) ： 通过固化控制面资源和 API Server 基线配置，从源头消除弹性扩容的不确定性，而非依赖弹性机制事后追赶，以保障控制面性能始终可预期。 支持 Pro / Pro XL / Pro 2XL / Pro 4XL 之间的升档或降档操作。 | 集群控制面全托管；Worker 节点由您自行运维。 | 集群控制面非托管，Master 和 Worker 节点均由您自行运维。 |
| 适用场景 | 企业生产与测试环境。 期望降低成本的场景。 更希望关注业务应用，减少集群运维投入的场景。 | 集群规模上限较小，适用于个人学习与测试。 | 对成本相对不敏感，并掌握 Kubernetes 技术，可以自行规划、管理、运维集群的场景。 需要对 Kubernetes 进行研究与深度定制，例如对集群控制面（Master 节点）有定制需求的场景。 |
| 收费方式 | 收取集群管理费用（按集群数量计费），同时对 Worker 节点及部分组件使用的其他阿里云产品（例如日志服务 SLS）收费。 说明 ACK 托管集群 Pro 版 支持使用资源包，详细信息请参见 [集群管理费用](../product-overview/cluster-management-fee.md) 。 | 不收取集群管理费用，但对 Worker 节点及部分组件使用的其他阿里云产品（例如日志服务 SLS）收费。 | 不收取集群管理费用，对 Mast
