### 配额与限制
在专有网络下创建的单个路由表可创建的自定义路由数限额是200条。如需更大的配额，请前往[配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=route)提交申请。关于其他资源的配额限制及升配详情，请参见[依赖底层云产品配额限制](../../product-overview/limits.md)。
请合理配置开启自动伸缩的节点池的最大实例数，保证此范围内的节点所依赖的资源和配额充足，例如合理规划VPC网段、交换机等网络资源，以避免节点扩容失败。配置开启自动伸缩的节点池的最大实例数，请参见[配置实例数量](../../ack-managed-and-ack-dedicated/user-guide/auto-scaling-of-nodes.md)。关于ACK的网络规划，请参见[Kubernetes](../../ack-managed-and-ack-dedicated/user-guide/kubernetes-cluster-network-planning.md)[集群网络规划](../../ack-managed-and-ack-dedicated/user-guide/kubernetes-cluster-network-planning.md)。
节点伸缩功能不支持包年包月付费类型的节点。如需新建开启自动伸缩的节点池，请勿选择付费类型为包年包月。如需为已有节点池开启自动伸缩，请确保节点池内没有包年包月付费类型的节点。
