### Flannel网络模式（Overlay容器网络）
在ACK Edge集群中Flannel采用了VXLAN模式，在三层主机网络上构建一层VXLAN容器网络，实现跨主机的Pod互访。
Flannel网络模式中Pod的网段独立于VPC的网段。Pod网段会按照掩码均匀划分给每个集群中的节点，每个节点上的Pod会从节点上划分的网段中分配IP地址。具有以下特点：
Pod网段独立于VPC的虚拟网段。
容器间数据包会通过主机进行VXLAN封包以进行传输。
开箱即用，无需外部网络设备的额外配置。
关于Flannel网络插件详细信息，请参见[Flannel](flannel-network-plugin.md)[网络插件](flannel-network-plugin.md)。
