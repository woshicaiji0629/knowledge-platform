# 创建ACK专有集群
在ACK专有集群中，您需要创建至少3个Master节点以保证高可用性，以及若干Worker节点，以对集群基础设施进行更细粒度的控制，但需要自行规划、维护、升级集群。本文介绍如何通过控制台、API、Terraform、SDK以及CLI等方式创建ACK专有集群。
重要
容器服务 Kubernetes 版已于2024年08月21日起停止ACK专有集群的创建。推荐您在生产环境中使用具有更高可靠性、安全性和调度效率的ACK托管集群Pro版。
如需创建ACK托管集群Pro版，请参见[创建](create-an-ack-managed-cluster-2.md)[ACK](create-an-ack-managed-cluster-2.md)[托管集群](create-an-ack-managed-cluster-2.md)。
如需将ACK专有集群迁移至ACK托管集群Pro版，请参见[热迁移](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[专有集群至](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[托管集群](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[Pro](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[版](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)。
