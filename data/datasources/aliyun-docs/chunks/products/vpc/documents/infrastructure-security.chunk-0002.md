y/user-guide/create-and-manage-an-egress-only-rule)，可以灵活定义IPv6的出流量和入流量。
创建[自定义路由表](network-traffic-management-using-custom-routing-tables.md)并绑定交换机，添加自定义路由条目来控制该交换机的流量，便于更灵活地进行网络管理。
通过创建[VPC](vpc-peer-to-peer-connection.md)[对等连接](vpc-peer-to-peer-connection.md)，并为两端VPC分别配置路由，可以实现VPC私网互通。对等连接功能支持同账号/跨账号、同地域/跨地域VPC互通，配置前需确保两端VPC的网段不重叠。
[云企业网](../../cen/documents/product-overview/what-is-cen.md)作为多VPC互连的解决方案，可以实现企业内部多个VPC之间的网络互通，打造灵活、可靠、大规模的企业级云上网络。
使用[高速通道](https://help.aliyun.com/zh/express-connect/product-overview/what-is-express-connect/)、[VPN](https://help.aliyun.com/zh/vpn/product-overview/what-is-vpn-gateway)[网关](https://help.aliyun.com/zh/vpn/product-overview/what-is-vpn-gateway)，可以实现[阿里云](connect-vpc-to-local-idc-office-terminal-other-cloud.md)[VPC](connect-vpc-to-local-idc-office-terminal-other-cloud.md)[与用户本地数据中心、办公终端或其他云厂商网络互通](connect-vpc-to-local-idc-office-terminal-other-cloud.md)。
[网关终端节点](vpc-connection-to-cloud-service.md)是虚拟网关设备，在VPC中创建云服务的网关终端节点并指定关联的路由表，系统自动将增加下一跳指向网关终端节点的路由条目，实现对云服务的私网访问。
使用VPC的[流日志](vpc-flow-logs.md)功能捕获VPC网络中弹性网卡ENI的传入和传出流量信息，可以检查访问控制规则、监控网络流量和排查网络故障。
