## 集群删除及节点释放规则
删除集群时，将依次删除集群内的节点池，以完成集群内节点的释放。
对于集群内的边缘节点池：
集群删除后，需要您手动清理节点上的系统组件。相关操作，请参见[移除边缘节点](remove-edge-nodes.md)。
对于集群内的云端节点池：
已开启期望节点数的节点池：节点池内所有按量付费的节点将会被释放，包年包月的节点不会被释放。如需释放包年包月的节点，请登录[ECS](https://ecs.console.aliyun.com/)[控制台](https://ecs.console.aliyun.com/)，将包年包月的节点转换为按量付费的节点，再在[ECS](https://ecs.console.aliyun.com/)[控制台](https://ecs.console.aliyun.com/)释放节点。节点被释放后，节点的系统盘也随之释放。
未开启期望节点数的节点池：节点池内通过手动及自动添加到节点池的已有节点、包年包月的节点不会被释放，其余节点将被释放。
关于如何判断节点池是否开启了期望节点数，请参见[如何判断节点池是否已经开启期望节点数？](../../ack-managed-and-ack-dedicated/user-guide/delete-a-cluster-1.md)。
