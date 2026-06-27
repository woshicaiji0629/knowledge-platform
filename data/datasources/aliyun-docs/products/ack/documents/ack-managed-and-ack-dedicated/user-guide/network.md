# 容器网络互联负载均衡服务发现-网络-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/network

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-managed-and-ack-dedicated/product-overview.md)

- [快速入门](products/ack/documents/ack-managed-and-ack-dedicated/getting-started.md)

- [操作指南](products/ack/documents/ack-managed-and-ack-dedicated/user-guide.md)

- [实践教程](products/ack/documents/ack-managed-and-ack-dedicated/use-cases.md)

- [安全合规](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference.md)

- [服务支持](products/ack/documents/ack-managed-and-ack-dedicated/support.md)

[首页](https://help.aliyun.com/zh)

# 网络概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

容器服务 Kubernetes 版 ACK（Container Service for Kubernetes）将Kubernetes网络设计应用到了阿里云的资源上，提供了稳定高性能的容器网络。本文介绍ACK中容器网络的重要概念，例如容器网络插件CNI、Service、Ingress、提供服务发现能力的DNS等。您可以通过了解这些概念，更合理地设计应用部署模型和网络访问的方式。

## 容器网络插件（CNI Plugin）

Kubernetes本身并未实现容器间的网络互联能力，但是它通过[容器网络接口（CNI）](https://github.com/containernetworking/cni/tree/main)对容器间的网络做出了标准化的定义：

- 

Pod在容器网络中的状态随着Pod生命周期而变化。例如，Pod创建后需要加入网络，销毁后需要退出网络。

- 

Pod在容器网络中拥有唯一的IP地址，以便于识别身份。

- 

Pod可以与集群内的端点与集群外的端点互相访问。

[容器网络插件（CNI Plugins）](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)负责容器网络的具体实现。容器网络插件决定了Pod IP地址分配的机制、是否使用Overlay网络、集群内流量的转发链路、对Pod的访问控制机制等容器网络特性。目前已经有很多知名的开源容器网络插件，如Calico、Flannel、Cilium等。

容器服务 Kubernetes 版支持两种容器网络插件：Terway与Flannel。这两种插件拥有不同的特性，请参照下方的介绍以及[Terway](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)[与](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)[Flannel](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)[的对比](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)文档，在创建集群前完成容器网络插件的选型。

重要

集群创建完成后，不支持Terway与Flannel之间的变更切换。

### Terway容器网络插件

Terway网络插件是阿里云自研的容器网络插件。在容器服务 Kubernetes 版中作为节点的ECS实例使用ENI（[弹性网卡](products/ecs/documents/user-guide/eni-overview.md)）进行网络通信，Terway将节点的ENI分配给Pod，为Pod提供了网络互联能力。因此，在使用Terway时，Pod直接接入VPC网络。由于不需要使用VXLAN等隧道技术封装报文，Terway模式网络具有较高的通信性能。Terway适用于大规模集群以及对网络性能和访问控制能力有较高需求的场景。

在创建集群并安装Terway网络插件时，可以为Terway配置不同的工作模式。这些工作模式的区别主要在以下三个维度：

- 

Pod IP地址分配：Terway拥有两种IP地址分配模式：独占ENI模式与共享ENI模式。独占ENI模式中，Pod独占节点的ENI，拥有极致的网络性能；而共享ENI模式中，Pod共享节点的ENI，拥有更高的部署密度。

- 

网络加速能力：共享ENI模式支持DataPathv2加速模式。选择加速模式后，Terway会采取不同于共享ENI常规模式的流量转发链路，实现更快的网络通信。

- 

访问控制能力：共享ENI模式与独占ENI模式都支持为Pod配置固定IP、独立的安全组与虚拟交换机，独占ENI模式支持通过Kubernetes原生的Network Policy进行访问控制。

### Flannel容器网络插件

[Flannel](https://github.com/flannel-io/flannel)是一个经典的开源容器网络插件，它使用VXLAN等虚拟化网络技术为Pod构建了一个Overlay网络。Flannel的配置简单、易于使用，但是网络性能会受到NAT损失的影响，访问控制能力相较于Terway也更弱，并且集群的节点数量上限较低。Flannel适用于节点数量不超过1000的小规模集群，以及对网络性能和访问控制能力需求较低，希望快速搭建、使用集群的场景。

重要

关于Terway和Flannel插件的详细能力对比，请参见[Terway](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)[与](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)[Flannel](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)[的对比](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)。

## 服务（Service）

由于云原生应用通常需要敏捷的迭代和快速的弹性，Pod在Kubernetes中被认为是临时性的、随时可替换的资源。当Pod被销毁、替换时，与其相关的网络资源也会发生变化，因此需要为Pod提供固定的访问方式。Kubernetes采用Service方式为一组拥有相同功能的容器提供固定的访问入口，并对这一组容器进行负载均衡。实现原理如下：

- 

通过Selector关联一组容器，以将这个Service的IP地址和端口负载均衡到这一组容器IP和端口上。

- 

在Pod发生变化时，Service会自动更新后端的转发规则，以保证通过Service能访问到最新的Pod。

ACK集群中的Service目前支持ClusterIP、NodePort、LoadBalancer、Headless Service、ExternalName模式，适用于集群内访问、集群外访问、公网访问等场景，详细信息请参见[Service](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/service-management.md)[管理](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/service-management.md)。

## 路由（Ingress）

在ACK集群中，与Service的4层负载均衡不同，Ingress是集群内Service对外暴露7层的访问接入点，用于为集群中的多个Service提供统一的入口。您可以通过Ingress资源来配置不同的7层的转发规则，例如通过域名或者访问路径来路由到不同的Service上，从而达到7层的负载均衡作用。更多信息，请参见[Ingress](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ingress-management-2.md)[管理](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ingress-management-2.md)。

## 服务发现DNS

ACK使用DNS来实现应用的服务发现能力，例如客户端应用可以通过Service的服务名解析出它的ClusterIP访问，再通过Service访问后端Pod。采用DNS服务发现的能力让集群中应用间的调用与IP地址和部署环境解耦。关于集群DNS组件的详细信息，请参见[服务发现](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/service-discovery-dns-1.md)[DNS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/service-discovery-dns-1.md)。

## 相关文档

- 

在创建集群后，为Pod、Service、节点分配的网段无法修改。网段的大小决定这三种资源的数量上限，可能会对您的业务部署产生影响。规划不同的网段可以实现资源在网络逻辑上的隔离，以便于您实现访问控制、定制化路由等操作。因此推荐您在创建集群前完成网段规划。Terway与Flannel两种容器网络插件拥有不同的特性，需要使用不同的网络规划策略，推荐您阅读[Terway](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)[与](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)[Flannel](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)[的对比](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)了解它们的具体差别，然后参见[Kubernetes](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/kubernetes-cluster-network-planning.md)[集群网络规划](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/kubernetes-cluster-network-planning.md)完成网段规划。

- 

ACK集群网络的常见问题，请参见[网络管理](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-network-management.md)[FAQ](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-network-management.md)。

[上一篇：工作负载FAQ](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-applications.md)[下一篇：容器网络插件Terway与Flannel对比](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)

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
