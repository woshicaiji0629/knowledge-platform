### RBAC预置角色不满足需求，如何创建自定义权限？
可通过编写YAML来创建自定义Role或ClusterRole。例如，创建一个只允许查看Pod的ClusterRole，然后在授权时选择自定义权限并绑定对应的ClusterRole。具体操作，请参见[使用自定义](customize-an-rbac-role.md)[RBAC](customize-an-rbac-role.md)[限制集群内资源操作](customize-an-rbac-role.md)。
RBAC的权限策略仅支持允许（Allow）访问资源，不支持显式拒绝（Deny）访问资源。
