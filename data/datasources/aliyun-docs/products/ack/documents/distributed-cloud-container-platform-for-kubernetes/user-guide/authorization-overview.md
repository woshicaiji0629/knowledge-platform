# 权限类型角色与策略详解-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/distributed-cloud-container-platform-for-kubernetes/user-guide/authorization-overview

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/product-overview.md)

- [快速入门](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/getting-started.md)

- [操作指南](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide.md)

- [实践教程](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases.md)

- [开发参考](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/developer-reference.md)

- [服务支持](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/support.md)

[首页](https://help.aliyun.com/zh)

# 授权概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

根据权限类型，分布式云容器平台 ACK One的权限包括服务角色、RAM权限策略和RBAC权限。您需要为服务账号授予对应的权限，才能正常使用分布式云容器平台 ACK One的功能。本文将为您介绍服务角色、RAM权限策略和RBAC权限关系，以及如何为服务账号授予相应权限。

## 权限类型

| 权限类型 | 是否必须授权 | 权限说明 |
| --- | --- | --- |
| [服务角色](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/authorization-overview.md) | 首次使用 ACK One 服务时需要授权，使用阿里云账号（主账号）或者 [RAM](products/ram/documents/create-admin-user.md) [管理员账号](products/ram/documents/create-admin-user.md) （子账号）授权一次即可。 | 授权后，ACK One 服务才能访问其他关联云服务资源。 |
| [RAM](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/authorization-overview.md) [系统权限策略](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/authorization-overview.md) | RAM 用户或 RAM 角色必须授权，阿里云账号默认拥有权限，无需额外授权。 | 授权后，RAM 用户或 RAM 角色才能使用 ACK One 的功能。 |
| [RBAC](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/authorization-overview.md) [权限](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/authorization-overview.md) | RAM 用户或 RAM 角色必须授权，阿里云账号默认拥有权限，无需额外授权。 | 授权后，RAM 用户或 RAM 角色才能对 ACK One 集群内的 K8s 资源进行操作。 |


## 服务角色

服务角色是云服务在特定情况下，为完成功能而获取其他云服务访问权限的RAM角色。

例如，ACK One上创建工作流集群后，需要创建弹性容器ECI实例运行工作流，因此需要拥有创建ECI实例的相应权限。

ACK One提供以下服务角色，具体的策略内容请参见[ACK One](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/manage-the-service-linked-role-for-ack-one.md)[服务角色策略内容](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/manage-the-service-linked-role-for-ack-one.md)。

- 

- 

- 

- 

- 

- 

- 

- 

| 角色名称 | 角色权限说明 |
| --- | --- |
| AliyunCSDefaultRole | ACK One 在集群管控操作中使用该角色访问您在 ECS、VPC、SLB、ROS、ESS 等服务中的资源。 必须授予该角色的权限，授权后才能正常使用 ACK One 功能。 |
| AliyunServiceRoleForAdcp | ACK One 在集群管控操作中使用该角色访问您在 ECS、VPC、SLB 等相关云服务中的资源。 必须授予该角色的权限，授权后才能正常使用 ACK One 功能。 |
| AliyunAdcpServerlessKubernetesRole | ACK One 多集群舰队和分布式工作流 Argo 集群需要使用该角色，访问 VPC、ECS、PrivateZone、ECI、SLS 等服务中的资源。 必须授予该角色的权限，授权后才能正常使用 ACK One 功能。 |
| AliyunAdcpManagedMseRole | ACK One 多集群舰队需要使用该角色访问 MSE 等服务中的资源。 该角色权限仅在使用 [多集群网关](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/manage-multi-cluster-gateways.md) 功能时需要授权，未授权不影响其他功能使用。 |
| AliyunCSManagedKubernetesRole | ACK One 多集群舰队需要使用该角色访问 ACK 服务的资源。 |
| AliyunCSManagedLogRole | ACK One 中日志组件使用此角色来访问您在其他云产品中的资源。 |
| AliyunCSManagedCmsRole | ACK One 中的 CMS 组件使用此角色来访问您在其他云产品中的资源。 |
| AliyunCSManagedArmsRole | ACK One 中的 Arms 插件使用此角色来访问您在其他云产品中的资源。 |


服务角色无需手动创建，首次使用[ACK One](https://cs.console.aliyun.com/one)[控制台](https://cs.console.aliyun.com/one)，界面会自动弹出授权提示，您只需按提示操作即可完成授权。

重要

仅阿里云账号（主账号）或[RAM](products/ram/documents/create-admin-user.md)[管理员账号](products/ram/documents/create-admin-user.md)可以完成自动授权，普通RAM用户没有授权操作的权限。如果系统提示权限不足，请将账号切换到阿里云（主账号）或RAM管理员账号完成授权。

## RAM系统权限策略

默认情况下，RAM用户在使用云服务的OpenAPI时没有任何权限。如果您通过RAM用户或RAM角色访问ACK One，需要为其授予相应的操作权限，以确保正常使用ACK One的功能。ACK One提供了一些默认的系统权限策略，用于控制全局资源的读写访问，您可以根据业务需求为RAM用户或RAM角色添加相应的系统策略。

具体授权操作，请参见[为](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/grant-system-permissions-to-ram-users-or-ram-roles.md)[RAM](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/grant-system-permissions-to-ram-users-or-ram-roles.md)[用户或](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/grant-system-permissions-to-ram-users-or-ram-roles.md)[RAM](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/grant-system-permissions-to-ram-users-or-ram-roles.md)[角色授予系统权限策略](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/grant-system-permissions-to-ram-users-or-ram-roles.md)。

| RAM 系统权限策略 | 权限说明 | 集群是否涉及 |  |  |
| --- | --- | --- | --- | --- |
| 注册集群 | 多集群舰队 | 工作流集群 |  |  |
| AliyunAdcpFullAccess | 当 RAM 用户或 RAM 角色需要 ACK One 所有资源的读写权限。 | 是 | 是 | 是 |
| AliyunAdcpReadOnlyAccess | 当 RAM 用户或 RAM 角色需要 ACK One 所有资源的只读权限。 | 是 | 是 | 是 |
| AliyunCSFullAccess | 当 RAM 用户或 RAM 角色需要容器服务产品所有资源的读写权限。 | 是 | 是 | 不涉及 |
| AliyunCSReadOnlyAccess | 当 RAM 用户或 RAM 角色需要容器服务产品所有资源的只读权限。 | 是 | 是 | 不涉及 |
| AliyunVPCReadOnlyAccess | 当 RAM 用户或 RAM 角色在创建集群时选择指定 VPC。 | 是 | 是 | 是 |
| AliyunECIReadOnlyAccess | 当 RAM 用户或 RAM 角色需要将集群 Pod 调度到 ECI 上。 | 是 | 是 | 是 |
| AliyunLogReadOnlyAccess | 当 RAM 用户或 RAM 角色在创建集群时选择已有 Log Project 存储审计日志，或查看指定集群的配置巡检。 | 是 | 是 | 是 |
| AliyunARMSReadOnlyAccess | 当 RAM 用户或 RAM 角色需要查看集群阿里云 Prometheus 插件的监控状态。 | 是 | 是 | 是 |
| AliyunRAMReadOnlyAccess | 当 RAM 用户或 RAM 角色需要查看已有的权限策略。 | 是 | 是 | 是 |
| AliyunECSReadOnlyAccess | 当 RAM 用户或 RAM 角色为集群添加已有云上节点或查看节点详细信息。 | 是 | 不涉及 | 不涉及 |
| AliyunContainerRegistryReadOnlyAccess | 当 RAM 用户或 RAM 角色需要查看阿里云账号内的业务镜像。 | 是 | 不涉及 | 不涉及 |
| AliyunAHASReadOnlyAccess | 当 RAM 用户或 RAM 角色需要使用集群拓扑功能。 | 是 | 不涉及 | 不涉及 |
| AliyunYundunSASReadOnlyAccess | 当 RAM 用户或 RAM 角色需要查看指定集群的运行时安全监控。 | 是 | 不涉及 | 不涉及 |
| AliyunKMSReadOnlyAccess | 当 RAM 用户或 RAM 角色在创建集群时启用 Secret 落盘加密功能。 | 是 | 不涉及 | 不涉及 |
| AliyunESSReadOnlyAccess | 当 RAM 用户或 RAM 角色需要执行云上节点池的相关操作，例如查看、编辑和扩缩容等。 | 是 | 不涉及 | 不涉及 |


## RBAC权限

RAM系统策略仅控制ACK One集群资源的操作权限，若RAM用户或RAM角色需要操作指定集群内的K8s资源，（如创建并获取GitOps Application和Argo Workflow），还需要获取指定ACK One集群及其命名空间的操作权限即RBAC权限。

ACK One提供以下预置角色：

- 

多集群舰队和工作流集群RBAC权限

| RBAC 权限 | 权限说明 | 集群是否涉及 |  |
| --- | --- | --- | --- |
| 多集群舰队 | 工作流集群 |  |  |
| admin（管理员） | 具有集群范围和所有命名空间下资源的读写权限。 | 是 | 是 |
| dev（开发人员） | 具有所选命名空间下的资源读写权限。 | 是 | 是 |
| gitops-dev（gitops 开发人员） | 具有 argocd 命名空间下应用资源的读写权限。 | 是 | 不涉及 |


- 

[注册集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[RBAC](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[权限](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)

RBAC权限所控制的具体资源列表以及授权操作，请参见[为](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/grant-rbac-permissions-to-a-ram-user-or-ram-role.md)[RAM](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/grant-rbac-permissions-to-a-ram-user-or-ram-role.md)[用户或](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/grant-rbac-permissions-to-a-ram-user-or-ram-role.md)[RAM](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/grant-rbac-permissions-to-a-ram-user-or-ram-role.md)[角色授予](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/grant-rbac-permissions-to-a-ram-user-or-ram-role.md)[RBAC](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/grant-rbac-permissions-to-a-ram-user-or-ram-role.md)[权限](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/grant-rbac-permissions-to-a-ram-user-or-ram-role.md)。

[上一篇：授权管理](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/authorization-management-1.md)[下一篇：为RAM用户或RAM角色授予系统权限策略](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/grant-system-permissions-to-ram-users-or-ram-roles.md)

该文章对您有帮助吗？

反馈

### 为什么选择阿里云

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)

### 大模型

[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)

### 产品和定价

[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)

### 技术内容

[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)

### 权益

[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)

### 服务

[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)

### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

联系我们：4008013260

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
