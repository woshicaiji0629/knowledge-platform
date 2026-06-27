### 使用RAM权限策略
您可以通过RAM访问控制策略，对专有网络VPC的访问权限进行控制。
权限用来描述用户、用户组、角色对具体资源的访问能力，策略是具体授权的方法。您可以通过RAM权限策略，决定哪些用户或角色可以访问哪些资源，或执行哪些操作。
权限策略配置
您可以通过以下常用的权限策略对VPC的访问权限进行控制。关于VPC的权限定义，请参见[授权信息（VPC）](developer-reference/api-vpc-2016-04-28-ram.md)和[授权信息（VPC](developer-reference/api-vpcpeer-2022-01-01-ram.md)[对等连接）](developer-reference/api-vpcpeer-2022-01-01-ram.md)。

| 权限策略 | 描述 |
| --- | --- |
| AliyunVPCFullAccess | 为 RAM 用户授予 VPC 的完全管理权限。 |
| AliyunVPCReadOnlyAccess | 为 RAM 用户授予 VPC 的只读访问权限。 |

您可以为用户创建系统权限策略，当系统权限策略不能满足您的要求时，您可以创建自定义权限策略。关于如何创建自定义权限策略，请参见[通过](../../ram/documents/use-cases/use-ram-roles-to-manage-vpc-permissions.md)[RAM](../../ram/documents/use-cases/use-ram-roles-to-manage-vpc-permissions.md)[对](../../ram/documents/use-cases/use-ram-roles-to-manage-vpc-permissions.md)[VPC](../../ram/documents/use-cases/use-ram-roles-to-manage-vpc-permissions.md)[进行权限管理](../../ram/documents/use-cases/use-ram-roles-to-manage-vpc-permissions.md)。
该文章对您有帮助吗？
反馈
