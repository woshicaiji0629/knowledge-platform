# Nginx Ingress概述-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/serverless-kubernetes/user-guide/overview-2

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/serverless-kubernetes/product-overview.md)

- [快速入门](products/ack/documents/serverless-kubernetes/getting-started.md)

- [操作指南](products/ack/documents/serverless-kubernetes/user-guide.md)

- [实践教程](products/ack/documents/serverless-kubernetes/use-cases.md)

- [安全合规](products/ack/documents/serverless-kubernetes/security-and-compliance.md)

- [开发参考](products/ack/documents/serverless-kubernetes/developer-reference.md)

- [服务支持](products/ack/documents/serverless-kubernetes/support.md)

[首页](https://help.aliyun.com/zh)

# Nginx Ingress概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍Ingress基本概念、Ingress Controller工作原理和Nginx Ingress Controller的使用说明。

重要

由于Ingress NGINX开源项目于2026年3月后停止维护更新，容器服务 Kubernetes 版将停止Nginx Ingress Controller组件维护，请充分了解使用风险。更多详细内容，请参见[【产品公告】关于停止维护](products/ack/documents/product-overview/product-announcement-announcement-on-end-of-maintenance-for-nginx-ingress-controller.md)[Nginx Ingress Controller](products/ack/documents/product-overview/product-announcement-announcement-on-end-of-maintenance-for-nginx-ingress-controller.md)[组件的公告](products/ack/documents/product-overview/product-announcement-announcement-on-end-of-maintenance-for-nginx-ingress-controller.md)。

## Ingress基本概念

在Kubernetes集群中，Ingress作为集群内服务对外暴露的访问接入点，几乎承载着集群内服务访问的所有流量。Ingress是Kubernetes中的一个资源对象，用来管理集群外部访问集群内部服务的方式。您可以通过Ingress资源来配置不同的转发规则，从而实现根据不同的规则设置访问集群内不同的Service所对应的后端Pod。关于ACK中Ingress对比的详细内容，请参见[Nginx Ingress、ALB Ingress](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-among-nginx-ingresses-alb-ingresses-and-mse-ingresses-1.md)[和](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-among-nginx-ingresses-alb-ingresses-and-mse-ingresses-1.md)[MSE Ingress](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-among-nginx-ingresses-alb-ingresses-and-mse-ingresses-1.md)[对比](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-among-nginx-ingresses-alb-ingresses-and-mse-ingresses-1.md)。

## Ingress Controller工作原理

Ingress Controller用于解析Ingress的转发规则。Ingress Controller收到请求，匹配Ingress转发规则转发到后端Service所对应的Pod，由Pod处理请求。Kubernetes中Service、Ingress与Ingress Controller有着以下关系：

- 

Service是后端真实服务的抽象，一个Service可以代表多个相同的后端服务。

- 

Ingress是反向代理规则，用来规定HTTP、HTTPS请求应该被转发到哪个Service所对应的Pod上。例如根据请求中不同的Host和URL路径，让请求落到不同Service所对应的Pod上。

- 

Ingress Controller是一个反向代理程序，负责解析Ingress的反向代理规则。如果Ingress有增删改的变动，Ingress Controller会及时更新自己相应的转发规则，当Ingress Controller收到请求后就会根据这些规则将请求转发到对应Service的Pod上。

Ingress Controller通过API Server获取Ingress资源的变化，动态地生成Load Balancer所需的配置文件，然后依次生成新的路由转发规则。

## Nginx Ingress Controller使用说明

当前Kubernetes官方维护的是Nginx Ingress Controller，ACK Serverless基于社区版的Nginx Ingress Controller进行了优化。当在创建ACK Serverless集群时，您选择安装的Nginx Ingress Controller组件即为ACK Serverless定制版的Nginx Ingress Controller组件。

## 相关文档

- 

[安装](products/ack/documents/serverless-kubernetes/user-guide/install-the-nginx-ingress-controller.md)[Nginx Ingress Controller](products/ack/documents/serverless-kubernetes/user-guide/install-the-nginx-ingress-controller.md)

- 

[创建并使用](products/ack/documents/serverless-kubernetes/user-guide/create-an-nginx-ingress.md)[Nginx Ingress](products/ack/documents/serverless-kubernetes/user-guide/create-an-nginx-ingress.md)[对外暴露服务](products/ack/documents/serverless-kubernetes/user-guide/create-an-nginx-ingress.md)

- 

[Ingress](products/ack/documents/serverless-kubernetes/user-guide/advanced-ingress-configurations.md)[高级用法](products/ack/documents/serverless-kubernetes/user-guide/advanced-ingress-configurations.md)

[上一篇：Nginx Ingress管理](products/ack/documents/serverless-kubernetes/user-guide/nginx-ingress-management-1.md)[下一篇：安装Nginx Ingress Controller](products/ack/documents/serverless-kubernetes/user-guide/install-the-nginx-ingress-controller.md)

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
