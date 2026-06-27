# 对节点进行统一的生命周期管理-节点池-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/node-pool-overview

# 节点池概述
节点池是具有相同属性的一组节点的逻辑集合，允许对节点进行统一的管理和运维，例如节点升级、弹性伸缩等。ACK还提供多种节点池自动化运维能力，包括OS CVE漏洞自动修复、故障节点自动恢复等，以降低运维成本。
## 节点池介绍
简单来说，节点池是一个配置模板，后续节点池中扩容出的节点都将使用它的配置。一个集群中可以创建多个不同配置和类型的节点池。节点池的配置包含节点的属性，例如节点实例规格、计费类型、可用区（vSwitch）、[操作系统镜像](overview-of-os-images.md)、CPU架构、标签和污点等。这些属性可以在[创建节点池](create-a-node-pool.md)时指定，也可以在创建后[编辑](create-a-node-pool.md)。
ACK节点池功能推出前创建的老集群中，可能存在未被节点池管理的游离Worker节点。如仍需要保留这些节点，推荐将其纳入节点池进行管理。具体操作，请参见[迁移游离节点至节点池](add-free-nodes-to-a-node-pool.md)。
可使用单节点池，减少管理和配置的复杂性，也可使用多节点池，实现更精细的资源隔离和不同类型节点的混合部署管理。
| 单节点池 | 多节点池 |
| --- | --- |
| 通过一个节点池管理多个团队或多种工作负载的计算资源，简化操作和维护工作。单节点池可支持以下功能。 同时管理多个团队的计算资源。 配置多种实例类型，例如普通 ECS 实例、GPU 实例、弹性裸金属实例、高性能计算优化型实例等，以满足不同工作负载的需求。 在多个可用区中分布节点，提高高可用性。 目前不支持混合不同操作系统类型和 CPU 架构（Arm 和 x86）的实例。 | 创建多个节点池，为不同工作负载或团队提供独立的计算资源，从而避免资源争用和潜在的安全风险。适用于以下场景。 租户隔离，为不同团队提供独立的计算资源，也便于计费管理。 不同硬件规格（例如 CPU 架构、GPU、FPGA 等）机器的隔离，确保硬件资源的合理分配。 增强敏感应用的安全隔离。 部署不同的操作系统。 |
使用多节点池时，可通过调度策略定义不同节点池的优先级顺序，以优化资源和成本管理。例如以下场景。
控制不同成本的计算资源供给（例如抢占式实例、包年包月实例等）的优先级顺序，以降低成本。
根据工作负载需求，按比例分配不同类型的实例，例如x86架构和Arm架构的使用比例。
## 节点池功能
ACK在节点池维度提供多种节点管理能力。如需减少Worker节点运维压力，更关注于上层应用开发，建议开启节点池的托管能力，使用多种自动化运维能力。
### 基础功能
| 功能项 | 说明 | 相关文档 |
| --- | --- | --- |
| 创建、编辑、删除与查看 | 支持通过控制台创建节点池，配置节点池的基础信息、网络配置、实例规格配置、存储配置、期望节点数等。 支持调整已有节点池的部分配置。支持编辑的配置项及操作注意事项，请参见文档了解。 节点无需使用时，可删除节点池。节点池是否开启期望节点数以及节点的计费模式会影响节点释放的行为。 支持查看节点池详情，包括基本配置信息、资源监控大盘、节点列表、伸缩活动等。 | [创建和管理节点池](create-a-node-pool.md) |
| 手动或自动扩缩容 | 支持通过手动调整节点池的期望节点数，实现节点池的扩缩容，将节点数目维持在期望数量，节省资源成本。 一些非标准的移除、修改、释放等操作可能导致节点池未按照预期扩容，请参见文档了解。 支持配置节点自动伸缩方案，当集群的容量规划无法满足应用 Pod 调度时，自动扩缩节点资源。 | [手动扩缩容节点池](scale-a-node-pool.md) [节点伸缩](overview-of-node-scaling.md) |
| 添加已有节点 | 如购买 ECS 实例后需将其添加到 ACK 集群中作为 Worker 节点，或移除 Worker 节点后需重新加入节点池，可以使用添加已有节点的功能。此功能存在一些使用限制和注意事项，请参见文档了解。 | [添加已有节点](add-existing-ecs-instances-to-an-ack-cluster.md) |
| 移除节点 | 如果不再需要某些节点，可将节点从集群或节点池中移除。请按标准化操作移除，避免出现预期外行为。 | [移除节点](remove-a-node-11.md) |
| 升级 kubelet 版本 | 可通过 [自动升级集群](automatically-upgrade-an-ack-cluster.md) 实现 kubelet 和运行时的自动升级 升级节点池中节点的 kubelet 版本和 containerd 版本。 | [升级节点池](node-pool-updates.md) |
| 更换操作系统 | 支持操作系统版本的升级和操作系统类型的更换（例如将 EOL 的操作系统切换为 ContainerOS 或 Alibaba Cloud Linux）。 | [更换操作系统](replace-the-operating-system.md) |
| CVE 漏洞修复 | 可开启 [自动化运维能力](node-pool-overview.md) 手动执行 CVE 漏洞的扫描并修复节点操作系统存在的安全漏洞。部分 CVE 漏洞的修复需要通过重启节点来实现，请参见文档了解功能说明及注意事项。 | [操作系统](cve-patching.md) [CVE](cve-patching.md) [漏洞手动修复](cve-patching.md) |
| 自定义节点池 kubelet 参数 | 在节点池维度自定义节点的 kubelet 参数配置，调整节点行为，例如调整集群资源预留以调配资源用量等。 | [自定义节点池](customize-the-kubelet-configurations-of-a-node-pool.md) [kubelet](customize-the-kubelet-configurations-of-a-node-pool.md) [配置](customize-the-kubelet-configurations-of-a-node-pool.md) |
| 自定义节点池 OS 参数 | 在节点池维度自定义节点的 OS 参数配置，以调优系统性能。 | [管理节点池](custom-node-pool-os-parameters.md) [OS](custom-node-pool-os-parameters.md) [参数](custom-node-pool-os-parameters.md) |
| 成本洞察 | 节点池维度的资源使用情况及成本分布分析，便于节约成本，提升集群资源利用率。 | [成本洞察](cost-analysis-overview.md) |
### 自动化运维能力
启用节点池的自动化运维能力能够降低Worker节点的运维负担，让ACK自动化完成某些运维操作，例如操作系统（OS）CVE漏洞自动修复、kubelet自动升级、节点故障自愈等。但如果业务对底层节点的变更比较敏感，无法容忍节点的重启以及业务Pod的迁移，不推荐启用。
准备工作
确保操作系统为[Alibaba Cloud Linux 3](https://help.aliyun.com/zh/alinux/alibaba-cloud-linux-3-container-optimized-images)[容器优化版](https://help.aliyun.com/zh/alinux/alibaba-cloud-linux-3-container-optimized-images)、[ContainerOS](containeros-overview.md)、Alibaba Cloud Linux、Red Hat、Ubuntu。
关于ACK集群支持的操作系统镜像介绍及镜像的使用限制，请参见[操作系统](overview-of-os-images.md)。
使用节点池的自动化运维能力前，需在[容器服务管理控制台](https://cs.console.aliyun.com)的节点池页面完成以下操作（配置完成后均支持修改）。
关于如何创建和编辑节点池，请参见[创建和管理节点池](create-a-node-pool.md)。
展开查看操作流程
为节点池开启托管能力
新建节点池：创建节点池的过程中选择托管节点池。
存量节点池：在节点池列表的操作列，单击节点池对应的更多>开启托管。
按需启用节点池的自动化运维能力
包括开启节点自愈、自动升级kubelet、运行时和OS版本、自动修复OS CVE漏洞等。
配置集群维护窗口
节点池的自动化运维能力需配置集群维护窗口使用，节点池会在集群维护窗口内执行自动化运维任务。
新建节点池：创建节点池的过程中配置托管节点池的集群维护窗口。
存量节点池：在节点池列表的操作列，单击存量托管节点池对应的更多>托管配置，配置维护窗口。
功能介绍
| 功能项 | 说明 |
| --- | --- |
| 节点自愈 | ACK 会自动监控节点状态，在节点发生异常时自动执行自愈任务，修复系统和 K8s 组件异常以及节点实例异常问题，请参见 [开启节点自愈](auto-repair.md) 。 |
| OS CVE 漏洞自动修复 | ACK 将扫描节点上存在的安全漏洞，根据集群运维窗口排期并执行 CVE 漏洞修复计划，以提升集群稳定性、安全性、合规性。相关注意事项，请参见 [修复节点池操作系统](cve-patching.md) [CVE](cve-patching.md) [漏洞](cve-patching.md) 。 |
| ECS 系统事件自动响应 | 支持 [ECS](../../../../ecs/documents/user-guide/overview-of-ecs-system-events.md) [系统事件](../../../../ecs/documents/user-guide/overview-of-ecs-system-events.md) 的自动响应。目前支持的系统事件类型如下。 因系统维护实例重启（SystemMaintenance.Reboot） 自动响应流程 ACK 接收到事件后，同步发送短信或站内信通知。请及时关注。 执行操作前，ACK 根据 ECS 的计划执行时间进行安排： 如果节点池在计划执行时间前有可用的维护窗口，ACK 会在维护窗口内执行自动响应流程。 否则，ACK 会在 ECS 计划执行时间的前一个小时执行该流程。 流程开始后，ACK 针对受影响的 ECS 实例执行 [节点排水](node-pool-overview.md) （Drain），尝试将节点上的 Pod 迁移到其他可用节点，随后重启 ECS 实例。 节点排水规则 执行节点排水时，ACK 会首先驱逐该节点上所有可安全排水的 Pod，对于不能安全排水的 Pod，将返回错误信息，并且终止自动响应流程。 以下情况的 Pod 被视为不能安全排水： Pod 带有 Label goatscaler.io/safe-to-evict=false 。 不受控制器管理的 Pod（即没有 OwnerReference 的独立 Pod）。 Pod 使用了 emptyDir 类型的卷。 由于排水操作会驱逐节点上的 Pod，为避免节点维护影响服务的整体可用性，强烈建议： 确保服务应用后端采用多副本（Replicas）方式部署在不同节点上。 为重要应用配置 [PodDisruptionBudget（PDB）](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#pod-disruption-budgets) ，以避免节点上 Pod 被驱逐后影响服务的整体可用性。 |
自2026年01月31日起，托管节点池 kubelet 和容器运行时的自动升级配置入口将下线，可配置[自动升级集群](automatically-upgrade-an-ack-cluster.md)来完成节点池的自动升级。详情请参见[【产品变更】关于托管节点池安全漏洞修复和自动升级的变更公告](../../product-overview/announcement-on-security-vulnerabilithy-fixes-and-automatic-upgrades-for-managed-node-pools.md)。
## 节点池生命周期
ACK集群节点池的生命周期涉及多个阶段和状态，从节点池的创建部署、运行维护（扩容缩容、更新升级、节点移除等），到最终的删除。不同状态的含义和流转如下。
| 节点池状态 | 说明 |
| --- | --- |
| 初始化中（initial） | 正在创建节点池。 |
| 已激活（active） | 成功创建节点池，运行中。 |
| 失败（failed） | 节点池创建失败。 |
| 扩容中（scaling） | 节点池扩容中或正在添加节点。 |
| 更新中（updating） | 节点池配置更新中。 |
| 移除节点中（removing_nodes） | 正在移除节点池中的节点。 |
| 升级中（upgrading） | 节点池升级中。 |
| 修复中（repairing） | 节点池修复中，例如修复节点池节点、节点池 CVE 漏洞等。 |
| 删除中（deleting） | 正在删除节点池。 |
| 已删除（deleted，该状态您不可见） | 成功删除节点池。 |
| 删除失败（deleted_failed） | 节点池删除失败。请重新删除。 如仍然删除失败，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 。 |
## 节点池计费
使用节点池和节点池提供的自动化运维能力不收费，但节点池内ECS实例等云资源由对应的云产品收取费用。
关于ECS实例的计费说明，请参见[计费概述](../../../../ecs/documents/billing-overview.md)。
如需修改节点池中已有节点的付费类型，请参见[按量付费转包年包月](../../../../ecs/documents/change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md)。修改节点池的付费类型仅对扩容的新节点生效，不会改变节点池内已有节点的付费类型。
关于弹性伸缩组的计费详情，请参见[弹性伸缩产品计费](https://help.aliyun.com/zh/auto-scaling/product-overview/billing-rules#concept-nw2-h3m-qfb)。
## 相关术语
首次使用节点池前，建议了解节点池相关的概念术语。
伸缩组：当对节点池进行扩容和缩容时，ACK通过[弹性伸缩](https://help.aliyun.com/zh/auto-scaling/product-overview/what-is-auto-scaling)[ESS](https://help.aliyun.com/zh/auto-scaling/product-overview/what-is-auto-scaling)服务下发扩容和移除节点的操作。节点池与弹性[伸缩组](https://help.aliyun.com/zh/auto-scaling/user-guide/scaling-group-overview#concept-25880-zh)实例为一一对应的关系。一个伸缩组是一个或多个ECS实例（Worker节点）的合集。
伸缩配置：节点池底层使用伸缩配置管理节点配置。ESS伸缩配置是弹性伸缩时ECS实例使用的模板。当弹性伸缩触发弹性扩张活动后，弹性伸缩以该伸缩配置为模板自动创建ECS实例。
伸缩活动：节点池的每次扩缩容、添加节点、移除节点都会触发伸缩活动。触发伸缩活动后，所有扩容和缩容动作都交由系统自动完成，并留下相关记录。可通过节点池的伸缩活动查看节点池的历史伸缩活动记录。
替换系统盘：节点池的某些操作，例如自动添加已有节点、更换容器运行时等，会通过替换节点系统盘（替盘升级）的方式初始化节点。该节点的实例属性不发生改变，例如节点名称、实例ID、IP等，但节点系统盘上的数据将被删除。额外挂载到该节点上的数据盘不受影响。
ACK执行替盘时会进行节点排水操作，遵循[Pod Disruption Budget（PDB）](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#pod-disruption-budgets)的前提下将节点上的Pod驱逐至其他可用节点。为确保服务高可用性，建议采用多副本部署策略，将工作负载分散在多个节点上，同时为关键业务配置PDB，控制同时中断的Pod数量。
原地升级：与替盘升级对应的一种升级方式，直接在原节点上更新替换所需的组件。原地升级不会替换系统盘，也不会重新初始化节点，原节点的数据不受影响。
## 相关文档
关于集群支持的Kubernetes资源（例如集群中最大支持的节点数量、Pod数量等）容量上限，请参见[配额（Quota）](../../product-overview/limits.md)。
ACK支持[自动升级集群](automatically-upgrade-an-ack-cluster.md)。
1.24版本的集群将不再支持使用Docker作为内置容器运行时，请迁移至containerd，请参见[将节点容器运行时从](change-the-container-runtime-from-docker-to-containerd.md)[Docker](change-the-container-runtime-from-docker-to-containerd.md)[迁移到](change-the-container-runtime-from-docker-to-containerd.md)[containerd](change-the-container-runtime-from-docker-to-containerd.md)。
随着集群负载的增加，可启用弹性伸缩方案，动态调整节点资源，请参见[弹性伸缩](auto-scaling-overview.md)。
如需指定应用Pod使用的节点池，请参见[调度应用至指定节点池](schedule-an-application-pod-to-a-specific-node-pool.md)。
ACK托管集群基础版支持的节点上限为10，建议热迁移至ACK托管集群Pro版以获得更大的资源配额，请参见[热迁移](hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[托管集群基础版至](hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[托管集群](hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[Pro](hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[版](hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)。
如果在使用节点或节点池的过程中遇到问题，可参见[节点与节点池](faq-about-node-management.md)[FAQ](faq-about-node-management.md)进行自排查。
ACK提供集群成本管理解决方案，请参见[成本套件](cost-management-suite-overview.md)。
节点池相关的最佳实践，请参见[节点与节点池最佳实践](best-practices-for-nodes-and-node-pools.md)。
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
