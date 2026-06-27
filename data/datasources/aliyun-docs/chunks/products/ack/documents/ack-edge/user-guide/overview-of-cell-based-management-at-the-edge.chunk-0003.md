## 边缘节点池
边缘节点池作为边缘节点分组的抽象，[创建边缘节点池](edge-node-pool-management.md)时您需要预先明确该节点池内节点的一些[基本属性](edge-node-pool-management.md)，如云边网络连接、节点间网络互通、Pod网络模式等。另外，我们也建议您根据其他属性，如CPU/GPU、地域、AMD64/Arm64等，将边缘节点分散到多个边缘节点池中管理。
在创建完成后，您可以通过[编辑边缘节点池](edge-node-pool-management.md)批量管理节点池内节点的标签和污点。当所有的边缘节点都移除集群后，您可以删除该边缘节点池。
当多个节点池都需要部署同一套应用时，您可以[使用应用集](node-pool-yurtappset-management.md)（YurtAppSet）将应用便捷地部署到多个节点池中。YurtAppSet提供了灵活的响应机制以感知节点池标签的变化，统一管理多个节点池的工作负载配置，如实例数量和软件版本等。
原生Kubernetes Service的后端可以分布在集群中任意节点。因此，当两个边缘节点池间网络不互通，跨越不同边缘节点池的Service流量，大概率会出现访问不可达或者访问效率低下的问题。[Service](configure-a-service-topology.md)[流量拓扑](configure-a-service-topology.md)支持将Service流量限制在同一个边缘节点池（或边缘节点）上，从而避免边缘场景下跨网域访问导致的Service网络不通的问题。
该文章对您有帮助吗？
反馈
