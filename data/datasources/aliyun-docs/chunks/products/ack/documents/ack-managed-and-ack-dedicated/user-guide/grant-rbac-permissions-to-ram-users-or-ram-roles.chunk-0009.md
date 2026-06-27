### 操作时遇到无权限错误码怎么办？
通过控制台或OpenAPI所做的部分操作缺少所需的RBAC权限时，将返回相应的无权限错误码。可参见下表解决。

| 错误码或错误信息 | 说明 | 解决方案 |
| --- | --- | --- |
| ForbiddenCheckControlPlaneLog | 查看控制面日志被拒绝。 | 为用户授予管理员或运维人员权限。 |
| ForbiddenHelmUsage | 执行 Helm 操作被拒绝。 | 为用户授予管理员权限。 |
| ForbiddenRotateCert | 证书轮换被拒绝。 | 为用户授予管理员权限。 |
| ForbiddenAttachInstance | 添加节点被拒绝。 | 为用户授予管理员或运维人员权限。 |
| ForbiddenUpdateKMSState | 修改集群 KMS 落盘加密状态被拒绝。 | 为用户授予管理员或运维人员权限。 |
| Forbidden get trigger | 获取应用触发器信息被拒绝。 | 为用户授予管理员、运维人员或开发人员权限。 |
| ForbiddenQueryClusterNamespace | 查询集群命名空间被拒绝。 | 为用户授予管理员、运维人员、开发人员或受限用户的权限。 |
