## Service概述
Service是可以对一组容器提供固定访问入口的服务暴露方式，支持以下多种模式，以满足不同来源和类型的客户端访问需求。

| 类型 | 说明 |
| --- | --- |
| ClusterIP | ClusterIP 类型的 Service 用于在集群内部实现应用间的访问。如果您的应用需要暴露到集群内部提供服务，可使用 ClusterIP 类型的 Service 进行暴露。 说明 创建 Service 时默认的 Service 类型为 ClusterIP。 |
| NodePort | NodePort 类型的 Service 通过集群节点上的一个固定端口，将应用向外部暴露，您就可以在集群外部通过节点的 IP 地址和端口访问集群内的应用。 |
| LoadBalancer | LoadBalancer 类型的 Service 同样是将集群内部部署的应用向外暴露，它通过阿里云的负载均衡进行暴露的，相对于 NodePort 方式，有更高的可用性和性能。关于如何通过 LB 类型的 Service 服务暴露，请参见 [使用负载均衡类型的](expose-an-application-by-using-a-service-of-the-load-balancing-type.md) [Service](expose-an-application-by-using-a-service-of-the-load-balancing-type.md) [暴露应用](expose-an-application-by-using-a-service-of-the-load-balancing-type.md) 。 |
| Headless Service | Headless Service 类型的 Service 是在 Service 属性中指定 clusterIP 字段为 None 类型。采用 Headless Service 类型后，Service 将没有固定的虚拟 IP 地址，客户端访问 Service 的域名时会通过 DNS 返回所有的后端 Pod 实例的 IP 地址，客户端需要采用 DNS 负载均衡来实现对后端的负载均衡。 |
| ExternalName | ExternalName 类型的 Service 会在集群中将一个内部服务名称映射到一个外部域名。这种映射使得集群内的 Pod 可以通过 Service Name 来访问外部域名。 |

在ACK Edge集群中，由于计算资源通常分布在不同的网络域，针对分布式场景为您提供了以下能力。
