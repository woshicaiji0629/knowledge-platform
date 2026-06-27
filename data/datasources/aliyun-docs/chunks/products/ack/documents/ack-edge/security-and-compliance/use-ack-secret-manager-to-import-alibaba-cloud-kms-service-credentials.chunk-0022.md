创建自定义权限策略并为上一步账号B下创建的RAM角色授权。
创建ack-secret-manager导入KMS凭据时所需的权限策略。策略内容如下，具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Resource": "acs:ram:*:<account-id>:role/<role-name>" # KMS所在账号A下的RAM角色的ARN。 } ], "Version": "1" }
上述自定义策略中的Resource为角色ARN，其中，<account-id>为KMS实例所在的阿里云账号A的账号ID，<role-name>为账号A中创建的RAM角色名称。关于如何查看角色ARN，请参见[如何查看](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[RAM](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[角色的](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[ARN？](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)。
为上一步在账号B下创建的RAM角色授权。具体操作，请参见[为](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色授权](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
创建自定义资源SecretStore并部署。
使用以下内容，替换相关字段后，创建secretstore-ramrole.yaml文件。
{ACK-accountID}：替换为集群所在的阿里云账号B的账号ID。
{clusterID}：替换为集群ID。
{ACK-roleName}：替换为集群所在的阿里云账号B下创建的RAM角色的名称。
{KMS-accountID}：替换为KMS实例所在的阿里云账号A的账号ID
