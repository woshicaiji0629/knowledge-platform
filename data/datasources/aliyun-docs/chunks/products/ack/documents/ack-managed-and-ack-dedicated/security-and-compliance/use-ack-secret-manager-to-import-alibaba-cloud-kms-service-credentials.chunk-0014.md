COUNT_NAME> 为服务账户名称。根据本文测试应用的信息，此处需填入 system:serviceaccount:kube-system:ack-secret-manager 。 说明 如果将 ack-secret-manager 安装在其他的命名空间，请将 kube-system 替换为对应命名空间的名称。 |

创建自定义权限策略并为上一步创建的RAM角色授权。
创建ack-secret-manager导入KMS凭据时所需的权限策略。策略内容如下。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Version": "1", "Statement": [ { "Action": [ "kms:GetSecretValue", "kms:Decrypt" ], "Resource": [ "*" ], "Effect": "Allow" } ] }
为上一步创建的RAM角色授权。具体操作，请参见[为](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色授权](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
创建自定义资源SecretStore关联对应的认证方式并部署。
使用以下内容，替换相关字段后，创建secretstore-rrsa.yaml文件。
<ACCOUNT_ID>：替换为同步KMS凭据的阿里云账号ID。
<CLUSTER_ID>：替换为集群ID。
<ROLE_NAME>：替换为[步骤](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[2](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)中创建的RAM角色名称。
apiVersion: alibabacloud.com/v1alpha1 kind: SecretStore metadata: name: scdemo-rrsa spec: KMS: KMSAuth: oidcProviderARN: "acs:ram::<ACCOUNT_ID>:oidc-provider/ack-rrsa-<CLUSTER_ID>" ramRoleARN: "acs:ram::<ACCOUNT_ID>:role/<ROLE_NAME>"
执行以下命令，部署SecretStore。
kubectl apply -f secretstore-rrsa.yaml
