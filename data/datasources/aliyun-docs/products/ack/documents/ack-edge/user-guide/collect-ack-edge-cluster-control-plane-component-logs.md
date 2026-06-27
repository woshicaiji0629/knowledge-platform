# 收集边缘容器集群控制平面组件日志-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/collect-ack-edge-cluster-control-plane-component-logs

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

# 收集ACK Edge集群控制平面组件日志

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

通过收集控制平面（Control Plane）组件日志可以帮助您更安全有效地运维集群，容器服务 Edge 版支持收集托管集群控制平面组件日志，您可以将控制平面组件日志从控制层采集到您账号中的日志服务SLS的Log Project中，以便集中管理和分析日志。

## 前提条件

- 

您账号下日志服务中的日志库配额充足，配额详情请参见[基础资源使用限制](products/sls/documents/basic-resources.md)。

- 

采集的日志将以日志流的形式发送到您账号下指定的日志服务的Log Project中，且日志服务使用统一的按量付费方式计费。计费信息，请参见[按使用功能计费](products/sls/documents/pay-as-you-go.md)。

## 开启收集控制平面组件日志

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择运维管理>日志中心。

- 

在日志中心页面，单击控制面组件日志页签，然后单击开启组件日志。

等待一段时间，安装完成后，自动跳转至控制平面组件日志页面。

## 查看集群控制面组件日志

您可以在容器服务控制台或日志服务控制台查看集群控制面组件日志。具体的查询语法，请参见[索引模式查询与分析](products/sls/documents/query-and-analyze-logs-in-index-mode.md)。

## 通过容器服务控制台查看

通过以下任一方式查看控制平面组件。

- 

通过集群信息入口查看控制平面组件。

- 

在集群信息管理页面单击基本信息页签，单击控制面组件日志右侧的链接。

- 

在页面左上角选择控制面组件后，查看组件日志信息。

- 

通过运维管理入口查看四种控制平面组件。

- 

在集群管理左侧导航栏中，选择运维管理>日志中心，然后单击控制面组件日志页签。

- 

在页面左上角选择控制面组件后，查看组件日志信息。

## 通过日志服务控制台查看

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标集群对应的日志服务Project名称。

- 

在日志存储>日志库页签中，单击目标日志库（Logstore）。

## 控制面组件Logstore说明

集群支持收集以下类型的控制面组件日志，每种日志服务Logstore对应一个Kubernetes控制面组件。关于这些组件的更多信息，请参见[Kubernetes](https://kubernetes.io/docs/concepts/overview/components/)[组件](https://kubernetes.io/docs/concepts/overview/components/)。

| 组件 | Logstore | 是否默认收集 | 说明 |
| --- | --- | --- | --- |
| [kube-apiserver](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/) | apiserver | 是 | kube-apiserver 组件是暴露 Kubernetes API 接口的控制层面的组件。 |
| [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/) | kcm | 是 | kube-controller-manager 组件是 Kubernetes 集群内部的管理控制中心，内嵌了 Kubernetes 发布版本中核心的控制链路。 |
| [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/) | scheduler | 是 | kube-scheduler 组件是 Kubernetes 集群的默认调度器。 |
| [Cloud Controller Manager](products/ack/documents/product-overview/cloud-controller-manager.md) | ccm | 是 | Cloud Controller Manager 提供 Kubernetes 与阿里云基础产品的对接能力，例如 CLB（原 SLB）、VPC 等，功能包括管理负载均衡、跨节点通信等。 |
| controlplane-events | controlplane-events | 是 | controlplane-events 组件支持投递集群控制面组件的运维事件，比如 OOM killed 事件等。 |
| [ALB Ingress Controller](products/ack/documents/product-overview/alb-ingress-controller.md) | alb | 是 | ALB Ingress 基于阿里云应用型负载均衡 ALB 服务，为集群中的 Service 提供统一的入口。 |
| [cluster-autoscaler](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/auto-scaling-of-nodes.md) | cluster-autoscaler | 否 | cluster-autoscaler 为 ACK 节点自动伸缩组件。 |
| [ack-goatscaler](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/instant-elasticity.md) | ack-goatscaler | 否 | ack-goatscaler 为 ACK 节点即时弹性组件。 |
| [kuberay-operator](products/ack/documents/cloud-native-ai-suite/use-cases/ray-cluster-best-practices.md) | kuberay-operator | 否 | kuberay-operator 基于社区 KubeRay 组件功能，并结合 容器服务 Kubernetes 版 的调度、弹性配额、资源优先级调度等能力，帮助您能更便捷地管理和使用 Ray 集群的服务。 |


说明

默认收集为否时，如果您需要采集该组件日志，需要通过[更新日志收集的组件列表](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-control-plane-component-logs-of-ack-managed-cluster.md)为指定组件开启日志收集功能。

## 关闭收集控制面组件日志功能

您可以通过运维管理入口关闭收集控制面组件日志功能。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择运维管理>日志中心。

- 

在日志中心页面，单击控制面组件日志页签，然后单击关闭。

## 相关文档

如需通过日志服务查询和分析日志，请参见[查询与分析快速指引](products/sls/documents/quick-guide-to-query-and-analysis.md)。

[上一篇：通过日志服务采集ACK Edge集群的容器日志](products/ack/documents/ack-edge/user-guide/use-log-service-to-collect-log-data-from-containers-of-ack-edge-clusters.md)[下一篇：AI套件](products/ack/documents/ack-edge/user-guide/cloud-native-ai-suite-overview.md)

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
