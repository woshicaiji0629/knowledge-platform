## 为什么选择应用型负载均衡ALB
应用型负载均衡ALB，提供应用层处理能力和多种高级[路由](https://www.aliyun.com/getting-started/what-is/what-is-routing)功能，聚焦HTTP、HTTPS和QUIC应用层协议，是阿里云官方云原生Ingress网关。关于云原生网关ALB Ingress的介绍和使用，请参见[ALB Ingress](../user-guide/alb-ingress.md)[管理](../user-guide/alb-ingress.md)和[ALB Ingress](../user-guide/functions-and-features-of-alb-ingresses.md)[功能操作指导](../user-guide/functions-and-features-of-alb-ingresses.md)。
应用层高弹性：ALB面向应用层，提供域名与VIP，多级分发承载大规模请求。ALB支持通过流量分发扩展应用系统的服务能力，消除单点故障提升应用系统的可用性。ALB允许自定义可用区组合和在可用区间弹性伸缩，避免单可用区资源瓶颈。
先进的协议支持：ALB支持HTTP、HTTPS和QUIC协议，具备超大规模的流量处理能力。在实时音视频、互动直播和游戏等移动互联网应用中，访问速度更快，传输链路更安全可靠。ALB支持gRPC框架，可实现[微服务](https://www.aliyun.com/getting-started/what-is/what-is-microservice)间的API通信。
基于内容的高级路由：ALB支持基于路径、HTTP标头、查询字符串、HTTP请求方法、Cookie和SourceIp等多种条件来识别特定业务流量，并将其转发至不同的后端服务器。同时ALB还支持重定向、重写以及自定义HTTPS标头等高级操作。
安全可靠：ALB自带DDoS防护，集成Web应用防火墙。同时提供全链路HTTPS加密，支持预制和自定义安全策略、TLS 1.3等高效安全加密协议，面向加密敏感型业务，满足Zero-Trust新一代安全技术架构需求。
面向云原生：随着[云原生](https://www.aliyun.com/getting-started/what-is/what-is-cloud-native)逐步成熟，互联网、金融、企业等新建业务时都会选择云原生部署，或对现有业务进行云原生化改造。ALB与[容器](https://www.aliyun.com/getting-started/what-is/what-is-container)服务[Kubernetes](https://www.aliyun.com/getting-started/what-is/what-is-ku
