## 用NAT网关统一公网流量出口
单台服务器可以通过公网IP地址主动访问公网。
但当需要主动访问公网的服务器较多时，需要占用较多的公网IP资源与成本，也加大了网络运维管理的复杂度。
您可以使用[公网](../../nat-gateway/documents/user-guide/public-network-nat-gateway.md)[NAT](../../nat-gateway/documents/user-guide/public-network-nat-gateway.md)[网关](../../nat-gateway/documents/user-guide/public-network-nat-gateway.md)并配置SNAT条目，实现VPC内的多个ECS实例共享EIP上网，节省公网IP资源与成本、简化网络运维管理。同时公网NAT网关通过地址转换，隐藏云服务器的真实IP地址避免对外暴露，提升了公网安全性。

| 对比项 | 直接使用弹性公网 IP | 公网 NAT 网关 |
| --- | --- | --- |
| 是否支持多服务器共享使用 EIP | 不支持 | 支持 |
| 使用单个 EIP 的粒度 | ECS/弹性网卡粒度 | VPC 粒度 交换机粒度 ECS/弹性网卡粒度 自定义网段粒度 |
| 服务器较多时总体资源成本 | 高 | 低 |
| 安全性 | 一般 | 较高 |
