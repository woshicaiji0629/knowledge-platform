限，这是允许通过会话管理建立与ECS实例连接的必要权限。
此外，在自定义权限策略时，可以通过指定Resource字段来限定RAM用户能够通过会话管理连接的具体ECS实例。权限策略示例如下：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "ecs:StartTerminalSession", "Resource": "*" } ] }
关于CredentialsURI、STS Token的更多说明，请参见[创建](../../../ram/documents/create-an-accesskey-pair-1.md)[AccessKey](../../../ram/documents/create-an-accesskey-pair-1.md)、[什么是](../../../ram/documents/user-guide/what-is-sts.md)[STS](../../../ram/documents/user-guide/what-is-sts.md)。
为RAM用户授权，请参见[为](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
示例三：通过RAM策略限制可以使用会话管理功能的用户
通过赋予子账号如下的权限策略，可以限制RAM用户只能以testUser1、testUser2创建Session Manager。
{ "Statement": [ { "Effect": "Allow", "Action": [ "ecs:StartTerminalSession" ], "Resource": [ "acs:ecs:*:*:instance/*" ], "Condition": { "StringEquals": { "ecs:SessionStartAs": [ "testUser1", "testUser2" ] } } } ], "Version": "1" }
通过赋予子账号如下的权限策略，可以禁止RAM用户以testUser1、testUser2创建Session Manager。
{ "Statement": [ { "Effect": "Allow", "Action": [ "ecs:StartTerminalSession" ], "Resource
