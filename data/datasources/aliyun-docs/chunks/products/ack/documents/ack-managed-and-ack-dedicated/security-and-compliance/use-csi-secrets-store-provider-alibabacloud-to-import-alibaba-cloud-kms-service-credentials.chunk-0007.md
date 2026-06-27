](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[角色](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)。

| 配置项 | 描述 |
| --- | --- |
| 身份提供商类型 | OIDC 。 |
| 身份提供商 | 选择 ack-rrsa-<cluster_id>。其中，<cluster_id>为集群 ID。 |
| 条件 | oidc:iss：保持默认。 oidc:aud：保持默认。 oidc:sub：需手动添加该条件。 条件键：选择 oidc:sub 。 运算符：选择 StringEquals 。 条件值：填入 system:serviceaccount:<namespace>:<serviceAccountName> ，其中， <namespace> 为应用所在的命名空间。 <serviceAccountName> 为服务账户名称。根据本文测试应用的信息，此处需填入 system:serviceaccount:kube-system:csi-secrets-store-provider-alibabacloud 。 说明 建议将组件安装在默认的 kube-system 命名空间下。如将 csi-secrets-store-provider-alibabacloud 安装在其他的命名空间，请将 kube-system 替换为对应命名空间的名称。 |
