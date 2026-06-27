## 注意事项

| 注意项 | 说明 |
| --- | --- |
| 计费说明 | ACK 托管集群基础版 迁移至 ACK 托管集群 Pro 版 后，将新增 [集群管理费用](../product-overview/cluster-management-fee.md) （由 ACK 收取），其他云资源计费保持不变。 |
| 集群版本 | 仅支持 1.18 及以上版本的集群。迁移后，集群版本不变。关于集群版本机制，请参见 [版本说明](support-for-kubernetes-versions.md) 。 集群迁移不支持回退，即不能将 ACK 托管集群 Pro 版 迁移为 ACK 托管集群基础版 。若集群迁移失败，系统会自动回滚。 迁移后，集群版本保持不变。如同时有迁移集群和升级集群版本的需求，建议先完成迁移，再 [升级集群版本](update-the-kubernetes-version-of-an-ack-cluster.md) 。 |
