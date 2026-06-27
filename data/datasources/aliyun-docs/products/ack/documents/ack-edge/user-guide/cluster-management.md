# 不同集群类型的功能差异与选型-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/cluster-management/

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

# 集群管理概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

容器服务 Edge 版的集群类型分为ACK Edge集群Pro版和ACK Edge集群基础版。这两类集群拥有不同的功能特性、运维需求以及赔付标准，适用于不同的场景。您可参照本文中的对比，选择适合您业务的集群类型。

## 集群类型

ACK Edge集群Pro版和ACK Edge集群基础版的对比详情如下表。

- 

- 

- 

- 

| 比较项 | ACK Edge 集群 Pro 版 | ACK Edge 集群基础版 |
| --- | --- | --- |
| 集群规模 | 主机网络模式：单集群最大 1000 节点。 容器网络模式：单集群最大 200 节点。 关于网络模式的信息，请参见 [Pod](products/ack/documents/create-an-edge-node-pool-1.md) [网络模式](products/ack/documents/create-an-edge-node-pool-1.md) 。 | 单集群最大 10 节点。 |
| SLA | 区域级集群提供服务可用性 99.95%的 SLA 保障；可用区级集群提供服务可用性 99.50%的 SLA 保障。更多信息请参见 [阿里云容器服务](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud202010221416_90184.html?spm=a2c4g.11186623.0.0.a36c4e9ctmvDZO) [Kubernetes](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud202010221416_90184.html?spm=a2c4g.11186623.0.0.a36c4e9ctmvDZO) [版服务等级协议](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud202010221416_90184.html?spm=a2c4g.11186623.0.0.a36c4e9ctmvDZO) 。 | 不支持 SLA。 |
| 适用场景 | 企业生产与测试环境。 期望降低成本的场景。 | 集群规模上限较小，不保证集群控制面的可用性，适用于个人学习与测试。 |
| 收费方式 | 收取集群管理费用（按集群数量计费）、边缘节点管理费（按接入的非云端节点数量计费）以及在使用 ACK Edge 集群 过程中涉及到其他的阿里云产品资源费用，详细信息请参见 [ACK Edge](products/ack/documents/ack-edge/product-overview/billing-of-ack-edge-clusters.md) [集群计费说明](products/ack/documents/ack-edge/product-overview/billing-of-ack-edge-clusters.md) 。 | 不收取集群管理费用，但仍然收取边缘节点管理费（按接入的非云端节点数量计费）以及在使用 ACK Edge 集群过程中涉及到其他的阿里云产品资源费用，详细信息请参见 [ACK Edge](products/ack/documents/ack-edge/product-overview/billing-of-ack-edge-clusters.md) [集群计费说明](products/ack/documents/ack-edge/product-overview/billing-of-ack-edge-clusters.md) 。 |


### ACK Edge集群能力对比

您可参照下方的表格，了解ACK Edge集群Pro版与ACK Edge集群基础版的能力差异。

说明

下方表格中，代表支持某项功能，代表不支持某项功能。

