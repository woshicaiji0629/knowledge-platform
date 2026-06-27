权](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
说明
如果 RAM 用户或 RAM 角色已被授予 AliyunCSFullAccess 权限，则无需额外进行ram:PassRole授权。
RAM 权限策略示例如下：

| 授权使用特定的 RAM 角色 | 授权使用所有 RAM 角色 |
| --- | --- |
| { "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "ram:PassRole", "Resource": [ "<role_arn>" // 替换为 RAM 角色的 ARN。 ], "Condition": { "StringEquals": { "acs:Service": [ "cs.aliyuncs.com" ] } } } ] } 请参见 [如何查看](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md) [RAM](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md) [角色的](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md) [ARN？](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md) 获取 RAM 角色 ARN。 | { "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "ram:PassRole", "Resource": "*", "Condition": { "StringEquals": { "acs:Service": [ "cs.aliyuncs.com" ] } } } ] } |
