# ALB Ingress的工作原理及应用场景-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/user-guide/alb-ingress/

# ALB Ingress管理
ALB Ingress是阿里云推出的云原生Ingress网关，它与阿里云容器服务ACK/ACK Serverless等Kubernetes产品深度集成，支持将外部流量路由到集群内部，实现七层负载均衡。本文介绍ALB Ingress的基本概念、使用方法、产品优势及应用场景。
## ALB Ingress基本概念
阿里云容器服务ACK/ACK Serverless等Kubernetes产品，可以使用ALB Ingress，将集群外部流量路由到集群内部的Service，实现七层负载均衡功能。K8s集群中部署了ALB Ingress Controller组件，负责监听API Server中AlbConfig、Ingress、Service等资源的变化，并动态转换为ALB所需的配置。关于ALB Ingress Controller组件的介绍，请参见[ALB Ingress Controller](../../../../ack/documents/product-overview/alb-ingress-controller.md)。
## ALB Ingress的使用
ALB Ingress基于阿里云应用型负载均衡ALB（Application Load Balancer）之上提供更强的Ingress流量管理方式，兼容Nginx Ingress，具备处理复杂业务路由和证书自动发现的能力，支持HTTP、HTTPS和QUIC协议，满足在云原生应用场景下对弹性和大规模七层流量处理能力的需求。
### ALB Ingress使用流程
警告
ALBIngress由容器服务Kubernetes 管理，请勿在ALB控制台上进行配置，以免服务异常。关于ALB额度的更多信息，请参见[配额与限制](../product-overview/quotas-and-limits.md)。
ALB Ingress与云原生服务做了深度集成，在具备多种功能的同时也保证了易用性。使用ALB Ingress的操作流程如下：
| 功能 | 描述 |
| --- | --- |
| 安装 ALB Ingress Controller 组件 | 您可以在创建集群或组件管理页面安装 ALB Ingress Controller。具体操作，请参见： ACK 托管集群 、 ACK 专有集群 ： [管理](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-the-alb-ingress-controller-1.md) [ALB Ingress Controller](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-the-alb-ingress-controller-1.md) [组件](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-the-alb-ingress-controller-1.md) ACK Serverless 集群 ： [管理](../../../../ack/documents/serverless-kubernetes/user-guide/manage-the-alb-ingress-controller.md) [ALB Ingress Controller](../../../../ack/documents/serverless-kubernetes/user-guide/manage-the-alb-ingress-controller.md) [组件](../../../../ack/documents/serverless-kubernetes/user-guide/manage-the-alb-ingress-controller.md) 说明 ALB Ingress Controller 组件支持 1.18 及以上版本的集群。 如果您使用的是 Flannel 网络插件，则 ALB Ingress 后端 Service 服务仅支持 NodePort 和 LoadBalancer 类型。 |
| （可选）为专有集群授予 ALB Ingress Controller 访问权限 | 安装 ALB Ingress Controller 后，若需在 ACK 专有版集群中通过 ALB Ingress 访问服务，在部署服务前您还需要 [授予](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/grant-permissions-to-the-alb-ingress-controller.md) [ALB Ingress Controller](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/grant-permissions-to-the-alb-ingress-controller.md) [相关权限](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/grant-permissions-to-the-alb-ingress-controller.md) 。 |
| 创建 Service、Deployment 等后端服务 | 您可以在 K8s 中部署 Service、Deployment 等后端服务，作为 ALB Ingress 转发流量的目标。具体操作，请参见： ACK 托管集群 、 ACK 专有集群 ： [管理](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-the-alb-ingress-controller-1.md) [ALB Ingress Controller](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-the-alb-ingress-controller-1.md) [组件](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-the-alb-ingress-controller-1.md) ACK Serverless 集群 ： [管理](../../../../ack/documents/serverless-kubernetes/user-guide/manage-the-alb-ingress-controller.md) [ALB Ingress Controller](../../../../ack/documents/serverless-kubernetes/user-guide/manage-the-alb-ingress-controller.md) [组件](../../../../ack/documents/serverless-kubernetes/user-guide/manage-the-alb-ingress-controller.md) |
| （可选）创建 AlbConfig 与 IngressClass 资源 | 重要 如果您在安装 ALB Ingress Controller 组件时，为 ALB 云原生网关实例来源 选择了 新建 或 使用已有 选项，controller 会自动创建一个名为“alb”的 AlbConfig 和名为“alb”的 IngressClass 资源，您可忽略此步骤。 完成 ALB Ingress Controller 授权后，您可以创建 AlbConfig 和 IngressClass，并进行关联。具体操作，请参见： ACK 托管集群 、 ACK 专有集群 ： [创建](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-and-use-alb-ingress-to-expose-services-to-the-public.md) [AlbConfig](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-and-use-alb-ingress-to-expose-services-to-the-public.md) [与](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-and-use-alb-ingress-to-expose-services-to-the-public.md) [IngressClass](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-and-use-alb-ingress-to-expose-services-to-the-public.md) ACK Serverless 集群 ： [创建](../../../../ack/documents/serverless-kubernetes/user-guide/access-services-by-using-an-alb-ingress-2.md) [AlbConfig](../../../../ack/documents/serverless-kubernetes/user-guide/access-services-by-using-an-alb-ingress-2.md) [与](../../../../ack/documents/serverless-kubernetes/user-guide/access-services-by-using-an-alb-ingress-2.md) [IngressClass](../../../../ack/documents/serverless-kubernetes/user-guide/access-services-by-using-an-alb-ingress-2.md) |
| 创建 Ingress 资源 | 配置完以上步骤后，您可以创建 Ingress 资源，在 Ingress 中配置将用户请求流量转发到后端 Service 的转发规则，并将 Ingress 资源与 IngressClass 和 AlbConfig 关联。完成后，客户端就可以通过 ALB Ingress 访问 K8s 中的资源。具体操作，请参见： ACK 托管集群 、 ACK 专有集群 ： [创建](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-and-use-alb-ingress-to-expose-services-to-the-public.md) [Ingress](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-and-use-alb-ingress-to-expose-services-to-the-public.md) ACK Serverless 集群 ： [创建](../../../../ack/documents/serverless-kubernetes/user-guide/access-services-by-using-an-alb-ingress-2.md) [Ingress](../../../../ack/documents/serverless-kubernetes/user-guide/access-services-by-using-an-alb-ingress-2.md) |
说明
ALB Ingress不仅可以通过注解项配置转发规则，还可以通过注解项实现会话保持、灰度发布等高级功能。关于ALB Ingress其他功能，请参见：
容器集群ACK：[ALB Ingress](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/advanced-alb-ingress-configurations.md)[服务高级用法](../../../../ack/documents/ack-managed-and-ack-dedicated/user-guide/advanced-alb-ingress-configurations.md)
容器集群ACK Serverless：[ALB Ingress](../../../../ack/documents/serverless-kubernetes/user-guide/advanced-alb-ingress-settings.md)[服务高级用法](../../../../ack/documents/serverless-kubernetes/user-guide/advanced-alb-ingress-settings.md)
### ALB Ingress工作原理
ALB Ingress在兼容K8s原生功能基础上，还通过AlbConfig CRD和Ingress注解项提供了多种高级特性。
AlbConfig CRD：AlbConfig CRD用于配置ALB实例和监听。一个AlbConfig对应一个ALB实例。
Ingress注解项：用于配置转发规则，可将HTTP/HTTPS请求转发到对应的Service。
Service：后端真实服务的抽象，一个Service可以代表多个相同的后端服务。
## ALB Ingress的优势
ALB Ingress为全托管模式，提供更强的Ingress流量管理能力。Nginx Ingress需要用户自行维护，适用于对网关定制有强烈需求的场景。Nginx Ingress和ALB Ingress在产品定位、架构、性能、安全等方面均存在差异。更多差异请参见[Nginx Ingress](../../../../ack/documents/serverless-kubernetes/user-guide/comparison-among-nginx-ingresses-alb-ingresses-and-mse-ingresses.md)[和](../../../../ack/documents/serverless-kubernetes/user-guide/comparison-among-nginx-ingresses-alb-ingresses-and-mse-ingresses.md)[ALB Ingress](../../../../ack/documents/serverless-kubernetes/user-guide/comparison-among-nginx-ingresses-alb-ingresses-and-mse-ingresses.md)[对比](../../../../ack/documents/serverless-kubernetes/user-guide/comparison-among-nginx-ingresses-alb-ingresses-and-mse-ingresses.md)。
在以下场景中，ALB Ingress相比Nginx Ingress具有明显优势：
使用长连接的场景
长连接适用于交互频繁的业务场景，如物联网IoT、互联网金融和在线游戏等。当用户进行配置变更时，Nginx Ingress由于需要Reload Nginx进程，会导致长连接闪断，ALB Ingress配置变更支持热更新，保持长连接稳定，有效避免此问题。
高并发连接场景
物联网业务由于终端设备数量大，往往具有高并发连接的特点。ALB Ingress依托洛神云网络平台，能高效管理会话（session），单个ALB实例即支持千万级连接数。Nginx Ingress支持的会话数有限，同时需要用户自行运维。Nginx Ingress扩容时需要消耗集群内的资源，并且还需要用户手动操作，扩容成本较高。
高QPS场景
互联网业务往往具有高QPS的特点，比如预期内的大促活动和突发的热点事件。ALB Ingress支持自动弹性，高QPS时会自动弹出更多VIP，通过一个ALB实例即可支持百万QPS，因此ALB Ingress拥有比Nginx Ingress更低的延迟。同时Nginx Ingress依赖集群内的资源，在高QPS场景中更可能会遭遇性能瓶颈。
业务存在流量峰谷的场景
对于有波峰波谷的业务，比如电商和游戏，ALB Ingress拥有费用优势。ALB Ingress按量计费，流量波谷期间消耗较少的LCU，产生的费用更低，且因为自动弹性，用户无需关注和应对自身业务流量模型。而使用Nginx Ingress时则需要预留一部分集群资源，在波谷时会产生闲置成本，并且还需要手动设置与预留资源。
同城多活、异地多活容灾场景
对于业务连续性和可靠性有极高要求的行业和应用场景，比如社交网络平台和视频流媒体服务。您可以通过在分布式云容器平台ACK One创建[ALB](../../../../ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/alb-multi-cluster-gateway-overview.md)[多集群网关](../../../../ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/alb-multi-cluster-gateway-overview.md)，使用[ALB Ingress](../../../../ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/manage-north-south-traffic.md)[来管理多集群流量](../../../../ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/manage-north-south-traffic.md)，实现同城多活和异地多活的容灾方案。
## ALB Ingress应用场景
ALB Ingress具备高性能、自动弹性、免运维和开放可编程等特性。
多级负载和调度，单实例处理高达100万QPS。
软硬件一体化和硬件加速卡，具备高转发性能。
自动弹性简化运维，SLA多实例可用性高达99.995%。
自定义转发平台，提供多种高级路由特性。
ALB Ingress可覆盖多种业务场景，以下是几个常见的应用场景：
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
