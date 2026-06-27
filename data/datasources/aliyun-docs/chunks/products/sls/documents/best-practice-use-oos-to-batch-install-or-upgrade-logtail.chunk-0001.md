## 前提条件
至少拥有一台阿里云ECS服务器。
使用RAM用户操作时，该RAM用户需具备如下权限。
AliyunOOSFullAccess权限：为RAM用户授予AliyunOOSFullAccess权限的具体操作，请参见[管理](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
自定义权限：为RAM用户授予如下自定义权限时，需要先创建自定义策略并为RAM用户授权。具体操作，请参见[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)、[管理](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ecs:DescribeTagKeys", "ecs:DescribeTags", "ecs:DescribeInstances", "ecs:DescribeInvocationResults", "ecs:RunCommand", "ecs:DescribeInvocations" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "oos:ListTemplates", "oos:StartExecution", "oos:ListExecutions", "oos:GetExecutionTemplate", "oos:ListExecutionLogs", "oos:ListTaskExecutions" ], "Resource": "*" } ] }
