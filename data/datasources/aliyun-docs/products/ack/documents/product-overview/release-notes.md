# 容器服务ACK 2026年功能发布记录-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/product-overview/release-notes

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/product-overview.md)

- [操作指南](products/ack/documents/ack-user-guide.md)

- [服务支持](products/ack/documents/support.md)

[首页](https://help.aliyun.com/zh)

# 容器服务ACK 2026年功能发布记录

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍容器服务 Kubernetes 版 ACK（Container Service for Kubernetes）的最新功能发布记录。

## 背景信息

- 

关于容器服务 Kubernetes 版 ACK（Container Service for Kubernetes）支持的Kubernetes（K8s）版本，请参见[版本说明](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/support-for-kubernetes-versions.md)。

- 

容器服务 Kubernetes 版 ACK（Container Service for Kubernetes）支持的操作系统包括ContainerOS、Alibaba Cloud Linux 4 容器优化版，Alibaba Cloud Linux 3 容器优化版、Alibaba Cloud Linux 3、Alibaba Cloud Linux 3 Arm版、Alibaba Cloud Linux UEFI 3、Red Hat、Ubuntu、Windows等，请参见[操作系统](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/overview-of-os-images.md)。

## 2026年03月

| 产品 | 功能名称 | 功能描述 | 相关文档 |
| --- | --- | --- | --- |
| 容器服务 Kubernetes 版 | 支持 Alibaba Cloud Linux 4 容器优化版镜像 | Alibaba Cloud Linux 4 容器优化版是基于 Alibaba Cloud Linux 4 标准镜像，面向容器场景进行了深度优化。它搭载 ANCK 6.6 内核，默认启用 cgroup v2 以支持更精细的资源管理。该镜像是阿里云结合其在 ACK 的丰富客户实践经验自研而成，推荐用于各类容器化业务部署。 | [Alibaba Cloud Linux 4 容器优化版](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/alibaba-cloud-linux-4-container-optimized-edition.md) |
| 支持使用 AgentScope 将智能体应用部署为 Knative 服务 | 将 AgentScope 框架开发的智能体应用一键式部署到 ACK Knative 环境中后，可利用 Knative 的自动扩缩容（缩容至 0）、版本管理等 Serverless 能力，实现 AI 智能体的快速、弹性与低成本托管。 | [使用 AgentScope 将智能体应用部署为 Knative 服务](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-agentscope-to-deploy-smart-body-applications-as-knative-services.md) |  |
| 在 Auto Mode 集群中部署 Qwen 大语言模型推理服务 | ACK Auto Mode 集群支持 Auto Mode 节点池，结合 Knative Serving 的按需弹性能力，可将 Qwen3.5-4B 大模型部署为按需使用的 Serverless 推理服务。部署后，无需手动运维管理 GPU 资源，适用于对 GPU 成本敏感和运维复杂度有要求的模型推理场景。 | [基于 Knative 部署 Qwen3.5-4B](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/deploy-qwen3-5-4b-llm-inference-services-in-ack-auto-mode-clusters-with-knative.md) |  |
| 容器 Argo 工作流集群 | 使用 PythonSDK 构建大规模 Argo Workflows | Argo Workflows 是一个强大的工作流管理工具，广泛应用于定时任务、机器学习和 ETL 数据处理等场景，但是使用 YAML 定义工作流程可能会增加学习难度。Hera Python SDK 提供了一种简洁易用的替代方案，Hera 允许用户以 Python 代码构建工作流，支持复杂任务，易于测试，并与 Python 生态无缝集成，显著降低了工作流设计的门槛。本文将介绍如何使用 Python SDK 构建大规模 Argo Workflows。 | [使用](products/ack/documents/ack-argo-workflow-cluster/use-cases/use-pythonsdk-to-build-large-scale-argo-workflows.md) [Python SDK](products/ack/documents/ack-argo-workflow-cluster/use-cases/use-pythonsdk-to-build-large-scale-argo-workflows.md) [构建大规模](products/ack/documents/ack-argo-workflow-cluster/use-cases/use-pythonsdk-to-build-large-scale-argo-workflows.md) [Argo Workflows](products/ack/documents/ack-argo-workflow-cluster/use-cases/use-pythonsdk-to-build-large-scale-argo-workflows.md) |
| 基于 EventBridge 的事件驱动 CI Pipeline | 基于事件总线 EventBridge 和分布式工作流 Argo Workflows，可以构建高效、快速、低成本的事件驱动自动化 CI Pipeline，大幅简化和加速应用交付过程。本文介绍如何构建基于事件驱动的自动化 CI Pipeline 流程。 | [基于](products/ack/documents/ack-argo-workflow-cluster/use-cases/event-driven-ci-pipeline-via-eventbridge.md) [EventBridge](products/ack/documents/ack-argo-workflow-cluster/use-cases/event-driven-ci-pipeline-via-eventbridge.md) [的事件驱动](products/ack/documents/ack-argo-workflow-cluster/use-cases/event-driven-ci-pipeline-via-eventbridge.md) [CI Pipeline](products/ack/documents/ack-argo-workflow-cluster/use-cases/event-driven-ci-pipeline-via-eventbridge.md) |  |
| 基于工作流集群构建 Golang 项目的 CI Pipeline | 工作流集群基于开源 Argo Workflows 项目构建，全托管 Argo Workflows，具有极致弹性、自动扩展、无运维成本等优势，可以快速实现更简单、低成本、高效率的 CI 流水线。本文介绍如何基于工作流集群构建 Golang 项目的 CI Pipeline。 | [基于工作流集群构建](products/ack/documents/ack-argo-workflow-cluster/use-cases/use-workflow-clusters-to-build-a-ci-pipeline-for-go-projects.md) [Golang](products/ack/documents/ack-argo-workflow-cluster/use-cases/use-workflow-clusters-to-build-a-ci-pipeline-for-go-projects.md) [项目的](products/ack/documents/ack-argo-workflow-cluster/use-cases/use-workflow-clusters-to-build-a-ci-pipeline-for-go-projects.md) [CI Pipeline](products/ack/documents/ack-argo-workflow-cluster/use-cases/use-workflow-clusters-to-build-a-ci-pipeline-for-go-projects.md) |  |
| 容器服务 Edge 版 | 支持使用 Gateway with Inference Extension 访问服务 | Gateway API 是 Kubernetes 官方推出的下一代路由和负载均衡 API。本文介绍如何在 ACK Edge 集群中通过 Gateway with Inference Extension 组件配置 HTTP 路由、请求 Header 修改和按比例分发请求。 | [使用](products/ack/documents/ack-edge/user-guide/using-gateway-with-inference-extension-to-access-services.md) [Gateway with Inference Extension](products/ack/documents/ack-edge/user-guide/using-gateway-with-inference-extension-to-access-services.md) [访问服务](products/ack/documents/ack-edge/user-guide/using-gateway-with-inference-extension-to-access-services.md) |


## 2026年02月

| 产品 | 功能名称 | 功能描述 | 相关文档 |
| --- | --- | --- | --- |
| 容器服务 Kubernetes 版 | ACK AI 助手发布 Agent 模式 | AI 助手发布 Agent 模式，支持故障疑难根因分析、最佳实践推荐，简化集群运维。 | [授权使用容器服务计算](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/add-authorization.md) [AI](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/add-authorization.md) [助手](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/add-authorization.md) [Agent](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/add-authorization.md) [功能](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/add-authorization.md) |
| 发布 ContainerOS v3.7 | ContainerOS v3.7 新增预装 GPU 驱动的 ContainerOS 镜像。 | [ContainerOS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/containeros-release-record.md) [镜像发布记录](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/containeros-release-record.md) |  |
| 发布 Kubernetes 1.35 | ACK 发布 Kubernetes 1.35 版本。自 1.35 版本起，不再支持 cgroup v1，对 cgroup v2 的支持已在 1.25 版本进入稳定阶段。节点操作系统必须升级以支持 cgroup v2，否则 kubelet 将无法启动。详细变更说明参见文档。 | [Kubernetes 1.35](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/kubernetes-1-35-release-notes.md) |  |
| 在 Knative 中基于 AI 推理网关实现 LLM 服务部署与智能路由 | ACK Gateway with Inference Extension 组件基于 Kubernetes Gateway API 及 Inference Extension 规范实现。结合 Knative Serverless 架构，该方案能够简化生成式 AI 推理服务的管理流程，支持在多个推理服务工作负载之间进行高效的七层路由和负载均衡，并根据请求并发数实现 GPU 资源的弹性伸缩。 | [基于 AI 推理网关实现 LLM 服务部署与智能路由](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/llm-service-deployment-and-intelligent-routing-based-on-ai-inference-gateway.md) |  |
| 为 ACK Kube Queue 增加自定义准入检查 | 默认情况下，ACK Kube Queue 仅检查 ElasticQuotaTree 中定义的配额的 Max，配额检查通过后通过调度器进行调度。如果您需要自定义更复杂的出队检查逻辑，可基于 AdmissionCheck 机制来实现。 | [为](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/add-custom-admission-checks-to-ack-kube-queue.md) [ACK Kube Queue](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/add-custom-admission-checks-to-ack-kube-queue.md) [增加自定义准入检查](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/add-custom-admission-checks-to-ack-kube-queue.md) |  |
| 容器 Argo 工作流集群 | 发布 容器 Argo 工作流集群 | 容器 Argo 工作流集群 采用全托管免运维模式，通过优化开源工作流引擎，实现大规模工作流的高效稳定运行。 | [容器](products/ack/documents/ack-argo-workflow-cluster/product-overview/container-argo-workflow-cluster-overview.md) [Argo](products/ack/documents/ack-argo-workflow-cluster/product-overview/container-argo-workflow-cluster-overview.md) [工作流集群概述](products/ack/documents/ack-argo-workflow-cluster/product-overview/container-argo-workflow-cluster-overview.md) |


## 2026年01月

| 产品 | 功能名称 | 功能描述 | 相关文档 |
| --- | --- | --- | --- |
| 容器服务 Kubernetes 版 | 支持使用 CPFS 智算版动态存储卷 | 通过动态卷机制，可为 CPFS 智算版实现自动化按需存储，免去手动管理 PV 的繁琐。该方法支持多应用并行读写，尤其适用于 AI 训练、大数据分析等场景，可高效共享代码、配置文件、计算中间结果等数据。 | [使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-cpfs-for-lingjun-dynamic-volumes.md) [CPFS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-cpfs-for-lingjun-dynamic-volumes.md) [智算版动态存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-cpfs-for-lingjun-dynamic-volumes.md) |
| 支持将 OSS 数据按需预填充到高性能存储卷 | 在 AI 训练、数据分析等任务开始前，将存储于 OSS 的海量冷数据按需预热到高性能存储卷（如 CPFS 智算版、云盘），计算任务可直接从高性能卷中高速读取数据，任务结束后存储卷自动回收，实现计算加速与成本优化的平衡。 | [将 OSS 数据按需预填充到高性能存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/prefetch-oss-data-into-high-performance-volumes-on-demand.md) |  |
| 支持将应用调度到混合云节点池 | 混合云节点池支持将本地数据中心（IDC）的节点注册到 ACK 集群，实现云上云下资源的统一纳管与协同调度。 | [将应用调度到混合云节点池](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/scheduling-applications-to-a-hybrid-cloud-node-pool.md) |  |
| 新增 yurt-hub 组件 | yurt-hub 是为 ACK 集群混合云节点池提供自治能力的节点组件。 | [yurt-hub](products/ack/documents/product-overview/yurt-hub.md) |  |


## 更多信息

有关ACK的历史功能发布记录，请参见[历史功能发布记录（2025](products/ack/documents/product-overview/historical-release-notes.md)[年及之前）](products/ack/documents/product-overview/historical-release-notes.md)。

[上一篇：产品发布记录](products/ack/documents/product-overview/release-notes-1.md)[下一篇：历史功能发布记录（2025年及之前）](products/ack/documents/product-overview/historical-release-notes.md)

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
