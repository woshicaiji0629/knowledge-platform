创建自定义权限策略并为上一步创建的RAM角色授权。
创建指定导入KMS凭据时所需的权限策略。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Version": "1", "Statement": [ { "Action": [ "kms:GetSecretValue", "kms:Decrypt" ], "Resource": "acs:kms:<REGION_ID>:<ACCOUNT_ID>:secret/xxxx", // 指定的KMS凭据ARN "Effect": "Allow" } ] }
为上一步创建的RAM角色授权。具体操作，请参见[为](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色授权](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
在指定命名空间下创建访问指定KMS凭据管家的独立ServiceAccount。注意ServiceAccount需要添加键值为ack.alibabacloud.com/role-arn的指定annotation，值为该ServiceAccount绑定的目标RAM角色ARN。
apiVersion: v1 kind: ServiceAccount metadata: annotations: ack.alibabacloud.com/role-arn: acs:ram::<ACCOUNT_ID>:role/<ROLE_NAME> # RAM角色的ARN name: <SERVICEACCOUNT_NAME> # 需与RAM角色配置的oidc:sub条件值<SERVICEACCOUNT_NAME>保持一致 namespace: <NAMESPACE> # 需与RAM角色配置的oidc:sub条件值<NAMESPACE>保持一致
使用serviceAccountRef认证方式部署自定义资源SecretStore。
基于以下内容，替换相关字段后，创建secretstore-rrsa.yaml文件。
<NAME>：替换为指定的SecretStore实例名称。
<NAMESPACE>：替换为指定的集群命名空间名称。
<SERVICEACCOUNT_NAME>：替换为上一步中创建的ServiceAccount实例名称。
apiVersion: alibabacloud.
