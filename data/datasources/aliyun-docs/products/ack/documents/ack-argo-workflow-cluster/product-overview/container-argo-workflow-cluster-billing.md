# 计费组成计费项计费方式-容器服务Kubernetes版ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/product-overview/container-argo-workflow-cluster-billing

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-argo-workflow-cluster/product-overview.md)

- [服务支持](products/ack/documents/ack-argo-workflow-cluster/support.md)

- [实践教程](products/ack/documents/ack-argo-workflow-cluster/use-cases.md)

- [操作指南](products/ack/documents/ack-argo-workflow-cluster/user-guide.md)

[首页](https://help.aliyun.com/zh)

# 容器Argo工作流集群计费说明

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍容器Argo工作流集群的计费说明。

## 计费说明

### 计费组成

容器Argo工作流集群的费用由[集群管理计费](products/ack/documents/ack-argo-workflow-cluster/product-overview/container-argo-workflow-cluster-billing.md)和[云产品资源计费](products/ack/documents/ack-argo-workflow-cluster/product-overview/container-argo-workflow-cluster-billing.md)组成。

### 集群管理计费

容器Argo工作流集群对每个集群收取集群管理费用：

公共云的不同地域、金融云、政务云的集群管理费用单价可能不同，实际价格以控制台显示为准。

| 计费方式 | 价格 |
| --- | --- |
| 按量计费 | 每个集群 0.64 元/小时 |


### 云产品资源计费

容器Argo工作流集群在使用过程中，会使用阿里云其他云产品的资源，各云产品会按照计费规则收取费用。如果未使用特定阿里云云产品，则不收取资源费用。

| 云产品名称 | 开通选项 | 产品说明 | 是否支持包年包月 | 是否支持资源包 | 计费说明 |
| --- | --- | --- | --- | --- | --- |
| [容器计算服务](https://help.aliyun.com/zh/cs/product-overview/product-introduction) [ACS](https://help.aliyun.com/zh/cs/product-overview/product-introduction) | 必须开通 | 为运行 Argo 工作流提供算力。 | 不支持 | 不支持 ACS 支持 [节省计划](https://help.aliyun.com/zh/cs/product-overview/savings-plan) 。 | [产品计费](https://help.aliyun.com/zh/cs/product-overview/product-billing-rules) |
| [专有网络](products/vpc/documents/what-is-vpc.md) [VPC](products/vpc/documents/what-is-vpc.md) | 必须开通 | 用于构建集群网络环境和路由规则。 | 不支持 | 不支持 | [产品计费](products/vpc/documents/product-overview/product-billing.md) |
| [传统型负载均衡](products/slb/documents/classic-load-balancer/product-overview/what-is-clb.md) [CLB](products/slb/documents/classic-load-balancer/product-overview/what-is-clb.md) | 必须开通 | 为集群 API Server 提供负载均衡实例。 | 不支持 | 不支持 | [计费概述](products/slb/documents/classic-load-balancer/product-overview/billing-overview.md) |
| [弹性公网](products/eip/documents/product-overview/what-is-eip.md) [IP](products/eip/documents/product-overview/what-is-eip.md) | 可选 | 为 API Server 提供公网服务。 | 不支持 | 不支持 | [计费概述](products/eip/documents/billing-overview.md) |
| [日志服务](products/sls/documents/what-is-log-service.md) [SLS](products/sls/documents/what-is-log-service.md) | 可选 | 用于集群组件和应用的日志采集和检索。 | 不支持 | 支持 可根据业务需要 [选购资源包](products/sls/documents/purchase-a-resource-plan.md) 。 | [计费概述](products/sls/documents/billing-overview.md) |
| [对象存储](products/oss/documents/user-guide/what-is-oss.md) [OSS](products/oss/documents/user-guide/what-is-oss.md) | 可选 | 用于为工作流集群事件驱动功能提供事件源。 | 不支持 | 支持 可根据业务需要 [购买资源包](products/oss/documents/purchase-resource-plans.md) 。 | [计费概述](products/oss/documents/billing-overview.md) |
| [轻量消息队列（原 MNS）](https://help.aliyun.com/zh/mns/product-overview/what-is-mns) | 可选 | 用于为工作流集群事件驱动功能提供事件源。 | 不支持 | 不支持 | [计费说明](https://help.aliyun.com/zh/mns/product-overview/billing-overview) |
| [可观测监控 Prometheus 版](products/arms/documents/prometheus-monitoring/product-overview/what-is-prometheus.md) | 可选 | 基于 Prometheus 实现对集群的监控和告警。 | 不支持 | 不支持 | [计费概述](products/arms/documents/prometheus-monitoring/product-overview/billing-overview-2.md) |


[上一篇：容器Argo工作流集群概述](products/ack/documents/ack-argo-workflow-cluster/product-overview/container-argo-workflow-cluster-overview.md)[下一篇：服务支持](products/ack/documents/ack-argo-workflow-cluster/support.md)

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
