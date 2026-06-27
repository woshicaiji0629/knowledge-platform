### Terway容器网络插件
Terway网络插件是阿里云自研的容器网络插件。在容器服务 Kubernetes 版中作为节点的ECS实例使用ENI（[弹性网卡](../../../../ecs/documents/user-guide/eni-overview.md)）进行网络通信，Terway将节点的ENI分配给Pod，为Pod提供了网络互联能力。因此，在使用Terway时，Pod直接接入VPC网络。由于不需要使用VXLAN等隧道技术封装报文，Terway模式网络具有较高的通信性能。Terway适用于大规模集群以及对网络性能和访问控制能力有较高需求的场景。
在创建集群并安装Terway网络插件时，可以为Terway配置不同的工作模式。这些工作模式的区别主要在以下三个维度：
Pod IP地址分配：Terway拥有两种IP地址分配模式：独占ENI模式与共享ENI模式。独占ENI模式中，Pod独占节点的ENI，拥有极致的网络性能；而共享ENI模式中，Pod共享节点的ENI，拥有更高的部署密度。
网络加速能力：共享ENI模式支持DataPathv2加速模式。选择加速模式后，Terway会采取不同于共享ENI常规模式的流量转发链路，实现更快的网络通信。
访问控制能力：共享ENI模式与独占ENI模式都支持为Pod配置固定IP、独立的安全组与虚拟交换机，独占ENI模式支持通过Kubernetes原生的Network Policy进行访问控制。
