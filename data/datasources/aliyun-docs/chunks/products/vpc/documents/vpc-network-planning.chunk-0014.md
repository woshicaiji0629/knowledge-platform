## 公网访问
从互联网访问云上部署的应用或者应用主动访问公网时，有如下建议：
从互联网访问云上部署的应用，或者应用主动访问公网时，需要为应用服务器配置公网IP地址。公网IP地址类型分为固定公网IP与[弹性公网](../../eip/documents/product-overview/what-is-eip.md)[IP](../../eip/documents/product-overview/what-is-eip.md)。推荐您使用弹性公网IP为应用服务器配置公网IP地址。
单台后端服务器直接使用公网IP对外提供服务时，如果服务器出现问题容易导致业务单点故障，影响系统可用性。实际业务场景中，推荐您使用[负载均衡](../../slb/documents/product-overview/slb-overview.md)统一公网流量入口，并在多可用区挂载多台后端服务器，消除系统中的单点故障，提升应用系统的可用性。
当您需要主动访问公网的服务器较多时，需要占用较多的公网IP资源，此时您可以通过[公网](../../nat-gateway/documents/user-guide/public-network-nat-gateway.md)[NAT](../../nat-gateway/documents/user-guide/public-network-nat-gateway.md)[网关](../../nat-gateway/documents/user-guide/public-network-nat-gateway.md)的SNAT功能，实现VPC内的多个ECS实例共享EIP上网，节省公网IP资源。
当部署在云上的业务对互联网提供服务时，进行合适的访问控制，能够帮助阻止不必要或潜在的危险访问。您可以使用[IPv4](ipv4-gateway-overview.md)[网关](ipv4-gateway-overview.md)、[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)[网关](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)实现对VPC内实例访问公网的集中控制，增强VPC内的安全防护，严格管控公网访问。
