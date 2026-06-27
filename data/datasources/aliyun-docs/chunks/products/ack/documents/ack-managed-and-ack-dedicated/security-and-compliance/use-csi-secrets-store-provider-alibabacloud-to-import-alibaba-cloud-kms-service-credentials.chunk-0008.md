:csi-secrets-store-provider-alibabacloud 。 说明 建议将组件安装在默认的 kube-system 命名空间下。如将 csi-secrets-store-provider-alibabacloud 安装在其他的命名空间，请将 kube-system 替换为对应命名空间的名称。 |

创建自定义授权策略并为上一步创建的RAM角色授权。
创建csi-secrets-store-provider-alibabacloud导入KMS凭据时所需的权限策略。策略内容如下。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Action": [ "kms:GetSecretValue", "kms:Decrypt" ], "Resource": [ "*" ], "Effect": "Allow" }
为上一步创建的RAM角色授权。具体操作，请参见[管理](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
在集群中创建名为alibaba-credentials的Secret，配置模板如下，需要替换部分字段。
使用以下内容，替换相关字段后，创建secretstore-rrsa.yaml文件。
{rolearn}：替换为[步骤](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[2](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)创建的RAM角色的ARN（需要Base64编码）。
{oidcproviderarn}：替换为集群开启RRSA后生成的提供商ARN（需要Base64编码）。
apiVersion: v1 data: rolearn: {rolearn} oidcproviderarn: {oidcproviderarn} kind: Secret metadata: name: alibaba-credentials namespace: kube-system type: Opaque
执行以下命令，部署Secret。
kubectl apply -f secretstore-rrsa.yaml
