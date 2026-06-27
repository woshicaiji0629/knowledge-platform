](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[角色](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)。

| 配置项 | 描述 |
| --- | --- |
| 身份提供商类型 | OIDC 。 |
| 身份提供商 | 选择 ack-rrsa-<CLUSTER_ID>。其中，<CLUSTER_ID>为集群 ID。 |
| 条件 | oidc:iss：保持默认。 oidc:aud：保持默认。 oidc:sub：需手动添加该条件。 条件键：选择 oidc:sub 。 运算符：选择 StringEquals 。 条件值：输入 system:serviceaccount:<NAMESPACE>:<SERVICEACCOUNT_NAME> 。其中 <NAMESPACE> 为指定 ServiceAccount 的命名空间，<SERVICEACCOUNT_NAME>为服务账户 ServiceAccount 的名称。 说明 其中 <NAMESPACE> 和 <SERVICEACCOUNT_NAME> 需要与 [4. 在指定命名空间下创建访问指定](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) [KMS](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) [凭据管家的独立](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) [ServiceAccount](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) 中的配置保持一致。 |
