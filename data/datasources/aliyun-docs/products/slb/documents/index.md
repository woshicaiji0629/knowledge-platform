# 将流量按需分发到不同的后端-负载均衡-阿里云

Source: https://help.aliyun.com/zh/slb/

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/slb/documents/product-overview.md)

- [安全合规](products/slb/documents/security-and-compliance.md)

- [服务支持](products/slb/documents/support.md)

- [客户案例](products/slb/documents/customer-use-cases.md)

[首页](https://help.aliyun.com/zh)负载均衡

# 负载均衡

负载均衡SLB（Server Load Balancer）是一种对流量进行按需分发的服务，通过将流量分发到不同的后端服务来扩展应用系统的服务吞吐能力，并且可以消除系统中的单点故障，提升应用系统的可用性。

[免费试用](https://free.aliyun.com/?product=9555942)[ALB购买](https://common-buy.aliyun.com/?spm=5176.7921785.J_5253785160.3.25fb2229U1BBJr&commodityCode=slb_ealb_public_cn)[NLB购买](https://common-buy.aliyun.com/?commodityCode=slb_nlb_public_cn#/buy)[CLB购买](https://common-buy.aliyun.com/?spm=5176.2020520102.content.2.27e77067oX32Fy&commodityCode=slb&regionId=cn-hangzhou-dg-a01)[相关技术圈](https://developer.aliyun.com/group/networking/)

负载均衡产品简介

## 产品系列

### [应用型负载均衡ALB](products/slb/documents/application-load-balancer.md)

[专门面向七层，提供超强的业务处理性能，例如HTTPS卸载能力。单实例每秒查询数QPS可达100万次。同时ALB提供基于内容的高级路由特性，是阿里云官方云原生Ingress网关。](products/slb/documents/application-load-balancer.md)

### [网络型负载均衡NLB](products/slb/documents/network-load-balancer.md)

[面向万物互联时代推出的新一代四层负载均衡，支持超高性能和自动弹性能力，单实例可以达到1亿并发连接，帮您轻松应对高并发业务。](products/slb/documents/network-load-balancer.md)

### [传统型负载均衡CLB](products/slb/documents/classic-load-balancer.md)

[支持TCP、UDP、HTTP和HTTPS协议，具备良好的四层处理能力，以及基础的七层处理能力。](products/slb/documents/classic-load-balancer.md)

- 

## 学习路径

从浅入深，带您了解负载均衡

### ALB

ALB介绍

- [什么是ALB](products/slb/documents/application-load-balancer/product-overview/what-is-alb.md)

- [功能版本对比](products/slb/documents/application-load-balancer/product-overview/functions-and-features.md)

- [ALB计费](products/slb/documents/application-load-balancer/product-overview/billing-overview.md)

- [快速实现IPv4服务的负载均衡](products/slb/documents/application-load-balancer/getting-started/use-an-alb-instance-to-provide-ipv4-services.md)

- [快速实现IPv6服务的负载均衡](products/slb/documents/application-load-balancer/getting-started/implement-load-balancing-for-ipv6-services.md)

- [ALB Ingress管理](products/slb/documents/application-load-balancer/user-guide/alb-ingresses.md)

ALB实例

- [实例概述](products/slb/documents/application-load-balancer/user-guide/overview-of-alb-instances.md)

- [创建实例](products/slb/documents/application-load-balancer/user-guide/create-an-alb-instance.md)

- [管理实例](products/slb/documents/application-load-balancer/user-guide/manage-alb-instances.md)

- [实例变配](products/slb/documents/application-load-balancer/user-guide/modify-the-configurations-of-alb-instances.md)

- [变更网络类型](products/slb/documents/application-load-balancer/user-guide/change-the-network-type-of-an-alb-instance.md)

ALB监听

- [添加HTTP监听](products/slb/documents/application-load-balancer/user-guide/add-an-http-listener.md)

- [添加HTTPS监听](products/slb/documents/application-load-balancer/user-guide/add-an-https-listener.md)

- [添加QUIC监听](products/slb/documents/application-load-balancer/user-guide/add-a-quic-listener.md)

- [管理转发规则](products/slb/documents/application-load-balancer/user-guide/manage-forwarding-rules-for-a-listener.md)

- [可编程脚本Ascript](products/slb/documents/application-load-balancer/user-guide/ascript.md)

ALB服务器组

- [服务器组概述](products/slb/documents/application-load-balancer/user-guide/alb-server-group-overview.md)

- [管理服务器组](products/slb/documents/application-load-balancer/user-guide/create-and-manage-a-server-group.md)

- [配置会话保持](products/slb/documents/application-load-balancer/user-guide/configure-session-persistence-1.md)

ALB安全管理

- [访问控制](products/slb/documents/application-load-balancer/user-guide/network-acls.md)

- [健康检查](products/slb/documents/application-load-balancer/user-guide/health-check-management.md)

- [证书管理](products/slb/documents/application-load-balancer/user-guide/manage-certificates.md)

- [TLS安全策略](products/slb/documents/application-load-balancer/user-guide/tls-security-policies.md)

ALB教程

- [使用ALB将HTTP访问重定向至HTTPS](products/slb/documents/application-load-balancer/use-cases/redirect-http-requests-to-an-https-listener.md)

- [使用ALB挂载跨地域VPC内的服务器](products/slb/documents/application-load-balancer/use-cases/specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region.md)

- [使用ALB实现gRPC协议的负载均衡](products/slb/documents/application-load-balancer/use-cases/enable-load-balancing-for-grpc-services.md)

解决方案

- [ALB实现跨地域负载均衡](https://www.aliyun.com/solution/tech-solution/alb-acrlb)

- [灵活调度，高效编排，容器化管理云上应用](https://www.aliyun.com/solution/tech-solution/ack-services)

- [随需而动：自动弹性，稳定交付](https://www.aliyun.com/solution/tech-solution/improve-app-availability)

- [智能应对流量变化，容器化集群的弹性攻略](https://www.aliyun.com/solution/tech-solution/ack-hpa)

- [卓越效能，极简运维，Serverless高可用架构](https://www.aliyun.com/solution/tech-solution/serverless-ha)

- [云架构必修课：云上高可用架构](https://www.aliyun.com/solution/tech-solution/hablog)

### NLB

NLB介绍

- [什么是NLB](products/slb/documents/network-load-balancer/product-overview/what-is-nlb.md)

- [功能特性](products/slb/documents/network-load-balancer/product-overview/functions-and-features.md)

- [NLB计费](products/slb/documents/network-load-balancer/product-overview/nlb-billable-items.md)

- [快速入门](products/slb/documents/network-load-balancer/getting-started/nlb-quick-start.md)

NLB实例

- [实例概述](products/slb/documents/network-load-balancer/user-guide/overview-of-nlb-instances.md)

- [创建和管理NLB实例](products/slb/documents/network-load-balancer/user-guide/create-and-manage-an-nlb-instance.md)

NLB监听

- [监听概述](products/slb/documents/network-load-balancer/user-guide/overview-of-nlb-listeners.md)

- [添加TCP监听](products/slb/documents/network-load-balancer/user-guide/add-a-tcp-listener.md)

- [添加UDP监听](products/slb/documents/network-load-balancer/user-guide/add-a-udp-listener.md)

- [添加TCPSSL监听](products/slb/documents/network-load-balancer/user-guide/create-a-listener-that-uses-ssl-over-tcp.md)

- [管理NLB监听](products/slb/documents/network-load-balancer/user-guide/manage-nlb-listeners.md)

NLB服务器组

- [服务器组概述](products/slb/documents/network-load-balancer/user-guide/overview-of-nlb-server-groups.md)

- [创建和管理服务器组](products/slb/documents/network-load-balancer/user-guide/create-and-manage-a-server-group.md)

NLB安全管理

- [TLS安全策略](products/slb/documents/network-load-balancer/user-guide/tls-security-policies-1.md)

NLB API参考

- [API参考](products/slb/documents/network-load-balancer/developer-reference/list-of-operations-by-function.md)

### CLB

CLB介绍

- [什么是CLB](products/slb/documents/classic-load-balancer/product-overview/what-is-clb.md)

- [产品架构](products/slb/documents/classic-load-balancer/product-overview/architecture.md)

- [功能特性](products/slb/documents/classic-load-balancer/product-overview/features.md)

- [应用场景](products/slb/documents/classic-load-balancer/product-overview/scenarios.md)

CLB计费

- [计费概述](products/slb/documents/classic-load-balancer/product-overview/billing-overview.md)

- [包年包月](products/slb/documents/classic-load-balancer/product-overview/subscription.md)

- [按量计费](products/slb/documents/classic-load-balancer/product-overview/pay-as-you-go.md)

CLB快速入门

- [准备工作](products/slb/documents/classic-load-balancer/getting-started/preparations-1.md)

- [创建实例](products/slb/documents/classic-load-balancer/getting-started/create-a-clb-instance.md)

- [配置实例](products/slb/documents/classic-load-balancer/getting-started/configure-a-clb-instance.md)

- [释放实例](products/slb/documents/classic-load-balancer/getting-started/release-a-clb-instance.md)

CLB用户指南

- [实例](products/slb/documents/classic-load-balancer/user-guide/clb-overview-1.md)

- [监听](products/slb/documents/classic-load-balancer/user-guide/listener-overview.md)

- [后端服务器](products/slb/documents/classic-load-balancer/user-guide/backend-server-overview.md)

- [健康检查](products/slb/documents/classic-load-balancer/user-guide/health-check-overview.md)

- [证书管理](products/slb/documents/classic-load-balancer/user-guide/overview.md)

- [访问控制](products/slb/documents/classic-load-balancer/user-guide/overview-3.md)

- [监控报警](products/slb/documents/classic-load-balancer/user-guide/monitoring-and-alerting-metrics.md)

- [日志管理](products/slb/documents/classic-load-balancer/user-guide/view-operation-logs.md)

CLB开发指南

- [API参考](products/slb/documents/classic-load-balancer/developer-reference/list-of-operations-by-function.md)

- [SDK参考](products/slb/documents/classic-load-balancer/developer-reference/download-sdks-1.md)

CLB教程

- [HTTP重定向至HTTPS](products/slb/documents/classic-load-balancer/use-cases/redirect-requests-from-http-to-https.md)

- [获取客户端真实IP](products/slb/documents/classic-load-balancer/use-cases/preserve-client-ip-addresses-when-layer-7-listeners-are-used.md)

- 

## 热门视频

- 

负载均衡SLB介绍

- 

应用型负载均衡快速入门

- 

ALB Ingress概述

- 

使用CLB部署HTTPS业务（单向认证）

- 

传统型负载均衡CLB配置会话保持

- 

传统型负载均衡CLB配置访问控制

- 

CLB配置将流量转发到虚拟服务器组

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
