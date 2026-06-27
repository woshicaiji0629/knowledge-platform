# 如何在容器服务控制台创建ACK Serverless集群-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/serverless-kubernetes/user-guide/create-an-ask-cluster-2

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/serverless-kubernetes/product-overview.md)

- [快速入门](products/ack/documents/serverless-kubernetes/getting-started.md)

- [操作指南](products/ack/documents/serverless-kubernetes/user-guide.md)

- [实践教程](products/ack/documents/serverless-kubernetes/use-cases.md)

- [安全合规](products/ack/documents/serverless-kubernetes/security-and-compliance.md)

- [开发参考](products/ack/documents/serverless-kubernetes/developer-reference.md)

- [服务支持](products/ack/documents/serverless-kubernetes/support.md)

[首页](https://help.aliyun.com/zh)

# 创建ACK Serverless集群

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ACK Serverless集群是阿里云推出的无需购买节点即可部署工作负载的Kubernetes容器服务。ACK Serverless集群的秒级伸缩能力、根据应用配置的CPU和内存资源量按需、按量付费能力，降低业务的计算成本，尤其是有明显波峰波谷的业务。ACK Serverless集群提供完善的Kubernetes兼容能力，同时降低Kubernetes使用门槛，让您无需管理底层基础设施，更加专注于应用程序。本文介绍如何在容器服务管理控制台创建ACK Serverless集群。

重要

从2025年02月17日起，阿里云容器服务 Serverless 版将对尚未创建过集群的新用户关闭创建集群的入口。您可以通过容器计算服务 ACS（Container Compute Service）使用Serverless容器算力，ACS集群能够支持企业级K8s容器化应用的全生命周期管理，为您提供更强大的功能和更便捷的服务。关于ACS的详细介绍，请参见[ACS](https://help.aliyun.com/zh/cs/product-overview/product-introduction)[产品简介](https://help.aliyun.com/zh/cs/product-overview/product-introduction)。

- 

对于尚未创建过ACK Serverless集群的新用户，我们已关闭新建ACK Serverless集群的入口。您可以通过以下方式使用Serverless容器算力：

- 

创建ACS集群，并在其中使用Serverless容器算力。详细操作，请参见[创建](https://help.aliyun.com/zh/cs/user-guide/create-an-acs-cluster)[ACS](https://help.aliyun.com/zh/cs/user-guide/create-an-acs-cluster)[集群](https://help.aliyun.com/zh/cs/user-guide/create-an-acs-cluster)。

- 

在ACK托管集群Pro版中按需弹性使用Serverless容器算力。详细操作，请参见[通过](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster)[ACK](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster)[托管集群](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster)[Pro](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster)[版使用](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster)[ACS](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster)[算力](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster)。

- 

对于正在使用ACK Serverless集群的存量用户，您现有ACK Serverless集群的使用以及在默认额度内的新建操作不受此次变更的任何影响，您可以继续按照现有的帮助文档正常进行相关操作，无需担心业务中断或调整。

关于此次调整的详细内容，请参见[【产品变更】关于](products/ack/documents/product-overview/product-change-announcement-on-deprecation-of-cluster-creation-interface-for-ack-serverless-clusters.md)[ACK Serverless](products/ack/documents/product-overview/product-change-announcement-on-deprecation-of-cluster-creation-interface-for-ack-serverless-clusters.md)[集群对新用户关闭新建入口的公告](products/ack/documents/product-overview/product-change-announcement-on-deprecation-of-cluster-creation-interface-for-ack-serverless-clusters.md)。

## 前提条件

- 

[已开通并授权容器服务](products/ack/documents/ack-managed-and-ack-dedicated/getting-started/getting-started-with-ack-using-the-ack-console.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/getting-started/getting-started-with-ack-using-the-ack-console.md)。

- 

已登录[弹性容器实例控制台](https://eci.console.aliyun.com)开通ECI服务。

## 步骤一：登录容器服务管理控制台

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

在集群列表页面，单击创建集群。

## 步骤二：配置集群

单击ACK Serverless 集群页签，完成集群配置。

### 基础信息配置

- 

- 

| 配置项 | 描述 |
| --- | --- |
| 集群名称 | 自定义集群名称。 |
| 集群规格 | Pro 版：提供 SLA 保障，适用于企业生产和测试环境。 基础版： [配额](products/ack/documents/product-overview/limits.md) 有限（每个账号支持创建 2 个集群），仅供个人学习与测试。 关于规格对比，请参见 [集群对比](products/ack/documents/serverless-kubernetes/user-guide/ask-pro-cluster-overview.md) 。 |
| 地域 | 集群资源（ECS 实例、云盘等）所处 [地域](products/ack/documents/product-overview/supported-regions.md) 。地域与 用户和资源部署地域的距离越近，网络时延越低。 |
| Kubernetes 版本 | 仅支持创建最近三个 [次要版本](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/support-for-kubernetes-versions.md) ，推荐使用当前最新版本。请参见 [ACK](products/ack/documents/product-overview/release-notes-for-kubernetes-versions.md) [版本支持概览](products/ack/documents/product-overview/release-notes-for-kubernetes-versions.md) 了解 ACK 的版本支持情况。 |
| 自动升级 | 开启集群的自动升级能力，保持集群控制面的周期性自动升级。ACK 会在集群维护窗口期内执行集群自动升级。关于自动升级的策略介绍和使用方法，请参见 [自动升级集群](products/ack/documents/serverless-kubernetes/user-guide/automatically-upgrade-an-ack-cluster.md) 。 |
| 集群维护窗口 | ACK 将在维护窗口期内进行集群版本自动升级。您可以单击 设置 ，配置具体的维护策略。 |


### 网络配置

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 配置项 | 描述 |
| --- | --- |
| IPv6 双栈 | 公测中，请前往 [配额平台](https://quotas.console.aliyun.com/white-list-products/csk/quotas) 申请。 开启 IPv6 双栈后，将创建双栈集群。 重要 仅 1.20.11-aliyun.1 及以上版本的集群支持此功能。 集群使用的 VPC 已支持 IPv6 双栈。 |
| 专有网络 | 集群的专有网络 VPC。为保障高可用，建议选择 2 个及以上不同可用区。 自动创建：ACK 在已选择的可用区下创建对应 vSwitch。 使用已有：选择 vSwitch，指定集群的可用区，可新建或使用已有 vSwitch。 推荐集群 VPC 使用标准私有地址（如 10.0.0.0/8、172.16.0.0/12 和 192.168.0.0/16）。如有特殊需求，请前往 [配额中心](https://quotas.console.aliyun.com/white-list-products/csk/quotas) 申请（ 使用公网网段 VPC 创建集群 ）。 云资源及计费说明： [VPC](products/vpc/documents/what-is-vpc.md) |
| 为专有网络配置 SNAT | 使用共享 VPC 时请勿勾选 节点需访问公网（拉取公网镜像或访问外部服务）时勾选此项，ACK 将自动配置 NAT 网关和 SNAT 规则，确保集群内资源可以访问公网。 VPC 中没有 NAT 网关：ACK 自动创建 NAT 网关，新购 EIP，并为集群使用的 vSwitch 配置 SNAT 规则。 VPC 已有 NAT 网关：ACK 判断是否需要额外新购 EIP 以及配置 SNAT 规则。当无可用 EIP 时，将自动新购 EIP；当不存在 VPC 级别的 SNAT 规则时，将为集群使用的 vSwitch 配置 SNAT 规则。 若不勾选，也可在创建集群后自行配置 NAT 网关和 SNAT 规则，请参见 [公网 NAT 网关](products/nat-gateway/documents/user-guide/use-internet-nat-gateway-for-public-network-access.md) 。 云资源及计费说明： [NAT](products/nat-gateway/documents/nat-gateway-billing.md) [网关](products/nat-gateway/documents/nat-gateway-billing.md) 、 [EIP](products/eip/documents/billing-overview.md) |
| 交换机 | 在列表中根据可用区选择已有 vSwitch 交换机，或单击 创建虚拟交换机 创建新的 vSwitch。集群控制面与默认节点池将使用此处指定的 vSwitch。推荐选择多个不同可用区的 vSwitch，更好地保障集群高可用。 |
| 安全组 | 使用已有 VPC 时，支持使用 选择已有安全组 此 [安全组](products/ecs/documents/user-guide/overview-44.md) 应用于集群控制面、默认节点池和未指定自定义安全组的节点池。 相较于普通安全组，企业级安全组可以容纳更多私网 IP 地址数量，但不支持组内互通功能，详见 [安全组分类](products/ecs/documents/user-guide/overview-44.md) 。 自动创建：出方向默认全部允许，入方向基于 [推荐配置](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-security-group-rules-to-enforce-access-control-on-ack-clusters.md) 放行。后续如需修改，请确保在入方向已放行 100.64.0.0/10 网段。 该网段用于访问阿里云其他服务，以执行镜像拉取、查询 ECS 基础信息等操作。 使用已有：ACK 默认不会为安全组配置额外的访问规则。需自行管理安全组规则，以避免访问异常，请参见 [配置集群安全组](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/configure-security-group-rules-to-enforce-access-control-on-ack-clusters.md) 。 |
| API server 访问 | ACK 自动新建一个按量付费的私网 CLB 实例作为 API Server 的内网连接端点。该 CLB 实例不可复用且不可删除，删除后 API Server 将无法访问且无法恢复。 若需使用已有 CLB 实例，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 申请。选择 使用已有 的 专有网络 后，可选择 负载均衡来源 为 使用已有 。 可选开启 使用 EIP 暴露 API server 。 开放：为 API Server 私网 CLB 实例绑定 EIP，支持从公网访问 API Server，连接并管理集群。 这并不代表集群内资源可以访问公网。如需让集群内资源访问公网，需勾选 为专有网络配置 SNAT 。 不开放：仅能在 VPC 内使用 KubeConfig 连接并操作集群。 如需后续启用，请参见 [实现从公网访问](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/control-public-access-to-the-api-server-of-a-cluster.md) [API Server](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/control-public-access-to-the-api-server-of-a-cluster.md) 。 自 2024 年 12 月 01 日起，新建 CLB 实例 不再支持 包年包月 付费类型，同时 将新增收取实例费，请参见 [【产品公告】关于取消新增集群](products/ack/documents/product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [API Server](products/ack/documents/product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [负载均衡](products/ack/documents/product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [CLB](products/ack/documents/product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [包年包月付费的公告](products/ack/documents/product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) 、 [传统型负载均衡](products/slb/documents/product-overview/announcement-on-adjustment-of-traditional-load-balancing-clb-billing-items.md) [CLB](products/slb/documents/product-overview/announcement-on-adjustment-of-traditional-load-balancing-clb-billing-items.md) [计费项调整公告](products/slb/documents/product-overview/announcement-on-adjustment-of-traditional-load-balancing-clb-billing-items.md) 。 云资源及计费说明： [CLB](products/slb/documents/classic-load-balancer/product-overview/billing-overview.md) 、 [EIP](products/eip/documents/billing-overview.md) |
| 服务网段 | 即 Service CIDR，为集群内部 Service 分配 IP 地址的地址池。此网段不能与 VPC 及 VPC 内已有集群使用的网段重复，且不能与 容器网段 重复。 |
| IPv6 服务网段 | 需同时开启 IPv6 双栈 为 Service 网段配置 IPv6 地址段。需使用 ULA 地址（ fc00::/7 范围内），地址前缀长度在/112~/120 之间。推荐与 服务网段 的可用地址数量保持一致。 |


### 高级配置

| 配置项 | 描述 |
| --- | --- |
| 集群删除保护 | 推荐开启，防止通过控制台或 OpenAPI 误删除集群。 |
| 资源组 | 将集群归属于选择的 [资源组](products/ecs/documents/user-guide/resource-groups.md) ，便于权限管理和成本分摊。 一个资源只能归属于一个资源组。 |
| 标签 | 为集群绑定键值对 [标签](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview) ，作为云资源的标识。 |
| 集群本地域名 | 集群内 Service 使用的顶级域名（标准后缀）。默认为 cluster.local ，也支持自定义域名。自定义本地域名时，请参见 [配置集群本地域名（ClusterDomain）有哪些注意事项？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-container-networks.md) 。 例如，名为 my-service 的 Service 位于 default 命名空间中，其 DNS 域名为 my-service.default.svc.cluster.local 。 |
| 时区 | 集群使用的 [时区](products/ack/documents/product-overview/supported-time-zones.md) 。默认为浏览器配置的时区。 |


## 步骤三：配置组件

单击下一步：组件配置，完成组件配置。

- 

- 

- 

- 

- 

| 配置项 | 描述 |
| --- | --- |
| 服务发现 | 设置集群的服务发现，支持 不开启 、 PrivateZone 和 CoreDNS 三种方式。 [PrivateZone](https://help.aliyun.com/zh/dns/introduction-to-intranet-analysis) ：基于阿里云专有网络 VPC 环境的私有 DNS 服务。该服务允许您在自定义的一个或多个 VPC 中将私有域名映射到 IP 地址。 CoreDNS：一个灵活可扩展的 DNS 服务器，也是 Kubernetes 标准的服务发现组件。 |
| Ingress | 设置是否安装 Ingress 组件，支持 不安装 、 Nginx Ingress 、 ALB Ingress 和 MSE Ingress 方式。 [Nginx Ingress](products/ack/documents/serverless-kubernetes/user-guide/overview-2.md) ：基于社区版的 ingress-nginx 进行了优化，为您的 Kubernetes 集群提供灵活可靠的路由服务（Ingress）。 [ALB Ingress](products/ack/documents/serverless-kubernetes/user-guide/alb-ingress-overview.md) ：基于阿里云应用型负载均衡 ALB（Application Load Balancer）之上提供更为强大的 Ingress 流量管理方式，兼容 Nginx Ingress，具备处理复杂业务路由和证书自动发现的能力，支持 HTTP、HTTPS 和 QUIC 协议，完全满足在云原生应用场景下对超强弹性和大规模七层流量处理能力的需求。 [MSE Ingress](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-mse-ingresses-to-access-applications-in-ack-clusters.md) ：在 Kubernetes 集群中，Ingress 对集群服务（Service）中外部可访问的 API 对象进行管理，提供七层负载均衡能力。为了更好地支持云原生应用场景，MSE 云原生网关与容器服务进行了深度集成和优化，推出了 MSE Ingress，提供更强大的集群入口流量管理能力。 |
| 容器监控 | 您可以使用阿里云 Prometheus 查看集群预先配置的监控大盘和监控性能指标。更多信息，请参见 [阿里云](products/ack/documents/serverless-kubernetes/user-guide/enable-prometheus-service.md) [Prometheus](products/ack/documents/serverless-kubernetes/user-guide/enable-prometheus-service.md) [监控](products/ack/documents/serverless-kubernetes/user-guide/enable-prometheus-service.md) 。 您可以同时勾选 安装 metrics-server 集群基础监控组件 ， [metrics-server](products/ack/documents/product-overview/metrics-server.md) [组件](products/ack/documents/product-overview/metrics-server.md) 是基于社区开源监控组件进行改造和增强的离线监控数据组件，提供查看集群离线监控数据功能。 |
| 日志服务 | 设置是否 使用日志服务 ，您可使用已有 Project 或新建一个 Project。 不开启时，将无法使用集群审计功能。关于日志服务详情，请参见 [使用](products/sls/documents/getting-started.md) [LoongCollector](products/sls/documents/getting-started.md) [采集并分析](products/sls/documents/getting-started.md) [ECS](products/sls/documents/getting-started.md) [文本日志](products/sls/documents/getting-started.md) 。 |
| Knative | 设置是否 开启 Knative 。 [Knative](products/ack/documents/serverless-kubernetes/user-guide/knative-overview.md) 是一款基于 Kubernetes 的 Serverless 框架，支持基于请求的自动弹性、在没有流量时将实例数量自动缩容至零、版本管理与灰度发布等能力。 |


## 步骤四：确认配置

单击下一步：确认配置，确认配置信息和使用须知，仔细阅读并选中服务协议，然后单击创建集群。

集群创建成功后，您可以在容器服务管理控制台的集群列表页面查看所创建的集群。

说明

一个集群的创建时间一般约为十分钟。

## 相关操作

- 

查看集群基本信息

在集群列表页面中，找到刚创建的集群，单击操作列中的详情，单击基本信息和连接信息页签，查看集群的基本信息和连接信息。其中：

- 

API Server 公网端点：Kubernetes的API Server对公网提供服务的地址和端口，可以通过此服务在用户终端使用kubectl等工具管理集群。

绑定公网IP和解绑公网IP功能仅支持托管版Kubernetes集群。

- 

绑定公网IP：您可以选择在已有EIP列表中绑定EIP或者新建EIP。

绑定公网IP操作会导致API Server短暂重启，请避免在此期间操作集群。

- 

解绑公网IP：解绑公网IP后您将无法通过公网访问API Server。

解绑公网IP操作会导致API Server短暂重启，请避免在此期间操作集群。

- 

API Server 内网端点：Kubernetes的API Server对集群内部提供服务的地址和端口，此IP为负载均衡的地址。

- 

查看集群日志信息

您可以单击集群日志页签，查看集群的日志信息。

[上一篇：集群概述](products/ack/documents/serverless-kubernetes/user-guide/ask-pro-cluster-overview.md)[下一篇：通过OpenAPI创建ACK Serverless集群](products/ack/documents/serverless-kubernetes/user-guide/create-an-ask-cluster-1.md)

该文章对您有帮助吗？

反馈

### 为什么选择阿里云

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)

### 大模型

[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)

### 产品和定价

[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)

### 技术内容

[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)

### 权益

[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)

### 服务

[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)

### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

联系我们：4008013260

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
