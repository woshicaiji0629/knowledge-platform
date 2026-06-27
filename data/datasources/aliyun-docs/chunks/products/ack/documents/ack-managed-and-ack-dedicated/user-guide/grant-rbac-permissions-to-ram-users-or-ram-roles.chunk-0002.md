### Kubernetes RBAC 机制
ClusterRole：定义一个在整个集群范围生效的权限集合，再通过ClusterRoleBinding将其绑定至授权主体，使其权限在整个集群内生效。
Role：定义一个仅在单个命名空间内有效的权限集合，再通过RoleBinding将其绑定至授权主体，使其权限仅在当前命名空间内生效。
