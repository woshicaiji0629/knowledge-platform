### 示例一：使用ACK Edge集群管理地域分散的应用
准备环境
选择一个地域作为中心地域，在该地域下[创建](../user-guide/create-an-ack-edge-cluster-1.md)[ACK Edge](../user-guide/create-an-ack-edge-cluster-1.md)[集群](../user-guide/create-an-ack-edge-cluster-1.md)。
已安装OpenKruise组件。具体操作，请参见[组件管理](../user-guide/component-overview.md)。
为每个地域分别[创建边缘节点池](../user-guide/edge-node-pool-management.md)， 并将ECS实例接入到对应的节点池中。
操作步骤
您可以通过原生的DaemonSet或者OpenKruise的DaemonSet两种方式部署并管理业务。
