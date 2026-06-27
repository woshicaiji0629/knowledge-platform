## 相关文档
在创建集群后，为Pod、Service、节点分配的网段无法修改。网段的大小决定这三种资源的数量上限，可能会对您的业务部署产生影响。规划不同的网段可以实现资源在网络逻辑上的隔离，以便于您实现访问控制、定制化路由等操作。因此推荐您在创建集群前完成网段规划。Terway与Flannel两种容器网络插件拥有不同的特性，需要使用不同的网络规划策略，推荐您阅读[Terway](comparison-between-terway-and-flannel.md)[与](comparison-between-terway-and-flannel.md)[Flannel](comparison-between-terway-and-flannel.md)[的对比](comparison-between-terway-and-flannel.md)了解它们的具体差别，然后参见[Kubernetes](kubernetes-cluster-network-planning.md)[集群网络规划](kubernetes-cluster-network-planning.md)完成网段规划。
ACK集群网络的常见问题，请参见[网络管理](faq-about-network-management.md)[FAQ](faq-about-network-management.md)。
该文章对您有帮助吗？
反馈
