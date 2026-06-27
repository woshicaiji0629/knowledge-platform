### 跨账号同步凭据
如果KMS实例（账号A中）与集群（账号B中）不在同一个阿里云账号中，可以通过ack-secret-manager组件将KMS凭据跨账号同步到集群中。下文通过RRSA认证机制，使ack-secret-manager组件能够获取跨账号访问KMS实例的权限。集群中的组件通过其OIDC提供商扮演账号A中的角色，从而获得对账号A中KMS实例的访问权限，并将该KMS实例导入到账号B的集群中。
账号A（KMS实例所在阿里云账号）权限配置
创建信任集群所在账号的RAM角色。具体操作，请参见[创建可信实体为阿里云账号的](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)[角色](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)。
重要
在选择信任主体名称时，选择其他云账号，填入账号B（集群所在的阿里云账号）的账号ID。
创建访问KMS服务凭据所需的权限策略。策略内容如下。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Action": [ "kms:GetSecretValue", "kms:Decrypt" ], "Resource": [ "*" ], "Effect": "Allow" }
为上一步创建的RAM角色授权。具体操作，请参见[为](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色授权](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
账号B（集群所在的阿里云账号）权限配置
在[容器服务管理控制台](https://cs.console.aliyun.com)开启集群的RRSA功能，用于创建集群的身份提供商信息。具体操作，请参见[启用](../../ack-managed-and-ack-dedicated/u
