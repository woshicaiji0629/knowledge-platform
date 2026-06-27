## 功能架构
VPC 提供丰富功能，支持构建满足特定业务需求的网络架构，同时具备精细化访问控制与监控运维能力。
[交换机](vpc-and-vswitch.md)：在 VPC 内划分地址空间以部署云资源。交换机是可用区级别的资源。
[路由表](vpc-route-table.md)：控制 VPC 内的流量走向。交换机与路由表绑定，由路由条目决定流经该交换机的数据包的下一跳。
[IP](ip-address-management-ipam.md)[地址管理（IPAM）](ip-address-management-ipam.md)：作为 IP 地址管理工具，自动化分配与管理 IP 地址，简化网络管理流程并避免地址冲突。
[IPv4](ipv4-gateway-overview.md)[网关](ipv4-gateway-overview.md)/[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)[网关](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)：结合路由表集中控制公网访问流量，降低分散接入带来的安全风险。
[VPC](vpc-peer-to-peer-connection.md)[对等连接](vpc-peer-to-peer-connection.md)：支持同账号/跨账号、同地域/跨地域 VPC 互连。
[网络](network-acl-overview.md)[ACL](network-acl-overview.md)：与交换机绑定，通过配置网络ACL规则，控制出入交换机的流量。
[流日志](vpc-flow-logs.md)：采集并记录弹性网卡的进出流量信息，可以监控网络性能、排查网络故障或优化流量成本。
[流量镜像](traffic-mirroring-overview.md)：作为旁路监控方案，在不影响业务流量的前提下，将符合筛选条件的流量复制并转发到安全分析设备，实现实时检测。
该文章对您有帮助吗？
反馈
