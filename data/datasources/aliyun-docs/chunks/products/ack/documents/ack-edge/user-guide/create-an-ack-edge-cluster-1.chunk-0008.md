nd-ack-dedicated/user-guide/control-public-access-to-the-api-server-of-a-cluster.md) 。 ACK Edge 集群 不支持更换和解绑 EIP。 |
| 网络插件 | 设置启用的网络插件和插件配置，支持 Flannel 和 Terway-edge 网络插件。详细信息，请参见 [网络管理](network-management-overview.md) 及 [如何选择网络插件](how-to-choose-a-network-plug-in.md) 。 Flannel ：基于社区的、简单稳定的 Flannel CNI 插件，采用了 VXLAN 模式，为 Overlay 容器网络，功能较为简单。 Terway-edge ：阿里云容器服务自研的网络插件。 在云端将阿里云的弹性网卡分配给容器。 在边缘侧从预先配置的容器网段给容器分配地址，通过主机路由进行转发。 |
| Pod 交换机 | 网络插件选择 Terway-edge 时，您需要为云端节点池内 Pod 分配 IP 的虚拟交换机。每个 Pod 虚拟交换机分别对应一个 Worker 节点的虚拟交换机，Pod 虚拟交换机和 Worker 节点的虚拟交换机的可用区需保持一致。 |
| 边缘 容器网段 | 容器地址从容器网段中分配。 网络插件选择为 Flannel 时，集群云端、边缘的容器从这个网段中分配地址。 网络插件选择为 Terway-edge 时，集群的边缘侧容器从这个网段中分配地址。 |
| 节点 Pod 数量 | 定义单个节点上可容纳的最大 Pod 数量。 |
| 服务网段 | 即 Service CIDR，为集群内部 Service 分配 IP 地址的地址池。此网段不能与 VPC 及 VPC 内已有集群使用的网段重复，且不能与 容器网段 重复。 |
