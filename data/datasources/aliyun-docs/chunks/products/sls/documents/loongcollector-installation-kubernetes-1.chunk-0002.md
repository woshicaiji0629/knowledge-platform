## 选择合适的安装方式
请根据您的集群类型和需求，选择下表中对应的安装方式：

| 安装方式 | 适用场景 |
| --- | --- |
| [ACK](loongcollector-installation-kubernetes-1.md) [集群安装（DaemonSet](loongcollector-installation-kubernetes-1.md) [模式）](loongcollector-installation-kubernetes-1.md) | 采集 同阿里云账号、同地域 下的 [ACK 托管与专有集群](../../ack/documents/ack-managed-and-ack-dedicated/product-overview/what-is-ack.md) 日志。 |
| [自建集群安装（DaemonSet](loongcollector-installation-kubernetes-1.md) [模式）](loongcollector-installation-kubernetes-1.md) | 跨阿里云账号或跨地域 采集阿里云 ACK 集群日志。 采集部署在自建 IDC 机房中的 Kubernetes 集群日志。 采集部署在 其他云服务商上 的 Kubernetes 集群日志。 |
| [Sidecar](loongcollector-installation-kubernetes-1.md) [模式安装](loongcollector-installation-kubernetes-1.md) | 需要对特定业务应用进行日志采集，且有以下需求的场景： 资源隔离 ：避免 DaemonSet 模式影响节点上其他 Pod。 精细化采集 ：为每个应用单独配置采集源、过滤规则、输出目标等。 |
