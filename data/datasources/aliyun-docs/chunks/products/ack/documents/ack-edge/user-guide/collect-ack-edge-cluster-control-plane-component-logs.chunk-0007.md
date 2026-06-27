| 组件 | Logstore | 是否默认收集 | 说明 |
| --- | --- | --- | --- |
| [kube-apiserver](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/) | apiserver | 是 | kube-apiserver 组件是暴露 Kubernetes API 接口的控制层面的组件。 |
| [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/) | kcm | 是 | kube-controller-manager 组件是 Kubernetes 集群内部的管理控制中心，内嵌了 Kubernetes 发布版本中核心的控制链路。 |
| [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/) | scheduler | 是 | kube-scheduler 组件是 Kubernetes 集群的默认调度器。 |
| [Cloud Controller Manager](../../product-overview/cloud-controller-manager.md) | ccm | 是 | Cloud Controller Manager 提供 Kubernetes 与阿里云基础产品的对接能力，例如 CLB（原 SLB）、VPC 等，功能包括管理负载均衡、跨节点通信等。 |
| controlplane-events | controlplane-events | 是 | controlplane-events 组件支持投递集群控制面组件的运维事件，比如 OOM killed 事件等。 |
| [ALB Ingress Controller](../../product-overview/alb-ingress-controller.md) | alb | 是 | ALB Ingress 基于阿里云应用型负载均衡 ALB 服务，为集群中的 Service 提供统一的入口。 |
| [cluster-autoscaler](../../ack-managed-and-ack-dedicated/user-guide/auto-scaling-of-nodes.md) | cluster-autoscaler | 否 | cluster-autoscaler 为 ACK 节点自动伸
