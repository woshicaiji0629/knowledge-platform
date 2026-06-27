-a-custom-policy.md)。
{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Resource": "acs:ram:*:<account-id>:role/<role-name>" } ], "Version": "1" }
上述自定义策略中的Resource为角色ARN，其中，<ACCOUNT_ID>为阿里云账号ID，<ROLE_NAME>为RAM角色名称。关于如何查看角色ARN，请参见[如何查看](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[RAM](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[角色的](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[ARN？](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)。
将上述自定义策略授权给RAM用户，便可以指定具体可以扮演的RAM角色。关于如何为RAM用户授权，请参见[管理](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
在集群中创建名为alibaba-credentials的Secret，配置模板如下，需要替换部分字段。
使用以下内容，替换相关字段后，创建alibaba-credentials.yaml文件。
{rolearn}：替换为[步骤](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[1](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)已创建的RAM角色的ARN（需要Base64编码）。
{ak}：替换
