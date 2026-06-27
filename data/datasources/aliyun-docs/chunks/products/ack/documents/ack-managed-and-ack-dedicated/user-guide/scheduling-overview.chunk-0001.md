## 阅读前提示
本文面向集群运维人员（包括集群资源管理员）和应用开发人员提供集群调度方案。您可以根据您的业务场景和角色选择合适的调度策略。
集群运维人员：关注集群成本和资源最大化利用，并确保集群高可用性和节点间的负载均衡，避免单点故障。
应用开发人员：希望简便地部署和管理应用，并根据性能要求获取所需资源（如CPU、GPU、内存）。
为了更好地使用ACK提供的调度策略，建议您在使用前参见Kubernetes官方文档了解[调度器（Scheduler）](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)、[节点标签（Label）](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#built-in-node-labels)、[驱逐（Evict）](https://kubernetes.io/zh-cn/docs/concepts/scheduling-eviction/node-pressure-eviction/)、[拓扑分布约束（Topology Spread Constraints）](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#pod-topology-spread-constraints)等基本概念。
此外，ACK Scheduler的默认调度策略与社区Kubernetes调度器保持一致，包括[Filter](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#filter)（过滤）和[Score](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#scoring)（评分）两个环节。
