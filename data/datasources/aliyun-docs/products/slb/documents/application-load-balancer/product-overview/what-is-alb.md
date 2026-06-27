# 什么是应用型负载均衡ALB-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/product-overview/what-is-alb

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/slb/documents/application-load-balancer/product-overview.md)

- [快速入门](products/slb/documents/application-load-balancer/getting-started.md)

- [操作指南](products/slb/documents/application-load-balancer/user-guide.md)

- [实践教程](products/slb/documents/application-load-balancer/use-cases.md)

- [开发参考](products/slb/documents/application-load-balancer/developer-reference.md)

- [服务支持](products/slb/documents/application-load-balancer/support.md)

[首页](https://help.aliyun.com/zh)

# 什么是应用型负载均衡ALB

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/slb)

[我的收藏](https://help.aliyun.com/my_favorites.html)

应用型负载均衡ALB（Application Load Balancer）是阿里云推出的专门面向HTTP、HTTPS和QUIC等应用层负载场景的负载均衡服务，具备弹性及大规模应用层流量处理能力。ALB具备处理复杂业务路由的能力，与云原生相关服务深度集成，是阿里云官方提供的云原生Ingress网关。

## 为什么选择应用型负载均衡ALB

应用型负载均衡ALB，提供应用层处理能力和多种高级[路由](https://www.aliyun.com/getting-started/what-is/what-is-routing)功能，聚焦HTTP、HTTPS和QUIC应用层协议，是阿里云官方云原生Ingress网关。关于云原生网关ALB Ingress的介绍和使用，请参见[ALB Ingress](products/slb/documents/application-load-balancer/user-guide/alb-ingress.md)[管理](products/slb/documents/application-load-balancer/user-guide/alb-ingress.md)和[ALB Ingress](products/slb/documents/application-load-balancer/user-guide/functions-and-features-of-alb-ingresses.md)[功能操作指导](products/slb/documents/application-load-balancer/user-guide/functions-and-features-of-alb-ingresses.md)。

- 

应用层高弹性：ALB面向应用层，提供域名与VIP，多级分发承载大规模请求。ALB支持通过流量分发扩展应用系统的服务能力，消除单点故障提升应用系统的可用性。ALB允许自定义可用区组合和在可用区间弹性伸缩，避免单可用区资源瓶颈。

- 

先进的协议支持：ALB支持HTTP、HTTPS和QUIC协议，具备超大规模的流量处理能力。在实时音视频、互动直播和游戏等移动互联网应用中，访问速度更快，传输链路更安全可靠。ALB支持gRPC框架，可实现[微服务](https://www.aliyun.com/getting-started/what-is/what-is-microservice)间的API通信。

- 

基于内容的高级路由：ALB支持基于路径、HTTP标头、查询字符串、HTTP请求方法、Cookie和SourceIp等多种条件来识别特定业务流量，并将其转发至不同的后端服务器。同时ALB还支持重定向、重写以及自定义HTTPS标头等高级操作。

- 

安全可靠：ALB自带DDoS防护，集成Web应用防火墙。同时提供全链路HTTPS加密，支持预制和自定义安全策略、TLS 1.3等高效安全加密协议，面向加密敏感型业务，满足Zero-Trust新一代安全技术架构需求。

- 

面向云原生：随着[云原生](https://www.aliyun.com/getting-started/what-is/what-is-cloud-native)逐步成熟，互联网、金融、企业等新建业务时都会选择云原生部署，或对现有业务进行云原生化改造。ALB与[容器](https://www.aliyun.com/getting-started/what-is/what-is-container)服务[Kubernetes](https://www.aliyun.com/getting-started/what-is/what-is-kubernetes)版、SAE、函数计算和开源K8s等深度集成，是阿里云的官方云原生Ingress网关。

- 

SSE流式传输：ALB支持SSE流式传输，在大模型AI应用中，可通过SSE实时返回生成的推理结果，以提升用户体验。

- 

弹性灵活的计费：ALB通过弹性公网IP（Elastic IP Address，简称EIP）和共享带宽提供公网能力，实现公网灵活计费；同时采用了更先进的、更适合弹性业务峰值的性能容量单位LCU（Load Balancer Capacity Unit）的计价方案。

## 实例性能指标

说明

自北京时间2025年2月25日00:00:00起，对于新建实例默认使用升级后的ALB，已创建的ALB实例不受影响（提交自助申请创建的实例除外）。具体可参考[应用型负载均衡](products/slb/documents/product-overview/alb.md)[ALB](products/slb/documents/product-overview/alb.md)[实例升级公告](products/slb/documents/product-overview/alb.md)。

## 升级后

ALB实例会从每个指定的交换机中分配3个IP地址，包含1个VIP（对外提供服务）和2个Local IP（用于与后端服务器交互并进行健康检查）。

说明

为确保ALB各项弹性能力可用，建议您在ALB实例所在的每个交换机内预留至少8个IP地址。

| 单 VIP 性能指标 | 最高自动弹性性能 |
| --- | --- |
| 最大每秒请求数（QPS） | 500,000 |
| 最大新建连接数（CPS） | 200,000 |
| 最大并发连接数 | 5,000,000 |
| 最大私网带宽 | 25Gbps |


双可用区的ALB实例默认公网带宽为400Mbps，实际公网带宽以单ALB实例下EIP的带宽总和为准。

- 

单个[地域](https://www.aliyun.com/getting-started/what-is/what-is-a-region)下，单个阿里云账号下所有按使用流量计费EIP的实际业务带宽峰值总和不能大于 5 Gbps。更多信息，请参见[按量付费](products/eip/documents/pay-as-you-go.md)中的带宽峰值限制。

- 

如需更大带宽请购买共享带宽。关于如何购买共享带宽，请参见[创建与管理共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/user-guide/create-an-internet-shared-bandwidth-instance#task-hjr-jlk-z2b)。

说明

- 

ALB的性能容量会随着分钟级弹性SLA自动扩容，若您有如下场景或需要更高的弹性能力，请使用[ALB](products/slb/documents/application-load-balancer/user-guide/capacity-reservation.md)[资源预留](products/slb/documents/application-load-balancer/user-guide/capacity-reservation.md)。

- 

您准备推出系列运营活动，该活动将带来突发流量高峰，您希望确保ALB能够支持活动期间的流量高峰。

- 

您的业务属于突发型业务，无法有效预测流量洪峰。

- 

您上线或迁移的业务需要ALB在初始状态就具备较高性能，而不是等待自动扩容。

- 

您需要持续保持确定性容量，以满足业务诉求。

- 

您正在进行负载均衡之间的迁移，并希望目标负载均衡的性能规模与源负载均衡匹配。

- 

ALB支持多可用区部署，若当前地域支持2个及以上可用区，为保障业务[高可用](https://www.aliyun.com/getting-started/what-is/what-is-high-availability)，请至少选择2个可用区，且ALB不会额外收取可用区的费用。

- 

建议您使用自有域名，通过CNAME方式解析至ALB实例域名，对外提供业务访问。这种方式下ALB最高可提供99.995% SLA可用性保障。

上方规格表中的性能指标为ALB实例的最高自动弹性性能上限，与实例功能版本无关。

## 升级前

ALB的IP模式分为动态IP和固定IP。动态IP和固定IP的ALB实例性能存在差异。

说明

ALB实例性能指标仅与ALB的IP模式相关，与ALB功能版本无关。

单ALB实例性能（以默认2个可用区为例说明）

- 

- 

| IP 模式 | 最大每秒请求数（QPS） | 最大新建连接数（CPS） | 最大并发连接数 | 最大私网带宽 | 默认公网带宽 |
| --- | --- | --- | --- | --- | --- |
| 动态 IP | 100 万 | 100 万 | 1000 万 | 100 Gbps | 400 Mbps，实际公网带宽以单 ALB 实例下 EIP 的带宽总和为准。 单个 [地域](https://www.aliyun.com/getting-started/what-is/what-is-a-region) 下，单个阿里云账号下所有按使用流量计费 EIP 的实际业务带宽峰值总和不能大于 5 Gbps。更多信息，请参见 [按量付费](products/eip/documents/pay-as-you-go.md) 中的带宽峰值限制。 如需更大带宽请购买共享带宽。关于如何购买共享带宽，请参见 [创建与管理共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/user-guide/create-an-internet-shared-bandwidth-instance#task-hjr-jlk-z2b) 。 |
| 固定 IP | 10 万 | 10 万 | 100 万 | 10 Gbps |  |


说明

- 

多可用区地域，ALB实例QPS、CPS、并发连接数初始上限值分别为10万、10万、100万，不随可用区的增多而变化。ALB固定IP模式实例最大QPS、CPS、并发连接数分别为10万、10万、100万，ALB动态IP模式实例会随着弹性SLA自动扩容，最高QPS、CPS、并发连接数分别可达100万、100万、1000万。

- 

建议您使用自有域名，通过CNAME方式解析至ALB实例域名，对外提供业务访问。这种方式下ALB最高可提供99.995%SLA可用性保障。

- 

ALB支持多可用区部署，若当前地域支持2个及以上可用区，为保障业务[高可用](https://www.aliyun.com/getting-started/what-is/what-is-high-availability)，请至少选择2个可用区，且ALB不会额外收取可用区的费用。

## ALB组成

| 概念 | 说明 |
| --- | --- |
| 实例 | 面向七层提供负载均衡能力，通过将流量分发到不同的后端服务器来扩展应用系统的服务吞吐能力。单实例可处理高达 100 万 QPS。 |
| 监听 | 监听是 ALB 最小业务单元，监听上需要配置协议与端口以告知 ALB 需要处理什么流量，例如 HTTP 协议，80 端口。每个 ALB 至少有一个监听，才能开始流量处理与分发。每个 ALB 默认最多可以配置 50 个监听，用于处理不同的业务流量。 |
| 转发规则 | 转发规则用于确定 ALB 实例如何将请求路由到一个或多个后端服务器组中的后端服务器。 ALB 具备高级路由能力，在传统的路由规则基础上，还可以基于 HTTP 标头、Cookie 和 HTTP 请求方法等多种规则进行转发，实现基于业务的灵活调度。 |
| 服务器组 | 服务器组是一个逻辑组，包含多个后端服务器用于处理 ALB 分发的业务请求。 ALB 中服务器组独立于 ALB 存在，可以将同一服务器组挂载在不同 ALB 内。每个服务器组默认最多可以添加 1000 个后端服务器。 ALB 服务器组支持云 ECS、ECI、ENI 等多种类型的后端服务器。 |
| 健康检查 | ALB 通过健康检查来判断后端服务器的业务可用性。 ALB 探测服务器组中不健康的服务器，并避免将流量分发给不健康的服务器。 ALB 支持多种健康检查配置，如协议、端口、以及各种健康检查阈值。同时 ALB 提供健康检查模板，可将健康检查模板快速地应用到不同的服务器组。 |


## ALB类型

阿里云提供公网和私网两种类型的ALB。您可以根据业务场景选择配置对外公开或对内私有的ALB，系统会根据您的选择来决定是否使用共享带宽和弹性公网IP。

| 概念 | 说明 |
| --- | --- |
| VIP（Virtual IP address） | ALB 实施流量分发的实体。每个 VIP 都是专有网络 VPC（Virtual Private Cloud）中的一个私网 IP 地址。 |
| EIP | 您仅在创建公网 ALB 时需要使用 EIP，在创建私网 ALB 时无需配置。 ALB 对公网服务的 IP 地址，一个公网 ALB 可以有多个 EIP。为了实现高可用性，一个公网 ALB 至少应包含两个分布在不同可用区的 EIP。 |
| 共享带宽 | [共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/product-overview/what-is-internet-shared-bandwidth) 提供地域级的带宽共享和复用能力，您可将同地域下的弹性公网 IP（EIP）添加到共享带宽实例中，复用共享带宽中的带宽，以节省公网带宽使用成本。 |
| 域名 | 一个在公网（私网）上可解析的域名解析至对应的 VIP。您也可以将所拥有的可读性强的域名通过 CNAME 方式解析到 ALB 的域名上来使用，具体操作，请参见 [为](products/slb/documents/application-load-balancer/user-guide/configure-cname-resolution-for-alb.md) [ALB](products/slb/documents/application-load-balancer/user-guide/configure-cname-resolution-for-alb.md) [配置](products/slb/documents/application-load-balancer/user-guide/configure-cname-resolution-for-alb.md) [CNAME](products/slb/documents/application-load-balancer/user-guide/configure-cname-resolution-for-alb.md) [解析](products/slb/documents/application-load-balancer/user-guide/configure-cname-resolution-for-alb.md) 。 说明 自 北京时间 2024 年 11 月 15 日 00:00:00 起，对于新建的 ALB 实例默认使用新域名，阿里云平台将不允许用户直接使用平台侧提供的默认域名进行访问。 北京时间 2024 年 11 月 15 日 00:00:00 前，已创建的 ALB 实例不受影响。具体请参见 [负载均衡域名升级公告](products/slb/documents/product-overview/alb-and-nlb-domain-name-upgrade-announcement.md) 。 |


## 开通应用型负载均衡ALB

单击[创建应用型负载均衡](https://common-buy.aliyun.com/?commodityCode=slb_ealb_public_cn#/buy)[ALB](https://common-buy.aliyun.com/?commodityCode=slb_ealb_public_cn#/buy)可立即前往ALB产品购买页面。

## 部署和维护ALB

注册阿里云账号后，您可以通过以下方式部署和维护ALB：

- 

[应用型负载均衡](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)[ALB](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)[控制台](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)：具有交互式操作的Web服务页面。您可登录控制台完成ALB实例的创建、使用或释放，具体操作，请参见[创建和管理](products/slb/documents/application-load-balancer/user-guide/create-and-manage-alb-instances.md)[ALB](products/slb/documents/application-load-balancer/user-guide/create-and-manage-alb-instances.md)[实例](products/slb/documents/application-load-balancer/user-guide/create-and-manage-alb-instances.md)。

- 

[阿里云](https://next.api.aliyun.com/api-tools/sdk/Alb?version=2020-06-16&language=java-async-tea)[SDK](https://next.api.aliyun.com/api-tools/sdk/Alb?version=2020-06-16&language=java-async-tea)：提供Java、Go、Python等多种编程语言的[SDK](https://www.aliyun.com/getting-started/what-is/what-is-sdk)。

- 

[OpenAPI](https://next.api.aliyun.com/api/Alb/2020-06-16/DescribeRegions?lang=JAVA)[开发者门户](https://next.api.aliyun.com/api/Alb/2020-06-16/DescribeRegions?lang=JAVA)：提供快速检索接口、在线调用[API](https://www.aliyun.com/getting-started/what-is/what-is-api#t2558977.html)和动态生成SDK示例代码等服务。

- 

[阿里云](https://www.aliyun.com/aliyunapp/web/download)[App](https://www.aliyun.com/aliyunapp/web/download)：移动端类型的管理工具。

- 

[Terraform](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/alb_acl)：能够通过配置文件在阿里云以及其他支持Terraform的云商平台调用计算资源，并对其进行版本控制的开源工具。

## 相关文档

- 

[功能特性](products/slb/documents/application-load-balancer/product-overview/functional-characteristics.md)

- 

[ALB](products/slb/documents/application-load-balancer/product-overview/alb-billing-rules.md)[计费规则](products/slb/documents/application-load-balancer/product-overview/alb-billing-rules.md)

- 

[ALB](products/slb/documents/application-load-balancer/product-overview/supported-regions-and-zones.md)[支持的地域与可用区](products/slb/documents/application-load-balancer/product-overview/supported-regions-and-zones.md)

- 

[ALB](https://help.aliyun.com/zh/document_detail/453685.html)[快速入门](https://help.aliyun.com/zh/document_detail/453685.html)

[上一篇：产品概述](products/slb/documents/application-load-balancer/product-overview.md)[下一篇：ALB扩展版概述](products/slb/documents/application-load-balancer/product-overview/alb-extensible-edition-overview.md)

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
