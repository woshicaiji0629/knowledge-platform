### 基础设施层可观测性
指容器服务ACK所依赖的底层资源的可观测场景：定位Pod与节点组成的资源池的调用链路，可视化拓扑关系，例如宿主机节点、网络基础组件的性能监控等。

| 解决方案 | 方案介绍 | 适用场景 | 参考文档 |
| --- | --- | --- | --- |
| 架构可视化感知方案 | Kubernetes 集群中的业务是运行在节点组成的资源池上，使得定位 Pod 的调用链路以及拓扑关系非常复杂。如何以可视化的方式监控 Kubernetes 中的负载状态，以及更好地可视化集群中流量的吞吐是非常重要的问题。 阿里云 Kubernetes 监控基于 eBPF 技术，结合阿里云 Prometheus 容器监控，最终整合了指标监控、应用链路追踪、日志分析和事件监控等多种功能，提供 Kubernetes 集群一站式可观测性产品。使 ACK 集群具备网络监控、架构可视化感知等能力。为 IT 开发和运维人员提供无代码侵入、整体的可观测性方案。 | 适用于全部场景。 支持 Kubernetes 集群中 Node、Pod 之间的网络流量监控。 支持 Pod 之间 4 层以上网络流量的监控，以及多协议（如 TCP、HTTP）和 DNS 解析等网络链路监控。 | 更多信息，请参见 [集群拓扑监控](architecture-aware-monitoring.md) 。 |
| 内核层容器监控能力 | 容器服务 Kubernetes 版 ACK（Container Service for Kubernetes） 提供独特的操作系统内核层的容器监控可观测能力 SysOM（System Observer Monitoring）。该能力可以帮助您更好地进行容器化部署和迁移，同时也可以提供更好的容器监控和可观测能力。 | 适用于全部场景。 | 更多信息，请参见 [SysOM](sysom-kernel-level-container-monitoring.md) [内核层容器监控](sysom-kernel-level-container-monitoring.md) 。 |
| 基础设施指标监控方案 | 资源监控是 Kubernetes 中最常见的底层资源监控方式，通过资源监控可以快速查看负载的 CPU、内存、网络等指标的使用率。 | 适用于全部场景。 | 更多信息，请参见 [【停止维护】基础资源监控](monitor-basic-resources.md) 。 |
