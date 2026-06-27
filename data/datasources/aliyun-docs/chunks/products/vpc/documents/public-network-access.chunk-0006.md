## IPv6网关
VPC内实例默认申请的IPv6地址只具备IPv6私网通信能力。您可以使用[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)[网关](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)，为IPv6地址[开通](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth)[公网带宽](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth)，使其具备公网通信能力。
IPv6网关是VPC的公网IPv6流量网关，可以支持设置[仅主动出规则](https://help.aliyun.com/zh/ipv6-gateway/user-guide/create-and-manage-an-egress-only-rule)，使IPv6地址仅可主动访问公网，无法被公网的客户端访问。
公网CLB不属于VPC内的资源，IPv6流量不受IPv6网关的控制。
