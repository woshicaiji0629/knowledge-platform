退到原始版本。 |  |
| 更改节点 IP。 | 节点不可用。 | 改回原 IP。 |  |
| 自行修改核心组件（kubelet、docker、containerd 等）参数。 | 可能导致节点不可用。 | 按照官网推荐配置参数。 |  |
| 修改操作系统配置。 | 可能导致节点不可用。 | 尝试还原配置项或删除节点重新购买。 |  |
| 修改节点时间。 | 可能导致节点上组件工作异常。 | 还原节点时间。 |  |
| 通过不受 ACK 支持的方式向集群中添加节点算力资源。 | ACK 提供控制台、OpenAPI、CLI 等方式向集群中增加节点算力资源，请参见 [添加已有节点](../ack-managed-and-ack-dedicated/user-guide/add-existing-ecs-instances-to-an-ack-cluster.md) 。如果您通过其他方式向集群中添加了节点，ACK 无法识别此类节点的来源，无法提供节点生命周期管理、自动化运维和技术支持等产品能力。详细风险说明，请参见 [为什么控制台显示节点所属节点池的来源为“其他节点”？](../ack-managed-and-ack-dedicated/user-guide/faq-about-node-management.md) 。 | 建议通过节点池的方式纳管算力资源。如需继续使用，请自行确保节点与集群各组件（如 Kubernetes 组件、网络、存储、安全组件等）的兼容性。 |  |
| Master 节点（ACK 专有版集群） | 修改集群内节点安全组。 | 可能导致 Master 节点不可用。 | 将节点重新添加到集群自动创建的节点安全组中，请参见 [为实例（主网卡）关联安全组](../../../ecs/documents/user-guide/manage-ecs-instances-in-security-groups.md) 。 |
| 节点到期或被销毁。 | 该 Master 节点不可用。 | 不可恢复。 |  |
| 重装操作系统。 | Master 节点上组件被删除。 | 不可恢复。 |  |
| 自行升级 Master 或者 etcd 组件版本。 | 可能导致集群无法使用。 | 回退到原始版本。 |  |
| 删除或格式化节点 /etc/kubernetes 等核心目录数据。 | 该 Master 节点不可用。 | 不可恢复。 |  |
| 更改节点 IP。 | 该 Master 节点不可用。 | 改回原 IP。 |  |
| 自行修改核心组件（etcd、kube-apiserver、docker 等）参数。 | 可能导致 Master 节点不可用。 | 按照官网推荐配置参数。 |  |
| 自行更换 Master 或 etcd 证书 | 可
