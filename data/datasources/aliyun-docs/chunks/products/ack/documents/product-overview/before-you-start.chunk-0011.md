|  |
| 更改节点 IP。 | 该 Master 节点不可用。 | 改回原 IP。 |  |
| 自行修改核心组件（etcd、kube-apiserver、docker 等）参数。 | 可能导致 Master 节点不可用。 | 按照官网推荐配置参数。 |  |
| 自行更换 Master 或 etcd 证书 | 可能导致集群无法使用。 | 不可恢复。 |  |
| 自行增加或减少 Master 节点。 | 可能导致集群无法使用。 | 不可恢复。 |  |
| 修改节点时间。 | 可能导致节点上组件工作异常。 | 还原节点时间。 |  |
| 其他 | 通过 RAM 执行权限变更或修改操作。 | 集群部分资源如负载均衡可能无法创建成功。 | 恢复原先权限。 |
| 说明 仅适用于 1.26 以下版本的集群。 修改或删除集群内预置的 PodSecurityPolicy 相关资源（包括名称为 ack.privileged 的 PodSecurityPolicy 资源，名称以 ack:podsecuritypolicy: 开头的 ClusterRole、ClusterRoleBinding、Role 和 RoleBinding 资源）。 | 可能导致集群核心组件异常、可能导致无法在集群内创建和更新 Pod 资源。 | 恢复相关资源。具体操作，详见 [配置或恢复](../ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md) [ACK](../ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md) [默认的](../ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md) [Pod](../ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md) [安全策略](../ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md) 。 |  |
