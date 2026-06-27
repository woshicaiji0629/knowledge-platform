## 使用IPv6访问公网

| 实现方式 | 适用场景 | 特点 | 相关文档 |
| --- | --- | --- | --- |
| 分配已开通公网带宽的 IPv6 地址 | 适用于已支持 IPv6 的应用或服务。 业务需要与 IPv6 终端互访。 未来面向大规模设备连接的 IoT 及云服务。 | 与传统 IPv4 方案相比，IPv6 提供了更充足的地址空间和更先进的网络特性。支持直接访问的 IPv6 互联网。 | [IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md) [通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md) |
| 通过负载均衡 SLB 分发公网流量 | 适用于超大规模互联网应用，如春节红包、双十一秒杀抢购、大规模在线物联网应用等高并发场景。 为企业级应用提供持续稳定的服务，实现高可用、自动故障转移和跨可用区负载均衡等。 流量较大的 Web 应用，自动应对流量高峰。 | 可在多可用区挂载多台后端服务器，通过将流量（ IPv4 、 IPv6 ）分发到不同的后端服务来扩展应用系统的服务吞吐能力，消除系统中的单点故障，提升应用系统的可用性。更多信息，请参见 [负载均衡](../../../slb/documents/product-overview/slb-overview.md) [SLB](../../../slb/documents/product-overview/slb-overview.md) [产品家族介绍](../../../slb/documents/product-overview/slb-overview.md) 。 | [快速入门](../../../slb/documents/getting-started.md) |
