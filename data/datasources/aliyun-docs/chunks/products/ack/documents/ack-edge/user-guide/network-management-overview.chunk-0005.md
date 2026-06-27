### Terway Edge网络模式（Underlay容器网络）
在ACK Edge集群中，Terway Edge版在云端节点池中采用云原生的网络方案，直接基于阿里云VPC中的弹性网卡资源构建容器网络，Pod会通过弹性网卡直接分配VPC中的IP地址。在边缘节点池中则需要指定一个虚拟的Pod网段，容器会从这个虚拟的Pod网段中获取IP地址。具有以下特点：
云端Pod网段与ECS同位于VPC网段中，在同一网络平面。
边缘Pod网段独立于主机网络网段。
容器间通信无需封包，相比于Overlay容器网络效率更高。
需要配置外部网络设备的路由，实现容器网络包的传输。
支持集群外主机、容器、云产品通过Pod IP直接访问集群内容器。
关于Terway Edge网络插件详细信息，请参见[Terway Edge](terway-edge-network-plug-in-introduction.md)[网络插件](terway-edge-network-plug-in-introduction.md)。
