### 核心组件

| 组件名称 | 组件类型 | 描述 |
| --- | --- | --- |
| [Kube Scheduler](../../product-overview/kube-scheduler.md) | 系统组件 | 控制面组件，负责结合节点资源使用情况和 Pod 的调度要求将 Pod 调度到集群的合适节点上。 |
| [Cloud Controller Manager](../../product-overview/cloud-controller-manager.md) | 系统组件 | 在 Kubernetes 集群中提供管理负载均衡实现跨节点通信的功能。提供 Kubernetes 与阿里云网络产品的对接能力，例如 CLB、NLB、VPC 等。 |
| [Kube API Server](../../product-overview/kube-api-server.md) | 系统组件 | Kubernetes 集群的总线和入口网关。 |
| [Kube Controller Manager](../../product-overview/kube-controller-manager.md) | 系统组件 | Kubernetes 集群内部资源的管理器。 |
| [ACK Virtual Node](../../product-overview/ack-virtual-node.md) | 可选组件 | 基于社区开源项目 Virtual Kubelet，扩展了对 Aliyun Provider 的支持，并做了大量优化，实现 Kubernetes 与 ACS 和 ECI 的无缝连接。 |
