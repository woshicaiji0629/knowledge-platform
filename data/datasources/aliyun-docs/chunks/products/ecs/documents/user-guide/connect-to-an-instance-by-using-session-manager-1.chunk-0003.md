00.0.0/16 | 用于访问云助手服务端。 |
| 允许 | 1 | 自定义 TCP | 443 | 100.0.0.0/8 | 访问 云助手 Agent 安装包所在服务器，用于安装或更新您的 云助手 Agent 。 |
| 允许 | 1 | 自定义 UDP | 53 | 0.0.0.0/0 | 用于解析域名。 |

此外，如果您计划仅通过会话管理连接实例，为了增加ECS实例的安全性，您可以取消放行安全组入方向上的SSH端口（默认22）或者RDP端口（默认3389）的规则。
RAM用户使用该功能需拥有相关权限
如果RAM用户需要在控制台使用会话管理连接实例，根据最小授权原则，需要具有以下权限。
ecs:StartTerminalSession：通过会话管理连接实例的权限，此外，可以通过Resource字段，限制RAM用户可连接（会话管理）的ECS实例。
ecs:DescribeCloudAssistantStatus：查询ECS实例是否需要安装云助手，该权限用于控制台在连接前进行校验。
ecs:DescribeUserBusinessBehavior：查询会话管理功能是否已经开启，该权限用于控制台在连接前进行校验。
ecs:ModifyCloudAssistantSettings（可选）：打开或关闭会话管理的权限，如果当前阿里云账号已经开通会话管理，无需分配该权限。
自定义权限策略示例如下：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "ecs:StartTerminalSession", "Resource": "*" }, { "Effect": "Allow", "Action": [ "ecs:DescribeUserBusinessBehavior", "ecs:DescribeCloudAssistantStatus", "ecs:ModifyCloudAssistantSettings" ], "Resource": "*" } ] }
为RAM用户授权，请参见[为](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
