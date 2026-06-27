# 为工作流指定GPU或AMD等ECS实例规格-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/distributed-cloud-container-platform-for-kubernetes/user-guide/run-a-workflow-using-a-specified-ecs-specification

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

# 使用指定ECS规格运行工作流

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在某些场景下，业务存在着特殊的规格需求，例如GPU、增强的网络能力、高主频、本地盘、AMD机型等。工作流集群支持通过指定的ECS规格运行工作流。本文介绍如何使用指定ECS规格运行工作流。

## 索引

- 

[规格说明](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/run-a-workflow-using-a-specified-ecs-specification.md)

- 

[GPU](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/run-a-workflow-using-a-specified-ecs-specification.md)[规格说明](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/run-a-workflow-using-a-specified-ecs-specification.md)

- 

[AMD](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/run-a-workflow-using-a-specified-ecs-specification.md)[规格说明](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/run-a-workflow-using-a-specified-ecs-specification.md)

- 

[使用示例](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/run-a-workflow-using-a-specified-ecs-specification.md)

- 

[GPU](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/run-a-workflow-using-a-specified-ecs-specification.md)[示例](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/run-a-workflow-using-a-specified-ecs-specification.md)

- 

[AMD](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/run-a-workflow-using-a-specified-ecs-specification.md)[示例](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/run-a-workflow-using-a-specified-ecs-specification.md)

## 规格说明

### GPU规格说明

当前ECI GPU支持的驱动版本为NVIDIA 460.73.01，可支持的CUDA Tookit版本为11.2。关于CUDA Toolkit的更多信息，请参见[NVIDIA CUDA](https://hub.docker.com/r/nvidia/cuda)。

ECI支持通过指定ECS GPU规格来进行实例的创建。运行工作流支持的ECS GPU规格如下所示。

- 

GPU计算型实例规格族gn6v（NVIDIA V100)，例如ecs.gn6v-c8g1.2xlarge。

- 

GPU计算型实例规格族gn6i（NVIDIA T4)，例如ecs.gn6i-c4g1.xlarge。

- 

GPU计算型实例规格族gn5（NVIDIA P100)，例如ecs.gn5-c4g1.xlarge。

- 

GPU计算型实例规格族gn5i（NVIDIA P4)，例如ecs.gn5i-c2g1.large。

关于完整的ECS GPU规格定义，请参见[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)。

### AMD规格说明

ECI支持指定ECS AMD规格来创建AMD实例。AMD实例指的是处理器为AMD EPYCTM ROME的实例，该规格的特点为：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，可以提供稳定可预期的超高性能。适用于视频编解码、高网络包收发、Web前端服务器、大型多人在线游戏（MMO）前端、测试开发（DevOps）等场景。

运行工作流支持指定的ECS AMD规格族如下。

- 

通用型实例规格族g7a、g6a，例如ecs.g7a.large、ecs.g6a.large。

- 

计算型实例规格族c7a、c6a，例如ecs.c7a.large、ecs.c6a.large。

- 

内存型实例规格族r7a、r6a，例如ecs.r7a.large、ecs.r6a.large。

关于完整的ECS AMD规格定义，请参见[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)。

## 使用示例

您可以在Pod metadata中添加Annotation来指定ECS GPU和ECS AMD规格，即在Pod声明中增加annotations: k8s.aliyun.com/eci-use-specs指定支持使用的实例规格。使用示例如下。

### GPU示例

apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: hello-world- spec: entrypoint: whalesay templates: - name: whalesay metadata: annotations: k8s.aliyun.com/eci-use-specs: ecs.gn5i-c4g1.xlarge # 指定支持的ECS GPU规格。 container: image: docker/whalesay command: [ cowsay ] args: [ "hello world" ]

### AMD示例

apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: hello-world- spec: entrypoint: whalesay templates: - name: whalesay metadata: annotations: k8s.aliyun.com/eci-use-specs: "ecs.c6a.xlarge" # 指定支持的ECS AMD规格。 container: image: docker/whalesay command: [ cowsay ] args: [ "hello world" ]

[上一篇：创建工作流](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/create-a-workflow.md)[下一篇：使用存储卷](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/use-volumes.md)

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
