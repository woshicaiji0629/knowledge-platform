# 网络架构模型与核心组件详解-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/network-management-overview

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-edge/product-overview.md)

- [快速入门](products/ack/documents/ack-edge/quick-start.md)

- [操作指南](products/ack/documents/ack-edge/user-guide.md)

- [实践教程](products/ack/documents/ack-edge/use-cases.md)

- [安全合规](products/ack/documents/ack-edge/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-edge/developer-reference.md)

- [服务支持](products/ack/documents/ack-edge/support.md)

[首页](https://help.aliyun.com/zh)

# 网络管理概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ACK Edge集群支持将云下IDC服务设备以及边缘设备接入到阿里云容器服务平台，并提供云上的ACK功能，同时可以管理自有的计算资源，本文介绍ACK Edge集群网络的重要概念和网络模型，包括云边连接网络、容器网络CNI、Service和Ingress等。通过了解这些概念，您可以更合理地设计应用部署以及网络访问方式。

## 云边网络连接类型

ACK Edge集群提供两种接入网络类型：公网型和专线型。

- 

公网接入：本地IDC设备或边缘设备通过公网NAT或公网网卡访问云上托管的ACK控制面和阿里云产品，实现控制面网络通信以及云产品的访问。

- 

专线接入：本地IDC或边缘设备通过专线、VPN、或其他网络方案打通，通过专线等访问云上托管的ACK控制面和阿里云云产品。下图以阿里云[高速通道](https://help.aliyun.com/zh/express-connect/product-overview/what-is-express-connect/)为例。

## 云边运维通信组件

ACK Edge集群采用了中心云管理IDC或边缘设备的架构，由于计算设备通常分散在多个地域及不同的网络域中，因此中心云与边缘侧无法直接通信。

为满足中心云对边缘侧运维、监控的需求，可以采用以下两种解决方案：

- 

专线通信：通过专线的方案连接中心云VPC以及边缘侧的IDC或边缘设备，实现云边通过专线进行私网通信。

- 

公网隧道：通过云边运维通信组件Raven在云边之间的公网上构建反向隧道，通过反向隧道实现运维监控流量通信。要求边缘侧IDC或设备具有访问公网的能力。更多详细信息，请参见[跨域运维通信组件](products/ack/documents/ack-edge/user-guide/cloud-edge-communication-component-raven-overview.md)[Raven](products/ack/documents/ack-edge/user-guide/cloud-edge-communication-component-raven-overview.md)。

## 容器网络CNI

Kubernetes本身并未实现容器间的网络互联能力，但是它通过[容器网络接口（CNI）](https://github.com/containernetworking/cni/tree/main)对容器间的网络做出了标准化的定义：

- 

Pod在容器网络中的状态随着Pod生命周期而变化。例如，Pod创建后需要加入网络，销毁后需要退出网络。

- 

Pod在容器网络中拥有唯一的IP地址，以便于识别身份。

- 

Pod可以与集群内的端点与集群外的端点互相访问。

[容器网络插件（CNI Plugins）](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)负责容器网络的具体实现。容器网络插件决定了Pod IP地址分配的机制、是否使用Overlay网络、集群内流量的转发链路、对Pod的访问控制机制等容器网络特性。目前已经有很多知名的开源容器网络插件，如Calico、Flannel、Cilium等。

ACK Edge集群支持两种容器网络插件：Flannel与Terway Edge。这两种插件拥有不同的特性，请参照下方介绍，在创建集群前完成容器网络插件的选型。

重要

集群创建完成后，不支持Terway Edge与Flannel之间的变更切换。

### Flannel网络模式（Overlay容器网络）

在ACK Edge集群中Flannel采用了VXLAN模式，在三层主机网络上构建一层VXLAN容器网络，实现跨主机的Pod互访。

Flannel网络模式中Pod的网段独立于VPC的网段。Pod网段会按照掩码均匀划分给每个集群中的节点，每个节点上的Pod会从节点上划分的网段中分配IP地址。具有以下特点：

- 

Pod网段独立于VPC的虚拟网段。

- 

容器间数据包会通过主机进行VXLAN封包以进行传输。

- 

开箱即用，无需外部网络设备的额外配置。

关于Flannel网络插件详细信息，请参见[Flannel](products/ack/documents/ack-edge/user-guide/flannel-network-plugin.md)[网络插件](products/ack/documents/ack-edge/user-guide/flannel-network-plugin.md)。

### Terway Edge网络模式（Underlay容器网络）

在ACK Edge集群中，Terway Edge版在云端节点池中采用云原生的网络方案，直接基于阿里云VPC中的弹性网卡资源构建容器网络，Pod会通过弹性网卡直接分配VPC中的IP地址。在边缘节点池中则需要指定一个虚拟的Pod网段，容器会从这个虚拟的Pod网段中获取IP地址。具有以下特点：

- 

云端Pod网段与ECS同位于VPC网段中，在同一网络平面。

- 

边缘Pod网段独立于主机网络网段。

- 

容器间通信无需封包，相比于Overlay容器网络效率更高。

- 

需要配置外部网络设备的路由，实现容器网络包的传输。

- 

支持集群外主机、容器、云产品通过Pod IP直接访问集群内容器。

关于Terway Edge网络插件详细信息，请参见[Terway Edge](products/ack/documents/ack-edge/user-guide/terway-edge-network-plug-in-introduction.md)[网络插件](products/ack/documents/ack-edge/user-guide/terway-edge-network-plug-in-introduction.md)。

## Service概述

Service是可以对一组容器提供固定访问入口的服务暴露方式，支持以下多种模式，以满足不同来源和类型的客户端访问需求。

| 类型 | 说明 |
| --- | --- |
| ClusterIP | ClusterIP 类型的 Service 用于在集群内部实现应用间的访问。如果您的应用需要暴露到集群内部提供服务，可使用 ClusterIP 类型的 Service 进行暴露。 说明 创建 Service 时默认的 Service 类型为 ClusterIP。 |
| NodePort | NodePort 类型的 Service 通过集群节点上的一个固定端口，将应用向外部暴露，您就可以在集群外部通过节点的 IP 地址和端口访问集群内的应用。 |
| LoadBalancer | LoadBalancer 类型的 Service 同样是将集群内部部署的应用向外暴露，它通过阿里云的负载均衡进行暴露的，相对于 NodePort 方式，有更高的可用性和性能。关于如何通过 LB 类型的 Service 服务暴露，请参见 [使用负载均衡类型的](products/ack/documents/ack-edge/user-guide/expose-an-application-by-using-a-service-of-the-load-balancing-type.md) [Service](products/ack/documents/ack-edge/user-guide/expose-an-application-by-using-a-service-of-the-load-balancing-type.md) [暴露应用](products/ack/documents/ack-edge/user-guide/expose-an-application-by-using-a-service-of-the-load-balancing-type.md) 。 |
| Headless Service | Headless Service 类型的 Service 是在 Service 属性中指定 clusterIP 字段为 None 类型。采用 Headless Service 类型后，Service 将没有固定的虚拟 IP 地址，客户端访问 Service 的域名时会通过 DNS 返回所有的后端 Pod 实例的 IP 地址，客户端需要采用 DNS 负载均衡来实现对后端的负载均衡。 |
| ExternalName | ExternalName 类型的 Service 会在集群中将一个内部服务名称映射到一个外部域名。这种映射使得集群内的 Pod 可以通过 Service Name 来访问外部域名。 |


在ACK Edge集群中，由于计算资源通常分布在不同的网络域，针对分布式场景为您提供了以下能力。

| 类型 | 说明 |
| --- | --- |
| Service 的服务拓扑 | 当客户端和被访问的服务端 Pod 位于不同网络域时，通信将无法完成，采用 Service 服务拓扑能力后，客户端的请求只达到本网络域或本节点上的后端 Pod，相关操作，请参见 [节点池服务拓扑管理](products/ack/documents/ack-edge/user-guide/configure-a-service-topology.md) 。 |
| NodePort Service 的端口隔离 | 为了让多个网络域的 NodePort Service 进行端口隔离，您可以对所监听端口进行隔离，相关操作，请参见 [NodePort](products/ack/documents/ack-edge/user-guide/nodeport-service-isolation.md) [端口监听隔离](products/ack/documents/ack-edge/user-guide/nodeport-service-isolation.md) 。 |


## Ingress概述

在ACK Edge集群中，与Service的4层负载均衡不同，Ingress是集群内Service对外暴露7层的访问接入点，用于为集群中的多个Service提供统一的入口。您可以通过Ingress资源来配置不同的7层的转发规则，例如通过域名或者访问路径来路由到不同的Service上，从而达到7层的负载均衡作用。更多信息，请参见[Ingress](products/ack/documents/ack-edge/user-guide/edge-cluster-ingress-overview.md)[概述](products/ack/documents/ack-edge/user-guide/edge-cluster-ingress-overview.md)。

[上一篇：新增Pod虚拟交换机](products/ack/documents/ack-edge/user-guide/add-a-pod-vswitch.md)[下一篇：公网接入的网络配置](products/ack/documents/ack-edge/user-guide/network-configuration-for-public-network-access.md)

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
