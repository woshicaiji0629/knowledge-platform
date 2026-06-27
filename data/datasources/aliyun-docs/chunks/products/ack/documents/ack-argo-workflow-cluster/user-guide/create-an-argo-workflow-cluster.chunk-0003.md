| 参数 | 描述 |
| --- | --- |
| 集群名称 | 填写集群的名称。 长度为 1～63 个字符，可包含字母、数字、下划线（_）或中划线（-），且仅允许以字母开头。 |
| 地域 | 选择集群所在的地域。 |
| 专有网络 | 设置集群的专有网络 VPC，在下拉列表中选择已创建的 VPC。 |
| 虚拟交换机 | 在下拉列表中选择已创建的交换机。 |
| 资源组 | 将集群归属于选择的 [资源组](../../../../ecs/documents/user-guide/resource-groups.md) ，便于权限管理和成本分摊。 一个资源只能归属于一个资源组。 |
| 标签 | 为集群绑定键值对 [标签](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview) ，作为云资源的标识。 |
| API Server 访问 | 无需设置，创建 容器 Argo 工作流集群 时会默认自动新建一个按量付费的私网 CLB 实例作为 API Server 的内网连接端点。 重要 请勿删除该实例，否则会导致集群 API Server 无法访问。 |
| 创建并绑定 EIP | 开启后，集群 API Server 使用的 CLB 实例将绑定一个弹性公网 IP，使集群 API Server 支持公网访问。 |
| 开启组件及审计日志 | 同时将启用集群 API Server 审计功能，收集对 Kubernetes API 的请求以及请求结果。如需后续启用，请参见 [采集](../../ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [ACK](../../ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [集群容器日志](../../ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) 、 [使用集群](../../ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md) [A
