## 协议版本
ALB实例的协议版本分为IPv4和双栈。IPv4和双栈的区别：

| 协议版本 | 默认值 | 说明 |
| --- | --- | --- |
| IPv4 | 协议版本为 IPv4 的公网 ALB ，每个可用区提供一对 IP 地址，包括一个公网 IPv4 地址和一个私网 IPv4 地址。 协议版本为 IPv4 的私网 ALB ，每个可用区提供一个私网 IPv4 地址。 | 仅支持客户端使用 IPv4 地址（例如，192.0.2.1）访问。 仅支持将 IPv4 的客户端流量转发至 IPv4 的后端服务，且后端服务支持服务器类型（ECS、ENI、ECI）、IP 类型和函数计算类型。 |
| 双栈 | 协议版本为双栈的公网 ALB ，每个可用区提供三个 IP 地址，包括一个公网 IPv4 地址、一个私网 IPv4 地址和一个 IPv6 地址。 协议版本为双栈的私网 ALB ，每个可用区提供一对 IP 地址，包括一个私网 IPv4 地址和一个 IPv6 地址。 | 支持客户端同时使用 IPv4 地址（例如，192.168.0.1）和 IPv6 地址（例如，2001:db8:1:1:1:1:1:1）访问。 支持将 IPv4 和 IPv6 的客户端流量转发至 IPv4 或 IPv6 的后端服务。后端服务支持服务器类型（ECS、ENI、ECI）、IP 类型，不支持函数计算类型。 说明 如果您双栈 ALB 实例的服务器组类型为 IP 类型，且需要挂载 IPv6 的后端服务时，您需要使用 [ALB](../../product-overview/alb.md) [升级实例](../../product-overview/alb.md) 。 |

ALB对外通过DNS域名提供服务。ALB联动DNS，可实现自定义域名的解析，建议您使用CNAME解析的方式将自定义域名指向到ALB实例的DNS名称，使您更方便访问网络资源，配置可参考[为](configure-cname-resolution-for-alb.md)[ALB](configure-cname-resolution-for-alb.md)[配置](configure-cname-resolution-for-alb.md)[CNAME](configure-cname-resolution-for-alb.md)[解析](configure-cname-resolution-for-alb.md)。
