### 如何手动为CSI授权？
CSI在执行存储卷的挂载、卸载、创建、删除等操作时，需要被授予访问其他产品资源的相应权限。通常情况下，集群已默认安装CSI且配置相关权限。如需手动授权，可参见以下内容。
使用RAM角色授权（默认）：CSI使用AliyunCSManagedCsiRole角色来访问其他云产品资源，详见[容器服务](ack-default-roles.md)[ACK](ack-default-roles.md)[服务角色](ack-default-roles.md)。
ACK托管集群：CSI使用的RAM角色权限的Token被保存在名为addon.csi.token的Secret中。可挂载该Secret，从而实现RAM角色授权。
ACK专有集群：CSI继承其Pod所在节点的RAM角色。
关于如何为RAM角色授权，请参见[管理](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
使用AccessKey授权
通过环境变量：将AccessKey创建为Kubernetes Secret，再通过环境变量的方式注入到CSI的Pod中，避免在部署模板中明文暴露密钥。
直接写入YAML：直接在CSI的YAML中写入AccessKey信息。不推荐在生产环境使用。
