# 根据负载需求自动调整集群计算资源-弹性伸缩-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/auto-scaling-overview

# 弹性伸缩概述
如果您业务的资源需求不易预测或有周期性变化（例如Web应用、游戏服务、在线教育等），推荐您在集群中启用弹性伸缩。根据负载需求情况，工作负载伸缩支持自动调整应用Pod的副本数量或资源配置，计算资源伸缩支持自动调整节点资源，从而平稳应对流量峰值并降低成本。
## 使用前说明
本文面向集群运维人员、开发人员等介绍ACK集群的弹性伸缩方案（工作负载伸缩和节点伸缩）。建议您已了解社区工作负载伸缩方案（例如[HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)、[VPA](https://github.com/kubernetes/autoscaler/tree/vpa-release-0.8/vertical-pod-autoscaler)等）和节点伸缩方案（例如[Cluster Autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/cluster-autoscaling/)）的相关内容等。
如果您的集群为大规模集群（通常为超过500个节点或者10,000个Pod的集群），请参见[规划集群资源弹性速率](suggestions-on-how-to-work-with-large-ack-pro-clusters.md)了解相关使用建议，以确保集群和控制面的稳定性。
## 工作负载伸缩和计算资源伸缩
ACK的弹性伸缩提供以下两种维度的方案。
工作负载伸缩：调度层弹性方案，作用于Pod，通过增减Pod副本数量或调整Pod资源配置来适应负载变化。例如，HPA支持根据工作负载流量自动调整工作负载Pod的副本数，调整的副本数会改变当前负载占用的调度容量，从而实现调度层的伸缩。
计算资源伸缩：资源层弹性方案，包括节点伸缩方案和虚拟节点方案，支持根据Pod的调度情况和资源使用情况动态地添加或移除计算资源。
推荐您将两种方案搭配使用，既能通过调整工作负载Pod副本数来提高资源利用率，又能在集群维度通过调整计算资源容量来保证Pod总能获得足够的计算资源。
### 工作负载伸缩方案
Kubernetes支持使用kubectl scale命令手动调整工作负载Pod的数量，但需要运维人员自行判断，仅适用于临时性的副本数管理。您可以参见下表选择方案，享受ACK工作负载伸缩方案在成本控制、稳定性保障和资源容量灵活管理等维度提供的支持。
| 方案 | 介绍 | 扩缩依据的指标 | 使用场景 | 相关文档 |
| --- | --- | --- | --- | --- |
| HPA | 在业务负载上升时快速扩容 Pod 副本来缓解压力，在业务负载变小时适当缩容以节省资源，是最常用的应用弹性方案。 | 资源指标（CPU、内存使用率） 其他 [自定义指标](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#scaling-on-custom-metrics) | 服务波动较大、服务数量多且需要频繁扩缩容的在线业务场景，例如电商服务、在线教育、金融服务等。 | [使用容器水平伸缩（HPA）](horizontal-pod-autoscaling.md) |
| CronHPA | 类似 Crontab 的策略，定时对 Pod 进行扩缩容，可配置时区、执行的日期、跳过执行的日期（例如节假日），支持和 HPA 协同使用。 | 定时扩缩容 | 业务流量有明显高峰时段、应用程序需要在特定时间执行任务等场景。 | [使用容器定时水平伸缩（CronHPA）](cronhpa.md) [实现](make-cronhpa-compatible-with-hpa.md) [CronHPA](make-cronhpa-compatible-with-hpa.md) [与](make-cronhpa-compatible-with-hpa.md) [HPA](make-cronhpa-compatible-with-hpa.md) [的协同](make-cronhpa-compatible-with-hpa.md) |
| VPA | 监控 Pod 的资源消耗模式，灵活推荐 CPU 和内存资源分配的配置，并在适当的情况下自动进行调整，而不调整 Pod 的副本数量。 | 推荐并自动调整 Pod 中容器的 CPU 及内存的 Request 和 Limit | 需要稳定资源配置的有状态应用的扩容、大型单体应用等场景，通常是在 Pod 出现异常恢复时生效。 | [使用容器垂直伸缩（VPA）](vertical-pod-autoscaling.md) |
| KEDA | 支持丰富的事件源，为工作负载提供事件驱动的自动伸缩能力。 | 事件数量，例如队列长度 | 需要即时弹性的场景，尤其是基于事件源的离线作业场景，例如音视频离线转码、事件驱动作业、流式数据处理等。 | [事件驱动弹性](ack-keda.md) |
| AHPA | 根据业务历史指标，自动、主动识别弹性周期并对容量进行预测，提前进行弹性规划，解决弹性滞后的问题。 | 资源指标（CPU、内存、GPU 使用率） 流量指标（QPS、RT） 其他自定义指标 | 业务流量有明显周期性的场景，例如直播、在线教育、游戏服务等。 | [弹性伸缩预测（AHPA）](ahpa-overview-1.md) |
此外，您也可以使用UnitedDeployment来定义工作负载。UnitedDeployment通过弹性单元Subset来灵活、便捷地管理多个同质的工作负载，动态分配在各Subset上的工作负载副本数量。您可以将UnitedDeployment和上述工作负载伸缩方案搭配使用，实现工作负载的灵活扩缩容与调度，例如多种计算资源混合使用场景。更多信息，请参见[基于](use-the-uniteddeployment-controller-in-ack-clusters.md)[UnitedDeployment](use-the-uniteddeployment-controller-in-ack-clusters.md)[实现工作负载的伸缩](use-the-uniteddeployment-controller-in-ack-clusters.md)。
### 计算资源伸缩方案
在业务量波动大、需要快速响应的场景下，集群需要一种能够根据工作负载变化情况自动调整计算资源的方案，以在提高系统弹性的同时降低运维成本。计算伸缩方案提供的组件会监听Pod是否处于调度失败的状态，以判断是否需要新增ECS节点或ECI Pod资源。
您可以参见[节点伸缩](overview-of-node-scaling.md)了解节点伸缩的功能原理。
重要
下表提供的资源交付数据仅为理论值（参考值），实际数据以您的操作环境为准。
| 方案 | 介绍 | 使用场景 | 资源交付速度 | 相关文档 |
| --- | --- | --- | --- | --- |
| 节点自动伸缩 | 当集群的容量规划无法满足应用 Pod 调度时，自动调整节点的数量。 | 全场景通用，面向在线业务、深度学习等场景，适用于扩容规模较小（例如开启弹性的节点池数量少于 20，或对应节点池中的节点数量少于 100），工作负载批次较为稳定，以单次伸缩为主等业务场景。 | 以 100 节点为一个交付批次为例： 标准模式：120s 极速模式：60s 标准模式- [Qboot](https://help.aliyun.com/zh/alinux/product-overview/alibaba-cloud-linux-overview#section-to6-5lp-7d6) [镜像](https://help.aliyun.com/zh/alinux/product-overview/alibaba-cloud-linux-overview#section-to6-5lp-7d6) ：90s 极速模式- [Qboot](https://help.aliyun.com/zh/alinux/product-overview/alibaba-cloud-linux-overview#section-to6-5lp-7d6) [镜像](https://help.aliyun.com/zh/alinux/product-overview/alibaba-cloud-linux-overview#section-to6-5lp-7d6) ：45s | [启用节点自动伸缩](auto-scaling-of-nodes.md) |
| 节点即时弹性 | 在 节点自动伸缩 的基础上， 节点即时弹性 在伸缩速度和效率、资源交付确定性等方面 [更具优势](overview-of-node-scaling.md) ，还支持根据 ECS 实例的库存查看健康度。 | 全场景通用， 集群规模较大（例如弹性节点池中节点数大于 100，或弹性节点池数大于 20）、对资源交付速度有更高要求、期望灵活实现多实例规格和跨可用区自动伸缩、对高级调度策略（例如 TopologySpread Constraints）有需求。 | 以 100 节点为一个交付批次为例： ContainerOS 极速扩容：45s 标准模式：103s 极速模式：暂未支持 | [启用节点即时弹性](instant-elasticity.md) [查看节点即时弹性健康度](view-the-status-of-node-instant-elastic.md) |
| 虚拟节点 | 无需节点运维和容量规划，支持单集群超大 Pod 容量（最多可支持 50000 个 Pod），突发业务流量场景下能够扩容工作负载 Pod，实现每分钟 10000 Pod 弹性能力。 | 全场景通用，尤其适用于任务和定时任务、数据计算、AI、突发业务等场景。 | 以 1000 个 Pod 作为一个交付批次为例： 未开启镜像缓存：30s 开启 [镜像缓存](https://help.aliyun.com/zh/eci/user-guide/overview-of-image-caches-1) ：15s | [将](deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md) [Pod](deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md) [调度到](deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md) [ECI](deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md) [上运行](deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods.md) |
## 计费说明
弹性伸缩功能本身不收费，但弹性伸缩组件会占用Pod资源（节点伸缩的情况下需要至少保留一个节点）。节点伸缩方案下，扩容节点资源产生的计费会正常收取。更多信息，请参见[计费概述](../product-overview/ack-pro-cluster-billing.md)。
## 常见问题
如您在使用弹性伸缩功能时遇到问题，可参见[弹性伸缩](overview-faq-about-auto-scaling.md)[FAQ](overview-faq-about-auto-scaling.md)进行排查。
展开查看节点自动伸缩的FAQ索引
| 分类 | 二级分类 | 跳转链接 |
| --- | --- | --- |
| 节点自动伸缩 的扩缩容行为 | [已知限制](faq-about-node-auto-scaling.md) |  |
| [扩容行为相关](faq-about-node-auto-scaling.md) | [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件使用哪些调度策略来判断不可调度](faq-about-node-auto-scaling.md) [Pod](faq-about-node-auto-scaling.md) [能否调度到开启了弹性的节点池？](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件可模拟判断的资源有哪些？](faq-about-node-auto-scaling.md) [为什么节点自动伸缩组件无法弹出节点？](faq-about-node-auto-scaling.md) [如果一个伸缩组内配置了多资源类型的实例规格，弹性伸缩时如何计算这个伸缩组的资源呢？](faq-about-node-auto-scaling.md) [弹性伸缩时，如何在多个开启弹性的节点池之间进行选择？](faq-about-node-auto-scaling.md) [开启弹性的节点池如何配置自定义资源？](faq-about-node-auto-scaling.md) [为什么为节点池设置自动扩缩容失败？](faq-about-node-auto-scaling.md) |  |
| [缩容行为相关](faq-about-node-auto-scaling.md) | [为什么](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件无法缩容节点？](faq-about-node-auto-scaling.md) [如何启用或禁用特定](faq-about-node-auto-scaling.md) [DaemonSet](faq-about-node-auto-scaling.md) [的驱逐？](faq-about-node-auto-scaling.md) [什么类型的](faq-about-node-auto-scaling.md) [Pod](faq-about-node-auto-scaling.md) [可以阻止](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件移除节点？](faq-about-node-auto-scaling.md) |  |
| [拓展支持相关](faq-about-node-auto-scaling.md) | [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件是否支持](faq-about-node-auto-scaling.md) [CRD？](faq-about-node-auto-scaling.md) |  |
| 自定义的扩缩容行为 | [通过](faq-about-node-auto-scaling.md) [Pod](faq-about-node-auto-scaling.md) [控制扩缩容行为](faq-about-node-auto-scaling.md) | [如何延迟](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件对不可调度](faq-about-node-auto-scaling.md) [Pod](faq-about-node-auto-scaling.md) [的扩容反应时间？](faq-about-node-auto-scaling.md) |
| [通过节点控制扩缩容行为](faq-about-node-auto-scaling.md) | [如何指定节点不被](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件缩容？](faq-about-node-auto-scaling.md) [如何通过](faq-about-node-auto-scaling.md) [Pod Annotation](faq-about-node-auto-scaling.md) [影响](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件的节点缩容？](faq-about-node-auto-scaling.md) |  |
| cluster-autoscaler 组件 相关 | [如何升级](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件至最新版本？](faq-about-node-auto-scaling.md) [哪些操作会触发](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件自动更新？](faq-about-node-auto-scaling.md) [ACK](faq-about-node-auto-scaling.md) [托管集群已经完成了角色授权，但节点伸缩活动仍然无法正常运行？](faq-about-node-auto-scaling.md) |  |
展开查看节点即时弹性的FAQ索引
| 分类 | 二级分类 | 跳转链接 |
| --- | --- | --- |
| 节点即时弹性 的扩缩容行为 | [已知限制](faq-about-node-instant-scaling.md) |  |
| [扩容行为相关](faq-about-node-instant-scaling.md) | [节点即时弹性可模拟判断的资源类型有哪些？](faq-about-node-instant-scaling.md) [节点即时弹性是否支持根据](faq-about-node-instant-scaling.md) [Pod Request](faq-about-node-instant-scaling.md) [资源在节点池中扩容合适资源的实例规格？](faq-about-node-instant-scaling.md) [节点池配了多个实例规格，节点即时弹性默认如何选择？](faq-about-node-instant-scaling.md) [使用节点即时弹性时，如何实时感知节点池中的实例规格库存变化？](faq-about-node-instant-scaling.md) [如何优化节点池配置，尽量避免库存不足而导致扩容失败？](faq-about-node-instant-scaling.md) [为什么节点即时弹性无法弹出节点？](faq-about-node-instant-scaling.md) [开启节点即时弹性的节点池如何配置自定义资源？](faq-about-node-instant-scaling.md) |  |
| [缩容行为相关](faq-about-node-instant-scaling.md) | [为什么节点即时弹性无法缩容节点？](faq-about-node-instant-scaling.md) [什么类型的](faq-about-node-instant-scaling.md) [Pod](faq-about-node-instant-scaling.md) [可以阻止节点即时弹性移除节点？](faq-about-node-instant-scaling.md) |  |
| 自定义的扩缩容行为 | [通过](faq-about-node-instant-scaling.md) [Pod](faq-about-node-instant-scaling.md) [控制扩缩容行为](faq-about-node-instant-scaling.md) | [如何通过](faq-about-node-instant-scaling.md) [Pod](faq-about-node-instant-scaling.md) [控制节点即时弹性的节点缩容？](faq-about-node-instant-scaling.md) |
| [通过节点控制扩缩容行为](faq-about-node-instant-scaling.md) | [节点即时弹性在缩容过程中如何指定需要删除的节点？](faq-about-node-instant-scaling.md) [如何指定节点不被节点即时弹性缩容？](faq-about-node-instant-scaling.md) [节点即时弹性能否仅缩容空节点？](faq-about-node-instant-scaling.md) |  |
| [节点即时弹性组件相关](faq-about-node-instant-scaling.md) | [是否有操作会触发节点即时弹性组件的自动更新？](faq-about-node-instant-scaling.md) [ACK](faq-about-node-instant-scaling.md) [托管集群已经完成了角色授权，但节点伸缩活动仍然无法正常运行？](faq-about-node-instant-scaling.md) |  |
展开查看工作负载伸缩（包括HPA、CronHPA等）的FAQ索引
[HPA](faq-about-workload-auto-scaling.md)[的监控数据](faq-about-workload-auto-scaling.md)[current](faq-about-workload-auto-scaling.md)[字段为何显示为](faq-about-workload-auto-scaling.md)[unknown？](faq-about-workload-auto-scaling.md)
[HPA](faq-about-workload-auto-scaling.md)[扩缩容失败，指标获取异常怎么办？](faq-about-workload-auto-scaling.md)
[为何](faq-about-workload-auto-scaling.md)[HPA](faq-about-workload-auto-scaling.md)[在滚动时扩容出了多余的](faq-about-workload-auto-scaling.md)[Pod？](faq-about-workload-auto-scaling.md)
[HPA](faq-about-workload-auto-scaling.md)[到达阈值为何不进行扩缩容？](faq-about-workload-auto-scaling.md)
[HPA](faq-about-workload-auto-scaling.md)[采集周期如何配置？](faq-about-workload-auto-scaling.md)
[CronHPA](faq-about-workload-auto-scaling.md)[是否兼容](faq-about-workload-auto-scaling.md)[HPA？如何兼容](faq-about-workload-auto-scaling.md)[HPA？](faq-about-workload-auto-scaling.md)
[如何解决](faq-about-workload-auto-scaling.md)[HPA](faq-about-workload-auto-scaling.md)[启动时](faq-about-workload-auto-scaling.md)[CPU](faq-about-workload-auto-scaling.md)[或内存飙高造成扩容出多余](faq-about-workload-auto-scaling.md)[Pod](faq-about-workload-auto-scaling.md)[的多弹现象？](faq-about-workload-auto-scaling.md)
[为什么](faq-about-workload-auto-scaling.md)[HPA](faq-about-workload-auto-scaling.md)[审计日志数值未达阈值但扩缩了？](faq-about-workload-auto-scaling.md)
[HPA](faq-about-workload-auto-scaling.md)[缩容时，能够决定](faq-about-workload-auto-scaling.md)[Pod](faq-about-workload-auto-scaling.md)[缩容的顺序吗？](faq-about-workload-auto-scaling.md)
[HPA](faq-about-workload-auto-scaling.md)[使用率指标单位的含义是什么？](faq-about-workload-auto-scaling.md)
[如果执行](faq-about-workload-auto-scaling.md)[kubectl get hpa](faq-about-workload-auto-scaling.md)[后发现](faq-about-workload-auto-scaling.md)[target](faq-about-workload-auto-scaling.md)[一栏为](faq-about-workload-auto-scaling.md)[unknown](faq-about-workload-auto-scaling.md)[怎么办？](faq-about-workload-auto-scaling.md)
[如何查找](faq-about-workload-auto-scaling.md)[HPA](faq-about-workload-auto-scaling.md)[支持的指标名称？](faq-about-workload-auto-scaling.md)
[自定义了](faq-about-workload-auto-scaling.md)[Nginx Ingress](faq-about-workload-auto-scaling.md)[日志格式后如何进行适配操作？](faq-about-workload-auto-scaling.md)
## 相关文档
在一些预安装或者高性能场景下，您可能期望使用弹性性能优化的操作系统镜像，提高复杂场景下弹性伸缩的便捷性，请参见[弹性优化之自定义镜像](create-custom-images.md)。
如需收集弹性伸缩的日志，请参见[收集系统插件日志](collect-log-files-of-system-components.md)。
推荐您在配置工作负载时结合[工作负载推荐配置](recommended-configurations-for-high-reliability.md)中的使用建议。
在Serverless容器场景下，Knative支持基于请求数或并发数扩缩容，当请求为零时可将Pod副本数量自动缩容至零，更多信息，请参见[Knative](knative-overview.md)、[基于流量请求数实现服务自动扩缩容](enable-automatic-scaling-for-pods-based-on-the-number-of-requests.md)。
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
