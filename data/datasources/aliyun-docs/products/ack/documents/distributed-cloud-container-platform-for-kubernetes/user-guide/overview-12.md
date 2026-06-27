# 分布式无服务器工作流编排-分布式工作流Argo集群-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/distributed-cloud-container-platform-for-kubernetes/user-guide/overview-12

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

# Serverless Argo Workflows集群概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

分布式工作流Argo集群（简称工作流集群或Serverless Argo Workflows）采用无服务器模式，使用阿里云容器计算服务ACS/弹性容器实例ECI运行工作流，通过优化开源工作流引擎性能及Kubernetes集群参数，实现大规模工作流的高效弹性调度，同时配合Best Effort实例/抢占式ECI实例，优化成本。本文介绍工作流集群的控制台操作入口、功能优势、原理图和网络规划。

## 控制台操作入口

[ACK One](https://cs.console.aliyun.com/one#/argowf/cluster/detail)[工作流集群控制台](https://cs.console.aliyun.com/one#/argowf/cluster/detail)

## 适用场景

Argo Workflows是一个强大的云原生工作流引擎，是CNCF毕业项目，毕业意味着该项目符合用户采用、安全、广泛度的最高标准。其使用场景主要包括批量数据处理、机器学习Pipeline、基础设施自动化、CI/CD等。在自动驾驶、科学计算、金融量化、数字媒体等行业均有非常广泛的实践。

Argo Workflows拥有以下几大特性让其在批量任务编排领域脱颖而出：

- 

云原生：专为Kubernetes而设计，每个任务都是一个Pod，是Kubernetes上最受欢迎的工作流引擎。

- 

轻量可扩展：轻量化，无VM开销。弹性可扩展，可并行启动数千个任务。

- 

强大的编排能力：可以编排各种类型任务，包括普通Job、Spark、Ray、Tensor Job等。

## Serverless Argo Workflows优势

工作流集群基于[开源](https://argoproj.github.io/argo-workflows/)[Argo Workflow](https://argoproj.github.io/argo-workflows/)[项目](https://argoproj.github.io/argo-workflows/)构建，完全符合开源工作流标准，如果您已在ACK集群或者其他Kubernetes集群运行Argo工作流，无需修改现有工作流，可以无缝迁移至工作流集群。

通过工作流集群，您可以轻松编排工作流，每个工作流步骤使用容器运行，可以在短时间内轻松运行大规模机器学习或数据处理的计算密集型作业，可以快速运行CI/CD流水线。

- 

基于开源Argo Workflows，无需修改现有Argo工作流可无缝迁移。

- 

开箱即用，无运维成本，无需关心版本升级，专注工作流运行。

- 

极致弹性，自动扩展，资源用完即释放，有效优化计算成本。

- 

可靠性高，多可用区负载均衡，调度可靠性高。

- 

增强控制面，性能、效率、稳定性、可观测性大幅提升。

- 

OSS存储管理增强，支持大文件上传、Artifacts GC、流式传输。

- 

社区专家支持，帮助业务团队优化工作流，有效提升运行性能、降低成本。

## 原理图

工作流集群是无服务器Serverless工作流引擎，基于Kubernetes集群构建，托管了开源[Argo Workflows](https://argoproj.github.io/argo-workflows/)。

## 网络规划

- 

目前开放地域：华北2（北京）、华东1（杭州）、华东2（上海）、华南1（深圳）、华北2（张家口）、华南2（河源）、华南3（广州）、中国香港、新加坡、马来西亚（吉隆坡）、印度尼西亚（雅加达）、日本（东京）、德国（法兰克福）、英国（伦敦）、泰国（曼谷）。如有其他地域的需求，请加入钉钉群（钉钉群号：35688562），联系产品技术专家进行咨询。

- 

创建或选择一个VPC专有网络。

- 

创建或选择交换机。

- 

规划交换机的网段，保证可用IP数量以满足Argo workflow的运行要求。因为Argo Workflows工作流在运行过程中可能会创建大量的Kubernetes Pod，每个Pod运行过程中都会消耗一个交换机的IP。

- 

在所选地域的每个可用区创建一个交换机，并使用多个交换机的ID作为创建工作流引擎实例的输入。工作流引擎实例将自动选择库存充足的可用区创建ACS Pod/ECI，从而满足大规模工作流的运行。否则，若可用区库存不足，将导致工作流不能获取ACS Pod/ECI资源而运行失败。

[上一篇：分布式工作流Argo集群](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/kubernetes-clusters-for-distributed-argo-workflows.md)[下一篇：工作流集群快速入门](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/workflow-cluster-quickstart.md)

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
