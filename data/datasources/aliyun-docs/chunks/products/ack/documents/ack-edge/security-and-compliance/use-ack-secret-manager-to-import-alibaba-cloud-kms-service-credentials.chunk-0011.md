### 为集群对应的Worker RAM角色添加权限
由于ACK Serverless集群没有绑定Worker RAM角色，该方式只适用于ACK托管集群、ACK专有集群和ACK One注册集群。
创建如下自定义权限策略。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Action": [ "kms:GetSecretValue", "kms:Decrypt" ], "Resource": [ "*" ], "Effect": "Allow" }
为集群的Worker RAM角色添加上一步创建的自定义权限。具体操作，请参见[为集群的](../../product-overview/product-changes-permissions-of-the-worker-ram-role-of-ack-managed-clusters-are-revoked.md)[Worker RAM](../../product-overview/product-changes-permissions-of-the-worker-ram-role-of-ack-managed-clusters-are-revoked.md)[角色授权](../../product-overview/product-changes-permissions-of-the-worker-ram-role-of-ack-managed-clusters-are-revoked.md)。
