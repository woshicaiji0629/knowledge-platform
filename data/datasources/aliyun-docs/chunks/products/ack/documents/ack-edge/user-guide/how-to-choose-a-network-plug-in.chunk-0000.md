## 插件功能对比
ACK Edge集群支持以下两种容器网络插件：
Flannel：采用了VXLAN模式，是一种Overlay的容器网络插件。详细信息，请参见[Flannel](flannel-network-plugin.md)[网络插件](flannel-network-plugin.md)。
Terway Edge：是一种Underlay的网络插件。详细信息，请参见[Terway Edge](terway-edge-network-plug-in-introduction.md)[网络插件](terway-edge-network-plug-in-introduction.md)。

| 对比项 | Terway Edge 版 | Flannel VXLAN |
| --- | --- | --- |
| 插件来源 | 阿里云自研的网络插件。 | Flannel 社区提供的网络插件。 |
| 适用场景 | 管理自建 IDC、ENS 实例等。 适用于规模较大、网络效率要求高等场景。 | 管理边缘设备，其他云厂商计算实例。 适用于规模小，设备分散等场景。 |
| Pod 网段 | 云端支持 Pod 网段扩容，Pod 网段可以直接使用 VPC 网段。 边缘不支持 Pod 网段扩容，需在创建集群时指定 Pod 网段。 | 不支持 Pod 网段扩容，需在创建集群时指定 Pod 网段。 |
| 网络性能 | 网络性能高，相比于 VXLAN 封包性能提升约 20%。 | 网络性能适中，有 VXLAN 封包。 |
| 云产品对接 | 无缝对接云产品，例如 CLB、ALB、NLB、ECI 等。 | 有限对接云产品，部分能力不可用。 |
| 容器互访 | 支持集群外客户端直接访问容器 IP。 | 不支持集群外客户端直接访问容器 IP。 |
| 网络插件模式 | Underlay 模式，容器与计算资源在同一个网络平面。 | Overlay 模式，容器和计算资源不在同一个网络平面。 |
| 跨网络域容器通信条件 | 若您需要实现容器间跨局域网通信（例如云边容器通信、多个局域网之间容器通信），则需要满足如下条件：（1）节点与云端 VPC 有专线打通；（2）节点交换机需要支持 BGP 协议以接受路由发布。 | 若您需要实现容器间跨局域网通信，则需要节点间三层网络互通。 |

该文章对您有帮助吗？
反馈
