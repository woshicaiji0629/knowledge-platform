## 容器网络插件（CNI Plugin）
Kubernetes本身并未实现容器间的网络互联能力，但是它通过[容器网络接口（CNI）](https://github.com/containernetworking/cni/tree/main)对容器间的网络做出了标准化的定义：
Pod在容器网络中的状态随着Pod生命周期而变化。例如，Pod创建后需要加入网络，销毁后需要退出网络。
Pod在容器网络中拥有唯一的IP地址，以便于识别身份。
Pod可以与集群内的端点与集群外的端点互相访问。
[容器网络插件（CNI Plugins）](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)负责容器网络的具体实现。容器网络插件决定了Pod IP地址分配的机制、是否使用Overlay网络、集群内流量的转发链路、对Pod的访问控制机制等容器网络特性。目前已经有很多知名的开源容器网络插件，如Calico、Flannel、Cilium等。
容器服务 Kubernetes 版支持两种容器网络插件：Terway与Flannel。这两种插件拥有不同的特性，请参照下方的介绍以及[Terway](comparison-between-terway-and-flannel.md)[与](comparison-between-terway-and-flannel.md)[Flannel](comparison-between-terway-and-flannel.md)[的对比](comparison-between-terway-and-flannel.md)文档，在创建集群前完成容器网络插件的选型。
重要
集群创建完成后，不支持Terway与Flannel之间的变更切换。
