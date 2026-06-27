## 如何在ACK Edge集群部署Ingress Controller
ACK Edge集群在ACK托管集群Pro版的基础上扩展了边缘节点池功能，用于接入边缘节点和IDC机器。有关节点池的详细信息，请参见[节点池](../../ack-managed-and-ack-dedicated/user-guide/node-pool-overview.md)。ACK Edge集群分为以下两个部分。
云端节点池：包含位于集群VPC内的阿里云ECS计算设备等资源。
边缘节点池：集群中可以存在多个边缘节点池，这些节点池主要用于接入边缘节点和IDC机器。
Ingress Controller作为外部请求流量的入口，将对应的HTTP/HTTPS请求转发到后端Service关联的Pod中。您可以通过以下方法来部署Ingress Controller。

| 部署方式 | 特点 | 云边网络类型/流量拓扑 |
| --- | --- | --- |
| 节点池部署 | 在集群中每个有需要的节点池内部署一套 Ingress，仅支持 Nginx Ingress 类型。具体操作，请参见 [部署](install-the-nginx-ingress-controller.md) [Nginx Ingress Controller](install-the-nginx-ingress-controller.md) 。 | 专线：可选是否开启流量拓扑。 公网：必须开启流量拓扑。 |
| 云端部署 | 仅在云端节点池中部署一套 Ingress，支持 Nginx Ingress 和 ALB Ingress 两种类型。具体操作，请参见 [部署](install-the-nginx-ingress-controller.md) [Nginx Ingress Controller](install-the-nginx-ingress-controller.md) 、 [管理](../../ack-managed-and-ack-dedicated/user-guide/manage-the-alb-ingress-controller-1.md) [ALB Ingress Controller](../../ack-managed-and-ack-dedicated/user-guide/manage-the-alb-ingress-controller-1.md) [组件](../../ack-managed-and-ack-dedicated/user-guide/manage-the-alb-ingress-controller-1.md) 。 | 专线，不使用流量拓扑。 |
