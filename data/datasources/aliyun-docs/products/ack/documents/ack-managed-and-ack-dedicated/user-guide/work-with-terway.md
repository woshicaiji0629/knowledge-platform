# 使用Terway网络插件-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/work-with-terway

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

# 使用Terway网络插件

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Terway是阿里云开源的基于专有网络VPC的容器网络接口CNI（Container Network Interface）插件，支持基于Kubernetes标准的网络策略来定义容器间的访问策略。

## 阅读前提示

为了让您能更好地了解Terway的工作模式，建议您在使用Terway网络插件前阅读本文档。

阅读本文前，推荐您参见[网络](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/network.md)、[容器网络插件](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)[Terway](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)[与](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)[Flannel](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)[对比](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)文档了解容器网络插件的基本概念并完成容器网络插件选型。

创建集群前需要对集群中的网段进行规划，具体操作请参见[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/kubernetes-cluster-network-planning.md)[托管集群网络规划](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/kubernetes-cluster-network-planning.md)。

## 费用说明

使用Terway插件并不收费，但在每个节点上都会部署Terway所使用的Pod，这些Pod会占用少量节点资源。关于ACK的云产品资源计费信息，请参见[云产品资源费用](products/ack/documents/ack-managed-and-ack-dedicated/product-overview/billing-of-cloud-services.md)。

## 重要说明

Terway 配置文件eni-config包含大量系统参数，修改、删除非允许的字段，可能会造成网络中断、Pod无法创建等异常。可修改配置参数声明在[自定义](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/terway-configuration-parameters.md)[Terway](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/terway-configuration-parameters.md)[配置参数](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/terway-configuration-parameters.md)。

Terway组件使用CRD来跟踪资源状态，若您误操作系统资源，可能会造成网络中断、Pod无法创建等异常。

| 资源名称 | 资源类型 | 用户是否可以操作 CRD | 用户是否可以操作 CR |
| --- | --- | --- | --- |
| podnetworkings.network.alibabacloud.com | 用户资源 | 否 | 是 |
| podenis.network.alibabacloud.com | 系统资源 | 否 | 否 |
| networkinterfaces.network.alibabacloud.com | 系统资源 | 否 | 否 |
| nodes.network.alibabacloud.com | 系统资源 | 否 | 否 |
| noderuntimes.network.alibabacloud.com | 系统资源 | 否 | 否 |
| *.cilium.io | 系统资源 | 否 | 否 |
| *.crd.projectcalico.org | 系统资源 | 否 | 否 |


## 节点Pod限额计算方法

使用Terway网络插件时，单节点支持的最大数量基于节点使用的ECS规格支持的ENI数量。Terway对单节点的Pod限额有最低限制，单节点支持的Pod限额需要满足限制才能正常加入集群。详细信息请参见下表：

