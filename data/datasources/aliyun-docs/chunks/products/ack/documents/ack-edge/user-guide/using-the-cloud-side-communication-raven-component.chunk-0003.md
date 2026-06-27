## 基于raven-agent-ds配置通信模式和访问控制白名单
ACK Edge集群安装时，会自动安装raven-agent-ds组件，并默认启动代理模式。您可以自行同步配置通信模式（代理模式、隧道模式）并设置边缘网关节点的访问控制白名单。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。
搜索并定位raven-agent-ds，在目标卡片区域，单击配置，然后完成相关参数配置。

| 配置项 | 说明 |
| --- | --- |
| controller | Raven 组件是否开启代理模式 （推荐配置）：代理模式，构建反向代理通道，实现跨域主机网络通信。 Raven 组件是否开启隧道模式 ：隧道模式仅支持节点间网络互通的节点池。通过构建 VPN 隧道，实现跨域容器网络通信，主要支持云边容器 Metrics 监控。 重要 由于跨域通信通过公网传输，可能存在数据丢失风险，请勿传输重要业务数据。如在使用过程中遇到问题或有相关产品建议，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 联系容器服务团队。 关于两种通信模式的更多信息，请参见 [跨域运维通信组件](cloud-edge-communication-component-raven-overview.md) [Raven](cloud-edge-communication-component-raven-overview.md) 。 |
| accessControlListEntry | 访问控制白名单条目。放行的边缘网关节点可以与云上构建隧道，增强网络安全性。 采用 CIDR 标准格式，固定 IP 地址以“ /32 ”为掩码，多个地址之间使用英文半角逗号（,）分隔。不填写时，表示所有源地址均可被负载均衡放行访问云上服务。 如果您添加 ACL 条目，请放行 CLB 健康检查 IP 地址段 100.64.0.0/10 。 |
