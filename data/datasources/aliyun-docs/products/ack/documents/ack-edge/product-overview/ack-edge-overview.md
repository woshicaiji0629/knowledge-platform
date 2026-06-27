# 边缘计算场景云边一体化协同托管-ACK Edge集群-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/product-overview/ack-edge-overview

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

# 什么是ACK Edge集群

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

阿里云容器服务 Edge 版是阿里云容器服务针对边缘计算场景推出的云边一体化协同托管方案。本文介绍阿里云ACK Edge集群的产生背景和主要功能。

## 产品简介

随着互联网智能终端设备数量的急剧增加，以及5G和物联网时代的到来，传统[云计算](https://www.aliyun.com/getting-started/what-is/what-is-cloud-computing)中心集中存储、计算的模式已经无法满足终端设备对于时效、容量、算力的需求。将云计算的能力下沉到边缘侧、设备侧，并通过中心进行统一交付、运维、管控，将是云计算的重要发展趋势。

阿里云ACK Edge集群在云端提供一个标准、安全、[高可用](https://www.aliyun.com/getting-started/what-is/what-is-high-availability)的[Kubernetes](https://www.aliyun.com/getting-started/what-is/what-is-kubernetes)集群，整合阿里云[虚拟化](https://www.aliyun.com/getting-started/what-is/what-is-virtualization)、存储、网络和安全等能力，并简化集群运维工作，让您专注于[容器](https://www.aliyun.com/getting-started/what-is/what-is-container)化应用的开发与管理。ACK Edge集群具有以下特点：

- 

支持本地IDC资源快速接入，实现云原生容器化管理。

- 

支持各种类型GPU异构设备接入，并支持云原生AI套件，提升AI任务开发、调度与运行效率。

- 

支持云上弹性，本地IDC资源不足，及时补充云上CPU和GPU算力，并支持云上云下混合调度能力。

- 

支持多种边缘计算资源的快速接入，包括[CDN](https://www.aliyun.com/getting-started/what-is/what-is-cdn)资源、[IoT](https://www.aliyun.com/getting-started/what-is/what-is-iot)网关设备、端设备等。

- 

支持云端托管，帮助您快速构建集成云端、IDC、[边缘计算](https://www.aliyun.com/getting-started/what-is/what-is-edge-computing)资源的分布式[云原生](https://www.aliyun.com/getting-started/what-is/what-is-cloud-native)基础设施。

- 

支持丰富的应用场景，包括IDC计算资源容器化管理、GPU异构资源管理、边缘智能、智慧楼宇、智慧工厂、音视频直播、在线教育、CDN等。

阿里云ACK Edge集群，采用非侵入方式增强，提供边缘自治、边缘单元、边缘流量管理、原生运维[API](https://www.aliyun.com/getting-started/what-is/what-is-api)支持等能力，以原生方式支持边缘计算场景下的应用统一生命周期管理和统一资源调度。

## 功能介绍

ACK Edge集群支持对边缘计算场景的容器应用和资源全生命周期管理，具有以下功能：

- 

通过控制台一键创建高可用的ACK Edge集群，并提供集群的扩容、升级、日志、监控等生命周期管理运维能力。

- 

支持丰富的异构边缘节点资源，包括自建IDC资源、[ENS](https://www.aliyun.com/product/network/ens)、IoT设备、x86、Arm架构等，并支持异构资源的混合调度。

- 

面向边缘计算弱网络连接场景，提供节点自治和网络自治能力，以保证边缘节点和边缘业务的高可靠运行。

- 

提供反向运维网络通道能力。

- 

提供边缘单元管理、单元化部署、单元流量管理能力。

## ACK Edge集群交流群

如果您对于ACK Edge集群有任何疑问，欢迎使用钉钉搜索群号21976595加入钉钉交流群。

## 相关文档

[快速入门](products/ack/documents/ack-edge/quick-start.md)

[上一篇：产品概述](products/ack/documents/ack-edge/product-overview.md)[下一篇：ACK Edge集群计费说明](products/ack/documents/ack-edge/product-overview/billing-of-ack-edge-clusters.md)

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
