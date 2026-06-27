### 控制台
创建流程
说明
如需使用RAM用户在控制台创建集群，需配置对应的权限后才能正常使用，请参见[容器服务控制台权限依赖](ack-console-permission-dependencies.md)完成精细化授权。
您可以参见控制台指引，基于ACK默认的集群配置创建一个集群。如果您想更细粒度地控制集群配置，请参见[ACK](description-of-configuration-items-for-ack-managed-clusters.md)[托管集群配置项说明](description-of-configuration-items-for-ack-managed-clusters.md)了解并启用对应配置项。下文介绍流程概览。
步骤一：进入创建页面
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在页面左侧顶部，选择目标资源所在的资源组和地域。
在集群列表页面，单击创建集群。在ACK 托管集群页面，按照页面指引完成集群配置、节点池配置、组件配置。
下文步骤未开启智能托管模式。如需使用，请参见[创建](create-ack-managed-clusters-in-auto-mode.md)[ACK](create-ack-managed-clusters-in-auto-mode.md)[托管集群（智能托管模式）](create-ack-managed-clusters-in-auto-mode.md)。
步骤二：配置集群

| 配置类型 | 说明 | 示例样式 |
| --- | --- | --- |
| 基础配置 | 集群的基础信息，包括名称、规格、地域、版本等。支持启用集群版本自动升级，并配置计划执行的维护窗口。 |  |
| 网络配置 | IPv6 双栈开关、VPC 和 vSwitch 配置、是否允许通过公网访问 API Server、安全组、网络插件、网段配置等。 推荐集群 VPC 使用标准私有地址（如 10.0.0.0/8、172.16.0.0/12 和 192.168.0.0/16）。如有特殊需求，请前往 [配额中心](https://quotas.console.aliyun.com/white-list-products/csk/quotas) 申请（ 使用公网网段 VPC 创建集群 ）。 |  |
| 高级配置 | 集群资源管理、集群安全相关的配置。 |  |
