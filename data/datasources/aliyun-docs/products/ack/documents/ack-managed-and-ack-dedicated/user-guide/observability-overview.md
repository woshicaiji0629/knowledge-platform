# 容器集群应用业务可观测性-可观测性-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/observability-overview

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-managed-and-ack-dedicated/product-overview.md)

- [快速入门](products/ack/documents/ack-managed-and-ack-dedicated/getting-started.md)

- [操作指南](products/ack/documents/ack-managed-and-ack-dedicated/user-guide.md)

- [实践教程](products/ack/documents/ack-managed-and-ack-dedicated/use-cases.md)

- [安全合规](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference.md)

- [服务支持](products/ack/documents/ack-managed-and-ack-dedicated/support.md)

[首页](https://help.aliyun.com/zh)

# 可观测性体系概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

可观测性是一种通过分析系统外部输出结果推断及衡量系统内部状态的能力。Kubernetes可观测性体系包含监控和日志两部分，监控可以帮助开发者查看系统的运行状态，而日志可以协助问题的排查和诊断。本文介绍阿里云容器服务ACK可观测性生态分层和各层的可观测能力，以帮助您对容器服务可观测性生态有一个全面的认识。

## 容器服务可观测生态概述

从可观测性的角度，以ACK为基础的系统架构可以粗略分为4个层次。自下而上分别是：基础设施层、容器性能层、应用性能层、用户业务层。

以下分别是基础设施层、容器性能层、应用性能层、用户业务层的可观测性介绍。

### 基础设施层可观测性

指容器服务ACK所依赖的底层资源的可观测场景：定位Pod与节点组成的资源池的调用链路，可视化拓扑关系，例如宿主机节点、网络基础组件的性能监控等。

- 

- 

| 解决方案 | 方案介绍 | 适用场景 | 参考文档 |
| --- | --- | --- | --- |
| 架构可视化感知方案 | Kubernetes 集群中的业务是运行在节点组成的资源池上，使得定位 Pod 的调用链路以及拓扑关系非常复杂。如何以可视化的方式监控 Kubernetes 中的负载状态，以及更好地可视化集群中流量的吞吐是非常重要的问题。 阿里云 Kubernetes 监控基于 eBPF 技术，结合阿里云 Prometheus 容器监控，最终整合了指标监控、应用链路追踪、日志分析和事件监控等多种功能，提供 Kubernetes 集群一站式可观测性产品。使 ACK 集群具备网络监控、架构可视化感知等能力。为 IT 开发和运维人员提供无代码侵入、整体的可观测性方案。 | 适用于全部场景。 支持 Kubernetes 集群中 Node、Pod 之间的网络流量监控。 支持 Pod 之间 4 层以上网络流量的监控，以及多协议（如 TCP、HTTP）和 DNS 解析等网络链路监控。 | 更多信息，请参见 [集群拓扑监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/architecture-aware-monitoring.md) 。 |
| 内核层容器监控能力 | 容器服务 Kubernetes 版 ACK（Container Service for Kubernetes） 提供独特的操作系统内核层的容器监控可观测能力 SysOM（System Observer Monitoring）。该能力可以帮助您更好地进行容器化部署和迁移，同时也可以提供更好的容器监控和可观测能力。 | 适用于全部场景。 | 更多信息，请参见 [SysOM](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/sysom-kernel-level-container-monitoring.md) [内核层容器监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/sysom-kernel-level-container-monitoring.md) 。 |
| 基础设施指标监控方案 | 资源监控是 Kubernetes 中最常见的底层资源监控方式，通过资源监控可以快速查看负载的 CPU、内存、网络等指标的使用率。 | 适用于全部场景。 | 更多信息，请参见 [【停止维护】基础资源监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-basic-resources.md) 。 |


### 容器性能层可观测性

指基于容器服务ACK构建系统的容器抽象层的可观测场景，包括集群的性能、事件等监控，容器的性能，以及容器组件等监控。

集群、容器的性能指标监控

| 解决方案 | 方案介绍 | 适用场景 | 参考文档 |
| --- | --- | --- | --- |
| 云监控容器服务 ACK 的监控方案 | 容器服务 Kubernetes 版 ACK（Container Service for Kubernetes） 提供集群、容器的部分性能指标监控，并集成在容器服务控制台中展示。 | 适用于部分场景。 定制化提供基础的容器层性能指标和可观测能力。 | 更多信息，请参见 [【停止维护】基础资源监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-basic-resources.md) 。 |
| 阿里云托管版 Prometheus 的监控方案 | Prometheus 也是社区官方的容器场景云原生指标可观测方案。阿里云 Prometheus 监控全面对接开源 Prometheus 生态，支持类型丰富的组件监控，提供多种开箱即用的预置监控大盘，且提供全面托管的 Prometheus 服务。借助阿里云 Prometheus 监控，您无需自行搭建 Prometheus 监控系统，因此无需关心底层数据存储、数据展示、系统运维等问题。推荐使用阿里云托管版 Prometheus（ARMS Prometheus）云产品。 | 适用于所有场景，包括微服务（ServiceMesh）场景、集群自身组件指标，以及定制监控能力等高级可观测能力。 | 更多信息，请参见 [使用阿里云](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) [Prometheus](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) [监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) 。 |
| 开源 Prometheus 监控方案 | 阿里云容器服务在应用市场中提供了开源 Prometheus 监控方案的集成。 | 适用于所有场景，包括微服务（ServiceMesh）场景、集群自身组件指标以及定制监控能力等高级可观测能力。 | 更多信息，请参见 [开源](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-open-source-prometheus-to-monitor-an-ack-cluster.md) [Prometheus](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-open-source-prometheus-to-monitor-an-ack-cluster.md) [监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-open-source-prometheus-to-monitor-an-ack-cluster.md) 。 |


集群、容器事件监控

| 解决方案 | 方案介绍 | 适用场景 | 参考文档 |
| --- | --- | --- | --- |
| 事件的监控方案 | 事件监控是 Kubernetes 从事件角度出发的另一种监控方式，可以弥补资源监控在实时性、准确性和场景上的缺陷。开发者可以通过获取事件，实时诊断集群的异常与问题。推荐使用阿里云日志服务 SLS（Log Service）产品提供的事件中心监控能力。 | 适用于全部场景。 | 更多信息，请参见 [事件监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/event-monitoring.md) 。 |


### 应用性能层可观测性

指基于容器服务ACK构建系统的具体应用场景，包括应用指标性能（Metric）、系统调用链（Tracing）、日志监控（Logging）等，例如基于容器服务构建一个Java应用，Java应用的线程数指标等。

| 解决方案 | 方案介绍 | 适用场景 | 参考文档 |
| --- | --- | --- | --- |
| 无侵入 Java 应用监控 APM 监控方案 | 推荐使用阿里云应用性能监控 ARMS（Application Real-Time Monitor Service）作为应用性能层监控方案，ARMS 是一款阿里云应用性能管理（APM）类监控产品。只要为部署在容器服务 Kubernetes 版中的 Java 应用安装 ARMS 应用监控组件，您无需修改任何代码，就能借助 ARMS 对 Java 应用进行全方位监控，以便您更快速地定位出错接口和慢接口、重新调用参数、检测内存泄漏、发现系统瓶颈，从而大幅提升线上问题诊断的效率。 | 适用于部分场景，包括 Java 应用的应用监控，方案接入支持无侵入方式，无需进行代码改造。 | 更多信息，请参见 [Java](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-application-performance.md) [应用监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-application-performance.md) 。 |
| 侵入式应用监控 APM 监控方案 | 链路追踪 Tracing Analysis 为分布式应用的开发者提供了完整的调用链路还原、调用请求量统计、链路拓扑、应用依赖分析等工具，可以帮助开发者快速分析和诊断分布式应用架构下的性能瓶颈，提高微服务时代的开发诊断效率。链路追踪支持多种开源社区的 SDK，且支持 OpenTracing、OpenTelemetry 生态标准。 | 适用于所有场景，包括微服务（ServiceMesh）以及多种开发语言的应用。支持 OpenTelemetry 生态标准。方案接入需要侵入式代码引入改造。 | 更多信息，请参见 [在](https://help.aliyun.com/zh/asm/sidecar/enable-distributed-tracing-in-asm#task-2379623) [ASM](https://help.aliyun.com/zh/asm/sidecar/enable-distributed-tracing-in-asm#task-2379623) [中实现分布式跟踪](https://help.aliyun.com/zh/asm/sidecar/enable-distributed-tracing-in-asm#task-2379623) 。 |
| 可观测链路 OpenTelemetry 版 为分布式应用的开发者提供了完整的调用链路还原、调用请求量统计、链路拓扑、应用依赖分析等工具，可以帮助开发者快速分析和诊断分布式应用架构下的性能瓶颈，提高微服务时代下的开发诊断效率。 | 基于 OpenTracing 标准，兼容开源社区，例如 Jaeger、Zipkin。支持多语言开发程序接入，包括 Java、PHP、Go、Python、Node.js、.NET、C++、Ruby、Swift 等。 | 更多信息，请参见 [什么是可观测链路 OpenTelemetry 版](products/arms/documents/tracing-analysis/product-overview/what-is-tracing-analysis.md) 及 [接入指南](products/arms/documents/tracing-analysis/tutorials.md) 。 |  |


### 用户业务层可观测性

基于容器服务ACK构建的业务系统的具体业务场景，例如基于容器服务构建一套高可用、可扩展的网站，网站的业务运营数据PV、UV等，以及应用的成本审计场景等。

| 解决方案 | 方案介绍 | 适用场景 | 参考文档 |
| --- | --- | --- | --- |
| 自定义日志监控方案 | 推荐使用阿里云日志服务 SLS（Log Service）作为自定义指标的观测方案。您可以通过自定义应用系统的内容、格式，并通过日志服务收集日志，在日志服务中配置业务大盘，观测自己的业务情况，或做系统审计。 | 适用于全部场景，如流量监控、成本审计统计、业务订单走势统计等。 | 更多信息，请参见 [采集](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [集群容器日志](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) 。 |
| 通过可观测可视化 Grafana 版自定义业务大盘 | 阿里云可观测可视化 Grafana 版是云原生的运维数据可视化平台，面向用户提供免运维和快速启动 Grafana 运行环境的能力，默认集成如数据库、消息队列、Prometheus 监控、日志服务等各类阿里云服务数据源，并提供丰富的数据看板，让运维监控更加精细。 可观测可视化 Grafana 版可以帮助您在高效分析与查看指标、日志和跟踪的同时，无需关注服务器配置、软件更新等繁杂工作，有效降低运维复杂性与工作量，并借助阿里云强大的云原生能力，全面提升 Grafana 的安全性与可用性。 | 适用于全部场景。 用户可根据自身业务场景，直接使用 Grafana 配置业务大盘，如 PV、UV 等实时业务监控大盘。 | 更多信息，请参见 [什么是可观测可视化 Grafana 版](products/arms/documents/observable-visualization-grafana-edition/product-overview/what-is-grafana.md) 。 |
| 通过 ARMS 前端监控从网页前端感知业务流量、业务服务的健康状况。 | ARMS 前端监控专注于对 Web 场景、Weex 场景和小程序场景的监控，从页面打开速度（测速）、页面稳定性（JS 诊断错误）和外部服务调用成功率（API）这三个方面监测 Web 和小程序页面的健康状况。 | 适用 JavaScript 的前端应用场景。 | 更多信息，请参见 [什么是](products/arms/documents/browser-monitoring/product-overview/what-is-arms-browser-monitoring.md) [ARMS](products/arms/documents/browser-monitoring/product-overview/what-is-arms-browser-monitoring.md) [前端监控？](products/arms/documents/browser-monitoring/product-overview/what-is-arms-browser-monitoring.md) 。 |


## 相关文档

- 

关于日志监控的更多信息，请参见[日志管理](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/log-management-2.md)、[采集](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)[集群容器日志](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)、[采集](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-log4jappender-for-kubernetes-and-log-service.md)[Log4j](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-log4jappender-for-kubernetes-and-log-service.md)[日志至](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-log4jappender-for-kubernetes-and-log-service.md)[SLS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-log4jappender-for-kubernetes-and-log-service.md)。

- 

关于监控指标的更多信息，请参见[Java](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-application-performance.md)[应用监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-application-performance.md)、[集群拓扑监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/architecture-aware-monitoring.md)、[事件监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/event-monitoring.md)。

- 

关于如何使用监控和配置监控大盘，请参见[使用阿里云](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md)[Prometheus](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md)[监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md)、[Ingress Dashboard](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ingress-dashboard.md)[监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ingress-dashboard.md)、[CoreDNS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/coredns-monitoring.md)[组件监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/coredns-monitoring.md)、[通过](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-promql-to-query-prometheus-monitoring-data.md)[PromQL](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-promql-to-query-prometheus-monitoring-data.md)[查询](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-promql-to-query-prometheus-monitoring-data.md)[Prometheus](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-promql-to-query-prometheus-monitoring-data.md)[监控数据](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-promql-to-query-prometheus-monitoring-data.md)、[SysOM](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/sysom-kernel-level-container-monitoring.md)[内核层容器监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/sysom-kernel-level-container-monitoring.md)。

[上一篇：Knative FAQ](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/knative-faq.md)[下一篇：可观测计费说明](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/observable-billing-description.md)

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
