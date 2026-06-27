# 通过代码自动化管理云基础设施-Terraform-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/developer-reference/terraform-overview

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-edge/product-overview.md)

- [快速入门](products/ack/documents/ack-edge/quick-start.md)

- [操作指南](products/ack/documents/ack-edge/user-guide.md)

- [实践教程](products/ack/documents/ack-edge/use-cases.md)

- [安全合规](products/ack/documents/ack-edge/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-edge/developer-reference.md)

- [服务支持](products/ack/documents/ack-edge/support.md)

[首页](https://help.aliyun.com/zh)

# Terraform概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Terraform是一种开源工具，用于安全高效地预览、配置和管理云基础架构和资源。本文介绍Terraform的基本概念、使用优势和应用场景。

## 基本概念

Terraform是一个云上资源编排工具，实现基础设施即代码。

- 

Terraform能够让您在阿里云上轻松使用简单模板语言定义、预览和部署云基础架构。更多信息，请参见[Configuration Syntax](https://www.terraform.io/docs/configuration/syntax.html)。

- 

Terraform是一个安全、高效地部署、更改、版本化基础设施和应用程序的工具，可以用来管理多层次的资源。

- 

Terraform统一管理从上层的软件到底层的网络、系统的配置。

- 

Terraform可以创建、修改、删除ECS、VPC、RDS、SLB等多种阿里云云产品资源。

有关Terraform应用场景的具体介绍，请参见[应用场景](https://help.aliyun.com/zh/terraform/application-scenarios#concept-hny-xpc-rfb)。

- 

- 

- 

- 

| Terraform 资源 | Terrafo rm 工具 |
| --- | --- |
| Terraform 的资源分为 2 类： Resource：资源，指新创建的资源。 Data Source： 数据资源，查询已有的资源信息并获取其属性。 以下举例说明如何使用 Resource 和 Data Source。 ### Data Sources # 列出 2 Core 4 GB 这种规格的机器的型号。 # 参考文档：https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/instance_types data "alicloud_instance_types" "c2g4" { cpu_core_count = 2 memory_size = 4 } ## Resources # 创建一个 SLB。 # 参考文档：https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/instance resource "alicloud_slb" "default" { name = var.name specification = "slb.s2.small" vswitch_id = alicloud_vswitch.default.id } 关于容器服务 ACK 的 Resources 和 Data Resources 的相关信息，请参见 [通过](products/ack/documents/ack-edge/developer-reference/terraform-overview.md) [Terraform](products/ack/documents/ack-edge/developer-reference/terraform-overview.md) [使用](products/ack/documents/ack-edge/developer-reference/terraform-overview.md) [ACK](products/ack/documents/ack-edge/developer-reference/terraform-overview.md) 。 | Terraform 工具分为 2 部分： Terraform CLI：Terraform 客户端命令行工具。 Terraform Provider：各个云厂商都提供了自己的 Provider，用于将云产品接入到 Terraform 中。关于 Terraform Provider 的更多信息，请参见 [Provider](https://registry.terraform.io/browse/providers) 。 您可以下载 Terraform 工具。具体操作，请参见 [在本地安装和配置](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally#task-bts-tlz-dfb) [Terraform](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally#task-bts-tlz-dfb) 和 [在](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources#concept-pbn-2rd-rfb) [Cloud Shell](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources#concept-pbn-2rd-rfb) [中使用](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources#concept-pbn-2rd-rfb) [Terraform](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources#concept-pbn-2rd-rfb) 。 |


阿里云是中国第一家与Terraform集成的云厂商，阿里云Provider（[terraform-provider-alicloud](https://www.terraform.io/docs/providers/alicloud/index.html)）目前已经提供了超过163个Resource和113个Data Source，覆盖计算、存储、网络、负载均衡、CDN、容器服务、中间件、访问控制、数据库等超过35款产品，已经满足了大量大客户的自动化上云需求。

关于Terraform的更多信息，请参见[Terraform](https://www.terraform.io/)。

## 使用优势

- 

将基础架构部署到多个云

Terraform适用于多云方案，将类似的基础架构部署到阿里云、其他云提供商或者本地数据中心。开发人员能够使用相同的工具和相似的配置文件同时管理不同云提供商的资源。

- 

自动化管理基础架构

Terraform能够创建配置文件的模板，以可重复、可预测的方式定义、预配和配置ECS资源，减少因人为因素导致的部署和管理错误。通过使用Terraform，您能够多次部署同一模板，创建相同的开发、测试和生产环境。

- 

基础架构即代码

可以用代码来管理维护资源。允许保存基础设施状态，从而使您能够跟踪对系统（基础设施即代码）中不同组件所做的更改，并与其他人共享这些配置。

- 

降低开发成本

您可通过按需创建开发和部署环境来降低成本。并且，您可以在系统更改之前进行评估。

## 通过Terraform使用ACK

ACK支持通过Terraform管理以下Resource和Data Source。

| 名称 | 描述 |
| --- | --- |
| [alicloud_cs_edge_kubernetes](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_edge_kubernetes) | 管理 ACK 边缘托管版集群。 |
| [alicloud_cs_kubernetes_node_pool](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_kubernetes_node_pool) | 管理 ACK 节点池。 |
| [alicloud_cs_kubernetes_permissions](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_kubernetes_permissions) | 管理 ACK 集群内 RBAC 权限。 |
| [alicloud_cs_managed_kubernetes](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_managed_kubernetes) | 管理 ACK 托管版集群。 |
| [alicloud_cs_kubernetes](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_kubernetes) | 管理 ACK 专有版集群。 |
| [alicloud_cs_serverless_kubernetes](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_serverless_kubernetes) | 管理 ACK Serverless 集群 。 |
| [alicloud_cs_kubernetes_addon](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cs_kubernetes_addon) | 管理集群组件。 |


| 名称 | 描述 |
| --- | --- |
| [alicloud_ack_service](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/ack_service) | 开通容器服务 ACK。 |
| [alicloud_cs_edge_kubernetes_clusters](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/cs_edge_kubernetes_clusters) | 列举所有的 ACK 边缘托管版集群。 |
| [alicloud_cs_kubernetes_clusters](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/cs_kubernetes_clusters) | 列举所有的 ACK 专有版集群。 |
| [alicloud_cs_kubernetes_permissions](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/cs_kubernetes_permissions) | 列举 RAM 用户拥有的所有权限。 |
| [alicloud_cs_managed_kubernetes_clusters](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/cs_managed_kubernetes_clusters) | 列举所有的 ACK 托管版集群。 |
| [alicloud_cs_serverless_kubernetes_clusters](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/cs_serverless_kubernetes_clusters) | 列举所有的 ACK Serverless 集群 。 |
| [alicloud_cs_kubernetes_addon_metadata](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/cs_kubernetes_addon_metadata) | 列举集群组件元数据信息。 |
| [alicloud_cs_kubernetes_addons](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/cs_kubernetes_addons) | 列举集群可用的组件。 |
| [alicloud_cs_kubernetes_version](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/cs_kubernetes_version) | 列举可用的 Kubernetes 版本信息。 |


## 相关文档

- 

[在](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources#concept-pbn-2rd-rfb)[Cloud Shell](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources#concept-pbn-2rd-rfb)[中使用](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources#concept-pbn-2rd-rfb)[Terraform](https://help.aliyun.com/zh/terraform/use-terraform-to-quickly-create-resources#concept-pbn-2rd-rfb)

- 

[在本地安装和配置](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally#task-bts-tlz-dfb)[Terraform](https://help.aliyun.com/zh/terraform/install-and-configure-terraform-locally#task-bts-tlz-dfb)

- 

[创建](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-create-an-ack-managed-cluster.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-create-an-ack-managed-cluster.md)[托管版集群](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-create-an-ack-managed-cluster.md)

- 

[使用](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-create-an-auto-scaling-node-pool.md)[Terraform](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-create-an-auto-scaling-node-pool.md)[创建具备自动伸缩功能的节点池](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/use-terraform-to-create-an-auto-scaling-node-pool.md)

[上一篇：Terraform](products/ack/documents/ack-edge/developer-reference/terraform.md)[下一篇：首次开通ACK Edge并授权默认角色](products/ack/documents/ack-edge/developer-reference/activate-ack-edge-for-the-first-time-and-authorize-the-default-role.md)

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
