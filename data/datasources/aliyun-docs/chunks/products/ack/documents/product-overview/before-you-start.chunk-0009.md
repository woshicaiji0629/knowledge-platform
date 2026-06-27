| 分类 | 高危操作 | 影响 | 恢复方案 |
| --- | --- | --- | --- |
| API Server | 复用 API Server 所使用的 CLB 于其他场景，例如使用 LoadBalancer 类型 Service 复用该 CLB。 | 导致集群不可用，影响业务流量。 | 恢复原有配置，或请求售后服务支持。 |
| 修改 API Server 所使用的 CLB 的监听、服务器组、ACL 等控制 CLB 转发的配置、CLB 标签配置。 | 导致集群异常。 | 恢复原有配置。 |  |
| 删除 API Server 所使用的 CLB。 | 导致集群不可操作。 | 不可恢复，请重新创建集群。重建集群请参见 [创建](../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md) [ACK](../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md) [托管集群](../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md) 。 |  |
| Worker 节点 | 修改集群内节点安全组。 | 可能导致节点不可用。 | 将节点重新添加到集群自动创建的节点安全组中，请参见 [为实例（主网卡）关联安全组](../../../ecs/documents/user-guide/manage-ecs-instances-in-security-groups.md) 。 |
| 节点到期或被销毁。 | 该节点不可用。 | 不可恢复。 |  |
| 重装操作系统。 | 节点上组件被删除。 | 节点移出再加入集群。相关操作请参见 [移除节点](../ack-managed-and-ack-dedicated/user-guide/remove-a-node.md) 、 [添加已有节点](../ack-managed-and-ack-dedicated/user-guide/add-existing-ecs-instances-to-an-ack-cluster.md) 。 |  |
| 自行升级节点组件版本。 | 可能导致节点无法使用。 | 回退到原始版本。 |  |
| 更改节点 IP。 | 节点不可用。 | 改回原 IP。 |  |
| 自行修改核心组件（kubelet、docker、containerd 等）参数。 | 可能导致节点不可用。 | 按照官网推荐配置参数。 |  |
| 修改操作系统配置。 | 可能导致节点不可用。 | 尝试还原配置项或删除
