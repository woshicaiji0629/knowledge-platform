### 权限策略示例
示例一：在控制台使用会话管理
如果RAM用户需要在控制台使用会话管理连接实例，根据最小授权原则，需要具有以下权限。
ecs:StartTerminalSession：通过会话管理连接实例的权限，此外，可以通过Resource字段，限制RAM用户可连接（会话管理）的ECS实例。
ecs:DescribeCloudAssistantStatus：查询ECS实例是否需要安装云助手，该权限用于控制台在连接前进行校验。
ecs:DescribeUserBusinessBehavior：查询会话管理功能是否已经开启，该权限用于控制台在连接前进行校验。
ecs:ModifyCloudAssistantSettings（可选）：打开或关闭会话管理的权限，如果当前阿里云账号已经开通会话管理，无需分配该权限。
自定义权限策略示例如下：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "ecs:StartTerminalSession", "Resource": "*" }, { "Effect": "Allow", "Action": [ "ecs:DescribeUserBusinessBehavior", "ecs:DescribeCloudAssistantStatus", "ecs:ModifyCloudAssistantSettings" ], "Resource": "*" } ] }
为RAM用户授权，请参见[为](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
示例二：通过ali-instance-cli使用会话管理
在使用ali-instance-cli工具时，配置阶段要求设置RAM用户的AccessKey、STS Token。当通过会话管理操作连接实例时，系统会验证此凭证对应的RAM用户是否拥有ecs:StartTerminalSession权限，这是允许通过会话管理建立与ECS实例连接的必要权限。
此外，在自定义权限策略时，可以通过指定Resource字段来限定RAM用户能够通过会话管理连接的具体ECS实例。权限策略示例如下：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "
