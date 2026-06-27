### Flannel容器网络插件
[Flannel](https://github.com/flannel-io/flannel)是一个经典的开源容器网络插件，它使用VXLAN等虚拟化网络技术为Pod构建了一个Overlay网络。Flannel的配置简单、易于使用，但是网络性能会受到NAT损失的影响，访问控制能力相较于Terway也更弱，并且集群的节点数量上限较低。Flannel适用于节点数量不超过1000的小规模集群，以及对网络性能和访问控制能力需求较低，希望快速搭建、使用集群的场景。
重要
关于Terway和Flannel插件的详细能力对比，请参见[Terway](comparison-between-terway-and-flannel.md)[与](comparison-between-terway-and-flannel.md)[Flannel](comparison-between-terway-and-flannel.md)[的对比](comparison-between-terway-and-flannel.md)。
