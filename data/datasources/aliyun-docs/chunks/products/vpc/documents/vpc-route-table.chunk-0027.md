## 使用网关路由表
通过使用网关路由表，可将公网入向流量导向安全设备进行深度检测与过滤，防止恶意攻击和未经授权的访问，实现安全防护。还可结合自定义路由表，将出向流量引流至安全设备，实现入向和出向的全面安全防护。
使用时，需先创建一张绑定IPv4网关的路由表，再将路由表中交换机网段对应的系统路由下一跳改为：
ECS实例/弹性网卡：用于公网流量安全引流到特定ECS实例或弹性网卡。
网关型负载均衡终端节点：用于网关型负载均衡GWLB场景的第三方安全设备公网流量引流。
仅[这些地域](../../slb/documents/gateway-based-load-balancing-gwlb/product-overview/regions-and-zones-supported-by-gwlb.md)支持修改下一跳为网关型负载均衡终端节点。
使用自建防火墙
可在VPC中通过ECS自建防火墙，并使用网关路由表[将进入](use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)[VPC](use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)[的流量引流至防火墙过滤](use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)。
GWLB高可用架构
可[使用网关型负载均衡](../../slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)[GWLB](../../slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)，将流量分发到不同的安全设备，来提高应用系统的安全性和可用性。
