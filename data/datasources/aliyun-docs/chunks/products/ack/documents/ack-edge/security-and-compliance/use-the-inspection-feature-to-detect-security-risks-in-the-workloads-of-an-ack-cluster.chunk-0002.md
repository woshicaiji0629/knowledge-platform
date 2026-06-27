./../../sls/documents/use-custom-policies-to-grant-permissions-to-a-ram-user.md)。
展开查看日志服务日志读取授权代码
{ "Version": "1", "Statement": [ { "Action": [ "log:Get*", "log:List*" ], "Resource": "acs:log:*:*:project/<指定的Project名称>/*", "Effect": "Allow" } ] }
RBAC授权
请完成配置巡检页面涉及资源的RBAC授权，授予RAM用户指定集群的管理员权限，以确保RAM用户拥有操作配置巡检页面中涉及的Kubernetes资源的权限。具体操作，请参见[使用](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[RBAC](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[授予集群内资源操作权限](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)。
