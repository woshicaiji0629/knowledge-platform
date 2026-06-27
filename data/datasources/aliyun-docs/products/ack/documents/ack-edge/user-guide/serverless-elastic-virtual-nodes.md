# 调度Pod到弹性容器实例运行-虚拟节点-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/serverless-elastic-virtual-nodes

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

# 虚拟节点Serverless弹性

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当您需要在短时间内快速创建大量Pod时，云端ECS节点扩容速度可能无法满足要求，而预留额外的ECS节点又会产生资源浪费。借助虚拟节点，您无需提前预留和维护固定资源池，可以直接将Pod调度到虚拟节点上以弹性容器实例ECI来运行，在保障弹性的同时节约资源成本。

## 为什么使用虚拟节点

### 虚拟节点是什么

在ACK集群中，节点是运行工作负载的基本单位，提供实际的计算和存储资源。通常，您的ACK集群会有至少一组ECS节点池，创建Pod时，kubelet会将Pod调度到ECS节点上运行。这种架构能很好地应对流量稳定的业务。如果您的业务有不易提前预测的瞬时波峰，尽管ACK支持弹性伸缩，但ECS节点池扩容时，ECS实例的创建和启动本身会有一定的额外耗时。借助虚拟节点，您可以直接调度Pod到[阿里云弹性容器实例](https://cn.aliyun.com/product/eci)[ECI（Elastic Container Instance）](https://cn.aliyun.com/product/eci)上运行，降低节点运维操作负担，同时避免产生闲置节点资源，降低成本。

重要

相较于ECS节点，虚拟节点本身不支持自定义Label、Annotation、Taint。

虚拟节点通过[ack-virtual-node](products/ack/documents/product-overview/ack-virtual-node.md)[组件](products/ack/documents/product-overview/ack-virtual-node.md)封装计算资源，无需管理底层基础设施即可直接部署工作负载，ack-virtual-node会自动将应用Pod调度到ECI上运行。ECI是Serverless容器运行服务，一个ECI实例相当于一个Pod。使用ECI部署容器应用时，您只需要提供打包好的容器镜像，即可运行容器，并仅为容器实际运行消耗的资源付费。

### 功能优势

虚拟节点有如下使用优势。

- 

免运维：无需关心底层资源池的创建，减少运维负担。同时，虚拟节点为托管资源，省去Kubernetes节点的常规运维操作，例如系统升级、安全补丁修复等。

- 

超大容量：最多可弹出50,000个Pod，无需提前规划容量。

重要

在Pod大量关联Service的情况下，建议保持在20,000个以内。

- 

秒级弹性：在极短时间内创建出数千Pod，无需担心突发业务流量因Pod创建时延受到影响。

- 

安全隔离：Pod基于ECI创建，每个容器实例底层通过轻量级虚拟化安全沙箱技术完全强隔离，容器实例间互不影响。

- 

节省成本：应用按需创建，按量计费，不运行不计费，省去资源闲置费用，同时Serverless带来更低的运维成本。

### 使用场景

基于虚拟节点本身的特性和优势，其典型使用场景如下所示。

- 

在线业务

对于在线教育、电商等时常出现突发流量的在线业务，支持秒级扩容，避免流量激增扩容不及时可能导致的系统故障，以及平时大量闲置资源造成的浪费。

- 

数据处理

处理Spark、Presto等大批量在线数据并发任务时，可以不再因为成本原因受限于底层资源， 从而导致数据处理任务的并发度受限。支持在短时间内快速弹出数千Pod，满足大数据的在线处理诉求。

- 

AI任务

针对模型训练、模型推理等无需持续运行且需要大量计算资源的AI任务，无需预留资源，按需使用，按秒计费，降低AI推理成本。同时，支持秒级弹性，可以快速响应突发的任务需求。

- 

CI/CD测试环境

针对CI/CD过程中的批量测试任务，例如CI打包、压力测试、仿真测试等，可以借助虚拟节点随时创建和释放容器实例。支持按需使用，按秒计费，实现低成本的大规模资源供应。

- 

Job和CronJob

Job类任务无需持续运行，任务完成后，Job会自动终止，对应的Pod也会被删除。虚拟节点支持在任务完成后自动停止计费并释放计算资源，避免资源闲置浪费。

## 使用限制

您可以在1.28及以上版本的ACK Edge集群中使用虚拟节点，使用前，请先了解其使用限制。

- 

不支持DaemonSet型工作负载。您可以通过将DaemonSet重新配置为Pod的Sidecar容器来运行。

- 

不支持在Podmanifest中指定HostPath和HostNetwork。

- 

不支持Privileged特权容器。您可以使用Security Context为Pod添加Capability。

说明

特权容器功能正在内测中。如需体验，请提交工单申请。

- 

不支持NodePort类型的Service，不支持配置Session Affinity。

- 

不支持深圳金融云，不支持政务云。

## 计费说明

虚拟节点本身不收费，在虚拟节点上运行的ECI Pod按照ECI计费规则进行计费。具体请参见[ECI](https://help.aliyun.com/zh/eci/product-overview/billing-overview)[计费概述](https://help.aliyun.com/zh/eci/product-overview/billing-overview)。

说明

ECI Pod采用按量付费，从Pending状态开始计费，至Succeeded或Failed状态停止计费。更多信息，请参见[ECI Pod](https://help.aliyun.com/zh/eci/user-guide/lifecycle-of-an-elastic-container-instance-2)[生命周期](https://help.aliyun.com/zh/eci/user-guide/lifecycle-of-an-elastic-container-instance-2)。

## 快速体验

您可以参见[将](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md)[Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md)[调度到](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md)[ECI](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md)[上运行](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md)快速体验虚拟节点的基础用法。

## 相关操作

当您升级集群时，系统会自动校验ECI Platform Version和Kubernetes的兼容情况，对于ECI Platform Version和目标Kubernetes版本不兼容的ECI Pod，需要手动删除重建ECI Pod后，才能升级集群的Kubernetes版本。升级集群前，请确保ECI Platform Version与Kubernetes版本兼容。更多信息，请参见[升级](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/eci-platform-version-compatibility-matrix.md)[ECI Platform Version](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/eci-platform-version-compatibility-matrix.md)。

- 

- 

- 

- 

- 

| 支持的操作 | 说明 | 相关文档 |
| --- | --- | --- |
| 灵活配置 Pod | 在集群维度通过编写 ECI Profile 配置文件（名为 eci-profile 的 ConfigMap）批量配置 ECI Pod，例如指定安全组、指定交换区（即 ECI Pod 所在的可用区）等。配置更新后，ECI Pod 无需重启，新建 ECI Pod 可以即时生效，存量 ECI Pod 滚动发布后可生效。 | [配置](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-an-eci-profile.md) [eci-profile](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-an-eci-profile.md) |
| 对于 ECI 某些功能特性，例如指定 ECI 实例规格、启用镜像缓存以加速 Pod 创建、为 ECI Pod 分配 IPv6 地址、增加临时存储空间大小等，可以通过 Pod Annotation 来实现。 | [ECI Pod Annotation](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/pod-annotations-1.md) |  |
| 调度 Pod 至虚拟节点 | ACK 提供多种调度方案。您可以指定应用 Pod 只调度到虚拟节点，也可以指定 Pod 优先调度到 ECS 节点（包年包月或按量付费），并在 ECS 节点资源不足时再调度至虚拟节点，同时实现逆序缩容。请参见 [调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-and-introduction-of-virtual-node-scheduling-scheme-ack.md) [Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-and-introduction-of-virtual-node-scheduling-scheme-ack.md) [至虚拟节点](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-and-introduction-of-virtual-node-scheduling-scheme-ack.md) 完成调度策略的选型。 | [开启集群虚拟节点调度策略](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/enable-ack-serverless-cluster-virtual-node-scheduling-policy.md) [将](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md) [Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md) [调度到](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md) [ECI](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md) [上运行](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md) [通过](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster) [ACK](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster) [托管集群](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster) [Pro](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster) [版使用](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster) [ACS](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster) [算力](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster) [指定](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-eci-scaling.md) [ECS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-eci-scaling.md) [和](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-eci-scaling.md) [ECI](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-eci-scaling.md) [的资源分配](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-eci-scaling.md) [实现](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/spread-elastic-container-instance-based-pods-across-zones-and-configure-affinities.md) [ECI Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/spread-elastic-container-instance-based-pods-across-zones-and-configure-affinities.md) [可用区打散以及亲和调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/spread-elastic-container-instance-based-pods-across-zones-and-configure-affinities.md) |
| 调度 Pod 至指定的 OS 或 Arch | ACK 集群默认将工作负载 Pod 调度到 x86 架构的虚拟节点，并在 x86 节点资源不足时保持等待 x86 节点资源。您还可以将工作负载 Pod 调度至 Arm 架构的虚拟节点上。 | [调度至](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/schedule-workloads-to-arm-based-virtual-nodes.md) [Arm](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/schedule-workloads-to-arm-based-virtual-nodes.md) [虚拟节点](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/schedule-workloads-to-arm-based-virtual-nodes.md) |
| 如果您的容器需要运行在 Windows 环境中，您可以在集群中添加 Windows 虚拟节点，并将 Pod 调度到该虚拟节点上。 | [（邀测）调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/scheduling-a-pod-to-a-windows-virtual-node.md) [Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/scheduling-a-pod-to-a-windows-virtual-node.md) [到](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/scheduling-a-pod-to-a-windows-virtual-node.md) [Windows](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/scheduling-a-pod-to-a-windows-virtual-node.md) [虚拟节点](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/scheduling-a-pod-to-a-windows-virtual-node.md) |  |
| 虚拟节点最佳实践 | 通过虚拟节点运行 Job 任务的方式，您可以用最小的运维成本（无需调整节点数量）来应对集群计算资源高峰压力。 | [基于](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-an-elastic-container-instance-to-run-a-job.md) [ECI](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-an-elastic-container-instance-to-run-a-job.md) [运行](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-an-elastic-container-instance-to-run-a-job.md) [Job](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-an-elastic-container-instance-to-run-a-job.md) [任务](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-an-elastic-container-instance-to-run-a-job.md) |
| 您可以在 ACK 集群中使用弹性容器实例 ECI 运行 Spark 作业。通过使用 ECI 弹性资源并配置合适的调度策略，您可以按需创建 ECI Pod，并按资源使用量按需付费，从而有效减少资源闲置带来的成本浪费，进而更加经济高效地运行 Spark 作业。 | [使用](products/ack/documents/ack-managed-and-ack-dedicated/use-cases/use-eci-elastic-resources-to-run-spark-jobs-efficiently.md) [ECI](products/ack/documents/ack-managed-and-ack-dedicated/use-cases/use-eci-elastic-resources-to-run-spark-jobs-efficiently.md) [弹性资源运行](products/ack/documents/ack-managed-and-ack-dedicated/use-cases/use-eci-elastic-resources-to-run-spark-jobs-efficiently.md) [Spark](products/ack/documents/ack-managed-and-ack-dedicated/use-cases/use-eci-elastic-resources-to-run-spark-jobs-efficiently.md) [作业](products/ack/documents/ack-managed-and-ack-dedicated/use-cases/use-eci-elastic-resources-to-run-spark-jobs-efficiently.md) |  |
| 借助虚拟节点组件（ACK Virtual Node）仅为调度到虚拟节点上的 Pod 自动注入 Sidecar 容器，来解耦虚拟节点 Pod 的 Sidecar 容器与业务容器。 | [向虚拟节点](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/injecting-a-sidecar-container-into-a-virtual-node-pod.md) [Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/injecting-a-sidecar-container-into-a-virtual-node-pod.md) [注入](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/injecting-a-sidecar-container-into-a-virtual-node-pod.md) [Sidecar](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/injecting-a-sidecar-container-into-a-virtual-node-pod.md) [容器](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/injecting-a-sidecar-container-into-a-virtual-node-pod.md) |  |
| 通过修改 Prometheus 监控配置来采集指定虚拟节点的 Metrics。 | [采集指定虚拟节点的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-the-metrics-of-a-specified-virtual-node.md) [Metrics](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-the-metrics-of-a-specified-virtual-node.md) |  |
| 虚拟节点支持服务发现功能，目前支持 Intranet service、Headless service、ClusterIP service。 | [虚拟节点基于云解析](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-alibaba-cloud-dns-privatezone-to-implement-service-discovery-on-virtual-nodes.md) [PrivateZone](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-alibaba-cloud-dns-privatezone-to-implement-service-discovery-on-virtual-nodes.md) [的服务发现](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-alibaba-cloud-dns-privatezone-to-implement-service-discovery-on-virtual-nodes.md) |  |
| 虚拟节点 FAQ | 虚拟节点使用常见问题。 | [虚拟节点](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/virtual-node-faq.md) [FAQ](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/virtual-node-faq.md) |


、

[上一篇：启用节点自动伸缩](products/ack/documents/ack-edge/user-guide/auto-scaling-of-nodes.md)[下一篇：将Pod调度到ECI上运行](products/ack/documents/ack-edge/user-guide/deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md)

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
