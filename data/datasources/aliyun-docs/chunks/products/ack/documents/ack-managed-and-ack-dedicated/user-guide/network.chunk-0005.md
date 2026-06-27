## 路由（Ingress）
在ACK集群中，与Service的4层负载均衡不同，Ingress是集群内Service对外暴露7层的访问接入点，用于为集群中的多个Service提供统一的入口。您可以通过Ingress资源来配置不同的7层的转发规则，例如通过域名或者访问路径来路由到不同的Service上，从而达到7层的负载均衡作用。更多信息，请参见[Ingress](ingress-management-2.md)[管理](ingress-management-2.md)。
