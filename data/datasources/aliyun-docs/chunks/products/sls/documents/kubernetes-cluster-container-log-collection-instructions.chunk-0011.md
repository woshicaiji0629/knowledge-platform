### Sidecar模式原理
每个 Pod 中伴随业务容器注入一个 LoongCollector Sidecar容器，并将业务容器的日志目录通过K8s的Volume机制（如emptyDir、hostPath、PVC等）挂载为共享卷。这样，日志文件会同时出现在业务容器和Sidecar容器的挂载路径下，LoongCollector就能直接读取这些日志文件；特点：多租户隔离性好、性能好；但资源占用较多，配置与维护较复杂。
Sidecar模式工作原理
在Sidecar模式中，每个容器组（Pod）运行一个LoongCollector容器，用于采集当前容器组（Pod）所有容器（Containers）的日志。不同Pod的日志采集相互隔离。
为了采集同一Pod中其他容器的日志文件，需要通过共享存储卷的方式来完成，需要将同一份存储卷分别挂载到业务容器和LoongCollector容器。
当一个节点上的 Pod 数据量异常庞大，远超出 Daemonset 的采集性能上限时，Sidecar模式允许我们为LoongCollector分配特定的资源，从而提升其日志采集的性能和稳定性。
在 Serverless 容器中缺乏节点的概念，传统的 Daemonset 部署模式无法应用。此时，SideCar 模式能够有效地与无服务器架构结合，保证日志采集过程的灵活性和适应性。