| 对比项 | ACK Edge 集群 Pro 版 | ACK Edge 集群基础版 |
| --- | --- | --- |
| [控制面组件自定义参数设置](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-ack-pro-control-plane-component-parameters-1693464061811.md) |  |  |
| [API Server](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-kube-apiserver.md) [监控指标](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-kube-apiserver.md) |  |  |
| etcd 高频冷热备机制，异地容灾 |  |  |
| [etcd](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-etcd.md) [可观测性监控指标](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/monitor-etcd.md) |  |  |
| [Gang scheduling](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-gang-scheduling.md) [调度策略](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-gang-scheduling.md) |  |  |
| [启用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/topology-aware-cpu-scheduling.md) [CPU](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/topology-aware-cpu-scheduling.md) [拓扑感知调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/topology-aware-cpu-scheduling.md) |  |  |
| [GPU](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/overview-of-topology-aware-gpu-scheduling.md) [拓扑感知调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/overview-of-topology-aware-gpu-scheduling.md) |  |  |
| [共享](https://help.aliyun.com/zh/document_detail/212213.html) [GPU](https://help.aliyun.com/zh/document_detail/212213.html) [专业版调度](https://help.aliyun.com/zh/document_detail/212213.html) |  |  |
| 支持 [使用阿里云](products/ack/documents/ack-edge/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) [KMS](products/ack/documents/ack-edge/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) [进行](products/ack/documents/ack-edge/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) [Secret](products/ack/documents/ack-edge/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) [的落盘加密](products/ack/documents/ack-edge/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) |  |  |
| [托管节点池](products/ack/documents/overview-of-managed-node-pools.md) |  |  |


### 热迁移

ACK Edge集群基础版支持热迁移至ACK Edge集群Pro版，具体操作请参见[热迁移](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[集群基础版至](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[Pro](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)[版](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md)。

## 产品功能

ACK Edge集群是阿里云容器服务 Kubernetes 版 ACK（Container Service for Kubernetes）家族的一员，ACK Edge支持的集群相关操作与ACK集群Pro版保持一致。由于ACK Edge集群需要同时管理云上和云下的基础设施，一些操作仍有差别，差异总结如下表所示。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 比较项 | ACK Edge 集群 与 ACK 集群 Pro 版 的差异 | 操作链接 |  |
| --- | --- | --- | --- |
| 集群 | 创建集群 | 支持的网络插件，容器网段相关配置不同。具体信息，请参见 [如何选择网络插件](products/ack/documents/ack-edge/user-guide/how-to-choose-a-network-plug-in.md) 。 | [创建集群](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md) |
| 升级集群 | ACK Edge 集群 不支持集群自动升级。 ACK Edge 集群 的边缘节点池升级方式与云端节点池不同。 | [升级集群](products/ack/documents/ack-edge/user-guide/upgrade-ack-edge-cluster.md) |  |
| 连接集群 | 与 ACK 集群 Pro 版 完全一致。 | [获取集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md) [KubeConfig](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md) [并通过](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md) [kubectl](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md) [工具连接集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md) [在](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408.md) [CloudShell](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408.md) [上通过](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408.md) [kubectl](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408.md) [管理](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408.md) [Kubernetes](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408.md) [集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-kubectl-on-cloud-shell-to-manage-ack-clusters-1690962464408.md) [集群访问控制](products/ack/documents/cluster-access-control.md) [清除](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/clear-kubeconfig.md) [KubeConfig](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/clear-kubeconfig.md) |  |
| 管理集群 | 与 ACK 集群 Pro 版 完全一致。 | [查看集群信息](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/view-cluster-information.md) [集群生命周期](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cluster-abnormal-states.md) [配置集群安全组](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-security-group-rules-to-enforce-access-control-on-ack-clusters.md) [自定义](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-ack-pro-control-plane-component-parameters-1693464061811.md) [Pro](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-ack-pro-control-plane-component-parameters-1693464061811.md) [版集群的控制面组件参数](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-ack-pro-control-plane-component-parameters-1693464061811.md) [热迁移](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [集群基础版至](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [Pro](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) [版](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters.md) |  |
| 删除集群 | 边缘节点池在集群删除后，需要您手动清理节点上的系统组件。相关操作，请参见 [移除边缘节点](products/ack/documents/ack-edge/user-guide/remove-edge-nodes.md) 。 | [删除集群](products/ack/documents/ack-edge/user-guide/untitled-document.md) |  |
| 节点与节点池 | ACK Edge 集群 的云端节点池能力与 ACK 集群 Pro 版 节点池完全一致。 ACK Edge 集群 的边缘节点池支持管理线下分散地域的各种类型的节点，例如不同地域的 ECS 节点、IDC 节点、其他厂商云节点，以及分布在工厂、门店、车辆和船舶中的服务器节点。 ACK Edge 集群 的边缘节点支持设置节点自治与节点断网运维。 | [节点池管理](products/ack/documents/ack-edge/user-guide/overview-of-cell-based-management-at-the-edge.md) [节点管理](products/ack/documents/ack-edge/user-guide/node-management-overview.md) [设置边缘节点自治](products/ack/documents/ack-edge/user-guide/configure-node-autonomy.md) [边缘节点离线运维](products/ack/documents/ack-edge/user-guide/edge-node-offline-operation-and-maintenance-tool.md) |  |
| 存储 | ACK Edge 集群 的 CSI（csi-plugin 和 csi-provisioner）插件复用 ACK 集群的 CSI 插件，在云端节点上使用 CSI 插件和 ACK 集群完全保持一致，详情请参见 [CSI](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/csi-overview-1.md) [插件的存储方案](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/csi-overview-1.md) 。 ACK Edge 集群 的边缘节点根据节点类型和接入方式的不同支持不同的存储类型。 | [存储管理](products/ack/documents/ack-edge/user-guide/storage-overview.md) |  |
| 应用 | ACK Edge 集群 提供了新的工作负载和扩展能力，以增强应用管理能力。 节点池应用集管理：在边缘计算场景下，计算节点具有很明显的地域分布属性，相同的应用可能需要部署在不同地域的计算节点上。为简化边缘计算场景下分散部署的复杂性，ACK Edge 集群提供了 YurtAppSet，可以对多个工作负载（Workload 资源，如 Deployment）进行统一管理。 DaemonSet 升级扩展：在边缘计算场景下，原生的 DaemonSet 升级模型存在一些局限性。您可以通过配置扩展的 DaemonSet 升级模型 AdvancedRollingUpdate 和 OTA 以解决云边网络中断导致的升级阻塞以及 OTA 升级问题。 | [节点池应用集管理](products/ack/documents/ack-edge/user-guide/node-pool-yurtappset-management.md) [DaemonSet](products/ack/documents/ack-edge/user-guide/daemonset-upgrade-model.md) [升级模型](products/ack/documents/ack-edge/user-guide/daemonset-upgrade-model.md) |  |
| 网络 | ACK Edge 集群 的边缘节点支持公网接入和专线接入两种网络接入类型。 ACK Edge 集群 支持 Flannel 与 Terway Edge 两种容器网络插件。 ACK Edge 集群 提供了跨网域的云边运维通信组件 Raven，支持在多地域环境中实现高效的云边运维。 ACK Edge 集群 支持配置 Service 的服务拓扑以及 NodePort Service 的端口隔离。 Ingress 组件的部署方式不同。 | [网络管理](products/ack/documents/ack-edge/user-guide/network-management-overview.md) [如何选择网络插件](products/ack/documents/ack-edge/user-guide/how-to-choose-a-network-plug-in.md) [跨域运维通信组件](products/ack/documents/ack-edge/user-guide/cloud-edge-communication-component-raven-overview.md) [Raven](products/ack/documents/ack-edge/user-guide/cloud-edge-communication-component-raven-overview.md) [NodePort](products/ack/documents/ack-edge/user-guide/nodeport-service-isolation.md) [端口监听隔离](products/ack/documents/ack-edge/user-guide/nodeport-service-isolation.md) [节点池服务拓扑管理](products/ack/documents/ack-edge/user-guide/configure-a-service-topology.md) [Ingress](products/ack/documents/ack-edge/user-guide/edge-cluster-ingress-overview.md) [概述](products/ack/documents/ack-edge/user-guide/edge-cluster-ingress-overview.md) |  |
| 弹性伸缩 | 工作负载伸缩与节点伸缩能力与 ACK 集群 Pro 版 完全一致。 ACK Edge 集群 暂不支持 ECI 弹性。 | [弹性伸缩概述](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/auto-scaling-overview.md) |  |
| 调度 | 与 ACK 集群 Pro 版 完全一致。 | [调度概述](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/scheduling-overview.md) |  |
| 运维与安全 | 可观测能力与 ACK 集群 Pro 版 完全一致。 ACK Edge 集群 暂不支持 AIOps 套件的能力。 ACK Edge 集群 暂不支持成本套件中成本洞察的能力。 ACK Edge 集群 暂不支持安全沙箱、机密计算以及自动验证容器镜像签名的能力。 | [可观测性体系概述](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/observability-overview.md) [安全体系概述](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/security-system-overview.md) [成本套件概述](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cost-management-suite-overview.md) |  |
| 异构资源 | 边缘 GPU 节点接入方式不同。 ACK Edge 集群 支持除 GPU 隔离外完整的云原生 AI 套件的能力。 | [添加](products/ack/documents/ack-edge/user-guide/add-a-gpu-node.md) [GPU](products/ack/documents/ack-edge/user-guide/add-a-gpu-node.md) [节点](products/ack/documents/ack-edge/user-guide/add-a-gpu-node.md) [AI](products/ack/documents/ack-edge/user-guide/cloud-native-ai-suite-overview.md) [套件](products/ack/documents/ack-edge/user-guide/cloud-native-ai-suite-overview.md) |  |
| 开发者工具 | 与 ACK 集群 Pro 版 完全一致。 | [API](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-overview.md) [CLI](products/ack/documents/ack-edge/developer-reference/cli-reference.md) [SDK](products/ack/documents/ack-edge/developer-reference/sdk-reference.md) [Terraform](products/ack/documents/ack-edge/developer-reference/terraform.md) |  |


[上一篇：操作指南](products/ack/documents/ack-edge/user-guide.md)[下一篇：创建集群](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md)

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
