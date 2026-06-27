## 基本概念
在ACK Edge集群中，Ingress作为服务对外暴露的访问入口，承载了集群内几乎所有的访问流量。Ingress是Kubernetes中的一个资源对象，用于管理集群外部对于内部服务的访问方式。通过配置Ingress资源，可以定义不同的转发规则，从而实现根据不同规则访问集群内部各Service对应的后端Pod。关于Ingress原理详情，请参见[Ingress](../../ack-managed-and-ack-dedicated/user-guide/ingress-management-2.md)[管理](../../ack-managed-and-ack-dedicated/user-guide/ingress-management-2.md)。
Ingress资源主要用于配置HTTP和HTTPS流量的规则，无法配置一些高级特性，例如负载均衡算法、会话亲和性（Session Affinity）等，这些高级特性需要在Ingress Controller中进行配置。