| Terway 模式 | 单节点 Pod 限额 | 示例值 | 单节点支持固定 IP、独立虚拟交换机、独立安全组功能的 Pod 数量 |
| --- | --- | --- | --- |
| 共享 ENI 模式 | （ [ECS](products/ecs/documents/user-guide/overview-of-instance-families.md) [规格支持的](products/ecs/documents/user-guide/overview-of-instance-families.md) [ENI](products/ecs/documents/user-guide/overview-of-instance-families.md) [数量](products/ecs/documents/user-guide/overview-of-instance-families.md) -1）×单个 ENI 支持的私有 IP 数。 （EniQuantity-1）×EniPrivateIpAddressQuantity 说明 单节点的 Pod 限额必须>11 才能加入集群。 | 以通用型实例规格族 g7 的 ecs.g7.4xlarge 规格为例。该规格实例支持 8 个 ENI，单个 ENI 支持 30 个私有 IP。单节点 Pod 限额为（8-1）×30=210 个 Pod。 重要 使用节点 ENI 的 Pod 限额是由节点规格决定的固定值。修改 maxPods 只影响使用 hostNetwork 的 Pod 限额。 | 0 |
| 共享 ENI 模式+Trunk ENI | 单节点 Trunk Pod 限额： ECS 规格支持的总网卡数-ECS 规格支持的弹性网卡数。 EniTotalQuantity-EniQuantity |  |  |
| 独占 ENI 模式 | ECS 实例： [ECS](products/ecs/documents/user-guide/overview-of-instance-families.md) [规格支持的](products/ecs/documents/user-guide/overview-of-instance-families.md) [ENI](products/ecs/documents/user-guide/overview-of-instance-families.md) [数量](products/ecs/documents/user-guide/overview-of-instance-families.md) -1。 EniQuantity-1 灵骏实例： [创建及管理灵骏弹性网卡](https://help.aliyun.com/zh/pai/create-and-manage-lingjun-enis) -1。 LeniQuota-1 说明 单节点的 Pod 限额必须>6 才能加入集群。 | 以通用型实例规格族 g7 的 ecs.g7.4xlarge 规格为例。该规格实例支持 8 个 ENI。单节点 Pod 限额为（8-1）=7 个 Pod。 | [ECS](products/ecs/documents/user-guide/overview-of-instance-families.md) [规格支持的](products/ecs/documents/user-guide/overview-of-instance-families.md) [ENI](products/ecs/documents/user-guide/overview-of-instance-families.md) [数量](products/ecs/documents/user-guide/overview-of-instance-families.md) -1。 EniQuantity-1 说明 灵骏实例不支持。 |


重要

在Terway v1.11.0及之后的版本中，Terway支持为节点池选择独占ENI模式或共享ENI模式，在单个集群中可同时存在两种节点池，更多信息请参见[Terway](products/ack/documents/product-overview/terway.md)[发布记录](products/ack/documents/product-overview/terway.md)。

### 查看节点支持的最大容器网络Pod数量

- 

方式一：创建节点池时，在实例规格区域，通过Terway兼容性（可支持 Pod 数量）查看某一实例规格支持的Pod数量。

- 

方式二：先参考下列方式获取计算数据，然后手动计算ECS规格支持的Pod数量。

- 

通过[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)文档查询ECS实例支持的弹性网卡数量。

- 

通过[OpenAPI](https://next.api.aliyun.com/api/Ecs/2014-05-26/DescribeInstanceTypes?lang=JAVA&params=%7B%22InstanceTypes%22:%5B%22ecs.c1.large%22%5D%7D&tab=DOC)进行查询，通过指定已有节点的实例规格InstanceTypes，单击发起调用，返回值中EniQuantity表示实例规格支持的弹性网卡上限，EniPrivateIpAddressQuantity表示单个弹性网卡支持的私有IP数量。EniTotalQuantity表明实例规格支持的总网卡数量。

## 在创建集群时安装Terway网络插件

您需要在创建集群时安装Terway网络插件，已创建的集群不支持修改网络插件类型。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击创建集群。

- 

为Terway网络插件配置集群网络的关键参数。关于创建集群的其他参数，请参见[创建](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。

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

| 配置项 | 说明 |
| --- | --- |
| IPv6 双栈 | 勾选 开启 后，会为集群开启双栈，同时支持 IPv4 与 IPv6 地址。 仅支持 1.22 及以上版本，仅支持 Terway，不支持与 [eRDMA](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-erdma-in-ack-clusters.md) [功能](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-erdma-in-ack-clusters.md) 同时使用 集群同时支持 IPv4 和 IPv6 协议，但 Worker 节点与控制面间的通信仍使用 IPv4 地址。需确保： 集群 VPC 支持 IPv6 双栈。 使用 Terway 共享 ENI 模式时，节点的 [实例规格](products/ecs/documents/user-guide/overview-of-instance-families.md) 需支持 IPv6 且支持的 IPv4/IPv6 地址数量相同。 |
| 专有网络 | 集群所使用的 VPC。 |
| 网络插件 | 选择 Terway 。 |
| DataPath V2 | 勾选后，会使用 DataPathv2 加速模式。选择该模式后，Terway 会采取不同于共享 ENI 常规模式的流量转发链路，实现 [网络加速](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) 。更多内容，请参见 [Datapath V2](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/datapath-v2-best-practices.md) [下最佳实践](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/datapath-v2-best-practices.md) 。 说明 新建集群初始版本为 Kubernetes 1.34 或更高，且选择 DataPath V2 的情况下，Terway 节点将不再运行 kube-proxy。 此模式下默认支持 portmap，无需配置 portmap 插件， [配置自定义](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/custom-cni-chain.md) [CNI Chain](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/custom-cni-chain.md) 。 DataPath V2 仅支持下列操作系统镜像，且要求 Linux 内核版本为 5.10 或更高： Alibaba Cloud Linux 4 Alibaba Cloud Linux 3（所有版本） ContainerOS Ubuntu 开启后，Terway policy 容器预计会在每个 Worker 节点上多占用 0.5 核 512MB 的资源，此消耗会随着集群规模增大而增大。在 Terway 默认配置中，policy 容器的 CPU 上限为 1 核，内存无限制。 在 DataPath V2 模式下，容器网络的连接跟踪（conntrack）信息通过 eBPF map 进行存储。与 Linux 系统原生的 conntrack 机制类似，eBPF conntrack 基于 LRU（最近最少使用）算法实现，当 map 容量达到上限时，会自动淘汰最旧的连接记录以存储新连接，您需要根据实际业务规模合理配置相关参数，以防连接数超出限制。请参考 [优化](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/optimize-conntrack-configuration-in-terway-mode.md) [Terway](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/optimize-conntrack-configuration-in-terway-mode.md) [模式下](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/optimize-conntrack-configuration-in-terway-mode.md) [conntrack](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/optimize-conntrack-configuration-in-terway-mode.md) [配置](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/optimize-conntrack-configuration-in-terway-mode.md) 。 |
| NetworkPolicy 支持 | 勾选后，则会支持 Kubernetes 原生的 NetworkPolicy 。 说明 从 Terway v1.9.2 开始，新建集群 NetworkPolicy 由 eBPF 的实现提供，数据面会开启 DataPathv2 功能。 通过控制台管理 NetworkPolicy 的功能正在公测中，如果您希望使用，请在 [配额平台](https://quotas.console.aliyun.com/white-list-products/csk/quotas) 提交申请。 |
| Trunk ENI 支持 | 勾选后，会启用 Trunk ENI 模式，可以为每个 Pod 配置固定 IP、独立的虚拟交换机、安全组。 说明 ACK 托管集群 无需申请即可选择 Trunk ENI 选项。如果您希望在 ACK 专有集群 中开启 Trunk ENI，请先在 [配额平台](https://quotas.console.aliyun.com/white-list-products/csk/quotas) 提交申请。 从 Kubernetes 1.31 开始，新建的 ACK 托管集群 会自动启用 Trunk ENI 功能，无需手动进行选择。 |
| 交换机 | 集群中节点所使用的虚拟交换机网段。建议选择来自 3 个及以上不同可用区的交换机，以达到更高集群可用性等级。 |
| Pod 交换机 | Pod 所使用的虚拟交换机网段，可以与节点虚拟交换机网段重合。 |
| 服务网段 | Service 所使用的网段，不能与节点及 Pod 的网段重合。 |
| IPv6 服务网段 | IP 在启用 IPv6 双栈后可配置。 |


## Terway工作模式参考信息

您可参照下方的详细介绍，了解Terway多种模式具体的对比以及工作原理。

### 共享ENI模式与独占ENI模式

为Pod分配IP地址时，Terway有两种模式：共享ENI模式和独占ENI模式。

重要

- 

在Terway v1.11.0及之后的版本中，Terway在单个集群中支持为单个节点池选择共享ENI或独占ENI模式，在创建集群时不再支持勾选。

- 

节点上的主弹性网卡被分配给节点OS，其余弹性网卡会被Terway托管用于配置Pod网络，因此请勿手动配置这些弹性网卡。如果您需要自行管理部分弹性网卡，请参见[为弹性网卡（ENI）配置白名单](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-a-whitelist-for-an-eni.md)。

| 对比项 | 共享 ENI 模式 | 独占 ENI 模式 |  |
| --- | --- | --- | --- |
| Pod IP 地址管理 | ENI 分配方式 | 多个 Pod 共享一个 ENI。 | 每个 Pod 在其节点上独占一个 ENI。 |
| Pod 部署密度 | Pod 部署密度较高。单个节点可支持数百个 Pod。 | Pod 部署密度较低。常用规格的节点只支持个位数的 Pod。 |  |
| 网络架构 |  |  |  |
| 数据链路 | Pod 访问其他 Pod，或作为 Service 后端被访问时，流量都会经过节点的网络协议栈。 | Pod 访问 Service 时，流量仍旧会经过节点操作系统的协议栈。但当 Pod 访问其他 Pod，或作为 Service 后端被访问时，会直接使用挂载的 ENI 绕过节点网络协议栈，以此获得更高的性能。 |  |
| 适用场景 | 常规的 Kubernetes 使用场景。 | 这种模式中网络性能更接近于传统虚拟机，适合对网络性能有较高要求的场景，比如需要高网络吞吐量或低延迟的应用。 |  |
| 网络加速 | 支持 DataPathv2 网络加速，具体信息请参见 [网络加速](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) 。 | 不支持网络加速，但 Pod 独占 ENI 资源，已经提供了极佳的网络性能。 |  |
| NetworkPolicy 支持 | 支持 Kubernetes 原生的 NetworkPolicy ，提供了基于策略的访问控制能力，更多信息请参见 [NetworkPolicy](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) [支持](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) 。 | 不支持 NetworkPolicy 。 |  |
| 节点维度网络配置 | 支持。请参见 [节点维度的网络配置](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-network-settings-for-individual-nodes-in-a-terway-cluster.md) 。 | 支持。请参见 [节点维度的网络配置](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-network-settings-for-individual-nodes-in-a-terway-cluster.md) 。 |  |
| 访问控制 | 开启 Trunk ENI 配置后，支持为 Pod 配置固定 IP、独立的安全组和虚拟交换机，具体信息请参见 [为](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) [Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) [配置固定](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) [IP、独立虚拟交换机与安全组](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-terway.md) 。 | 支持为 Pod 配置固定 IP、独立的安全组和虚拟交换机。 |  |


### 网络加速

使用Terway共享ENI模式时，可以选择开启网络加速模式。选择开启加速模式后，Terway会采取不同于常规共享ENI模式的流量转发路径，以达成更高的性能。Terway目前支持DataPathv2加速模式，请参考下方的说明了解DataPathv2的特点。

重要

- 

DataPathv2是更早的IPvlan+eBPF加速模式的升级版。在Terway V1.8.0及更晚的版本中，创建集群并安装Terway插件时只支持选择DataPathv2加速。

- 

DataPathv2加速模式与IPvlan+eBPF加速模式仅适用于共享ENI节点池，不影响独占ENI节点池。

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

| DataPathv2 特点 | 说明 |
| --- | --- |
| 适用 Terway 版本 | Terway V1.8.0 及后续版本中创建的集群。 |
| 网络架构 |  |
| 加速数据链路 | Pod 访问 Service 时，会使用 eBPF 将 Service 地址解析为 Service 后端某个 Pod 的地址。 Pod 访问不同节点的 Pod 时，会使用 eBPF 绕过双方的节点网络协议栈。 Pod 访问同节点的 Pod 时，不但可以绕过节点协议栈，而且访问流量无需离开节点，直接在节点内部完成转发。 |
| 性能优化 | 简化了 Pod 的网络在宿主机上的转发流程，让 Pod 的网络性能几乎与宿主机的性能无异，延迟相对常规模式降低了 30%。 Service 的网络采用 eBPF 替换原有的 kube-proxy 模式，绕过节点上的 iptables 或者 IPVS 转发，请求延迟大幅降低。网络性能在大规模集群中受到的影响更小，扩展性更优。 Pod 的网络策略（ NetworkPolicy ）也采用 eBPF 替换掉原有的 iptables 的实现，不需要在宿主机上产生大量的 iptables 规则，降低网络策略对网络性能的影响。 |
| 使用方法 | 在创建集群时， 网络插件 选择 Terway 后，勾选 DataPath V2 选项。 |
| 注意事项 | 内核版本≥5.10，推荐使用 Alibaba Cloud Linux 操作系统镜像。 尚未支持安全沙箱运行时。 网络策略（ NetworkPolicy ）使用限制： CIDR 选择器不支持 Pod 网段控制。如果需控制 Pod 访问，需要使用 Pod 标签选择器。 对 CIDR 选择器中的 except 关键字支持不佳，不建议使用 except 关键字。 使用 Egress 类型的 NetworkPolicy 会导致访问集群中 Host 网络类型的 Pod 和集群中节点的 IP 失败。 集群内部访问对外暴露的 LoadBalancer 类型 Service 对应的 SLB 时可能存在回环问题而导致网络不通。更多信息，请参见 [为什么无法访问负载均衡](products/slb/documents/why-am-i-unable-to-access-an-slb-instance.md) 。 IPv6 hairpin 访问不受支持。 NodePort 使用限制： 如果通过 ExternalTrafficPolicy=Local 访问服务时，访问流量可能不通，请修改为 ExternalTrafficPolicy=Cluster 。 使用 ExternalTrafficPolicy=Cluster 情况下，需要对来源地址进行 SNAT，可用端口范围在 32768-65535 之间。 eBPF 加速功能和默认的 Linux 实现有所不同，根据不同业务流量规模需要调整组件配置，请务必参考 [Datapath V2](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/datapath-v2-best-practices.md) [下最佳实践](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/datapath-v2-best-practices.md) 进行监控配置、eBPF map 上限调整。 |


在更早创建的集群中，您可能选择了IPvlan+eBPF加速模式，您可以参照下方的说明了解其特点。

IPvlan+eBPF加速模式

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

| IPvlan+eBPF 特点 | 说明 |
| --- | --- |
| 适用 Terway 版本 | Terway V1.7.0 及更早版本中创建的集群。 |
| 网络架构 |  |
| 加速数据链路 | Pod 访问 Service 时，会使用 eBPF 在 Pod 网络命名空间内将 Service 地址解析为 Service 后端某个 Pod 的地址。 Pod 访问其他 Pod 时，会利用 IPvlan 虚拟网络技术，绕过双方的节点网络协议栈。 |
| 使用方法 | 在创建集群时， 网络插件 选择 Terway 后，勾选 Pod IPvlan 选项。 |
| 注意事项 | 内核版本≥4.19，推荐使用 Alibaba Cloud Linux 操作系统镜像。 尚未支持安全沙箱运行时。 网络策略（ NetworkPolicy ）使用限制： CIDR 选择器不支持 Pod 网段控制。如果需控制 Pod 访问，需要使用 Pod 标签选择器。 对 CIDR 选择器中的 except 关键字支持不佳，不建议使用 except 关键字。 使用 Egress 类型的 NetworkPolicy 会导致访问集群中 Host 网络类型的 Pod 和集群中节点的 IP 失败。 集群内部访问对外暴露的 LoadBalancer 类型 Service 对应的 SLB 时可能存在回环问题而导致网络不通。更多信息，请参见 [为什么无法访问负载均衡](products/slb/documents/why-am-i-unable-to-access-an-slb-instance.md) 。 IPv6 hairpin 访问不受支持。 NodePort 使用限制： 如果通过 ExternalTrafficPolicy=Local 访问服务时，访问流量可能不通，请修改为 ExternalTrafficPolicy=Cluster 。 使用 ExternalTrafficPolicy=Cluster 情况下，需要对来源地址进行 SNAT，可用端口范围在 32768-65535 之间。 eBPF 加速功能和默认的 Linux 实现有所不同，根据不同业务流量规模需要调整组件配置，请务必参考 [Datapath V2](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/datapath-v2-best-practices.md) [下最佳实践](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/datapath-v2-best-practices.md) 进行监控配置、eBPF map 上限调整。 |


### 访问控制

Terway共享ENI模式通过对NetworkPolicy的支持和Trunk ENI选项，允许对集群内的网络流量进行更精细化的管理。Terway独占ENI模式同样支持一部分流量控制能力。

## NetworkPolicy支持

- 

Terway独占ENI节点池不支持NetworkPolicy。

- 

Terway共享ENI节点池支持Kubernetes原生的NetworkPolicy功能，它通过用户定义的规则来控制Pod之间的网络流量。

在创建集群时，如果网络插件选择Terway后，勾选NetworkPolicy 支持选项，即可使集群支持NetworkPolicy。详细信息，请参见[在](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-network-policies.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-network-policies.md)[集群使用网络策略](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-network-policies.md)。

说明

通过控制台管理NetworkPolicy的功能正在公测中，如果您希望使用，请在[配额平台](https://quotas.console.aliyun.com/white-list-products/csk/quotas)提交申请。

## 为Pod配置固定IP、独立虚拟交换机与安全组

- 

Terway独占ENI节点池默认支持为每个Pod配置固定IP、独立的虚拟交换机及安全组，能提供精细化流量管理、流量隔离、网络策略配置和IP管理能力。

- 

Trunk ENI是Terway共享ENI节点池的一种选项。开启Trunk ENI后，可以为每个Pod配置固定IP、独立的虚拟交换机、安全组。

在创建集群时，网络插件选择Terway后，勾选Trunk ENI 支持选项。详细信息，请参见[为](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md)[Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md)[配置固定](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md)[IP](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md)[及独立虚拟交换机、安全组](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md)。

说明

- 

ACK托管集群无需申请即可选择Trunk ENI选项。如果您希望在ACK专有集群中开启Trunk ENI，请先在[配额平台](https://quotas.console.aliyun.com/white-list-products/csk/quotas)提交申请。

- 

从Kubernetes 1.31开始，新建的ACK托管集群会自动启用Trunk ENI功能，无需手动进行选择。

- 

开启Trunk ENI模式后，会安装terway-eniip与terway-controlplane组件。

## 规模约束

Terway 通过调用云产品OpenAPI完成节点网卡、IP 管理的操作。云产品OpenAPI使用限制请参考对应云产品的约束说明。

- 

共享ENI模式：最大并行分配节点数量 500。

- 

独占ENI/TrunkENI模式：最大并行分配Pod数量 100。

上述配额不支持调整。

## 数据面配置声明

Terway 的网络功能高度依赖内核级配置的精确顺序与完整性。任何外部组件对IP Rule、IP Route、eBPF钩子的非协调修改（包括优先级调整、规则覆盖、程序卸载），均可能导致 Pod 网络中断、策略失效、流量劫持异常等严重故障。所有第三方组件集成前必须严格校验，避免冲突。

### TC Filter 规则

| 接口 | 方向 | 程序 | 优先级 | 功能 |
| --- | --- | --- | --- | --- |
| ethx | toContainer | VLAN Untag | 20000 | 去 vlan 标签 |
| ethx | toContainer | cil_from_netdev | 25000 | cilium svc/网络策略 |
| veth | toContainer | cil_to_container | 25000 | cilium svc/网络策略 |
| veth | fromContainer | cil_from_container | 25000 | cilium svc/网络策略 |
| ethx | fromContainer | cil_to_netdev | 25000 | cilium svc/网络策略 |
| ethx | fromContainer | VLAN Tag | 50001 | 添加 vlan 标签 |


### IP Rule 规则

| 方向 | 优先级 | 路由表 |
| --- | --- | --- |
| toContainer | 512 | 1000 + linkIndex （eni index） |
| fromContainer | 512 | 1000 + linkIndex （eni index） |


## 常见问题

### 如何区分Terway是独占ENI模式还是共享ENI模式？

- 

在Terway v1.11.0及以上的版本中，Terway默认使用共享ENI模式，支持通过[为节点池配置独占](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-a-node-pool-level-container-network.md)[ENI](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-a-node-pool-level-container-network.md)[网络模式](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-a-node-pool-level-container-network.md)开启独占ENI模式。

- 

在Terway v1.11.0之前的版本中，创建集群时可以单独选择独占ENI模式或者共享ENI模式。集群创建之后可以使用以下方式区分：

- 

独占ENI模式: 在kube-system命名空间下Terway守护进程DaemonSet的名字是terway-eni。

- 

共享ENI模式: 在kube-system命名空间下Terway守护进程DaemonSet的名字是terway-eniip。

### 已经创建的ACK集群是否支持切换网络插件？

网络插件类型（Terway和Flannel）仅支持在集群创建阶段选择，集群创建后不支持修改。如需切换，请重新创建集群，具体操作，请参见[创建](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。

## 相关文档

- 

关于Terway插件的版本变更记录，请参见[Terway](products/ack/documents/product-overview/terway.md)。

- 

在使用过程中遇到容器网络相关问题，请参见[容器网络](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-container-networks.md)[FAQ](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-container-networks.md)。

- 

在Terway网络场景下，如果您的虚拟交换机（vSwitch）IP资源不足，或者您需要添加新的vSwitch（Pod网段），您需要对vSwitch进行扩容。详细信息，请参见[修改](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/increase-pod-vswitches-in-a-terway-cluster.md)[Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/increase-pod-vswitches-in-a-terway-cluster.md)[虚拟交换机](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/increase-pod-vswitches-in-a-terway-cluster.md)。

[上一篇：Terway网络插件](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/terway.md)[下一篇：为Pod配置固定IP及独立虚拟交换机、安全组](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md)

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
