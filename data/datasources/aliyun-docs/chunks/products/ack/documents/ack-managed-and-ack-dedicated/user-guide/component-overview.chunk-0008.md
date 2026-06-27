| 组件名称 | 组件类型 | 描述 |
| --- | --- | --- |
| [CoreDNS](../../product-overview/coredns.md) | 系统组件 | ACK 集群中默认采用的 DNS 服务发现插件，其遵循 Kubernetes DNS-Based Service Discovery 规范。 |
| [Gateway API](../../product-overview/gateway-api.md) | 系统组件 | Kubernetes 中用于对服务网络流量进行建模的一系列资源，目标是建立一套表现力强、易扩展、面向角色的服务网络模型。 |
| [ACK eRDMA Controller](../../product-overview/ack-erdma-controller.md) | 可选组件 | 使用 eRDMA 控制器管理 eRDMA 网卡。 |
| [ACK NodeLocal DNSCache](../../product-overview/ack-nodelocal-dnscache.md) | 可选组件 | 基于社区开源项目 NodeLocal DNSCache 的一套 DNS 本地缓存解决方案。 |
| [ALB Ingress Controller](../../product-overview/alb-ingress-controller.md) | 可选组件 | 基于阿里云应用型负载均衡 ALB（Application Load Balancer） ，提供更为强大的 Ingress 流量管理方式，兼容 Nginx Ingress，具备处理复杂业务路由和证书自动发现的能力，支持 HTTP、HTTPS 和 QUIC 协议，满足在云原生应用场景下对超强弹性和大规模七层流量处理能力的需求。 |
| [MSE Ingress Controller](https://help.aliyun.com/zh/mse/user-guide/manage-the-mse-ingress-controller-component) | 可选组件 | 基于 MSE 云原生网关，适用于微服务场景，兼容 Nginx Ingress。支持多种服务发现、认证鉴权以及多语言插件扩展，提供灰度发布、预热和限流等 Ingress 流量管理能力。 |
| [Terway](../../product-overview/terway.md) | 可选组件 | 阿里云开源的 Terway CNI 插件支持 eBPF 网络加速和 Kubernetes 标准的 NetworkPolicy，用于定义容器间的访问策略。使用 Terway 可以实现 Kubernetes 集群内部的网络互通。创建集群时，选择 Terway 网络插件会默认安装该
