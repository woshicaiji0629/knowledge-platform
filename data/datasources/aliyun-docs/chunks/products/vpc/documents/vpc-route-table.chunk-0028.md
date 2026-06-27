## 配置示例
为路由条目选择不同的下一跳时，会对应不同的场景：
[路由到](vpc-route-table.md)[IPv4](vpc-route-table.md)[网关](vpc-route-table.md)
[路由到](vpc-route-table.md)[IPv6](vpc-route-table.md)[网关](vpc-route-table.md)
[路由到](vpc-route-table.md)[NAT](vpc-route-table.md)[网关](vpc-route-table.md)
[路由到](vpc-route-table.md)[VPC](vpc-route-table.md)[对等连接](vpc-route-table.md)
[路由到转发路由器](vpc-route-table.md)
[路由到](vpc-route-table.md)[VPN](vpc-route-table.md)[网关](vpc-route-table.md)
[路由到](vpc-route-table.md)[ECS](vpc-route-table.md)[实例或弹性网卡](vpc-route-table.md)
[路由到路由器接口](vpc-route-table.md)
[路由到专线网关](vpc-route-table.md)
[路由到网关型负载均衡终端节点](vpc-route-table.md)
路由到IPv4网关
可将[IPv4](ipv4-gateway-overview.md)[网关](ipv4-gateway-overview.md)作为企业VPC与公网之间的统一出入口，结合自定义路由表集中控制公网访问流量，有利于实施统一的安全策略和审计，降低分散接入带来的安全风险。
路由到IPv6网关
VPC[开启](vpc-and-vswitch.md)[IPv6](vpc-and-vswitch.md)后，系统会自动在系统路由表中添加一条自定义路由条目：
目标网段为::/0，下一跳为IPv6网关。
该路由用于将默认IPv6流量路由至IPv6网关，[为](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-dvo-wjp-zcb)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-and-manage-ipv6-internet-bandwidth#section-dvo-wjp-zcb)[地址开通](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enabl
