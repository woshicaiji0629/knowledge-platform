### 为集群对应的Worker RAM角色添加权限
创建如下自定义权限策略。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Version": "1", "Statement": [ { "Action": [ "kms:GetSecretValue", "kms:Decrypt" ], "Resource": [ "*" ], "Effect": "Allow" } ] }
为集群的Worker RAM角色添加上一步创建的自定义权限。具体操作，请参见[为集群的](../../product-overview/product-changes-permissions-of-the-worker-ram-role-of-ack-managed-clusters-are-revoked.md)[Worker RAM](../../product-overview/product-changes-permissions-of-the-worker-ram-role-of-ack-managed-clusters-are-revoked.md)[角色授权](../../product-overview/product-changes-permissions-of-the-worker-ram-role-of-ack-managed-clusters-are-revoked.md)。
