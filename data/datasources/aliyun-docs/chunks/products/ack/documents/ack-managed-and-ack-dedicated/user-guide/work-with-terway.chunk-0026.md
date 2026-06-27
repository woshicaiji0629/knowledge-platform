### 如何区分Terway是独占ENI模式还是共享ENI模式？
在Terway v1.11.0及以上的版本中，Terway默认使用共享ENI模式，支持通过[为节点池配置独占](configure-a-node-pool-level-container-network.md)[ENI](configure-a-node-pool-level-container-network.md)[网络模式](configure-a-node-pool-level-container-network.md)开启独占ENI模式。
在Terway v1.11.0之前的版本中，创建集群时可以单独选择独占ENI模式或者共享ENI模式。集群创建之后可以使用以下方式区分：
独占ENI模式: 在kube-system命名空间下Terway守护进程DaemonSet的名字是terway-eni。
共享ENI模式: 在kube-system命名空间下Terway守护进程DaemonSet的名字是terway-eniip。
