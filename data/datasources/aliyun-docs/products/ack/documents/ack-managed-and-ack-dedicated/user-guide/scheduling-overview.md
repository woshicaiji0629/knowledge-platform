# ACK集群支持的调度Scheduling, 策略-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/scheduling-overview

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

# 调度概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在Kubernetes集群中，调度（Scheduling）指调度器组件（kube-scheduler）根据资源规划将Pod分配到最合适的节点上，以实现应用高可用、提高集群资源利用率等。ACK针对不同工作负载提供了更灵活、更丰富的调度策略，包括任务调度、拓扑感知调度、QoS感知调度、重调度等。

## 阅读前提示

- 

本文面向集群运维人员（包括集群资源管理员）和应用开发人员提供集群调度方案。您可以根据您的业务场景和角色选择合适的调度策略。

- 

集群运维人员：关注集群成本和资源最大化利用，并确保集群高可用性和节点间的负载均衡，避免单点故障。

- 

应用开发人员：希望简便地部署和管理应用，并根据性能要求获取所需资源（如CPU、GPU、内存）。

- 

为了更好地使用ACK提供的调度策略，建议您在使用前参见Kubernetes官方文档了解[调度器（Scheduler）](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)、[节点标签（Label）](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#built-in-node-labels)、[驱逐（Evict）](https://kubernetes.io/zh-cn/docs/concepts/scheduling-eviction/node-pressure-eviction/)、[拓扑分布约束（Topology Spread Constraints）](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#pod-topology-spread-constraints)等基本概念。

此外，ACK Scheduler的默认调度策略与社区Kubernetes调度器保持一致，包括[Filter](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#filter)（过滤）和[Score](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#scoring)（评分）两个环节。

## Kubernetes原生调度策略

Kubernetes原生的调度策略可以分为节点调度策略和Pod间（Inter-Pod）调度策略。

- 

节点调度策略：聚焦于节点的特性和资源情况，让Pod能够被调度到符合其需求的节点上。

- 

Pod间调度策略：聚焦于如何控制Pod之间的分布和定位，以优化Pod的总体布局，保障应用的高可用性。

- 

- 

- 

- 

| 策略 | 策略说明 | 适用场景 |
| --- | --- | --- |
| [nodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) | 使用标签（Label）的键值对对节点进行打标，然后在 Pod 配置中通过节点选择器（NodeSelector）将 Pod 调度至带有相应 Label 的节点上。 例如，可使用 NodeSelector [调度应用至指定节点](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/schedule-pods-to-specific-nodes.md) 或 [调度应用至指定节点池](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/schedule-an-application-pod-to-a-specific-node-pool.md) 。 | 基础的节点选择功能，但无法支持更复杂的调度功能，例如软性调度规则等。 |
| [nodeAffinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity) | 相较于 NodeSelector 更灵活、更精细的 Pod 的调度策略，支持配置硬性调度规则（ requiredDuringSchedulingIgnoredDuringExecution ）和软性的调度规则（ preferredDuringSchedulingIgnoredDuringExecution ）。 | 可根据节点特性（例如地区、机型、硬件配置等）指定 Pod 运行位置；反亲和性可实现跨节点分散部署。 |
| [污点和容忍](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) | 污点（Taint）主要由键（key）、值（value）和效果（effect）组成，常见的效果包括 NoSchedule 、 PreferNoSchedule 和 NoExecute 。节点打上污点后，只有声明了与节点污点匹配的容忍（Tolerations）的 Pod 才允许调度到此节点上。 | 为特定应用保留专用节点资源，例如为 AI/ML 工作负载预留 GPU 节点。 ACK 还支持为节点池添加污点或标签，使得某些应用可以调度到指定节点池，请参见 [创建和管理节点池](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-node-pool.md) 。 基于污点和容忍的 Pod 驱逐，例如为不健康的节点添加 NoExecute 的污点。 |
| [podAffinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) [和](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) [podAntiAffinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) | 通过 Pod 标签指定 Pod 是否应该被调度到某些节点上，支持配置硬性调度规则（ requiredDuringSchedulingIgnoredDuringExecution ）和软性调度规则（ preferredDuringSchedulingIgnoredDuringExecution ）。 | 让协同 Pod 调度到相同或临近的节点，从而减少网络延迟、提高通信效率。 将关键应用分散在不同节点或故障域上。 |


## ACK提供的调度策略

如果Kubernetes原生调度策略无法满足您更为复杂的业务需求，例如指定不同实例资源的顺序扩容及逆序缩容、 基于节点实际资源使用情况的负载感知调度等，您可以参照下文选择ACK提供的调度策略。

### 配置调度资源优先级

- 

适用角色：集群运维人员

- 

说明：如果集群中存在不同种类的实例资源，例如ECS和ECI，且付费类型不同（包年包月、按量付费和抢占实例等），推荐配置调度资源优先级，指定应用实例Pod被调度到不同类型节点资源的顺序，并实现逆序缩容。

- 

- 

- 

| 策略 | 策略说明 | 典型场景 | 参考文档 |
| --- | --- | --- | --- |
| 自定义弹性资源优先级调度 | 支持在应用发布或扩容过程中自定义 ResourcePolicy ，设置应用 Pod 被调度到不同类型节点资源的顺序，例如先调度到包年包月 ECS，再调度到按量计费 ECS，最后调度到 ECI。 应用缩容时也支持逆序缩容，例如优先删除 ECI Pod，然后删除按量计费 ECS 上的 Pod，最后再删除包年包月 ECS 上的 Pod。 | 指定优先使用或避免使用的节点，平衡集群中节点的资源利用率。 应用对节点性能要求高时，优先让应用 Pod 调度到较高性能的节点上。 应用对节点性能要求不高时，优先让应用 Pod 调度到抢占式实例或有剩余计算资源的节点，降低资源使用成本。 | [自定义弹性资源优先级调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-priority-based-resource-scheduling.md) |


### 任务调度

- 

适用角色：集群运维人员

- 

说明：调度器能够根据预设的规则决定将Pod放置在哪个节点上运行，但并不适用于批处理任务下Pod的协同调度。在此基础上，ACK为批量计算任务支持了Gang Scheduling、Capacity Scheduling能力。

- 

- 

- 

| 策略 | 策略说明 | 典型场景 | 参考文档 |
| --- | --- | --- | --- |
| Gang Scheduling | 相关 Pod 要么全部被调度，要么都不被调度，防止因部分进程的异常而导致整个关联进程组阻塞的问题。 | 批处理作业：作业中有多个相互依赖的任务组，需要同时处理。 分布式计算：例如机器学习训练任务或其他需要严格协调运行的分布式应用。 高性能计算：作业可能需要整套的资源同时可用才能开始执行。 | [使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-gang-scheduling.md) [Gang scheduling](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-gang-scheduling.md) |
| Capacity Scheduling | 为特定的命名空间或用户组预留一定的资源容量，并在集群资源紧张时，通过资源共享提升整体资源利用率。 | 多租户场景下，不同租户使用资源的周期和方式不同，造成集群的整体资源利用率较低，期望在固定资源分配的基础上允许资源的借用和回收。 | [使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-capacity-scheduling.md) [Capacity Scheduling](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-capacity-scheduling.md) |


### 拓扑感知调度

- 

适用角色：集群运维人员

- 

说明：在机器学习和大数据分析类作业中，Pod间通常有较大的网络通信需求。默认情况下，调度器会将Pod均匀打散在集群中，导致作业时间变长。原生的节点或Pod亲和调度方式无法在多个不同的拓扑域上进行重试，且节点上仅有可用区级别的标签。

- 

- 

| 策略说明 | 典型场景 | 参考文档 |
| --- | --- | --- |
| 调度器为作业添加 Gang 调度标识，限制 Pod 必须同时获得所需的资源，并结合拓扑感知调度能力实现 Pod，直到找到一个能够满足整个作业拓扑域的功能。 您还可以使用节点池的 [部署集](products/ecs/documents/user-guide/overview-43.md) 能力，将 Pod 调度到属于同一低延时部署集的 ECS 实例中，进一步提高作业性能。 | 机器学习或大数据分析类作业中，Pod 与 Pod 间通常有较大的网络通信需求。期望能让作业在多个拓扑域上重试，直至找到能够提供足够资源的拓扑域，减少作业的执行时间。 | [拓扑感知调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/topology-aware-scheduling.md) [节点池部署集最佳实践](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/best-practices-for-associating-deployment-sets-with-node-pools.md) |


### 负载感知调度

- 

适用角色：集群运维人员、应用开发人员

- 

说明：原生调度策略下，调度器主要基于资源的分配情况进行调度，即通过检查Pod的资源Requests与节点上尚未被分配的资源来决定Pod的调度。但节点的利用率会随着时间、集群环境、工作负载的流量或请求等动态变化，原生调度器并不能感知节点实际的资源负载情况。

| 策略说明 | 典型场景 | 参考文档 |
| --- | --- | --- |
| 通过参考节点负载的历史统计并对新调度 Pod 进行预估，ACK 调度器可以感知节点真实使用的资源量，将 Pod 优先调度到负载较低的节点，实现节点负载均衡的目标，避免出现因单个节点负载过高而导致的应用程序或节点故障。 | 对请求压力或访问延迟等指标有明确的要求、对资源质量较为敏感的延时敏感型应用。 | [使用负载感知调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-load-aware-pod-scheduling.md) |


推荐搭配[使用负载热点打散重调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-load-aware-hotspot-descheduling.md)使用，防止Pod调度完成后集群再次出现负载极不均衡的情况。

### QoS感知调度

- 

适用角色：集群运维人员、应用开发人员

- 

说明：为Pod配置特定的QoS（Quality of Service）类，包括[Guaranteed](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#guaranteed)、[Burstable](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#burstable)、[BestEffort](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#besteffort)。节点资源不足时，kubelet可以根据QoS类决定Pod的驱逐顺序。ACK提供差异化的SLO（Service Level Objectives）功能，以提升延迟敏感型应用的性能表现和服务质量，同时尽可能保证低优任务的资源使用。

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

| 策略 | 策略说明 | 典型场景 | 参考文档 |
| --- | --- | --- | --- |
| CPU Burst | 受 CPU Limit 机制的约束，操作系统会按照一定的时间周期约束资源使用，导致容器可能遭遇资源分配的限流，即 CPU Throttled。CPU Burst 功能可以让容器在空闲时积累一些 CPU 时间片，用于满足突发时的资源需求，以提升容器性能、降低延迟指标，进而提升应用的服务质量。 | 容器应用在启动加载阶段 CPU 资源消耗较高，但在加载完成后的日常状态下其 CPU 用量相对正常的场景。 CPU 资源需求可能会突然增长，需要快速应对突增的业务流量，例如电商、在线游戏等 Web 服务和应用。 | [启用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cpu-burst.md) [CPU Burst](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cpu-burst.md) [性能优化策略](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cpu-burst.md) |
| CPU 拓扑感知调度 | 针对性能敏感型应用，将 Pod 固定在节点上的 CPU 核心运行，缓解因 CPU 上下文切换、跨 NUMA 访存导致的应用性能下降问题。 | 应用尚未完成对云原生场景的适配，例如在设置线程数量时未考虑容器规格（而是整机物理核数量），导致应用出现性能下降问题。 应用运行在神龙裸金属（Intel、AMD）等多核机器上，且出现大量因跨 NUMA 访存带来的应用性能下降问题。 应用对 CPU 上下文切换十分敏感，无法承受因此带来的性能抖动。 | [启用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/topology-aware-cpu-scheduling.md) [CPU](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/topology-aware-cpu-scheduling.md) [拓扑感知调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/topology-aware-cpu-scheduling.md) |
| GPU 拓扑感知调度 | 集群中同时部署了多张 GPU 卡时，多个 GPU 密集型工作负载的 Pod 同时运行时，Pod 之间可能会争抢节点的 GPU 资源，导致 Pod 在不同的 GPU 之间（甚至是 NUMA Node 之间）频繁地切换，影响程序性能。GPU 拓扑感知调度能够将工作负载适当地分配到不同 GPU 卡上，减少跨越 NUMA 节点的内存访问，提升应用性能和响应速度。 | 需要在大规模分布式计算中实现高效的数据传输和处理，例如高性能计算。 机器学习和深度学习，需要大量 GPU 资源进行学习和训练，并合理将训练任务分配到各个 GPU。 图形渲染和游戏开发，需要合理地分配渲染任务至不同的 GPU。 | [GPU](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/overview-of-topology-aware-gpu-scheduling.md) [拓扑感知调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/overview-of-topology-aware-gpu-scheduling.md) [启用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/enable-numa-topology-aware-scheduling.md) [NUMA](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/enable-numa-topology-aware-scheduling.md) [拓扑感知调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/enable-numa-topology-aware-scheduling.md) |
| 动态资源超卖 | 将集群中已分配但未使用的资源量化并提供给低优先级任务使用，以实现对集群资源的超卖。需要结合以下单机 QoS 策略使用，以避免应用间的性能干扰。 弹性资源限制：在整机资源用量安全水位下，控制低优先级 Pod 可使用的 CPU 资源量，保障节点内容器稳定运行。 容器 CPU QoS：基于容器的 QoS 等级，优先保障高优先级应用的 CPU 性能。 容器内存 QoS：基于容器的 QoS 等级，优先保障高优先级应用 Pod 的内存性能，延迟其触发整机内存回收的时间。 容器 L3 Cache 及内存带宽隔离：基于容器的 QoS 等级，优先保障高优先级应用 L3 cache 和 MBA 内存带宽等资源的使用。 | 需要通过混部的方式提升集群资源利用率。典型的在离线混部的场景包括机器学习训练和推理、大数据批处理作业和数据分析、在线服务和离线备份服务等。 | [启用动态资源超卖](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/dynamic-resource-overcommitment.md) [启用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/elastic-resource-limit.md) [CPU](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/elastic-resource-limit.md) [资源弹性限制能力](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/elastic-resource-limit.md) [启用容器](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cpu-qos.md) [CPU QoS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cpu-qos.md) [启用容器内存](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/memory-qos-for-containers.md) [QoS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/memory-qos-for-containers.md) [启用容器](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/resource-isolation-based-on-the-l3-cache-and-mba.md) [L3 Cache](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/resource-isolation-based-on-the-l3-cache-and-mba.md) [及内存带宽隔离](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/resource-isolation-based-on-the-l3-cache-and-mba.md) [在离线混部最佳实践](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/overview-of-the-colocation-of-different-types-of-workloads.md) |
| 动态修改 Pod 资源参数 | 在 [Kubernetes 1.27](https://kubernetes.io/blog/2023/05/12/in-place-pod-resize-alpha/) [及更早版本中](https://kubernetes.io/blog/2023/05/12/in-place-pod-resize-alpha/) ，如需在 Pod 运行中临时修改容器参数，只能更新 PodSpec 后重新提交，这种方式会触发 Pod 删除重建。ACK 支持在不重启 Pod 的情况下，修改 CPU、内存、磁盘 IO 等单机隔离参数。 | 仅适用于 Pod 资源（CPU、内存资源）的临时性调整。 | [动态修改](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/dynamically-modify-the-resource-parameters-of-a-pod.md) [Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/dynamically-modify-the-resource-parameters-of-a-pod.md) [的资源参数](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/dynamically-modify-the-resource-parameters-of-a-pod.md) |


### 重调度

- 

适用角色：集群运维人员、应用开发人员

- 

说明：集群的状态会不断变化，出于某些原因，您可能需要将运行中的Pod移动到其他节点，即将Pod重调度到其他节点。

- 

- 

- 

- 

- 

- 

| 策略 | 策略说明 | 典型场景 | 参考文档 |
| --- | --- | --- | --- |
| 重调度 | 在集群利用率不均而产生热点节点、节点属性变化导致存量 Pod 调度规则不匹配等场景下，您可能需要将部署在某个节点上调度不合理的 Pod 重新调度到另一个节点，确保 Pod 在最佳节点上运行，从而保障集群的高可用性和工作负载的高效运行。 | 集群的工作负载分布不均，造成某些节点过载，例如在离线混部场景下不同应用被调度到同一节点上。 集群的总体资源利用率较低，期望下线部分节点以节约成本。 集群存在大量资源碎片，导致集群资源总量充足，但单节点上资源不足。 节点新增或移除了污点或标签。 | [重调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/overview-of-descheduling.md) [启用重调度功能](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/enable-descheduling.md) |
| 负载热点打散重调度 | 将负载感知调度和热点打散重调度结合使用，不仅能够实时感知集群内节点负载的变化，还能自动优化超过负载水位安全阈值的节点，防止出现负载极端不均衡的情况。 | [使用负载热点打散重调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-load-aware-hotspot-descheduling.md) |  |


## 相关计费

使用ACK提供的调度功能时，除涉及的集群管理费用、相关云产品资源产生的[计费](products/ack/documents/ack-managed-and-ack-dedicated/product-overview/ack-pro-cluster-billing.md)外，调度组件还会产生如下费用。

- 

ACK默认调度器由kube-scheduler组件提供，为控制面组件，安装和使用均为免费。

- 

ACK的资源调度优化能力和重调度能力基于ack-koordinator组件实现。ack-koordinator组件本身的安装和使用是免费的，但在部分场景中可能产生额外的费用。更多信息，请参见[ack-koordinator（ack-slo-manager）](products/ack/documents/product-overview/ack-koordinator-fka-ack-slo-manager.md)。

## 常见问题

如在使用调度功能时遇到问题，可参见[调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/virtual-switch-remaining-ip-state-aware-scheduling.md)[FAQ](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/virtual-switch-remaining-ip-state-aware-scheduling.md)进行排查。

## 相关文档

- 

kube-scheduler和ack-koordinator的组件介绍与变更记录，请参见[kube-scheduler](products/ack/documents/product-overview/kube-scheduler.md)、[ack-koordinator（ack-slo-manager）](products/ack/documents/product-overview/ack-koordinator-fka-ack-slo-manager.md)。

- 

如需自定义kube-scheduler的行为，请参见[自定义调度器参数](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-the-scheduler-parameters.md)。

- 

调度场景下的最佳实践，例如在离线混部最佳实践，请参见[调度功能最佳实践](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/best-practices-for-scheduling-features.md)。

- 

您可以搭配启用成本洞察功能，了解集群资源使用量及成本分布，获取成本节约建议，从而提升集群资源利用率。更多信息，请参见[成本洞察](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cost-analysis-overview.md)。

- 

如需实现GPU的共享调度、显存隔离等能力，请参见[共享](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cgpu-overview.md)[GPU](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cgpu-overview.md)[调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cgpu-overview.md)。

- 

关于虚拟节点的调度方案，请参见[调度](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-and-introduction-of-virtual-node-scheduling-scheme-ack.md)[Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-and-introduction-of-virtual-node-scheduling-scheme-ack.md)[至虚拟节点](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-and-introduction-of-virtual-node-scheduling-scheme-ack.md)。

[上一篇：GPU FAQ](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/gpu-faq.md)[下一篇：调度组件](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/scheduling-components.md)

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
