| ExternalName | ExternalName 类型的 Service 会在集群中将一个内部服务名称映射到一个外部域名。这种映射使得集群内的 Pod 可以通过 Service Name 来访问外部域名。 |

在ACK Edge集群中，由于计算资源通常分布在不同的网络域，针对分布式场景为您提供了以下能力。

| 类型 | 说明 |
| --- | --- |
| Service 的服务拓扑 | 当客户端和被访问的服务端 Pod 位于不同网络域时，通信将无法完成，采用 Service 服务拓扑能力后，客户端的请求只达到本网络域或本节点上的后端 Pod，相关操作，请参见 [节点池服务拓扑管理](configure-a-service-topology.md) 。 |
| NodePort Service 的端口隔离 | 为了让多个网络域的 NodePort Service 进行端口隔离，您可以对所监听端口进行隔离，相关操作，请参见 [NodePort](nodeport-service-isolation.md) [端口监听隔离](nodeport-service-isolation.md) 。 |
