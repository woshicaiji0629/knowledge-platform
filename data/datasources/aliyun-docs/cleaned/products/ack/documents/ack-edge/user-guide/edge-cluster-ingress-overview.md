# 集群服务七层负载均衡访问入口-边缘集群Ingress-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/edge-cluster-ingress-overview

# 边缘集群Ingress概述
在ACK Edge集群中，Ingress对集群服务（Service）中外部可访问的API对象进行管理，提供七层负载均衡能力。本文介绍Ingress基本概念、工作原理和使用说明。
## 基本概念
在ACK Edge集群中，Ingress作为服务对外暴露的访问入口，承载了集群内几乎所有的访问流量。Ingress是Kubernetes中的一个资源对象，用于管理集群外部对于内部服务的访问方式。通过配置Ingress资源，可以定义不同的转发规则，从而实现根据不同规则访问集群内部各Service对应的后端Pod。关于Ingress原理详情，请参见[Ingress](../../ack-managed-and-ack-dedicated/user-guide/ingress-management-2.md)[管理](../../ack-managed-and-ack-dedicated/user-guide/ingress-management-2.md)。
Ingress资源主要用于配置HTTP和HTTPS流量的规则，无法配置一些高级特性，例如负载均衡算法、会话亲和性（Session Affinity）等，这些高级特性需要在Ingress Controller中进行配置。
## 如何在ACK Edge集群部署Ingress Controller
ACK Edge集群在ACK托管集群Pro版的基础上扩展了边缘节点池功能，用于接入边缘节点和IDC机器。有关节点池的详细信息，请参见[节点池](../../ack-managed-and-ack-dedicated/user-guide/node-pool-overview.md)。ACK Edge集群分为以下两个部分。
云端节点池：包含位于集群VPC内的阿里云ECS计算设备等资源。
边缘节点池：集群中可以存在多个边缘节点池，这些节点池主要用于接入边缘节点和IDC机器。
Ingress Controller作为外部请求流量的入口，将对应的HTTP/HTTPS请求转发到后端Service关联的Pod中。您可以通过以下方法来部署Ingress Controller。
| 部署方式 | 特点 | 云边网络类型/流量拓扑 |
| --- | --- | --- |
| 节点池部署 | 在集群中每个有需要的节点池内部署一套 Ingress，仅支持 Nginx Ingress 类型。具体操作，请参见 [部署](install-the-nginx-ingress-controller.md) [Nginx Ingress Controller](install-the-nginx-ingress-controller.md) 。 | 专线：可选是否开启流量拓扑。 公网：必须开启流量拓扑。 |
| 云端部署 | 仅在云端节点池中部署一套 Ingress，支持 Nginx Ingress 和 ALB Ingress 两种类型。具体操作，请参见 [部署](install-the-nginx-ingress-controller.md) [Nginx Ingress Controller](install-the-nginx-ingress-controller.md) 、 [管理](../../ack-managed-and-ack-dedicated/user-guide/manage-the-alb-ingress-controller-1.md) [ALB Ingress Controller](../../ack-managed-and-ack-dedicated/user-guide/manage-the-alb-ingress-controller-1.md) [组件](../../ack-managed-and-ack-dedicated/user-guide/manage-the-alb-ingress-controller-1.md) 。 | 专线，不使用流量拓扑。 |
## 节点池部署
在云端节点池和边缘节点池分别部署Ingress Controller。
云端节点池的Ingress Controller通过LoadBalancer类型的Service对外暴露服务，使用阿里云CLB地址作为端点。
边缘节点池的Ingress Controller通过NodePort类型的Service对外暴露服务，使用节点池内任意节点的IP地址作为访问端点。
您需要配置Service流量拓扑，来确保外部请求通过Ingress Controller转发到后端Service时，流量仅限于转发到同一节点池内的后端Pod。具体操作，请参见[节点池服务拓扑管理](configure-a-service-topology.md)。
## 云端部署
只需在云端节点池部署Ingress Controller。
确保云端节点池和边缘节点池通过专线接入，实现内网互通，从而保证主机网络与容器网络的互联互通。
Ingress Controller通过LoadBalancer类型的Service对外暴露服务，使用阿里云CLB地址作为端点，外部请求通过Ingress Controller转发到Service的后端Pod，使用负载均衡策略，不使用流量拓扑。
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
