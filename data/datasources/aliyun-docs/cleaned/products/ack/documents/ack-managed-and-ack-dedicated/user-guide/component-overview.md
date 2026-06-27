# 管理ACK托管集群的相关组件-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/component-overview

# 管理ACK托管集群的相关组件
容器服务 Kubernetes 版提供应用管理、日志监控、网络等多种组件，便于您管理和运维集群。某些组件由ACK自动升级，部分组件需要您手动升级，或按需进行更小粒度的配置。本文介绍如何升级、安装、卸载组件，以及组件概览参考。
## 前提条件
[创建](create-an-ack-managed-cluster-2.md)[ACK](create-an-ack-managed-cluster-2.md)[托管集群](create-an-ack-managed-cluster-2.md)
## 操作步骤
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。
在组件管理页面，您可以搜索并定位目标组件，在组件卡片上按需进行安装、卸载、升级、修改组件参数等操作。
说明
为了保证控制面的稳定性，当前仅ACK托管集群Pro版、ACK Serverless集群Pro版、ACK Edge集群Pro版、ACK灵骏集群支持自定义部分控制面核心组件参数。
## 参考信息
### 组件类型
容器服务ACK管理的集群组件类型包括系统组件和可选组件：
系统组件：创建ACK集群时，默认安装的组件。
可选组件：创建ACK集群时，可选择安装的组件，用于扩展集群功能。
### 核心组件
| 组件名称 | 组件类型 | 描述 |
| --- | --- | --- |
| [Kube Scheduler](../../product-overview/kube-scheduler.md) | 系统组件 | 控制面组件，负责结合节点资源使用情况和 Pod 的调度要求将 Pod 调度到集群的合适节点上。 |
| [Cloud Controller Manager](../../product-overview/cloud-controller-manager.md) | 系统组件 | 在 Kubernetes 集群中提供管理负载均衡实现跨节点通信的功能。提供 Kubernetes 与阿里云网络产品的对接能力，例如 CLB、NLB、VPC 等。 |
| [Kube API Server](../../product-overview/kube-api-server.md) | 系统组件 | Kubernetes 集群的总线和入口网关。 |
| [Kube Controller Manager](../../product-overview/kube-controller-manager.md) | 系统组件 | Kubernetes 集群内部资源的管理器。 |
| [ACK Virtual Node](../../product-overview/ack-virtual-node.md) | 可选组件 | 基于社区开源项目 Virtual Kubelet，扩展了对 Aliyun Provider 的支持，并做了大量优化，实现 Kubernetes 与 ACS 和 ECI 的无缝连接。 |
### 应用管理
| 组件名称 | 组件类型 | 描述 |
| --- | --- | --- |
| [【停止维护】appcenter](../../product-overview/appcenter.md) | 可选组件 | 提供统一管理多集群应用部署和应用生命周期的应用中心组件。 后续可以使用 分布式云容器平台 ACK One 提供的 [应用分发](../../distributed-cloud-container-platform-for-kubernetes/user-guide/application-distribution-overview.md) 功能来获取多集群应用部署能力。 |
| [ack-kruise](../../product-overview/openkruise.md) | 可选组件 | 提供高效管理应用容器、Sidecar 容器及镜像分发功能。 |
| [migrate-controller](../../product-overview/migrate-controller.md) | 可选组件 | 基于开源项目 Velero 开发的一个用于备份与迁移 Kubernetes 应用和 PV 数据的组件。 |
### 日志与监控
| 组件名称 | 组件类型 | 描述 |
| --- | --- | --- |
| [alicloud-monitor-controller](../../product-overview/alicloud-monitor-controller.md) | 系统组件 | ACK 提供对接云监控的系统组件。 |
| [metrics-server](../../product-overview/metrics-server.md) | 系统组件 | ACK 基于社区开源监控组件进行改造和增强的监控采集和离线组件，并提供 Metrics API 进行数据消费，提供 HPA 的能力。 |
| [ack-cost-exporter](../../product-overview/ack-cost-exporter.md) | 可选组件 | ACK 成本分析功能进行数据处理的组件。 |
| [ack-node-problem-detector](../../product-overview/ack-node-problem-detector.md) | 可选组件 | ACK 基于社区开源项目进行改造和增强的集群节点异常事件监控组件，以及对接第三方监控平台功能的组件。 |
| [ack-onepilot](../../product-overview/ack-onepilot.md) | 可选组件 | ack-onepilot 是阿里云 ARMS 针对 Kubernetes 应用接入场景提供的探针接入助手，实现容器环境中对 Java、Golang、Python 应用的监控。 |
| [ack-sysom-monitor](../../product-overview/ack-sysom-monitor.md) | 可选组件 | ACK 集群操作系统内核层的容器监控组件。 |
| [ack-arms-cmonitor](../../product-overview/ack-arms-cmonitor.md) | 可选组件 | 使用 ARMS 应用监控 eBPF 版无侵入监控容器部署的应用。 |
| [ack-arms-prometheus](../../../../arms/documents/prometheus-monitoring/prometheus-monitoring-change-records.md) | 可选组件 | 使用 阿里云 Prometheus 实现容器服务集群监控。 |
| [logtail-ds](../../../../sls/documents/sls-release-notes.md) | 可选组件 | 使用日志服务采集 Kubernetes 容器日志。 |
### 存储
| 组件名称 | 组件类型 | 描述 |
| --- | --- | --- |
| [storage-operator](../../product-overview/storage-operator.md) | 系统组件 | 用于管理存储组件的生命周期。 |
| [csi-plugin](../../product-overview/csi-plugin.md) | 可选组件 | 支持存储卷的挂载、卸载功能。 创建集群时，默认安装该组件。 |
| [csi-provisioner](../../product-overview/csi-provisioner.md) | 可选组件 | 支持存储卷的自动创建能力。 创建集群时，如果选择 CSI 插件实现阿里云存储的接入能力，默认安装该组件。 |
| [csi-compatible-controller](../../product-overview/csi-compatible-controller.md) | 可选组件 | 可以使 csi-plugin 和 Flexvolume 存储组件实现共存。 |
### 网络
| 组件名称 | 组件类型 | 描述 |
| --- | --- | --- |
| [CoreDNS](../../product-overview/coredns.md) | 系统组件 | ACK 集群中默认采用的 DNS 服务发现插件，其遵循 Kubernetes DNS-Based Service Discovery 规范。 |
| [Gateway API](../../product-overview/gateway-api.md) | 系统组件 | Kubernetes 中用于对服务网络流量进行建模的一系列资源，目标是建立一套表现力强、易扩展、面向角色的服务网络模型。 |
| [ACK eRDMA Controller](../../product-overview/ack-erdma-controller.md) | 可选组件 | 使用 eRDMA 控制器管理 eRDMA 网卡。 |
| [ACK NodeLocal DNSCache](../../product-overview/ack-nodelocal-dnscache.md) | 可选组件 | 基于社区开源项目 NodeLocal DNSCache 的一套 DNS 本地缓存解决方案。 |
| [ALB Ingress Controller](../../product-overview/alb-ingress-controller.md) | 可选组件 | 基于阿里云应用型负载均衡 ALB（Application Load Balancer） ，提供更为强大的 Ingress 流量管理方式，兼容 Nginx Ingress，具备处理复杂业务路由和证书自动发现的能力，支持 HTTP、HTTPS 和 QUIC 协议，满足在云原生应用场景下对超强弹性和大规模七层流量处理能力的需求。 |
| [MSE Ingress Controller](https://help.aliyun.com/zh/mse/user-guide/manage-the-mse-ingress-controller-component) | 可选组件 | 基于 MSE 云原生网关，适用于微服务场景，兼容 Nginx Ingress。支持多种服务发现、认证鉴权以及多语言插件扩展，提供灰度发布、预热和限流等 Ingress 流量管理能力。 |
| [Terway](../../product-overview/terway.md) | 可选组件 | 阿里云开源的 Terway CNI 插件支持 eBPF 网络加速和 Kubernetes 标准的 NetworkPolicy，用于定义容器间的访问策略。使用 Terway 可以实现 Kubernetes 集群内部的网络互通。创建集群时，选择 Terway 网络插件会默认安装该组件。 |
| [Flannel](../../product-overview/flannel.md) | 可选组件 | 一种容器网络接口 CNI（Container Network Interface）插件，在阿里云上使用的 Flannel 网络模式采用阿里云 VPC 模式。 创建集群时，如果选择 Flannel 网络插件实现集群内部网络互通的话，默认安装该组件。 |
| [Nginx Ingress Controller](../../product-overview/nginx-ingress-controller.md) | 可选组件 | Nginx Ingress Controller 解析 Ingress 的转发规则。Ingress Controller 收到请求，匹配 Ingress 转发规则转发到后端 Service。 |
| [Poseidon](../../product-overview/poseidon.md) | 可选组件 | ACK 自研的容器 NetworkPolicy 插件。支持 Kubernetes 标准的 NetworkPolicy 功能。 针对 ACK Serverless 集群 以及在 ACK 集群中使用 ECI 实例的场景，如需使用 NetworkPolicy 功能，则需安装 Poseidon 组件。 针对 ACK 集群的其他场景，如需使用 NetworkPolicy 功能，则需安装 Terway 组件。 |
| [Sidecar Acceleration using eBPF](../../product-overview/sidecar-acceleration-using-ebpf.md) | 可选组件 | 使用 Sidecar 加速来减少阿里云服务网格中的网络延迟。 |
| [Gateway with Inference Extension](../../product-overview/ack-gateway-with-inference-extension.md) | 可选组件 | 基于 Envoy Gateway 开源项目构建，支持 Kubernetes 四层/七层路由服务，并提供面向 AI 大语言模型（LLM）推理场景的智能负载均衡能力。 |
### 安全
| 组件名称 | 组件类型 | 描述 |
| --- | --- | --- |
| [ack-advanced-audit](../../product-overview/ack-advanced-audit.md) | 可选组件 | ack-advanced-audit 组件基于开源项目 [Falco](https://falco.org/) ，使用内核提供的 eBPF 特性，实现了容器内操作的系统调用审计能力。通过 ack-advanced-audit 组件实现的容器内部操作审计功能，可以方便您审计组织内成员或应用程序进入容器后执行的命令操作。 |
| [ack-pod-identity-webhook](../../product-overview/ack-pod-identity-webhook.md) | 可选组件 | ack-pod-identity-webhook 组件可以帮您更便捷地使用容器服务提供的 RRSA（RAM Roles for Service Accounts）特性，它可以为您的应用 Pod 自动注入应用依赖的挂载 OIDC Token 和环境变量配置，免去繁琐的手动配置工作。 |
| [ack-ram-authenticator](../../product-overview/ack-ram-authenticator.md) | 系统组件 | ack-ram-authenticator 组件是面向 ACK 托管集群 的认证插件，基于 Kubernetes 原生 [Webhook Token](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication) [认证](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication) 方式，实现通过 RAM 完成集群 API Server 的请求认证。同时，该组件通过 CRD 形式提供 RAM 身份和 RBAC 权限的映射关系，帮您更灵活地配置 RBAC 鉴权。 |
| [gatekeeper](../../product-overview/gatekeeper.md) | 可选组件 | 帮助您方便地管理和应用集群内的 Open Policy Agent（OPA）策略，实现命名空间标签管理等功能。 |
| [kritis-validation-hook](../../product-overview/kritis-validation-hook.md) | 可选组件 | 部署可信容器环节中进行容器镜像签名验证的关键组件。 |
| [aliyun-acr-credential-helper](../../product-overview/aliyun-acr-credential-helper.md) | 可选组件 | aliyun-acr-credential-helper 通过读取 ACK 集群内的 kube-system 命名空间中的 acr-configuration 的配置，进行私有镜像拉取。支持以下功能： 免密组件目前仅支持与 ACR 企业版及 2024 年 09 月 08 日及更早创建的 ACR 个人版配合使用。 支持拉取集群当前用户容器镜像服务中的私有镜像，通过跨账号授权或 AccessKey ID 和 AccessKey Secret 配置可以拉取其他用户的私有镜像。 支持跨地域拉取容器镜像服务中的私有镜像。 |
| [policy-template-controller](../../product-overview/policy-template-controller.md) | 可选组件 | 实现策略管理功能的关键组件。 |
| [security-inspector](../../product-overview/security-inspector.md) | 可选组件 | 实现安全巡检功能的关键组件。 |
### 弹性与调度
| 组件名称 | 组件类型 | 描述 |
| --- | --- | --- |
| [ACK GOATScaler](instant-elasticity.md) | 可选组件 | 提供节点即时弹性功能。 |
| [ack-kubernetes-cronhpa-controller](../../product-overview/ack-kubernetes-cronhpa-controller.md) | 可选组件 | 使用 ack-kubernetes-cronhpa-controller 实现应用负载定时伸缩。 |
| [ack-vertical-pod-autoscaler](../../product-overview/ack-vertical-pod-autoscaler.md) | 可选组件 | ack-vertical-pod-autoscaler 组件能够监控 Pod 的资源消耗模式，灵活推荐 CPU 和内存资源分配的配置，并在适当的情况下自动进行调整，而不调整 Pod 的副本数量。这种能力更适用于需要稳定资源配置的有状态应用的扩容等场景。 |
| [AHPA Controller](../../product-overview/application-intelligence-controller.md) | 可选组件 | AHPA 基于应用历史指标预测未来 Pod 实例数量，帮助您解决弹性滞后的问题。AHPA 通过主动预测和被动预测相结合，实时调整资源实例数，并且增加了兜底保护策略，通过设置时间区间的实例数上下界值，实现弹性兜底。 |
| [ack-koordinator（ack-slo-manager）](../../product-overview/ack-koordinator-fka-ack-slo-manager.md) | 可选组件 | ACK 支持差异化 SLO（Service Level Objectives）能力的核心应用，可以在保证应用服务质量的同时，充分提升资源使用效率。 |
### 其他
| 组件名称 | 组件类型 | 描述 |
| --- | --- | --- |
| [ack-helm-manager](../../product-overview/ack-helm-manager.md) | 可选组件 | 提供管理自定义组件的能力。 |
| [ack-cgpu](../../product-overview/ack-cgpu.md) | 可选组件 | 通过 GPU 共享调度框架，实现多个容器共享同一 GPU 设备。 |
| [Argo Workflows](../../product-overview/argo-workflows.md) | 可选组件 | 该组件基于原生 Argo Workflows 开发，并在其基础上有稳定性和性能等方面的增强，支持您在集群中部署大型工作流。主要面向标准化的工作流场景，例如机器学习 Pipeline、自动驾驶仿真、基因测序任务、批量数据处理、CI/CD、基础设施自动化等。 |
| [aliyun-acr-acceleration-suite](../../product-overview/aliyun-acr-acceleration-suite.md) | 可选组件 | 提供镜像按需加载加速能力的客户端插件，以 DaemonSet 形式部署在 Worker 节点上。 |
| [sandboxed-container-controller](../../product-overview/sandboxed-container-controller.md) | 可选组件 | 安全沙箱运行时提供的专用控制器组件，旨在增强和扩展安全沙箱的基本功能。 |
| [sandboxed-container-helper](../../product-overview/sandboxed-container-helper.md) | 可选组件 | 为安全沙箱提供诊断和运维的组件。 |
| [sgx-device-plugin](../../product-overview/sgx-device-plugin.md) | 可选组件 | 由阿里云容器服务团队和蚂蚁金服安全计算团队针对 Intel SGX 联合开发的 Kubernetes Device Plugin，可以让您更容易地在容器中使用 SGX。 |
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
