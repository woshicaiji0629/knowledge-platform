## 为什么要使用ACK Knative
在完全兼容社区Knative并提供标准Kubernetes API接口的基础上，ACK Knative进一步增强产品化能力并提供了更丰富的产品方案。
产品化能力：提供了产品化一键部署能力，您无需购买资源搭建系统。同时提供产品控制台，支持白屏化操作，降低Kubernetes集群和Knative的使用门槛。
简化运维：
核心组件托管：在ACK集群中，Knative的核心组件Knative Serving和Knative Eventing均由ACK创建和托管，无需您承担资源费用，且提供高可用保障。
网关托管：ACK Knative提供ALB、ASM和Kourier网关。除社区兼容的Kourier外，其余云产品网关的Controller均由ACK创建，提供全托管、免运维的网关服务。
生态集成：无缝集成了阿里云的计算（[ECI](https://help.aliyun.com/zh/eci/product-overview/what-is-elastic-container-instance)、[ECS](../../../../ecs/documents/user-guide/what-is-ecs.md)、[ACS](https://help.aliyun.com/zh/cs/product-overview/product-introduction)）、可观测（[日志服务](../../../../sls/documents/what-is-log-service.md)[SLS](../../../../sls/documents/what-is-log-service.md)、[Prometheus](https://help.aliyun.com/zh/prometheus/product-overview/what-is-managed-service-for-prometheus)）、CI/CD（[云效](https://help.aliyun.com/zh/yunxiao/product-overview/what-is-cloud-effect)）、应用集成（[EventBridge](https://help.aliyun.com/zh/eventbridge/product-overview/what-is-eventbridge)）等产品，无需自行采购服务器，也无需自建服务，便能在Knative服务中实现日志与监控告警、持续交付、事件驱动等能力。
更丰富的功能特性：在社区Knative的基础上，ACK Knative结合实际业务场景提供了开箱即用的、更为丰富的产品方案。例如以下方案。
[保留实例](reserved-instances.md)：为延迟敏感应用保留一个低成本常驻实例，缓解社区Knativ
