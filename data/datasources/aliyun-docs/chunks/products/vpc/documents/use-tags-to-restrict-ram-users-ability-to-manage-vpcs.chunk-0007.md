可防止后续添加其他策略（如 vpc:）时意外授予标签修改权限。 // 创建资源时通过 Create 类API的 Tag 参数指定标签，由Statement 2授权允许，不受Statement 6影响。 "Effect": "Deny", "Action": [ "vpc:TagResources", "vpc:UnTagResources" ], "Resource": "*" } ] }
[为](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)： 资源范围选择账号级别，授权主体选择需要添加权限的RAM用户，权限策略选择自定义策略VpcTagAccessPolicy。
API
使用阿里云主账号（管理员）完成：
调用[CreateUser](../../ram/documents/developer-reference/api-ram-2015-05-01-createuser.md)创建 RAM 用户。
调用[TagResources](https://help.aliyun.com/zh/resource-management/tag/developer-reference/api-tag-2018-08-28-tagresources)为 VPC 创建并绑定标签。
调用[CreatePolicy](../../ram/documents/developer-reference/api-ram-2015-05-01-createpolicy.md)创建自定义权限策略。
调用[AttachPolicyToUser](../../ram/documents/developer-reference/api-ram-2015-05-01-attachpolicytouser.md)为 RAM 用户授权。
