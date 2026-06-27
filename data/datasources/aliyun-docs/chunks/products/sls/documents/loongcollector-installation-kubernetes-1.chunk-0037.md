### Loongcollector运行模式

| 特性 | DaemonSet 模式 | Sidecar 模式 |
| --- | --- | --- |
| 部署方式 | 每个节点部署 1 个采集容器 | 每个 Pod 部署 1 个采集容器 |
| 资源消耗 | 低（共享节点资源） | 较高（每个 Pod 单独占用） |
| 适用场景 | 节点级统一日志采集 | 特定应用独立隔离采集 |
| 隔离性 | 节点级共享 | Pod 级独立 |

DaemonSet模式原理
在集群的每个Node节点上部署一个 LoongCollector，负责采集该节点上所有容器的日志；特点：运维简单、资源占用少、配置方式灵活；但是隔离性较弱。
在DaemonSet模式中，Kubernetes集群确保每个节点（Node）只运行一个LoongCollector容器，用于采集当前节点内所有容器（Containers）的日志。
当新节点加入集群时，Kubernetes集群会自动在新节点上创建LoongCollector容器；当节点退出集群时，Kubernetes集群会自动销毁当前节点上的LoongCollector容器。通过DaemonSet的自动扩缩容机制以及标识型机器组，无需手动管理LoongCollector实例。
Sidecar模式原理
每个 Pod 中伴随业务容器注入一个 LoongCollector Sidecar容器，并将业务容器的日志目录通过K8s的Volume机制（如emptyDir、hostPath、PVC等）挂载为共享卷。这样，日志文件会同时出现在业务容器和Sidecar容器的挂载路径下，LoongCollector就能直接读取这些日志文件；特点：多租户隔离性好、性能好；但资源占用较多，配置与维护较复杂。
在Sidecar模式中，每个容器组（Pod）运行一个LoongCollector容器，用于采集当前容器组（Pod）所有容器（Containers）的日志。不同Pod的日志采集相互隔离。
为了采集同一Pod中其他容器的日志文件，需要通过共享存储卷的方式来完成，需要将同一份存储卷分别挂载到业务容器和LoongCollector容器。
当一个节点上的 Pod 数据量异常庞大，远超出 Daemonset 的采集性能上限时，Sidecar模式允许我们为LoongCollector分配特定的资源，从而提升其日志采集的性能和稳定性。
在 Serverless 容器中缺乏节点的概念，传统的 Daemonset 部署模式无法应用。此时，SideCar 模式能够有效地与无服务器架构结合，保证日志采集过程的灵活性和适应性。
该文章对您有帮助吗？
反馈
