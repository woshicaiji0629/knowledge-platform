## IPsec-VPN连接多云
阿里云和AWS平台下的IPsec-VPN连接均支持双隧道模式，但由于AWS平台的两条隧道默认关联至同一个客户网关，而阿里云侧两条隧道拥有不同的IP地址，导致AWS平台和阿里云侧的两条隧道无法做到一一对应建立连接。
为确保阿里云侧IPsec-VPN连接下两条隧道同时启用，您需要在AWS平台创建两个站点到站点的VPN连接，每个站点到站点VPN连接关联不同的客户网关。
多云环境下，往往有多个VPC需要互通，人工配置路由相对繁琐，您可以通过将IPsec连接绑定至[转发路由器](../../cen/documents/product-overview/how-transit-routers-work.md)[TR](../../cen/documents/product-overview/how-transit-routers-work.md)，结合BGP动态路由实现全网高效互联。动态路由能够根据网络拓扑的变化自动调整路由表，减少人工配置的工作量，降低组网配置复杂度。
阿里云IPsec-VPN绑定转发路由器TR时，默认开启ECMP，建议您在AWS侧也开启ECMP。如果AWS侧未开启ECMP，则AWS流向阿里云的流量需要指定连接，阿里云流向AWS的流量则会根据ECMP自动选择隧道。
