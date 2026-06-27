# ACK集群概述-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/ack-cluster-overview/

# ACK集群概述
容器服务 Kubernetes 版提供多种类型的集群。这些集群拥有不同的功能特性、运维需求以及赔付标准，适用于不同的场景。您可参照本文中的对比，选择适合您业务的集群类型。
## 集群类型
以集群控制面是否托管作为标准，支持两种集群：
ACK托管集群：托管集群的控制面完全托管在阿里云上。提供Pro版和基础版，区别在于控制面的可用性保障以及高级自定义功能。Pro版支持[预设控制面](ack-pro-provisioned-control-plane.md)（ Pro XL / Pro 2XL / Pro 4XL），可预先分配并固化控制面资源，保障控制面性能始终可预期。
ACK专有集群：专有集群的控制面需要您自行创建并运维。
重要
ACK专有集群目前已经停止新建集群。更多信息请参见[【产品公告】关于停止新建](../../product-overview/product-announcement-announcement-on-stopping-new-ack-dedicated-cluster.md)[ACK](../../product-overview/product-announcement-announcement-on-stopping-new-ack-dedicated-cluster.md)[专有集群的公告](../../product-overview/product-announcement-announcement-on-stopping-new-ack-dedicated-cluster.md)。
您可参照下表，了解不同集群类型的区别。
| 比较项 | ACK 托管集群 | ACK 专有集群 |  |
| --- | --- | --- | --- |
| Pro 版 | 基础版 |  |  |
| 集群规模 | 单账号最多 100 个集群。 单集群默认支持最大 5000 个 Worker 节点，可通过 [配额平台](https://quotas.console.aliyun.com/products/csk/quotas) 申请提高配额。 | 单账号最多 2 个集群。 单集群默认支持最大 10 个 Worker 节点，不支持提高配额。 | 单账号最多 100 个集群。 单集群默认支持最大 5000 个 Worker 节点，可通过 [配额平台](https://quotas.console.aliyun.com/products/csk/quotas) 申请提高配额。 |
| 托管范围 | 支持开启 [Auto Mode](ack-cluster-overview.md) [模式](ack-cluster-overview.md) ： 开启：仅需进行简单的规划配置即可创建集群，集群控制面和关键组件全托管，并默认创建一个 Auto Mode 节点池。 不开启：集群控制面全托管，Worker 节点由您自行运维。 支持 [预设控制面](ack-pro-provisioned-control-plane.md) ： 通过固化控制面资源和 API Server 基线配置，从源头消除弹性扩容的不确定性，而非依赖弹性机制事后追赶，以保障控制面性能始终可预期。 支持 Pro / Pro XL / Pro 2XL / Pro 4XL 之间的升档或降档操作。 | 集群控制面全托管；Worker 节点由您自行运维。 | 集群控制面非托管，Master 和 Worker 节点均由您自行运维。 |
| 适用场景 | 企业生产与测试环境。 期望降低成本的场景。 更希望关注业务应用，减少集群运维投入的场景。 | 集群规模上限较小，适用于个人学习与测试。 | 对成本相对不敏感，并掌握 Kubernetes 技术，可以自行规划、管理、运维集群的场景。 需要对 Kubernetes 进行研究与深度定制，例如对集群控制面（Master 节点）有定制需求的场景。 |
| 收费方式 | 收取集群管理费用（按集群数量计费），同时对 Worker 节点及部分组件使用的其他阿里云产品（例如日志服务 SLS）收费。 说明 ACK 托管集群 Pro 版 支持使用资源包，详细信息请参见 [集群管理费用](../product-overview/cluster-management-fee.md) 。 | 不收取集群管理费用，但对 Worker 节点及部分组件使用的其他阿里云产品（例如日志服务 SLS）收费。 | 不收取集群管理费用，对 Master 节点、Worker 节点及部分组件使用的其他阿里云产品（例如日志服务 SLS）收费。 |
| SLA | 区域级集群提供服务可用性 99.95%的 SLA 保障；可用区级集群提供服务可用性 99.50%的 SLA 保障。更多信息请参见 [阿里云容器服务](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud202010221416_90184.html?spm=a2c4g.11186623.0.0.a36c4e9ctmvDZO) [Kubernetes](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud202010221416_90184.html?spm=a2c4g.11186623.0.0.a36c4e9ctmvDZO) [版服务等级协议](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud202010221416_90184.html?spm=a2c4g.11186623.0.0.a36c4e9ctmvDZO) 。 | 不支持 SLA。 |  |
### ACK托管集群Pro版的能力优势
您可参照下方的表格，了解ACK托管集群Pro版与ACK托管集群基础版的能力差异。
说明
下方表格中，代表支持某项功能，代表不支持某项功能。
| 对比项 | ACK 托管集群 Pro 版 | ACK 托管集群基础版 |
| --- | --- | --- |
| [控制面组件自定义参数设置](customize-ack-pro-control-plane-component-parameters-1693464061811.md) |  |  |
| [API Server](monitor-kube-apiserver.md) [监控指标](monitor-kube-apiserver.md) |  |  |
| etcd 高频冷热备机制，异地容灾 |  |  |
| [etcd](monitor-etcd.md) [可观测性监控指标](monitor-etcd.md) |  |  |
| [Gang scheduling](work-with-gang-scheduling.md) [调度策略](work-with-gang-scheduling.md) |  |  |
| [启用](topology-aware-cpu-scheduling.md) [CPU](topology-aware-cpu-scheduling.md) [拓扑感知调度](topology-aware-cpu-scheduling.md) |  |  |
| [GPU](overview-of-topology-aware-gpu-scheduling.md) [拓扑感知调度](overview-of-topology-aware-gpu-scheduling.md) |  |  |
| [共享](../../cgpu-professional-edition.md) [GPU](../../cgpu-professional-edition.md) [专业版调度](../../cgpu-professional-edition.md) |  |  |
| 支持 [使用阿里云](../security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md) [KMS](../security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md) [进行](../security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md) [Secret](../security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md) [的落盘加密](../security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md) |  |  |
| [托管节点池](../../overview-of-managed-node-pools.md) |  |  |
### 热迁移
ACK托管集群基础版及ACK专有集群都支持热迁移至ACK托管集群Pro版，具体操作请参见以下文档：
[热迁移](hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[托管集群基础版至](hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[托管集群](hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[Pro](hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[版](hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)
[热迁移](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[专有集群至](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[托管集群](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[Pro](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[版](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)
## Auto Mode模式介绍
创建ACK托管集群时，可选择开启Auto Mode。开启后，仅需进行简单的网络规划配置，即可快速创建一个符合最佳实践的Kubernetes集群。其特性如下。
全面托管运维：集群控制面和关键组件全托管。默认创建一个开启了Auto Mode的节点池（简称[Auto Mode](create-a-node-pool.md)[节点池](create-a-node-pool.md)），该节点池将根据工作负载按需动态扩缩容，同时 ACK 将负责操作系统版本升级、软件版本升级、安全漏洞修复等运维职责。
智能资源供给：自动推荐最优实例规格，无需手动配置。
基础软件栈优化：通过 ContainerOS 不可变根文件系统强化安全防护，精简系统与配置加速节点启动，同时借助优化内核充分发挥硬件资源的性能表现。
在以下业务场景中，推荐使用Auto Mode。
动态资源弹性调度：在工作负载需求波动性较大的场景中，Auto Mode能够快速响应需求变化，自动扩容或缩容计算资源，降低集群资源成本。
DevOps 和 CI/CD 流水线：在持续集成和部署环境中，Auto Mode可以根据构建和测试需求自动调整资源，提高开发效率并降低成本。
Auto Mode采用弹性容量、不可变基础设施和免运维的设计理念，对强依赖于节点环境定制、节点本地持久化存储的业务场景，建议在迁移前进行全面的应用评估，识别潜在的兼容性风险点。
重要
Auto Mode旨在提供自动化、智能化的Kubernetes集群运维功能。但在部分场景下，仍需要您履行一部分义务。详情请参见[责任共担模型](auto-mode-overview.md)。
## 产品功能
| 功能 | 描述 |
| --- | --- |
| 集群管理 | 集群创建：您可根据需求创建多种形态集群，选择类型丰富的工作节点，并进行灵活的自定义配置。更多信息，请参见 [创建](create-an-ack-managed-cluster-2.md) [ACK](create-an-ack-managed-cluster-2.md) [托管集群](create-an-ack-managed-cluster-2.md) 和 [创建](create-an-ack-dedicated-cluster.md) [ACK](create-an-ack-dedicated-cluster.md) [专有集群（已停止新建）](create-an-ack-dedicated-cluster.md) 。 集群升级：自动或手动升级集群的 Kubernetes 版本，统一管理系统组件升级。更多信息，请参见 [手动升级集群](update-the-kubernetes-version-of-an-ack-cluster.md) 、 [自动升级集群](automatically-upgrade-an-ack-cluster.md) 。 [弹性伸缩](auto-scaling-overview.md) ：通过控制台一键垂直扩缩容来快速应对业务波动，同时支持服务级别的亲和性策略和横向扩展。 [调度](scheduling-overview.md) ：支持不同弹性资源的混合调度、异构资源的精细化调度、批量计算的任务调度等，提升应用的性能和集群整体资源的利用率。 [多集群管理](../../distributed-cloud-container-platform-for-kubernetes/user-guide/overview-9.md) ：支持线下 IDC 和多云多区域的集群统一接入，实现混合云应用管理。 授权管理：支持 RAM 授权和 RBAC 权限管理。 |
| 节点与节点池 | 支持节点池生命周期管理，支持在同一集群中配置不同规格的节点池，例如交换机、容器运行时、OS、安全组等。更多信息，请参见 [节点](../../node-18.md) 、 [节点池](node-pool-overview.md) 。 |
| 应用管理 | 应用创建：支持多种类型应用，从镜像、模板的创建，支持环境变量、应用健康、数据盘、日志等相关配置。 应用全生命周期：支持应用查看、更新、删除，应用历史版本回滚、应用事件查看、应用滚动升级、应用替换升级以及通过触发器重新部署应用。 应用调度：支持节点间亲和性调度、应用间亲和性调度、应用间反亲和性调度三种策略。 应用伸缩：支持手动伸缩应用 [容器](https://www.aliyun.com/getting-started/what-is/what-is-container) 实例，HPA 自动伸缩策略。 应用发布：支持灰度发布和蓝绿发布。 应用目录：支持应用目录，简化云服务集成。 [应用中心](../../application-center-overview.md) ：应用部署后，以统一的视角展现整体应用的拓扑结构，同时对持续部署等场景进行统一的版本管理与回滚。 应用备份和恢复：支持对 Kubernetes 应用进行备份和恢复。更多信息，请参见 [集群内备份和恢复应用](back-up-and-restore-applications-in-an-ack-cluster.md) 。 |
| 存储 | 存储插件：支持 CSI 存储插件。更多信息，请参见 [存储](csi-overview-1.md) 。 存储卷和存储声明： 支持创建 [块存储](https://www.aliyun.com/getting-started/what-is/what-is-block-storage) 、NAS、OSS 和 CPFS 类型的存储卷。 支持持久化存储卷声明（PVC）挂载存储卷。 支持存储卷的动态创建和迁移。 支持以脚本方式查看和更新存储卷和存储声明。 |
| 网络 | 支持 Terway 和 Flannel 两种容器网络插件。更多信息，请参见 [网络](network.md) 。 支持定义 Service 和 Pod 的 CIDR。 支持 NetworkPolicy，请参见 [在](use-network-policies.md) [ACK](use-network-policies.md) [集群使用网络策略](use-network-policies.md) 。 支持路由 Ingress，请参见 [Ingress](../../ingress-management.md) [管理](../../ingress-management.md) 。 支持服务发现 DNS，请参见 [服务发现](service-discovery-dns-1.md) [DNS](service-discovery-dns-1.md) 。 |
| 弹性伸缩 | 根据业务需求和策略，自动调整弹性计算资源，包括： 工作负载伸缩 （调度层弹性）：主要负责修改工作负载的调度容量变化。 节点伸缩 （资源层弹性）：在集群的容量规划不能满足集群调度容量时，会扩容节点资源，以补充调度容量。 更多信息，请参见 [弹性伸缩](auto-scaling-overview.md) 。 |
| 调度 | ACK 针对不同任务负载提供了多种调度策略，例如任务调度、QoS 感知调度、重调度等，以提升应用性能和集群整体资源的利用率。更多信息，请参见 [调度](scheduling-overview.md) 。 |
| 运维与安全 | [可观测性](observability-overview.md) ： 监控：支持集群、节点、应用、容器实例层面的监控；支持 Prometheus 插件。 日志：支持集群日志查看；支持应用日志采集；支持容器实例日志查看。 报警：支持容器服务异常事件报警，以及容器场景指标报警。更多信息，请参见 [容器服务报警管理](alert-management.md) 。 集群巡检与诊断（AIOps） [使用集群检查](work-with-cluster-check.md) ：支持在集群升级、迁移等操作前执行集群检查，确认集群是否符合要求。 [使用集群巡检](work-with-the-cluster-inspection-feature.md) ：扫描集群运行状况，发现集群中存在的潜在风险，例如云资源配额余量、Kubernetes 集群关键资源水位等，排查风险项并根据推荐的解决方案修复问题。 [使用集群诊断](work-with-cluster-diagnostics.md) ：提供一键故障诊断能力，包括节点诊断、Pod 诊断、Service 诊断、Ingress 诊断、内存诊断、网络诊断，可以辅助您定位集群中出现的问题。 [成本套件](cost-management-suite-overview.md) ：支持可视化集群资源使用量及成本分布，以提升集群资源利用率。 [安全中心](../security-and-compliance/use-security-monitoring-capabilities.md) ：支持运行时刻的安全策略管理，应用安全配置巡检和运行时刻的安全监控和告警，提升容器安全整体纵深防御能力。 [安全沙箱](overview-10.md) ：可以让应用运行在一个轻量虚拟机沙箱环境中，拥有独立的内核，具备更好的安全隔离能力。适用于不可信应用隔离、故障隔离、性能隔离、多用户间负载隔离等场景。 [机密计算](tee-based-confidential-computing.md) ：基于 Intel SGX 提供的可信应用或用于交付和管理机密计算应用的 [云原生](https://www.aliyun.com/getting-started/what-is/what-is-cloud-native) 一站式机密计算平台，帮助您保护数据使用中的安全性、完整性和机密性。机密计算可以让您把重要的数据和代码放在一个特殊的可信执行加密环境。 |
| 异构资源 | GPU：支持创建以 GPU 实例作为工作节点的集群，并支持 GPU 调度、GPU 监控、GPU 弹性伸缩、GPU 运维管理等。更多信息，请参见 [为集群添加](add-gpu-accelerated-nodes-to-a-cluster.md) [GPU](add-gpu-accelerated-nodes-to-a-cluster.md) [节点](add-gpu-accelerated-nodes-to-a-cluster.md) 。 共享 GPU：支持在云平台和自己的数据中心的集群中通过 GPU 共享调度框架实现多个容器运行在同一个 GPU 设备。更多信息，请参见 [共享](cgpu-overview.md) [GPU](cgpu-overview.md) [调度](cgpu-overview.md) 。 云原生 AI：提供了云原生 AI 能力，支持编排、管理数据计算类任务。更多信息，请参见 [云原生](../../cloud-native-ai-suite/product-overview/cloud-native-ai-suite-overview.md) [AI](../../cloud-native-ai-suite/product-overview/cloud-native-ai-suite-overview.md) [套件概述](../../cloud-native-ai-suite/product-overview/cloud-native-ai-suite-overview.md) 。 |
| 开发者工具 | [API](../developer-reference/api-cs-2015-12-15-overview.md) [CLI](../developer-reference/use-container-service-through-cli.md) [SDK](../developer-reference/download-the-sdk.md) [Terraform](../developer-reference/terraform-overview.md) |
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
