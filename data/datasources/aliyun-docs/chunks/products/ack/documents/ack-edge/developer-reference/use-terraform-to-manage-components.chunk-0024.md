| 集群类型 | 组件类型 | 默认安装组件名称 | 组件描述 |
| --- | --- | --- | --- |
| ACK 集群 | 系统组件 | kube-scheduler | 使用 Kube Scheduler 进行集群资源调度。 |
| cloud-controller-manager | 使用 Cloud Controller Manager 为 K8s 应用创建负载均衡，管理节点路由条目。 |  |  |
| kube-apiserver | APIServer 是 K8s 集群的总线和入口网关。 |  |  |
| kube-controller-manager | KCM 是 K8s 集群内部资源的管理器。 |  |  |
| 日志与监控 | alicloud-monitor-controller | 监控应用容器的生命周期和状态变化。 |  |
| metrics-server | Metrics Server 为集群的自动伸缩机制提供应用容器的资源监控指标。 |  |  |
| 存储 | csi-plugin | 使用 csi-plugin 插件实现存储卷生命周期管理（推荐）。 |  |
| csi-provisioner | 使用 csi-provisioner 插件实现存储卷创建和删除（推荐）。 |  |  |
| storage-operator | 使用 storage-operator 插件实现存储运维管理（推荐）。 |  |  |
| 网络 | CoreDNS | Kubernetes 集群域名解析服务器。 |  |
| Gateway API | Gateway API 网关资源模型。 |  |  |
| terway-eniip | Terway 网络插件。 |  |  |
| nginx-ingress-controller（Pro 版默认安装） | 基于 Nginx 流量转发的 Ingress 控制器。 |  |  |
| ACK Serverless 集群 | 系统组件 | kube-scheduler | 使用 Kube Scheduler 进行集群资源调度。 |
| ack-virtual-node | 使用虚拟节点和 ECI 弹性能力。 |  |  |
| cloud-controller-manager | 使用 Cloud Controller Manager 为 K8s 应用创建负载均衡，管理节点路由条目。 |  |  |
| kube-apiserver | APIServer 是 K8s 集群的总线和入口网关。 |  |  |
| kube-controller-manager | KCM 是 K8s 集群内部资源的管理器。 |  |  |
| 网络 | CoreDNS | K8s 集群域名解
