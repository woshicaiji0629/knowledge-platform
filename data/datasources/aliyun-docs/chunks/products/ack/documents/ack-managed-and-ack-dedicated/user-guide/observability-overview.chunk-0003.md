### 容器性能层可观测性
指基于容器服务ACK构建系统的容器抽象层的可观测场景，包括集群的性能、事件等监控，容器的性能，以及容器组件等监控。
集群、容器的性能指标监控

| 解决方案 | 方案介绍 | 适用场景 | 参考文档 |
| --- | --- | --- | --- |
| 云监控容器服务 ACK 的监控方案 | 容器服务 Kubernetes 版 ACK（Container Service for Kubernetes） 提供集群、容器的部分性能指标监控，并集成在容器服务控制台中展示。 | 适用于部分场景。 定制化提供基础的容器层性能指标和可观测能力。 | 更多信息，请参见 [【停止维护】基础资源监控](monitor-basic-resources.md) 。 |
| 阿里云托管版 Prometheus 的监控方案 | Prometheus 也是社区官方的容器场景云原生指标可观测方案。阿里云 Prometheus 监控全面对接开源 Prometheus 生态，支持类型丰富的组件监控，提供多种开箱即用的预置监控大盘，且提供全面托管的 Prometheus 服务。借助阿里云 Prometheus 监控，您无需自行搭建 Prometheus 监控系统，因此无需关心底层数据存储、数据展示、系统运维等问题。推荐使用阿里云托管版 Prometheus（ARMS Prometheus）云产品。 | 适用于所有场景，包括微服务（ServiceMesh）场景、集群自身组件指标，以及定制监控能力等高级可观测能力。 | 更多信息，请参见 [使用阿里云](use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) [Prometheus](use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) [监控](use-managed-service-for-prometheus-to-monitor-an-ack-cluster.md) 。 |
| 开源 Prometheus 监控方案 | 阿里云容器服务在应用市场中提供了开源 Prometheus 监控方案的集成。 | 适用于所有场景，包括微服务（ServiceMesh）场景、集群自身组件指标以及定制监控能力等高级可观测能力。 | 更多信息，请参见 [开源](use-open-source-prometheus-to-monitor-an-ack-cluster.md) [Prometheus](use-open-source-prometheus-to-monitor-an-ack-cluster.md) [监控](use-open-source-prometheus-to-monitor-an-ack-cluster.md) 。 |
