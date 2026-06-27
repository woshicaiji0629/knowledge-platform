### 2. 配置Terraform身份认证
Terraform身份认证是指在通过Terraform操作阿里云基础设施之前，对阿里云Terraform Provider进行身份验证。只有在身份认证成功后，才能与阿里云API进行通信，并创建和管理阿里云的基础设施资源。阿里云Terraform Provider提供多种身份认证方式，有关更多身份认证信息，请参见相关文档[Terraform 身份认证](https://help.aliyun.com/zh/terraform/terraform-authentication)。
说明
您如果使用Terraform Explorer或者Cloud Shell，则无需手动配置身份认证信息，只需确保所登录的账号具有操作VPC和ECS的权限即可。
本文以在环境变量中使用RAM用户AccessKey配置身份认证为例：
由于阿里云账号（主账号）拥有资源的所有权限，其AccessKey一旦泄露风险巨大，所以建议您使用RAM用户的AccessKey。如何创建RAM用户的AccessKey，请参见[创建](../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../ram/documents/user-guide/create-an-accesskey-pair.md)。
在为RAM用户授予操作云服务器ECS及专有网络VPC相关资源的权限时，建议所授予的权限应遵循最小权限原则。有关如何为RAM用户进行授权的详细信息，请参见[管理](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。本文提供的示例代码需要创建ECS、VPC、交换机等资源，为便于执行本文中的示例，您可以为授予RAM用户以下权限：

| 云产品 | 授予权限 |
| --- | --- |
| 专有网络 VPC | 本示例选择系统策略：AliyunVPCFullAccess |
| 云服务器 ECS | 本示例选择系统策略：AliyunECSFullAccess |

创建环境变量，存放身份认证信息。
