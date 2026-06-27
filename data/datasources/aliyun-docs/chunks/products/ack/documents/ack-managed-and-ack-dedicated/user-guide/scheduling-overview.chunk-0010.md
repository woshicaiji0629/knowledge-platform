### QoS感知调度
适用角色：集群运维人员、应用开发人员
说明：为Pod配置特定的QoS（Quality of Service）类，包括[Guaranteed](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#guaranteed)、[Burstable](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#burstable)、[BestEffort](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#besteffort)。节点资源不足时，kubelet可以根据QoS类决定Pod的驱逐顺序。ACK提供差异化的SLO（Service Level Objectives）功能，以提升延迟敏感型应用的性能表现和服务质量，同时尽可能保证低优任务的资源使用。
