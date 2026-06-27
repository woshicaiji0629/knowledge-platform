### 通过设置AK扮演指定RAM角色
适用于所有容器服务Kubernetes集群。
创建可信实体为阿里云账号的RAM角色，以供csi-secrets-store-provider-alibabacloud组件使用。具体操作，请参见[创建可信实体为阿里云账号的](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)[角色](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)。
说明
在选择信任主体名称时，请选择当前云账号。
创建自定义授权策略并为上一步已创建的RAM角色授权。
创建访问KMS服务凭据所需的权限策略。策略内容如下。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Action": [ "kms:GetSecretValue", "kms:Decrypt" ], "Resource": [ "*" ], "Effect": "Allow" }
为上一步已创建的RAM角色授权。具体操作，请参见[管理](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
创建扮演上述角色的自定义授权策略，并为指定的RAM用户授权。
创建扮演上述角色的自定义授权策略。策略内容如下。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Resource": "acs:ram:*:<account-id>:role/<role-name>" } ], "Version": "1
