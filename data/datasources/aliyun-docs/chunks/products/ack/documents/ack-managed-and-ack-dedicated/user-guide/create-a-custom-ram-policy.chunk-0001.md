## 使用系统策略授权
系统策略授权用于指定全局资源的读写访问控制。当RAM用户或RAM角色需要阿里云账号下所有集群的运维管理权限时，建议使用系统策略进行快捷授权。容器服务ACK的常用系统策略如下表所示：
重要
系统策略中Full级别的权限为高风险权限，请谨慎授予，以免造成安全风险。
展开查看容器服务ACK常用系统策略

| 系统策略名称 | 说明 |
| --- | --- |
| AliyunCSFullAccess | 当 RAM 用户或 RAM 角色需要容器服务产品所有 OpenAPI 的访问权限。 说明 此系统策略仅包含针对 ACK 产品的 RAM 授权。如您需要对 ACK 集群中的应用进行运维，还需要进行 RBAC 授权，请参见 [RBAC](authorization-overview.md) [授权](authorization-overview.md) 。 |
| AliyunVPCReadOnlyAccess | 当 RAM 用户或 RAM 角色在创建集群时选择指定 VPC。 |
| AliyunECSReadOnlyAccess | 当 RAM 用户或 RAM 角色为集群添加已有节点或查看节点详细信息。 |
| AliyunContainerRegistryFullAccess | 当 RAM 用户或 RAM 角色需要全局管理阿里云账号内的业务镜像。 |
| AliyunLogReadOnlyAccess | 当 RAM 用户或 RAM 角色在创建集群时选择已有 Log Project 存储审计日志，或查看指定集群的配置巡检。 |
| AliyunAHASReadOnlyAccess | 当 RAM 用户或 RAM 角色需要使用集群拓扑功能。 |
| AliyunRAMFullAccess | 当 RAM 用户或 RAM 角色需要负责阿里云账号内的全局授权管理。 |
| AliyunYundunSASReadOnlyAccess | 当 RAM 用户或 RAM 角色需要查看指定集群的运行时安全监控。 |
| AliyunARMSReadOnlyAccess | 当 RAM 用户或 RAM 角色需要查看集群阿里云 Prometheus 插件的监控状态。 |
| AliyunKMSReadOnlyAccess | 当 RAM 用户或 RAM 角色在创建 Pro 集群时启用 Secret 落盘加密能力。 |
| AliyunESSReadOnlyAccess | 当 RAM 用户或 RAM 角色需要执行节点池的相关操作，例如查看、编辑和扩缩容等。 |
