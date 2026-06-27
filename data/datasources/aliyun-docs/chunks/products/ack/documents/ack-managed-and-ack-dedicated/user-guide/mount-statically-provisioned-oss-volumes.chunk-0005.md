](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[角色](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)。

| 配置项 | 描述 |
| --- | --- |
| 身份提供商类型 | OIDC 。 |
| 身份提供商 | 选择 ack-rrsa-<cluster_id> 。其中， <cluster_id> 为集群 ID。 |
| 条件 | 手动添加 oidc:sub。 条件键：选择 oidc:sub 。 运算符：选择 StringEquals 。 条件值：默认输入 system:serviceaccount:ack-csi-fuse:csi-fuse-ossfs 。 ack-csi-fuse ：ossfs 客户端所在的命名空间，不支持自定义。 csi-fuse-ossfs ：ServiceAccount 名称。 如需修改，请参见 [如何在](faq-about-oss-volumes-1.md) [RRSA](faq-about-oss-volumes-1.md) [鉴权方式中使用指定的](faq-about-oss-volumes-1.md) [ARNs](faq-about-oss-volumes-1.md) [或](faq-about-oss-volumes-1.md) [ServiceAccount？](faq-about-oss-volumes-1.md) 。 |
| 角色名称 | 本示例为 demo-role-for-rrsa。 |
