### KubeConfig状态
容器服务 Kubernetes 版的KubeConfig具备以下四个状态。

| 状态 | 说明 |
| --- | --- |
| 未颁发 | 对当前 RAM 用户或 RAM 角色从未下发过该集群的 KubeConfig。 |
| 生效 | 当前 RAM 用户或 RAM 角色的集群 KubeConfig 存在且未过期。 |
| 当前 RAM 用户或 RAM 角色的集群 KubeConfig 已被清除，但仍然存在残留的 RBAC 权限。 |  |
| 过期 | 当前 RAM 用户或 RAM 角色的集群 KubeConfig 存在，但已过期。 |
| 已清除 | 当前 RAM 用户或 RAM 角色下发过集群的 KubeConfig，但是目前 KubeConfig 已经被清除。 清除 KubeConfig 即删除集群的 KubeConfig 信息和该 RAM 用户或 RAM 角色的 RBAC Binding。 |
