# Serverless编排标准Knative的功能介绍和ACK Knative的使用流程-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/knative-overview/

# Knative概述
Knative是一款基于Kubernetes的Serverless框架，支持基于请求的自动弹性、在没有流量时将实例数量自动缩容至零、版本管理与灰度发布等能力。在完全兼容社区Knative和Kubernetes API的基础上，ACK Knative进行了多维度的能力增强，例如通过保留实例降低冷启动时间、基于AHPA实现弹性预测等。
## 为什么要在Kubernetes集群中使用Knative
### Knative介绍
[Knative](https://knative.dev/docs/)是一款基于Kubernetes集群的Serverless框架，提供云原生、跨平台的Serverless编排标准。Knative通过整合容器构建、工作负载管理以及事件模型来实现这一Serverless标准。优势如下。
更聚焦于业务逻辑：Knative通过简单的应用配置、自动扩缩容等手段让开发者聚焦于业务逻辑，降低运维负担、减少对底层资源的关注。
标准化：将业务代码部署到Serverless平台时，需要考虑源码的编译、部署和事件的管理。目前社区和云厂商提供的Serverless解决方案和FaaS方案标准不一。Knative提供了一个标准、通用的Serverless框架。
例如，如需在Knative中实现事件驱动，您可以编写对应的YAML文件（CR）并在集群中部署，无需与云产品做深度绑定，便于跨平台迁移。
使用门槛低：Knative支持将代码自动打包为容器镜像并发布为服务，也支持将函数快捷地部署到Kubernetes集群中，以容器的方式运行。
自动弹性及版本管理：Knative支持在没有流量时自动将实例数量缩容至零，从而节省资源，还提供版本管理、灰度发布等功能。
事件驱动：Knative提供了完整的事件模型，便于接入外部系统的事件，并将事件路由到适当的服务或函数进行处理。
关于Knative应用模型（Knative Service）的介绍，请参见[Knative](introduction-to-the-knative-service-model.md)[应用模型介绍](introduction-to-the-knative-service-model.md)。
### 核心组件
Knative包括以下核心组件，分别执行不同的功能。
Knative Serving：管理Serverless工作负载，提供了应用部署、多版本管理、基于请求的自动弹性、灰度发布等能力，而且在没有业务流量时可以将应用实例缩容至零。
Knative Eventing：提供了事件源的接入、事件注册和订阅、以及事件过滤等一整套事件管理的能力。事件模型可以有效地解耦生产者和消费者的依赖关系。
Knative Functions: 提供了一个简单的方式来创建、构建和部署Knative服务。您无需深入了解底层技术栈（例如Kubernetes、容器、Knative），通过使用Knative Functions，即可将无状态、事件驱动的函数作为Knative服务部署到Kubernetes集群中。
## 为什么要使用ACK Knative
在完全兼容社区Knative并提供标准Kubernetes API接口的基础上，ACK Knative进一步增强产品化能力并提供了更丰富的产品方案。
产品化能力：提供了产品化一键部署能力，您无需购买资源搭建系统。同时提供产品控制台，支持白屏化操作，降低Kubernetes集群和Knative的使用门槛。
简化运维：
核心组件托管：在ACK集群中，Knative的核心组件Knative Serving和Knative Eventing均由ACK创建和托管，无需您承担资源费用，且提供高可用保障。
网关托管：ACK Knative提供ALB、ASM和Kourier网关。除社区兼容的Kourier外，其余云产品网关的Controller均由ACK创建，提供全托管、免运维的网关服务。
生态集成：无缝集成了阿里云的计算（[ECI](https://help.aliyun.com/zh/eci/product-overview/what-is-elastic-container-instance)、[ECS](../../../../ecs/documents/user-guide/what-is-ecs.md)、[ACS](https://help.aliyun.com/zh/cs/product-overview/product-introduction)）、可观测（[日志服务](../../../../sls/documents/what-is-log-service.md)[SLS](../../../../sls/documents/what-is-log-service.md)、[Prometheus](https://help.aliyun.com/zh/prometheus/product-overview/what-is-managed-service-for-prometheus)）、CI/CD（[云效](https://help.aliyun.com/zh/yunxiao/product-overview/what-is-cloud-effect)）、应用集成（[EventBridge](https://help.aliyun.com/zh/eventbridge/product-overview/what-is-eventbridge)）等产品，无需自行采购服务器，也无需自建服务，便能在Knative服务中实现日志与监控告警、持续交付、事件驱动等能力。
更丰富的功能特性：在社区Knative的基础上，ACK Knative结合实际业务场景提供了开箱即用的、更为丰富的产品方案。例如以下方案。
[保留实例](reserved-instances.md)：为延迟敏感应用保留一个低成本常驻实例，缓解社区Knative“缩容至0”策略带来的冷启动延迟，以提升服务响应速度，有效控制资源成本。
[Knative](knative-auto-scaling.md)[自动伸缩](knative-auto-scaling.md)： 提供开箱即用的基于请求的自动弹性[KPA](enable-automatic-scaling-for-pods-based-on-the-number-of-requests.md)（Knative Pod Autoscaler），同时也支持[HPA](use-hpa-in-knative.md)，您还可以为Knative服务配置AHPA（Advanced Horizontal Pod Autoscaler）弹性能力。如果您的应用所需资源具备周期性变化，推荐您使用AHPA进行弹性预测，提前预热所需的资源，缓解使用Knative时遇到的冷启动问题。
关于ACK Knative和社区Knative对比的更多信息，请参见[阿里云](comparison-between-alibaba-cloud-knative-and-open-source-knative.md)[Knative](comparison-between-alibaba-cloud-knative-and-open-source-knative.md)[和开源](comparison-between-alibaba-cloud-knative-and-open-source-knative.md)[Knative](comparison-between-alibaba-cloud-knative-and-open-source-knative.md)[对比](comparison-between-alibaba-cloud-knative-and-open-source-knative.md)。
## 使用场景
ACK Knative的典型使用场景如下。
| 业务场景 | 说明 |
| --- | --- |
| Web 服务的托管 | 简化部署： ACK Knative 封装了许多 Kubernetes 的底层细节，通过 Knative 服务大大简化了工作负载的部署和管理。 简化多版本管理：Revision 机制能够确保每个修订版本都有唯一标识，便于管理不同的版本，例如版本的回滚。 简化流量灰度发布： ACK Knative 提供流量管理功能。通过为不同 Revision 版本的服务分配不同的流量比例，可以快速实现灰度发布、A/B 测试等。 |
| Serverless 应用 | 聚焦业务逻辑：开发者无需关心 IaaS 资源，只需关注业务逻辑的开发，应用配置也大大简化，降低底层基础设施的运维成本。 资源按需使用、自动弹性： ACK Knative 可以根据流量请求和并发情况自动扩缩资源，当没有业务流量时还可以将实例数量缩减至零，节省资源和成本。 |
| AI 场景 | 聚焦业务逻辑：GPU 等异构计算场景下，开发者无需关心底层基础设施的维护，只需关注 AI 任务的构建和部署。 资源按需使用、自动弹性： ACK Knative 可以根据实际负载情况自动扩缩资源，针对负载具有波动性的推理服务能够有效降低资源使用成本。 可移植性： ACK Knative 可以运行在任何兼容 Kubernetes 的环境中，Knative 服务可以在云上、本地数据中心甚至是边缘设备上移植部署。 |
| 事件驱动场景 | Knative Eventing 提供了完整的事件模型，简化了接入外部系统的事件的流程。例如，IoT 设备可以将传感器数据发送到 Knative 服务中， ACK Knative 可以配置对应的事件源用于接收数据，并触发相应的处理逻辑，例如数据存储、实时分析、监控告警等。 |
## 使用流程
ACK Knative的使用流程如下图所示。
| 流程 | 说明 |
| --- | --- |
| 适用范围 | 1.22 及以上版本的 ACK 托管集群 。如需升级，请参见 [手动升级集群](update-the-kubernetes-version-of-an-ack-cluster.md) 。 |
| 已部署 ACK Knative ，安装 Knative Serving 组件，请参见 [部署与管理](deploy-knative.md) [Knative](deploy-knative.md) [组件](deploy-knative.md) 。 |  |
| 已完成网关选型并部署网，请参见 [为](comparison-between-kourier-and-alb-ingresses.md) [Knative](comparison-between-kourier-and-alb-ingresses.md) [选择网关](comparison-between-kourier-and-alb-ingresses.md) 。 [ALB](../../../../slb/documents/application-load-balancer/user-guide/functions-and-features-of-alb-ingresses.md) ：基于阿里云 ALB 提供了更为强大的 Ingress 流量管理方式，全托管免运维，且支持自动弹性能力。 [ASM](https://help.aliyun.com/zh/asm/sidecar/overview-of-asm-gateways) ：统一管理微服务应用流量、兼容 Istio 的托管式平台。通过流量控制、网格观测以及服务间通信安全等功能，简化您的服务治理，并为运行在异构计算基础设施上的服务提供统一的管理能力。 [Kourier](https://github.com/knative-extensions/net-kourier) ：基于 Envoy 架构实现的一款 Knative 社区开源的轻量级网关。 |  |
| 服务部署与管理 | 指定使用的资源类型： 默认使用 ECS 资源运行 Knative 服务。 使用 ECI 提供的 Pod 资源应对突发流量，请参见 [使用](use-elastic-container-instances-in-knative.md) [ECI](use-elastic-container-instances-in-knative.md) [资源](use-elastic-container-instances-in-knative.md) 。 使用 ACS 提供的 Pod 资源应对突发流量，请参见 [使用](using-acs-resources.md) [ACS](using-acs-resources.md) [资源](using-acs-resources.md) 。 在 AI 推理服务等场景下使用 GPU 资源，请参见 [使用](configure-gpu-resources-for-a-knative-service.md) [GPU](configure-gpu-resources-for-a-knative-service.md) [资源](configure-gpu-resources-for-a-knative-service.md) 。 集群中同时存在 ECS 和 ECI 资源时，可基于 ResourcePolicy 来声明资源的扩容和缩容顺序，请参见 [在](use-both-ecs-and-eci-resources-in-knative.md) [Knative](use-both-ecs-and-eci-resources-in-knative.md) [中同时使用](use-both-ecs-and-eci-resources-in-knative.md) [ECS](use-both-ecs-and-eci-resources-in-knative.md) [和](use-both-ecs-and-eci-resources-in-knative.md) [ECI](use-both-ecs-and-eci-resources-in-knative.md) [资源](use-both-ecs-and-eci-resources-in-knative.md) 。 与抢占式实例结合使用，降低云计算资源，请参见 [使用抢占式实例](knative-combined-with-preemptible-instance.md) 。 配置保留实例，保留一个低规格的突发性能实例，平衡好使用成本和启动时长，请参见 [配置保留实例](reserved-instances.md) 。 |
| 自动伸缩： 基于流量请求数（QPS）实现服务的自动扩缩容 KPA（Knative Pod Autoscaler），请参见 [基于流量请求数实现服务自动扩缩容](enable-automatic-scaling-for-pods-based-on-the-number-of-requests.md) 。 配置 AHPA（Advanced Horizontal Pod Autoscaler），既可以根据历史指标弹性预测未来负载的情况并提前准备扩缩容，又能够结合 Cron 表达式实现定时扩缩，请参见 [基于](knative-combined-with-ahpa-to-realize-timing-elasticity-based-on.md) [AHPA](knative-combined-with-ahpa-to-realize-timing-elasticity-based-on.md) [实现定时自动扩缩容](knative-combined-with-ahpa-to-realize-timing-elasticity-based-on.md) 。 配置基于 CPU 指标阈值的 HPA，请参见 [在](use-hpa-in-knative.md) [Knative](use-hpa-in-knative.md) [中使用](use-hpa-in-knative.md) [HPA](use-hpa-in-knative.md) 。 |  |
| 版本管理与灰度发布： 基于 Revision 修订版本实现版本的管理，例如版本的回滚，请参见 [创建修订版本](create-a-revision.md) 。 基于 Revision 版本，根据流量百分比灰度发布服务，请参见 [基于流量灰度发布服务](deploy-a-canary-release-for-a-knative-service-1.md) 。 |  |
| Knative 服务的访问： Knative 服务的默认域名格式为 {route}.{namespace}.{default-example.com} ，其中 {default-example.com} 是默认的域名后缀，您可以自定义域名后缀，请参见 [使用自定义域名和](set-a-custom-domain-name-for-knative-serving.md) [Path](set-a-custom-domain-name-for-knative-serving.md) 。 使用自定义域名时，推荐为自定义域名配置一个 HTTPS 证书，提高数据传输的安全性，请参见 [配置](configure-access-over-https.md) [HTTPS](configure-access-over-https.md) [证书访问](configure-access-over-https.md) 。 配置探针（Liveness Probe 和 Readiness Probe），监测和管理服务的健康状况和可用性，请参见 [在](configure-port-probing-in-knative.md) [Knative](configure-port-probing-in-knative.md) [中配置端口探测](configure-port-probing-in-knative.md) 。 |  |
| 进阶功能 | 事件驱动：Knative Eventing 提供完整、系统的 Serverless 事件驱动模式，包括外部事件源的接入、事件流转和订阅、以及对事件的过滤等功能。请参见 [Knative](overview-7.md) [事件驱动](overview-7.md) 。 |
| Knative Functions：简化在 Kubernetes 集群中创建、部署和调用函数的流程，请参见 [部署](creating-knative-based-functions-with-knative-functions.md) [Knative Functions](creating-knative-based-functions-with-knative-functions.md) 。 |  |
| AI 推理服务： 基于机器学习模型服务框架 KServe 将经过训练的模型（例如 TFServing、TorchServe、Triton 等）部署到模型服务运行时，请参见 [基于](quickly-deploy-the-first-inference-service-based-on-kserve.md) [KServe](quickly-deploy-the-first-inference-service-based-on-kserve.md) [快速部署推理服务](quickly-deploy-the-first-inference-service-based-on-kserve.md) 。 基于 Fluid 加速模型推理服务 Pod 的启动，请参见 [基于](accelerating-pod-startup-with-fluid.md) [Fluid](accelerating-pod-startup-with-fluid.md) [加速](accelerating-pod-startup-with-fluid.md) [Pod](accelerating-pod-startup-with-fluid.md) [启动](accelerating-pod-startup-with-fluid.md) 。 ACK 还提供了在 Knative 中部署 AI 模型推理服务的最佳实践，例如 如何在 Knative 中部署一个 vLLM 推理服务、 如何加速模型部署、如何配置 GPU 共享调度等，请参见 [基于](deploy-a-vllm-inference-application-based-on-knative.md) [Knative](deploy-a-vllm-inference-application-based-on-knative.md) [部署](deploy-a-vllm-inference-application-based-on-knative.md) [vLLM](deploy-a-vllm-inference-application-based-on-knative.md) [推理应用](deploy-a-vllm-inference-application-based-on-knative.md) 、 [在](best-configuration-practices-of-ai-model-inference-service-in-knative.md) [Knative](best-configuration-practices-of-ai-model-inference-service-in-knative.md) [中部署](best-configuration-practices-of-ai-model-inference-service-in-knative.md) [AI](best-configuration-practices-of-ai-model-inference-service-in-knative.md) [模型推理服务的最佳实践](best-configuration-practices-of-ai-model-inference-service-in-knative.md) 。 |  |
| 服务网格：在 Knative 服务中集成 [服务网格](https://help.aliyun.com/zh/asm/product-overview/what-is-asm) [ASM](https://help.aliyun.com/zh/asm/product-overview/what-is-asm) ，以实现复杂的流量管理并增强服务安全性。 |  |
| 可观测性与成本管理 | 日志采集：基于 SLS 无侵入式地完成日志数据采集、消费、投递以及查询分析等功能，请参见 [在](collect-application-logs.md) [Knative](collect-application-logs.md) [上实现日志采集](collect-application-logs.md) 。 |
| 监控大盘：把 Knative 接入阿里云 Prometheus 监控，查看 Knative 的响应延迟、请求并发数等数据，请参见 [查看](view-the-knative-dashboard-in-prometheus-service-1.md) [Knative](view-the-knative-dashboard-in-prometheus-service-1.md) [服务监控大盘](view-the-knative-dashboard-in-prometheus-service-1.md) 。 |  |
| 监控告警：使用 SLS 创建日志告警监控规则，请参见 [为](configure-alerting-on-knative.md) [Knative](configure-alerting-on-knative.md) [服务开启监控告警](configure-alerting-on-knative.md) 。 |  |
| 成本洞察：作为企业 IT 成本管理人员，可以为 Knative 服务启用成本洞察功能，了解 Knative 服务的资源使用量及成本分布，请参见 [启用](knative-service-cost-insight.md) [Knative](knative-service-cost-insight.md) [服务成本洞察](knative-service-cost-insight.md) 。 |  |
## 客户案例
| 典型客户 | 客户案例 | 相关实践 |
| --- | --- | --- |
| 数禾科技 | 数禾科技以大数据和技术为驱动，为金融机构提供高效的智能零售金融解决方案。为了解决支撑模型计算的底层应用资源无法灵活且快速地根据请求量调整算力等问题，数禾科技采用 ACK + Knative 的方式来部署模型服务，实现了根据请求的扩缩容能力、允许 Pod 缩容到 0 以及多版本管理的能力。 | [数禾科技 AI 模型服务基于阿里云容器服务实现 Serverless 容器化](https://www.aliyun.com/customer-stories/financial-services-2024-shuhegroup-serverless) |
| Rokid | 灵伴科技（Rokid）是一家专注于人机交互技术的产品平台公司，基于 ACK Knative 方案部署了其在线服务系统，实现了多版本管理以加快应用迭代、基于请求的自动扩缩容以精准调配 GPU 资源等能力，实现了运维、成本和性能之间的平衡。 | [灵伴科技（Rokid）借助 Knative 实现 AI 应用云原生 Serverless 化](https://www.aliyun.com/customer-stories/ai-2024-rokid-ack) |
| 合思 | 合思致力于财务数智化服务的应用与创新。随着公司业务的扩展，合思面临着大量涌现的新服务和急剧上升的集群运维成本。为此，合思采用了基于 Knative 的流量策略实现灰度发布并优化了微服务管理流程，提升业务的响应速度和系统稳定性的同时降低了运维成本。 | [拥抱 Knative，合思加速 Serverless 化演进实践](https://www.aliyun.com/customer-stories/financial-services-2024-ekuaibao) |
| XTransfer | XTransfer 是一站式外贸企业跨境金融和风控服务公司，基于 ACK Knative 方案搭建了 DevOps 平台，实现了算法模型的 Serverless 部署。在 DevOps 平台上，算法工程师可以创建待上线模型版本、定义推理脚本、指定模型服务所需资源（最小副本数、所需的 GPU 资源、所需的内存资源等），并最终完成模型的发布。 | [云原生 Knative 组件助力 XTransfer 加速应用云原生 Serverless 化](https://www.aliyun.com/customer-stories/financial-services-2024-xtransfer) |
| 硅基仿生 | 深圳硅基仿生科技股份有限公司是一家创新医疗器械研发与产业化公司，采用 ACK Knative 方案加速了深度学习模型的性能提升，同时降低了服务部署成本。 | [硅基仿生业务全面 Serverless 容器化的增效降本之旅](https://www.aliyun.com/customer-stories/health-care-2023-sibionics) |
## 计费说明
在ACK集群中使用ACK Knative时，ACK Knative本身不收取管理费用，但在使用过程中产生的集群管理费用、所创建的云服务器、负载均衡实例、NAT网关等，按照相应资源的价格计费。更多信息，请参见ACK集群的[计费概述](../product-overview/ack-pro-cluster-billing.md)、[云产品资源费用](../product-overview/billing-of-cloud-services.md)。
## 常见问题
如您在使用ACK Knative时遇到问题，可以先参见[Knative FAQ](knative-faq.md)自排查。
如果您在使用Knative的过程中有任何疑问或建议，欢迎您搜索钉群号23302777加入钉群。
[阿里云](knative-faq.md)[Knative](knative-faq.md)[和社区开源](knative-faq.md)[Knative](knative-faq.md)[有什么差异](knative-faq.md)
[安装](knative-faq.md)[Knative](knative-faq.md)[时，应该选择哪种网关](knative-faq.md)
[通过](knative-faq.md)[RAM](knative-faq.md)[用户或角色使用](knative-faq.md)[Knative](knative-faq.md)[时，需要有什么权限](knative-faq.md)
[Knative](knative-faq.md)[中的](knative-faq.md)[Pod](knative-faq.md)[需要多长时间会缩容至](knative-faq.md)[0](knative-faq.md)
[在](knative-faq.md)[Knative](knative-faq.md)[中，如何使用](knative-faq.md)[GPU](knative-faq.md)[资源](knative-faq.md)
[在](knative-faq.md)[Knative](knative-faq.md)[中，如何使用共享](knative-faq.md)[GPU](knative-faq.md)
[应用没有流量时](knative-faq.md)[Knative](knative-faq.md)[默认会将实例数缩容至零，如何解决冷启动延时的问题](knative-faq.md)
[ACK Knative](knative-faq.md)[组件的](knative-faq.md)[Activator](knative-faq.md)[组件是否计费](knative-faq.md)
[Knative](knative-faq.md)[服务的监听端口怎么配置](knative-faq.md)
## 相关文档
请及时升级Knative Serving组件，以便享受最新的功能特性和缺陷修复，请参见[Knative](knative-version-release-notes1.md)[版本发布说明](knative-version-release-notes1.md)、[升级](deploy-knative.md)[Knative Serving](deploy-knative.md)[组件](deploy-knative.md)。
Knative官方文档提供了一个在线书店应用程序教程，带您体验使用Knative构建、部署和监控应用程序的各个步骤，请参见[Knative Bookstore Tutorial](https://knative.dev/docs/bookstore/page-0/welcome-knative-bookstore-tutorial/)。
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
