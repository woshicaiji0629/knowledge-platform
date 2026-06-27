### 使用VPN连接
本地数据中心使用VPN连接到阿里云，推荐您使用[IPsec-VPN](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/product-overview/what-is-ipsec-vpn)产品。
IPsec-VPN有2种使用方式，主要区别如下：

| 使用方式 | 绑定 VPN 网关 | 绑定转发路由器 TR |
| --- | --- | --- |
| 应用场景 | 本地数据中心仅能与 VPN 网关实例所在的 VPC 互通。 | 本地数据中心可以通过 [转发路由器](../../cen/documents/product-overview/how-transit-routers-work.md) [TR](../../cen/documents/product-overview/how-transit-routers-work.md) 实例与 [云企业网](../../cen/documents/product-overview/what-is-cen.md) [CEN](../../cen/documents/product-overview/what-is-cen.md) 内的任意 VPC、其他本地数据中心互通。 |
| 双隧道时实现高可用链路的方式 | 主备链路 | ECMP 链路 ECMP（Equal-Cost Multipath Routing）通过多路径同时分担流量，实现负载均衡和链路备份，提升网络效率和可靠性。 |
| IPsec 连接带宽是否可扩充 | 否 | 是。可以创建多个 IPsec 连接，通过 ECMP 链路同时传输流量，从而间接实现带宽扩充。 |
