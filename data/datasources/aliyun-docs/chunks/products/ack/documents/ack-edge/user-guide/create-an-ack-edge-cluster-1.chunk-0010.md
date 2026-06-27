| 配置项 | 描述 |
| --- | --- |
| 集群删除保护 | 推荐开启，防止通过控制台或 OpenAPI 误删除集群。 |
| 资源组 | 将集群归属于选择的 [资源组](../../../../ecs/documents/user-guide/resource-groups.md) ，便于权限管理和成本分摊。 一个资源只能归属于一个资源组。 |
| 标签 | 为集群绑定键值对 [标签](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview) ，作为云资源的标识。 |
| Secret 落盘加密 | 选中 选择 KMS 密钥 可以使用在阿里云 [KMS](../../../../kms/documents/product-overview/what-is-kms.md) 中创建的密钥加密 Kubernetes Secret 密钥。使用说明，请参见 [使用阿里云](../security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) [KMS](../security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) [进行](../security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) [Secret](../security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) [的落盘加密](../security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) 。 |
| RRSA OIDC | 集群将创建一个 OIDC Provider。利用其 ServiceAccount 的临时 OIDC Token，应用 Pod 可以调用阿里云 RAM 服务并扮演指定 RAM 角色，从而安全地获取访问云资源的临时授权，实现 Pod 级别的权限最小化管理。 如需后续启用，请参见 [通过](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [RRSA](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-diff
