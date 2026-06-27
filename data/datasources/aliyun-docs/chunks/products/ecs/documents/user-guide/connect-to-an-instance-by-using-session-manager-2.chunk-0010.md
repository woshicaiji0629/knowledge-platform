: "1" }
通过赋予子账号如下的权限策略，可以禁止RAM用户以testUser1、testUser2创建Session Manager。
{ "Statement": [ { "Effect": "Allow", "Action": [ "ecs:StartTerminalSession" ], "Resource": [ "acs:ecs:*:*:instance/*" ], "Condition": { "StringNotEqualsIgnoreCase": { "ecs:SessionStartAs": [ "testUser1", "testUser2" ] } } } ], "Version": "1" }
为RAM用户授权，请参见[为](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
