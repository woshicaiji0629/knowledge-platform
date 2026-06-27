### 集群升级相关
请务必通过容器服务ACK的集群升级功能升级集群的K8s版本，自行升级K8s版本可能导致ACK集群的稳定性和兼容性问题。详细操作，请参见[升级集群和独立升级集群控制面和节点池](../ack-managed-and-ack-dedicated/user-guide/update-the-kubernetes-version-of-an-ack-cluster.md)。
阿里云容器服务ACK对集群升级提供以下支持：
提供集群K8s新版本的升级功能。
提供K8s新版本升级的前置检查功能，确保集群当前状态支持升级。
提供K8s新版本的版本说明文档，包括相较于前版本的变化。
提示升级到K8s新版本时因资源变化可能会发生的风险。
您在使用集群升级功能时，请遵循以下建议：
在集群升级前运行前置检查，并根据前置检查结果逐一修复集群升级的阻塞点。
详细阅读K8s新版本的版本说明文档，并根据ACK所提示的升级风险确认集群和业务的状态，自行判断升级风险。详细信息，请参见[Kubernetes](../overview-of-kubernetes-versions-supported-by-ack.md)[版本发布概览](../overview-of-kubernetes-versions-supported-by-ack.md)。
由于集群升级不提供回滚功能，请做好充分的升级计划和预后备份。
根据容器服务ACK的版本支持机制，在当前版本的支持周期内及时升级集群K8s版本。更多信息，请参见[版本说明](../ack-managed-and-ack-dedicated/user-guide/support-for-kubernetes-versions.md)。
