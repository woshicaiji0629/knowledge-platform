# 网络型负载均衡NLB-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/network-load-balancer/product-overview/what-is-nlb

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/slb/documents/network-load-balancer/product-overview.md)

- [快速入门](products/slb/documents/network-load-balancer/getting-started.md)

- [操作指南](products/slb/documents/network-load-balancer/user-guide.md)

- [实践教程](products/slb/documents/network-load-balancer/use-cases.md)

- [开发参考](products/slb/documents/network-load-balancer/developer-reference.md)

- [服务支持](products/slb/documents/network-load-balancer/service-support.md)

[首页](https://help.aliyun.com/zh)

# 什么是网络型负载均衡NLB

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/slb)

[我的收藏](https://help.aliyun.com/my_favorites.html)

网络型负载均衡NLB（Network Load Balancer ）是阿里云面向万物互联时代推出的新一代四层负载均衡，支持超高性能和自动弹性能力，单实例可以达到1亿并发连接。[NLB](products/slb/documents/network-load-balancer/product-overview/restrictions-on-use.md)[产品性能及使用限制](products/slb/documents/network-load-balancer/product-overview/restrictions-on-use.md)

## 前置概念

阅读本文前，您可能需要了解如下概念：

- 

[什么是负载均衡？](https://www.aliyun.com/getting-started/what-is/what-is-load-balance)

- 

[什么是](https://www.aliyun.com/getting-started/what-is/what-is-ssl)[SSL](https://www.aliyun.com/getting-started/what-is/what-is-ssl)[证书？](https://www.aliyun.com/getting-started/what-is/what-is-ssl)

## 产品优势

- 

高性能

NLB单实例支持超高并发连接与超大带宽，可应对互联网、AI、具身智能等行业的突发流量与高并发诉求。

- 

自动弹性伸缩

您无需指定或手动调整NLB的实例规格，实例性能会随着您的业务增减自动弹性伸缩。

- 

高可用

采用多层次容灾架构设计，通过集群容灾、会话保持、可用区多活等机制保障实例的可用性。

- 

TCPSSL卸载

支持大规模TCPSSL卸载，您可以在NLB上对SSL证书进行集中管理及卸载，有效提升后端业务处理效率。

- 

多场景流量分发

支持挂载IP类型后端服务，可以结合云企业网实现跨地域、跨VPC及云下IDC服务器等多个场景的流量分发调度。

- 

多种高级特性

支持IPv4/IPv6双栈、全端口、新建连接限速、连接优雅中断等高级特性，满足您多方位的业务定制需求。

## 应用场景

- 

物联网业务入口

在智能家居、智能停车、视频监控、车联网等业务场景中，NLB作为业务入口可以同时处理大量并发连接，同时提供TCPSSL卸载、连接限速等能力保障物联网业务安全稳定运行。

- 

互联网云上业务入口

NLB作为互联网流量入口，单实例提供超高的四层处理能力，同时可以基于业务变化自动弹性伸缩，业务波动时无需手工干预，降低了运维管理成本。

- 

混合云业务入口

NLB支持挂载本地IDC（Internet Data Center）服务器，可以搭配云企业网等产品将云上请求转发至线下服务器处理，实现线下IDC与云上服务互通。

## NLB组成

- 

- 

- 

- 

| 概念 | 说明 |
| --- | --- |
| 实例 | NLB 面向四层，提供四层负载均衡能力，通过将流量分发至不同的后端服务器来扩展应用系统的服务吞吐能力。单实例最大支持 1 亿并发连接。 |
| 监听 | 监听是 NLB 最小业务单元，监听上需要配置协议与端口以告知 NLB 需要处理什么流量，例如 TCP 协议，80 端口。 NLB 支持 TCP、UDP、TCPSSL 协议。每个 NLB 至少有一个监听，才能开始流量处理与分发。每个 NLB 默认最多配置的监听数量参见 [NLB](products/slb/documents/network-load-balancer/user-guide/nlb-quotas.md) [配额](products/slb/documents/network-load-balancer/user-guide/nlb-quotas.md) 。 |
| 服务器组 | 服务器组是一个逻辑组，包含多个后端服务器用于处理 NLB 分发的业务请求。 NLB 中的服务器组独立于 NLB 存在，可以将同一服务器组挂载在不同 NLB 内。每个服务器组默认最多添加的后端服务器数量参见 [NLB](products/slb/documents/network-load-balancer/user-guide/nlb-quotas.md) [配额](products/slb/documents/network-load-balancer/user-guide/nlb-quotas.md) 。 NLB 服务器组支持云服务器 ECS、弹性容器实例 ECI、弹性网卡 ENI 和 IP 类型的后端服务器。更多信息，请参见： [什么是云服务器](products/ecs/documents/user-guide/what-is-ecs.md) [ECS](products/ecs/documents/user-guide/what-is-ecs.md) [什么是弹性容器实例](https://help.aliyun.com/zh/eci/product-overview/what-is-elastic-container-instance#topic-1860079) [ECI](https://help.aliyun.com/zh/eci/product-overview/what-is-elastic-container-instance#topic-1860079) [弹性网卡](products/ecs/documents/user-guide/eni-overview.md) [ENI](products/ecs/documents/user-guide/eni-overview.md) [概述](products/ecs/documents/user-guide/eni-overview.md) [IP](products/slb/documents/network-load-balancer/user-guide/overview-of-nlb-server-groups.md) [类型后端服务器说明](products/slb/documents/network-load-balancer/user-guide/overview-of-nlb-server-groups.md) |
| 健康检查 | NLB 通过健康检查来判断后端服务器的业务可用性。 NLB 探测服务器组中不健康的服务器，并避免将流量分发给不健康的服务器。 NLB 支持多种健康检查配置，如协议、端口、以及各种健康检查阈值。 |


## NLB类型

本文从网络类型和协议版本两个方面介绍NLB类型。下图为您展示双栈公网NLB和双栈私网NLB。

### 网络类型

阿里云提供公网和私网两种网络类型的NLB。您可以根据业务场景选择配置对外公开或对内私有的NLB，系统会根据您的选择来决定是否使用共享带宽和弹性公网IP。上图中半透明框中所有元素分别实现了一个面向公网（私网）的NLB。

| 概念 | 说明 |
| --- | --- |
| 域名 | 一个在公网（私网）上可解析的域名解析至对应的 VIP。您也可以将所拥有的可读性强的域名通过 CNAME 方式解析到 NLB 的域名上来使用。 说明 自 北京时间 2024 年 11 月 15 日 00:00:00 起，对于新建的 NLB 实例默认使用新域名，阿里云平台将不允许用户直接使用平台侧提供的默认域名进行访问。 北京时间 2024 年 11 月 15 日 00:00:00 前，已创建的 NLB 实例不受影响，具体请参见 [负载均衡域名升级公告](products/slb/documents/product-overview/alb-and-nlb-domain-name-upgrade-announcement.md) 。 |
| 共享带宽 | 您仅在创建公网 NLB 时需要使用共享带宽。共享带宽提供 [地域](https://www.aliyun.com/getting-started/what-is/what-is-a-region) 级的带宽共享和复用能力，以及按带宽计费和按增强型 95 计费等多种计费模式，可有效节省公网带宽使用成本。公网 NLB 中将使用共享带宽来提供增强型 95 计费和按带宽计费能力。 |
| EIP | 您仅在创建公网 NLB 时需要使用 EIP，在创建私网 NLB 时无需配置。 NLB 对公网服务的 IP 地址，一个公网 NLB 可以有多个 EIP。为了实现 [高可用](https://www.aliyun.com/getting-started/what-is/what-is-high-availability) 性，一个公网 NLB 至少应包含两个分布在不同可用区的 EIP。 |
| VIP（Virtual IP address） | NLB 实施流量分发的实体。每个 VIP 都是专有网络 VPC（Virtual Private Cloud）中的一个私网 IP 地址。 |


### 协议版本

NLB协议版本分为IPv4和双栈。

| 概念 | 说明 |
| --- | --- |
| IPv4 | IPv4 实例对外提供 IPv4 的 VIP。 |
| 双栈 | 双栈实例对外同时提供 IPv4 和 IPv6 的 VIP，每个实例对外通过统一的域名提供服务。 |


## 开通网络型负载均衡NLB

单击[创建网络型负载均衡](https://common-buy.aliyun.com/?commodityCode=slb_nlb_public_cn#/buy)[NLB](https://common-buy.aliyun.com/?commodityCode=slb_nlb_public_cn#/buy)可立即前往NLB产品购买页面。

## 部署和维护NLB

注册阿里云账号后，您可以通过以下方式部署和维护NLB：

- 

[网络型负载均衡](https://slb.console.aliyun.com/nlb)[NLB](https://slb.console.aliyun.com/nlb)[控制台](https://slb.console.aliyun.com/nlb)：具有交互式操作的Web服务页面。您可登录控制台完成NLB实例的创建、使用或释放，具体操作，请参见[创建和管理](products/slb/documents/network-load-balancer/user-guide/create-and-manage-an-nlb-instance.md)[NLB](products/slb/documents/network-load-balancer/user-guide/create-and-manage-an-nlb-instance.md)[实例](products/slb/documents/network-load-balancer/user-guide/create-and-manage-an-nlb-instance.md)。

- 

[阿里云](https://next.api.aliyun.com/api-tools/sdk/Nlb?version=2022-04-30&language=java-tea)[SDK](https://next.api.aliyun.com/api-tools/sdk/Nlb?version=2022-04-30&language=java-tea)：提供Java、Go、Python等多种编程语言的[SDK](https://www.aliyun.com/getting-started/what-is/what-is-sdk)。

- 

[OpenAPI](https://next.api.aliyun.com/api/Nlb/2022-04-30/DescribeRegions?lang=JAVA)[开发者门户](https://next.api.aliyun.com/api/Nlb/2022-04-30/DescribeRegions?lang=JAVA)：提供快速检索接口、在线调用[API](https://www.aliyun.com/getting-started/what-is/what-is-api)和动态生成SDK示例代码等服务。

- 

[阿里云](https://www.aliyun.com/aliyunapp/web/download)[App](https://www.aliyun.com/aliyunapp/web/download)：移动端类型的管理工具。

- 

[Terraform](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/nlb_listener)：能够通过配置文件在阿里云以及其他支持Terraform的云商平台调用计算资源，并对其进行版本控制的开源工具。

## 相关文档

- 

[功能特性](products/slb/documents/network-load-balancer/product-overview/functions-and-features.md)

- 

[NLB](products/slb/documents/network-load-balancer/getting-started/nlb-quickly-implements-load-balancing-for-ipv4-services.md)[快速实现](products/slb/documents/network-load-balancer/getting-started/nlb-quickly-implements-load-balancing-for-ipv4-services.md)[IPv4](products/slb/documents/network-load-balancer/getting-started/nlb-quickly-implements-load-balancing-for-ipv4-services.md)[服务的负载均衡](products/slb/documents/network-load-balancer/getting-started/nlb-quickly-implements-load-balancing-for-ipv4-services.md)

- 

[NLB](products/slb/documents/network-load-balancer/product-overview/nlb-billable-items.md)[计费规则](products/slb/documents/network-load-balancer/product-overview/nlb-billable-items.md)

[上一篇：产品概述](products/slb/documents/network-load-balancer/product-overview.md)[下一篇：功能特性](products/slb/documents/network-load-balancer/product-overview/functions-and-features.md)

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
