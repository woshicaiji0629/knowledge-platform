）数量。虽然节点支持的最大Pod数跟CPU和内存并不是直接的线性关系，但通常较小规格的ECS实例支持的ENI数量较少，单节点的Pod限额也较小。
当节点Pod数量达到上限时，新Pod将调度失败，影响服务性能。您可以通过扩容节点池以增加更多可用的节点、升配节点以提升单节点最大Pod数等方式增加可使用的Pod数，请参见[调整可使用的节点](adjusting-the-number-of-node-pods.md)[Pod](adjusting-the-number-of-node-pods.md)[数量](adjusting-the-number-of-node-pods.md)。
购买后查看节点可用的CPU和内存资源，为什么比购买时的实例规格定义的少？
ACK需要占用一定的节点资源来为kube组件和system进程预留资源，从而保证OS内核和系统服务、Kubernetes守护进程的正常运行。这会导致节点的资源总数（Capacity）与可分配的资源数（Allocatable）之间存在差异。详细信息，请参见[节点资源预留策略](resource-reservation-policy.md)。
