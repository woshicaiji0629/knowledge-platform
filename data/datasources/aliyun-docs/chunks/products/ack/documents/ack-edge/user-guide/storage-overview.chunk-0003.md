## 容器存储能力概览
容器存储接口（CSI）插件是当前Kubernetes社区推荐的插件实现方案。ACK Edge集群的容器存储功能也是基于CSI插件实现。除完全兼容Kubernetes原生的存储卷类型，例如EmptyDir、HostPath、Secret、ConfigMap等之外，根据节点类型和接入方式，CSI插件支持的存储卷如下。
重要
ENS节点使用阿里云NAS和CPFS（注意：不是ENS的NAS）时需要专线和集群VPC打通，可以通过ENS[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)咨询。
使用本地存储的LVM时，需要确保云端节点能够访问存储节点的TCP 1736端口。相关信息，请参见[使用](use-lvm-to-manage-local-storage.md)[LVM](use-lvm-to-manage-local-storage.md)[本地存储](use-lvm-to-manage-local-storage.md)。
