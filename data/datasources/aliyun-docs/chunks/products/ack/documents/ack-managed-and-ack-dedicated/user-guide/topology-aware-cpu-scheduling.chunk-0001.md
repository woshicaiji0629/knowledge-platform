## 工作原理
Kubernetes默认依赖内核的CFS调度器（Completely Fair Scheduler）来实现CPU的负载均衡。该调度器通过公平分配CPU时间片将负载“打散”到各个核心，但可能因忽略了CPU的物理拓扑导致性能敏感型应用的性能抖动。
Kubernetes的[CPU Manager（](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/#static-policy)[static](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/#static-policy)[策略）](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/#static-policy)能够为Pod绑定并独占CPU核心，但仍存在以下局限：
调度器无感知：原生kube-scheduler仅在节点维度做决策，无法感知整个集群的CPU拓扑，不能为Pod在全局范围内寻找最优的物理核心布局。
拓扑不敏感：static策略在节点内分配核心时，不感知NUMA架构，可能导致跨NUMA节点的内存访问，引入额外延迟。
灵活性不足：该策略严格要求Pod的QoS为[Guaranteed](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#guaranteed)，不适用于[Burstable](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#burstable)和[BestEffort](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#burstable)类型的Pod。
为此，ACK基于新版Scheduling Framework提供了增强的CPU拓扑感知调度能力，由ACK kube-scheduler和ack-koordinator协同完成。
节点拓扑上报：ack-koordinator实时感知本地的CPU物理拓扑（如Socket、NUMA、缓存），并将其上报至调度中心。
全局拓扑感知调度：kube-scheduler基于全局拓扑信息，在集群范围内为Pod筛选出当前最优节点，并规划核心分配方案（如在选择最优节点时默认寻找已绑定应用数量最少的核）。该分配方案会作为调度结果写入Pod的Annotation中。
本地绑核执行：Pod调度至目标节点后，ack-koordinator会根据Po
