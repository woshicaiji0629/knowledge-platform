# 启用节点自动伸缩以实现节点的自动扩缩容-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/auto-scaling-of-nodes

# 启用节点自动伸缩
当集群的容量规划无法满足应用Pod调度时，您可以使用节点自动伸缩方案实现节点的自动扩缩。节点自动伸缩适用于扩容规模较小（例如开启弹性的节点池数量少于20，或对应节点池中的节点数量少于100），工作负载流量波动平缓，具有周期性或可预测性资源需求，并且单批次资源伸缩即可满足业务需求的场景。
## 阅读前提示
为了让您更好地使用节点自动伸缩功能，建议您在阅读本文档前，已阅读[节点伸缩](overview-of-node-scaling.md)并了解以下内容：
节点自动伸缩的工作原理与功能特性
哪些业务场景下，节点自动伸缩可以满足业务诉求
使用节点自动伸缩前需要了解的注意事项
缩容时，包年包月实例会被移除但不会被释放。为避免额外成本，启用本功能时请使用按量付费实例。
## 注意事项
使用前，请确保[已开通弹性伸缩](https://essnew.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre6.3be916d0JBbHR4#/v3/welcome/)[ESS](https://essnew.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre6.3be916d0JBbHR4#/v3/welcome/)[服务](https://essnew.console.aliyun.com/?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre6.3be916d0JBbHR4#/v3/welcome/)。
参见[注意事项](overview-of-node-scaling.md)了解使用节点伸缩的配额、限制等。
节点自动伸缩对某些调度策略的支持存在一定[已知限制](faq-about-node-auto-scaling.md)，可能导致扩缩容结果不符合预期。如果您的工作负载或组件使用了不支持的调度策略，建议采用以下方案进行调整：
方案一：切换使用[节点即时弹性](instant-elasticity.md)。
方案二：将相关工作负载或组件部署在未开启节点伸缩的节点池中。
以[ack-node-local-dns-admission-controller](../../product-overview/ack-nodelocal-dnscache.md)为例，请将该组件部署在未开启节点伸缩的节点池，并在组件配置中声明如下节点亲和性要求。
nodeAffinity: requiredDuringSchedulingIgnoredDuringExecution: nodeSelectorTerms: - matchExpressions: - key: "k8s.aliyun.com" operator: "NotIn" values: ["true"]
cluster-autoscaler 组件更新或部署时需要占用一定的节点资源；若资源不足，可能导致更新或部署失败，引发扩缩容异常。请确保节点资源充足。
本功能涉及以下流程：
[步骤一：为集群开启节点自动伸缩功能](auto-scaling-of-nodes.md)：先基于集群维度开启节点自动伸缩功能后，节点池设置的自动扩缩容策略才会生效。
[步骤二：配置开启弹性的节点池](auto-scaling-of-nodes.md)：节点自动伸缩功能仅对设置了自动扩缩容的节点池生效，因此，还需要将指定节点池的扩缩容模式配置为自动模式。
## 步骤一：为集群开启节点自动伸缩功能
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
在节点池页面，单击节点伸缩后方的去配置。
首次使用节点自动伸缩功能时，按照页面提示，开通ESS服务并完成授权（如已开通并授权，请跳过）。
ACK托管集群：完成[AliyunCSManagedAutoScalerRole](https://ram.console.aliyun.com/role/authorization?request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22CS%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunCSManagedAutoScalerRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedAutoScalerRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fcs.console.aliyun.com%2F%22%7D)[角色授权](https://ram.console.aliyun.com/role/authorization?request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22CS%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunCSManagedAutoScalerRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedAutoScalerRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fcs.console.aliyun.com%2F%22%7D)。
ACK专有集群：完成KubernetesWorkerRole角色授权和AliyunCSManagedAutoScalerRolePolicy系统策略的授权。
在节点伸缩配置弹窗中，前置检查通过后，单击提示区域中的 RAM 角色链接（如KubernetesWorkerRole-xxxx）即可跳转到访问控制完成授权。
在节点伸缩配置页面，选择节点伸缩方案为自动伸缩，配置伸缩的配置项，然后单击确定。
节点伸缩方案选择后支持切换。如需切换，您可以在此处变更为[节点即时弹性](instant-elasticity.md)，仔细阅读页面提示并按照页面指引完成操作。
| 配置 | 说明 |
| --- | --- |
| 节点池扩容顺序策略 | 随机策略 ：存在多个可扩容节点池时，从中任意选择一个节点池进行扩容。 默认策略 ：存在多个可扩容节点池时，从中选择一个资源浪费最少的节点池进行扩容。 优先级策略 ：存在多个可扩容节点池时，选择优先级高的节点池进行扩容。 节点池优先级通过 节点池扩容优先级 参数定义。 |
| 节点池扩容优先级 | 设置节点池的扩容优先级。仅当 节点池扩容顺序策略 选择为 优先级策略 时生效。 取值范围：1~100 的整数，数字越大，优先级越高。 您需要在参数右侧单击 添加 ，选择已开启了自动弹性的节点池，并为其设置优先级。 若无已开启自动弹性的节点池可选择，您可以暂时忽略该参数，待 [步骤二：配置开启弹性的节点池](auto-scaling-of-nodes.md) 执行后再重新设置节点池优先级。 |
| 弹性灵敏度 | 用于调整系统判断伸缩的间隔时间。默认值为 60s。 |
| 实施弹性伸缩时，弹性组件会基于调度情况自动触发扩容。 重要 ECS 节点：仅当同时满足 缩容阈值 、 缩容触发时延 和 静默时间 三个条件时，弹性组件才有可能执行节点缩容。 GPU 节点：仅当同时满足 GPU 缩容阈值 、 缩容触发时延 和 静默时间 三个条件时，弹性组件才有可能执行 GPU 节点缩容。 |  |
| 允许缩容 | 是否允许进行节点缩容。关闭时，缩容相关配置不生效。请谨慎设置。 |
| 缩容阈值 | 启用 节点自动伸缩 的节点池中，单个节点的请求资源（Request）与单个节点资源容量的比值。 仅当该比值低于配置的阈值时，即节点的 CPU 和内存资源利用率均低于 缩容阈值 时，节点才有可能被缩容。 |
| GPU 缩容阈值 | GPU 实例的缩容阈值。 仅当该比值低于配置的阈值时，即节点的 CPU、内存和 GPU 资源利用率均低于 GPU 缩容阈值 时，GPU 节点才有可能被缩容。 |
| 缩容触发时延 | 从检测到有缩容需求到实际执行缩容操作之间的时间间隔。单位：分钟。默认值：10 分钟。 重要 仅当满足 缩容阈值 配置，且达到 缩容触发时延 后，弹性组件才有可能执行节点缩容。 |
| 静默时间 | 距离最近一次扩容完成后，弹性组件不执行缩容的时间间隔。 在静默时间内，弹性组件不会缩容节点，但仍会判断节点是否可以缩容；超过静默时间后，如果节点满足缩容阈值和缩容触发时延两个条件，弹性组件则会正常执行缩容。例如，当静默时间为 10 分钟，缩容触发时延为 5 分钟时，弹性组件在最近一次扩容后的 10 分钟内不会缩容节点，但会在静默的 10 分钟内判断节点是否符合缩容条件。等待静默时间结束，节点达到缩容阈值且时间超过缩容触发时延规定的 5 分钟时，弹性组件会继续执行缩容。 |
查看高级配置的配置项说明
| 配置项 | 说明 |
| --- | --- |
| Pod 终止超时时间 | 缩容节点时等待节点上 Pod 终止的最长时间。单位：秒。 若超时后 Pod 仍未排水成功，本次缩容过程中 Pod 所在节点将不会被释放。 |
| Pod 最小副本数 | 为由 ReplicationController 或 ReplicaSet 管理的应用设置一个缩容保护阈值。当这类应用的当前实际副本数小于此值时，运行其 Pod 的节点将不会被缩容。 参数仅对由 ReplicationController 或 ReplicaSet 管理的 Pod 生效，对于 StatefulSet 、 DaemonSet 等其他控制器管理的 Pod 不生效。 |
| 开启 DaemonSet Pod 排水 | 开启 DaemonSet Pod 排水后，节点缩容时会驱逐节点上的 DaemonSet Pod。 |
| 跳过有 kube-system 命名空间下 Pod 所在节点 | 开启后，当集群执行节点自动缩容操作时，可以忽略运行在 kube-system 命名空间下的 Pod 所在的节点，确保这些节点不受缩容的影响。 说明 此功能对 DaemonSet Pod 和 Mirror Pod 不生效。 |
## 步骤二：配置开启弹性的节点池
您可以配置已有节点池，将节点扩缩容模式修改为自动模式，也可以新建开启自动弹性的节点池。
具体操作，请参见[创建和管理节点池](create-a-node-pool.md)。主要配置项如下：
| 配置 | 说明 |
| --- | --- |
| 扩缩容模式 | 手动 ：ACK 会根据配置的 期望节点数 调整节点池中的节点数，将节点数始终维持在 期望节点数 。详见 [手动扩缩容节点池](scale-a-node-pool.md) 。 自动 ：当集群的容量规划无法满足应用 Pod 调度时，ACK 会根据配置的最小和最大实例数自动扩缩节点资源。1.24 及以上版本的集群默认启用 节点即时弹性 ；1.24 以下版本的集群默认启用 节点自动伸缩 。详见 [节点伸缩](overview-of-node-scaling.md) 。 重要 开启缩容后，系统将根据资源使用率自动移除节点，可能导致业务中断。建议合理配置伸缩策略，并为业务容器配置优雅下线。 自动缩容时，节点上的本地数据将随节点一同销毁。请勿使用 HostPath 等方式将业务数据写入主机目录。 |
| 实例数量 | 节点池中可伸缩的 最小实例数 和 最大实例数 ，不包含您已有的实例。 说明 最小实例数不为 0 时，伸缩组生效后，将自动创建对应数量的 ECS 实例。 建议设置的最大实例数不要小于当前节点池中的节点数，否则弹性伸缩功能生效后会直接导致节点池的节点缩容。 |
| 实例相关的配置项 | 节点池扩容时，会从配置的 [ECS](../../../../ecs/documents/user-guide/overview-of-instance-families.md) [实例规格族](../../../../ecs/documents/user-guide/overview-of-instance-families.md) 中分配。为提高扩容成功率，请 选择多个可用区下的多种实例规格，避免规格不可用或库存不足 。具体扩容的实例规格由配置的 扩缩容策略 决定。 为确保业务稳定性和资源调度的准确性，请勿在同一个节点池中混合使用 GPU 和非 GPU 实例规格。 可通过以下两种方式配置扩容时使用的实例规格： 具体规格：基于 vCPU、内存、规格族、CPU 架构（实例的 CPU 架构需与 [操作系统镜像架构](overview-of-os-images.md) 一致）等维度指定实例规格。 使用 Terway 时，可在实例规格列表中查看目标实例规格提供的 [节点最大](adjusting-the-number-of-node-pods.md) [Pod](adjusting-the-number-of-node-pods.md) [数](adjusting-the-number-of-node-pods.md) 。 [泛化配置](configure-a-node-pool-using-the-specified-instance-attributes.md) ：根据属性（vCPU、内存等）选择 待使用或需排除的实例规格列表 ，进一步提升扩容成功率。 可参考控制台的弹性强度建议来配置，或在 节点池创建后 [查看节点池弹性强度](check-the-scalability-of-a-node-pool.md) 。 关于 ACK 不支持的实例规格及节点配置建议，请参见 [ECS](select-ecs-instances-to-create-the-master-and-worker-nodes-of-an-ack-cluster.md) [实例规格配置建议](select-ecs-instances-to-create-the-master-and-worker-nodes-of-an-ack-cluster.md) 。 云资源及计费说明： [ECS](../../../../ecs/documents/instance-types.md) [实例](../../../../ecs/documents/instance-types.md) 、 [GPU](https://help.aliyun.com/zh/egs/billing-2) [实例](https://help.aliyun.com/zh/egs/billing-2) |
| 操作系统 | 在开启自动伸缩时，支持选择 Alibaba Cloud Linux、Windows 镜像、Windows Core 镜像。 当所选镜像是 Windows 镜像或 Windows Core 镜像时，系统将自动配置污点（Taints） { effect: 'NoSchedule', key: 'os', value: 'windows' } 。 |
| 节点标签（Labels） | 在集群中添加节点标签（Label）后，会自动添加到弹性伸缩扩容出的节点上。 重要 当节点标签和污点配置映射到节点池 Tag 后，自动伸缩才可识别，且节点池 Tag 存在数量上限。因此，请将开启自动伸缩的节点池配置的 ECS 标签、污点和节点标签的总数控制在 12 个之内。 |
| 扩缩容策略 | 配置节点池在节点扩缩容时如何选择实例。 优先级策略 ：按集群配置的 vSwitch 优先级（vSwitch 顺序由上到下优先级递减）扩缩容。优先级较高的 vSwitch 所在可用区无法创建实例时，自动使用下一优先级 vSwitch。 成本优化策略 ：按 vCPU 单价从低到高扩缩容。 节点池使用 抢占式实例 时，则抢占式实例优先。支持同时配置 按量实例所占比例（% ），当抢占式实例规格因库存等原因无法创建时，自动使用按量付费实例来补充。 均衡分布策略 ：在且仅在多可用区场景下将 ECS 实例均匀分配至多可用区。如果由于库存不足等原因造成可用区分布不平衡，可再次进行均衡操作。 |
| 使用按量实例补充抢占式容量 | 需同时选择付费类型为抢占式实例。 开启后，如果因价格或库存等原因无法创建足够的抢占式实例，ACK 将自动尝试创建按量实例作为补充。 云资源及计费说明： [ECS](../../../../ecs/documents/instance-types.md) [实例](../../../../ecs/documents/instance-types.md) |
| 开启抢占式实例补偿 | 需同时选择付费类型为抢占式实例。 开启后，当收到抢占式实例将被回收的系统消息时（即抢占式实例被回收前 5 分钟），ACK 将尝试扩容新实例进行补偿。 补偿成功：ACK 对旧节点执行排水并从集群中移除。 补偿失败：ACK 不会对旧节点执行排水，到期实例仍然会在 5 分钟后被回收释放。当库存恢复或满足价格条件时，ACK 将自动购买实例以保证期望节点数，详情请参见 [抢占式实例节点池最佳实践](best-practices-for-preemptible-instance-based-node-pools.md) 。 抢占式实例的主动释放可能导致业务异常，为提高补偿成功率，建议同时开启 使用按量实例补充抢占式容量 。 云资源及计费说明： [ECS](../../../../ecs/documents/instance-types.md) [实例](../../../../ecs/documents/instance-types.md) |
| 伸缩模式 | 需开启节点池 自动伸缩 且 扩缩容模式 为 自动 。 标准模式 ：通过创建、释放 ECS 实例的方式进行伸缩。 极速模式 ：通过创建、停机、再启动 ECS 实例的方式进行伸缩，以便在需要再次伸缩时，直接重新启动处于停机状态的实例，提高伸缩速度。 ECS 实例停机时不收取计算资源费用，只收取存储费用（包含本地存储能力的实例规格族除外，例如大数据型、本地 SSD 型等）。关于 ECS 实例停机模式的计费详情及相关注意事项，请参见 [节省停机模式](../../../../ecs/documents/user-guide/economical-mode.md) 。 |
| 污点 （Taints） | 添加污点后，集群将不会将 Pod 调度到该节点上。 |
## 步骤三：（可选）结果验证
完成如上操作后，您便可以使用节点自动伸缩功能。此时，节点池将显示已开始自动伸缩且集群已自动安装cluster-autoscaler组件。
节点池已开启自动伸缩
在节点池页面，节点池列表中将展示已开启自动伸缩的节点池。
已安装cluster-autoscaler组件
在集群管理页左侧导航栏，选择工作负载>无状态。
选择kube-system命名空间，显示cluster-autoscaler组件。
## 常见问题
| 分类 | 二级分类 | 跳转链接 |
| --- | --- | --- |
| 节点自动伸缩 的扩缩容行为 | [已知限制](faq-about-node-auto-scaling.md) |  |
| [扩容行为相关](faq-about-node-auto-scaling.md) | [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件使用哪些调度策略来判断不可调度](faq-about-node-auto-scaling.md) [Pod](faq-about-node-auto-scaling.md) [能否调度到开启了弹性的节点池？](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件可模拟判断的资源有哪些？](faq-about-node-auto-scaling.md) [为什么节点自动伸缩组件无法弹出节点？](faq-about-node-auto-scaling.md) [如果一个伸缩组内配置了多资源类型的实例规格，弹性伸缩时如何计算这个伸缩组的资源呢？](faq-about-node-auto-scaling.md) [弹性伸缩时，如何在多个开启弹性的节点池之间进行选择？](faq-about-node-auto-scaling.md) [开启弹性的节点池如何配置自定义资源？](faq-about-node-auto-scaling.md) [为什么为节点池设置自动扩缩容失败？](faq-about-node-auto-scaling.md) |  |
| [缩容行为相关](faq-about-node-auto-scaling.md) | [为什么](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件无法缩容节点？](faq-about-node-auto-scaling.md) [如何启用或禁用特定](faq-about-node-auto-scaling.md) [DaemonSet](faq-about-node-auto-scaling.md) [的驱逐？](faq-about-node-auto-scaling.md) [什么类型的](faq-about-node-auto-scaling.md) [Pod](faq-about-node-auto-scaling.md) [可以阻止](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件移除节点？](faq-about-node-auto-scaling.md) |  |
| [拓展支持相关](faq-about-node-auto-scaling.md) | [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件是否支持](faq-about-node-auto-scaling.md) [CRD？](faq-about-node-auto-scaling.md) |  |
| 自定义的扩缩容行为 | [通过](faq-about-node-auto-scaling.md) [Pod](faq-about-node-auto-scaling.md) [控制扩缩容行为](faq-about-node-auto-scaling.md) | [如何延迟](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件对不可调度](faq-about-node-auto-scaling.md) [Pod](faq-about-node-auto-scaling.md) [的扩容反应时间？](faq-about-node-auto-scaling.md) |
| [通过节点控制扩缩容行为](faq-about-node-auto-scaling.md) | [如何指定节点不被](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件缩容？](faq-about-node-auto-scaling.md) [如何通过](faq-about-node-auto-scaling.md) [Pod Annotation](faq-about-node-auto-scaling.md) [影响](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件的节点缩容？](faq-about-node-auto-scaling.md) |  |
| cluster-autoscaler 组件 相关 | [如何升级](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件至最新版本？](faq-about-node-auto-scaling.md) [哪些操作会触发](faq-about-node-auto-scaling.md) [cluster-autoscaler](faq-about-node-auto-scaling.md) [组件自动更新？](faq-about-node-auto-scaling.md) [ACK](faq-about-node-auto-scaling.md) [托管集群已经完成了角色授权，但节点伸缩活动仍然无法正常运行？](faq-about-node-auto-scaling.md) |  |
## 相关文档
如果您的集群规模较大（例如弹性节点池中节点数大于100，或弹性节点池数大于20）、对资源交付速度有更高要求、期望灵活实现多实例规格和跨可用区自动伸缩，推荐您使用节点即时弹性功能。具体操作，请参见[启用节点即时弹性](instant-elasticity.md)。
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
