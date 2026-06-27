## 用负载均衡统一公网流量入口
单台后端服务器直接使用公网IP对外提供服务时，如果服务器出现问题容易导致业务单点故障。
实际业务场景中，推荐您使用负载均衡产品，在负载均衡后端挂载不同可用区的多台后端服务器，通过将流量分发到不同的后端服务来扩展应用系统的服务吞吐能力，消除系统中的单点故障，提升应用系统的可用性。
推荐您优先使用新一代负载均衡产品，即[应用型负载均衡](../../slb/documents/application-load-balancer/product-overview/what-is-alb.md)[ALB](../../slb/documents/application-load-balancer/product-overview/what-is-alb.md)和[网络型负载均衡](../../slb/documents/network-load-balancer/product-overview/what-is-nlb.md)[NLB](../../slb/documents/network-load-balancer/product-overview/what-is-nlb.md)。

| 对比项 | 应用型负载均衡 ALB | 网络型负载均衡 NLB |
| --- | --- | --- |
| 产品定位 | 强大的七层处理能力与丰富的高级路由功能 聚焦 HTTP、HTTPS 和 QUIC 协议 | 强大的四层处理能力与大规模 TCPSSL 证书卸载功能 聚焦 TCP、UDP 和 TCPSSL 协议 |
| 产品性能 | 单实例最大支持 100 万 QPS | 单实例最大支持 1 亿并发 |
| 后端资源类型 | 云服务器 ECS 弹性网卡 ENI 弹性容器实例 ECI IP 地址 函数计算 FC | 云服务器 ECS 弹性网卡 ENI 弹性容器实例 ECI IP 地址 |
| 运维能力 | 均支持弹性和快速扩容，处理能力随着业务峰值自动伸缩，无需人工干预 |  |
| 典型应用场景 | 互联网应用七层高性能自动弹性场景 音视频应用大流量低时延场景 云原生应用金丝雀蓝绿发布场景 | 四层大流量高并发业务场景 物联网、车联网等 IoT 业务入口场景 多活容灾、IDC 云上出入口场景 |
