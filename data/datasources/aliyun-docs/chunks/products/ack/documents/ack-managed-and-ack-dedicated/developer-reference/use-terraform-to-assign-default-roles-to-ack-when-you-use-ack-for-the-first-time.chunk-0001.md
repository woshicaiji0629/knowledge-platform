## 前提条件
由于阿里云账号（主账号）具有资源的所有权限，一旦发生泄露将面临重大风险。建议您使用RAM用户，并为该RAM用户创建AccessKey，具体操作方式请参见[创建](../../../../ram/documents/user-guide/create-a-ram-user.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-user.md)[用户](../../../../ram/documents/user-guide/create-a-ram-user.md)和[创建](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)。
为运行Terraform命令的RAM用户绑定以下最小权限策略，以获取管理本示例所涉及资源的权限。更多信息，请参见[为](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
该权限策略允许RAM用户创建、查看和删除RAM角色，并支持对RAM角色权限策略的管理。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ram:GetRole", "ram:ListRoles", "ram:AttachPolicyToRole", "ram:ListPoliciesForRole", "ram:CreateRole", "ram:DetachPolicyFromRole", "ram:DeleteRole" ], "Resource": "*" } ] }
准备Terraform运行环境，您可以选择以下任一方式来使用Terraform。
[在](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)[Terraform Explorer](https://help.aliyun.com/zh/terraform/using-terraform-in
