## RBAC权限
RAM系统策略仅控制ACK One集群资源的操作权限，若RAM用户或RAM角色需要操作指定集群内的K8s资源，（如创建并获取GitOps Application和Argo Workflow），还需要获取指定ACK One集群及其命名空间的操作权限即RBAC权限。
ACK One提供以下预置角色：
多集群舰队和工作流集群RBAC权限

| RBAC 权限 | 权限说明 | 集群是否涉及 |  |
| --- | --- | --- | --- |
| 多集群舰队 | 工作流集群 |  |  |
| admin（管理员） | 具有集群范围和所有命名空间下资源的读写权限。 | 是 | 是 |
| dev（开发人员） | 具有所选命名空间下的资源读写权限。 | 是 | 是 |
| gitops-dev（gitops 开发人员） | 具有 argocd 命名空间下应用资源的读写权限。 | 是 | 不涉及 |

[注册集群](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[RBAC](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[权限](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)
RBAC权限所控制的具体资源列表以及授权操作，请参见[为](grant-rbac-permissions-to-a-ram-user-or-ram-role.md)[RAM](grant-rbac-permissions-to-a-ram-user-or-ram-role.md)[用户或](grant-rbac-permissions-to-a-ram-user-or-ram-role.md)[RAM](grant-rbac-permissions-to-a-ram-user-or-ram-role.md)[角色授予](grant-rbac-permissions-to-a-ram-user-or-ram-role.md)[RBAC](grant-rbac-permissions-to-a-ram-user-or-ram-role.md)[权限](grant-rbac-permissions-to-a-ram-user-or-ram-role.md)。
该文章对您有帮助吗？
反馈
