# 如何自定义Pro版集群的控制面核心组件参数-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/customize-ack-pro-control-plane-component-parameters-1693464061811

# 自定义Pro版集群的控制面组件参数
为了满足生产环境调整控制面参数的需求，容器服务 Kubernetes 版提供控制面参数自定义功能。您可以根据需要修改Kube API Server、Kube Controller Manager（KCM）、Cloud Controller Manager（CCM）、Kube Scheduler等核心托管组件的参数。本文介绍如何在容器服务管理控制台自定义控制面参数。
## 注意事项
为了保证控制面的稳定性，当前仅ACK托管集群Pro版、ACK Serverless集群Pro版、ACK Edge集群Pro版、ACK灵骏集群支持自定义部分控制面核心组件参数。
关于支持自定义的参数，请参见[默认参数列表](customize-ack-pro-control-plane-component-parameters-1693464061811.md)（具体请以控制台界面为准）。
部分参数仅支持特定版本的集群，如需升级集群，请参见[手动升级集群](update-the-kubernetes-version-of-an-ack-cluster.md)。
修改参数后，控制面会重启，请在业务低谷期操作。
自定义的参数会覆盖原集群的默认参数。自定义参数时，请确保输入的参数正确且完整，避免参数错误导致控制面启动失败。关于参数设置的详细信息，请根据集群版本参见Kubernetes官方文档[kube-apiserver](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)、[kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)、[kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/)。
## 自定义控制面组件参数
控制面组件参数修改的步骤类似。下文以修改Kube API Server组件为例，说明如何修改组件参数。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。
在核心组件区域，找到目标组件，然后单击卡片右下方的配置。
在Kube API Server 参数配置对话框中，输入自定义参数并确保参数完整且正确，按照页面提示完成配置的提交。
## 默认参数列表
## ACK托管集群Pro版
| 组件名 | 参数 | 参数说明 |
| --- | --- | --- |
| Kube API Server | enableAdmissionPlugins | 默认为空。 |
| serviceNodePortRange | 可选范围 10000～65535，默认为空。 重要 请谨慎修改 NodePort 端口范围，务必保证 NodePort 端口范围与集群节点上 Linux 内核提供的 net.ipv4.ip_local_port_range 参数的端口范围不冲突。更多信息，请参见 [如何正确配置](faq-about-network-management.md) [NodePort](faq-about-network-management.md) [范围？](faq-about-network-management.md) 。 |  |
| requestTimeout | 默认为空。 |  |
| defaultNotReadyTolerationSeconds | 默认为空。 |  |
| defaultUnreachableTolerationSeconds | 默认为空。 |  |
| maxMutatingRequestsInflight | 可选范围 1~1000，默认为空。 |  |
| maxRequestsInflight | 可选范围 1~3000，默认为空。 |  |
| featureGates | 可选参数包括 ServerSideApply 、 TTLAfterFinished 、 EphemeralContainers 、 RemoveSelfLink 、 HPAScaleToZero ，默认为空。 说明 支持在 1.18 及以上集群中使用 HPAScaleToZero ，不支持在 1.24 及以上集群中修改 RemoveSelfLink 。 |  |
| oidcIssuerURL | 默认为空。 支持 1.18 及以上集群。 重要 配置 oidcIssuerURL 后，集群中 API Server 会访问 oidcIssuerURL 配置项对应的地址，如果您的服务域名为公网域名，请确保集群已开启公网访问能力，具体操作请参见 [为集群开启访问公网的能力](enable-an-existing-ack-cluster-to-access-the-internet.md) 。 如果集群开启公网访问后，API Server 仍无法访问 oidcIssuerURL 配置项中的地址，您可以通过 kubectl get endpoints 来检查 Kubernetes 后端的 IP 数量。 如果 IP 大于 1 个，请登录 Worker 节点尝试访问 oidcIssuerURL，并检查公网配置、安全组规则等。 如果只有 1 个 IP，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 处理。 |  |
| oidcClientId | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcUsernameClaim | 默认值为 sub 。支持 1.18 以上集群。 |  |
| oidcUsernamePrefix | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcGroupsPrefix | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcGroupsClaim | 默认为空。支持 1.18 及以上集群。 |  |
| oidcRequiredClaim | 默认为空。支持 1.18 及以上集群。 |  |
| oidcCAContent | 默认为空。支持 1.18 及以上集群。 |  |
| hostAliases | 默认为空。支持 1.26 及以上集群。 |  |
| enableTrace | 默认为空。支持 1.28 及以上集群。 相关操作文档，请参见 [为集群控制面组件启用链路追踪](enable-tracing-for-control-plane-components.md) 。 |  |
| samplingRatePerMillion |  |  |
| Kube Controller Manager | horizontalPodAutoscalerSyncPeriod | 默认为空。 |
| horizontalPodAutoscalerTolerance | 默认为空。 |  |
| concurrentTTLAfterFinishedSyncs | 默认为空。 |  |
| concurrentHorizontalPodAutoscalerSyncs | 默认为空。支持 1.26 及以上集群。 |  |
| largeClusterSizeThreshold | 默认为空。 |  |
| unhealthyZoneThreshold | 默认为空。 |  |
| secondaryNodeEvictionRate | 默认为空。 |  |
| nodeEvictionRate | 默认为空。 |  |
| terminatedPodGCThreshold | 默认为空。 |  |
| kubeAPIQPS | 可选范围 1~1000，默认为空。 |  |
| kubeAPIBurst | 可选范围 1~1000，默认为空。 |  |
| concurrentCSRSyncs | 默认为空。支持 1.32 及以上集群。 |  |
| concurrentNodeTaintSyncs | 默认为空。支持 1.32 及以上集群。 |  |
| featureGates | 可选参数为 TTLAfterFinished ，默认为空。 |  |
| Cloud Controller Manager | routeTableIDs | 默认为空。如果 VPC 内有多个路由表，可以手动设置 CCM 支持多个路由表 ID，以半角逗号（,）分隔，例如 vtb-**,vtb*** 。 |
| Kube Scheduler | 关于通过 Kube Scheduler 自定义参数，请参见 [自定义调度器参数](customize-the-scheduler-parameters.md) 。 |  |
## ACK Serverless集群Pro版
| 组件名 | 参数 | 参数说明 |
| --- | --- | --- |
| Kube API Server | enableAdmissionPlugins | 默认为空。 |
| requestTimeout | 默认为空。 |  |
| defaultNotReadyTolerationSeconds | 默认为空。 |  |
| defaultUnreachableTolerationSeconds | 默认为空。 |  |
| maxMutatingRequestsInflight | 可选范围 1~1000，默认为空。 |  |
| maxRequestsInflight | 可选范围 1~3000，默认为空。 |  |
| featureGates | 可选参数包括 ServerSideApply 、 TTLAfterFinished 、 EphemeralContainers 、 RemoveSelfLink 、 HPAScaleToZero ，默认为空。 说明 支持在 1.18 及以上集群中使用 HPAScaleToZero ，不支持在 1.24 及以上集群中修改 RemoveSelfLink 。 |  |
| oidcIssuerURL | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcClientId | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcUsernameClaim | 默认值为 sub 。支持 1.18 以上集群。 |  |
| oidcUsernamePrefix | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcGroupsPrefix | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcGroupsClaim | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcRequiredClaim | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcCAContent | 默认为空。 支持 1.18 及以上集群。 |  |
| Kube Controller Manager | horizontalPodAutoscalerSyncPeriod | 默认为空。 |
| horizontalPodAutoscalerTolerance | 默认为空。 |  |
| concurrentTTLAfterFinishedSyncs | 默认为空。 |  |
| kubeAPIQPS | 可选范围 1~1000，默认为空。 |  |
| kubeAPIBurst | 可选范围 1~1000，默认为空。 |  |
| featureGates | 可选参数为 TTLAfterFinished ，默认为空。 |  |
| Kube Scheduler | 涉及多个。目前白名单开放中。 | 关于通过 Kube Scheduler 自定义参数，请参见 [自定义调度器参数](customize-the-scheduler-parameters.md) 。 |
## ACK Edge集群Pro版
| 组件名 | 参数 | 参数说明 |
| --- | --- | --- |
| Kube API Server | enableAdmissionPlugins | 默认为空。 |
| serviceNodePortRange | 可选范围 10000～65535，默认为空。 重要 您在修改 NodePort 端口范围时必须十分谨慎。务必保证 NodePort 端口范围与集群节点上 Linux 内核提供的 net.ipv4.ip_local_port_range 参数的端口范围不冲突。更多信息，请参见 [如何正确配置](faq-about-network-management.md) [NodePort](faq-about-network-management.md) [范围？](faq-about-network-management.md) 。 |  |
| requestTimeout | 默认为空。 |  |
| defaultNotReadyTolerationSeconds | 默认为空。 |  |
| defaultUnreachableTolerationSeconds | 默认为空。 |  |
| maxMutatingRequestsInflight | 可选范围 1~1000，默认为空。 |  |
| maxRequestsInflight | 可选范围 1~3000，默认为空。 |  |
| featureGates | 可选参数包括 ServerSideApply 、 TTLAfterFinished 、 EphemeralContainers 、 RemoveSelfLink 、 HPAScaleToZero ，默认为空。 说明 支持在 1.18 及以上集群中使用 HPAScaleToZero ，不支持在 1.24 及以上集群中修改 RemoveSelfLink 。 |  |
| oidcIssuerURL | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcClientId | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcUsernameClaim | 默认值为 sub 。支持 1.18 以上集群。 |  |
| oidcUsernamePrefix | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcGroupsPrefix | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcGroupsClaim | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcRequiredClaim | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcCAContent | 默认为空。 支持 1.18 及以上集群。 |  |
| Kube Controller Manager | horizontalPodAutoscalerSyncPeriod | 默认为空。 |
| concurrentTTLAfterFinishedSyncs | 默认为空。 |  |
| largeClusterSizeThreshold | 默认为空。 |  |
| unhealthyZoneThreshold | 默认为空。 |  |
| secondaryNodeEvictionRate | 默认为空。 |  |
| nodeEvictionRate | 默认为空。 |  |
| podEvictionTimeout | 默认为空。 |  |
| kubeAPIQPS | 可选范围 1~1000，默认为空。 |  |
| kubeAPIBurst | 可选范围 1~1000，默认为空。 |  |
| featureGates | 可选参数为 TTLAfterFinished ，默认为空。 |  |
| Cloud Controller Manager | routeTableIDs | 默认为空。如果 VPC 内有多个路由表，可以手动设置 CCM 支持多个路由表 ID，以半角逗号（,）分隔，例如 vtb-**,vtb*** 。 |
| Kube Scheduler | 关于通过 Kube Scheduler 自定义参数，请参见 [自定义调度器参数](customize-the-scheduler-parameters.md) 。 |  |
## ACK灵骏集群
| 组件名 | 参数 | 参数说明 |
| --- | --- | --- |
| Kube API Server | enableAdmissionPlugins | 默认为空。 |
| serviceNodePortRange | 可选范围 10000～65535，默认为空。 重要 请谨慎修改 NodePort 端口范围，务必保证 NodePort 端口范围与集群节点上 Linux 内核提供的 net.ipv4.ip_local_port_range 参数的端口范围不冲突。更多信息，请参见 [如何正确配置](faq-about-network-management.md) [NodePort](faq-about-network-management.md) [范围？](faq-about-network-management.md) 。 |  |
| requestTimeout | 默认为空。 |  |
| defaultNotReadyTolerationSeconds | 默认为空。 |  |
| defaultUnreachableTolerationSeconds | 默认为空。 |  |
| maxMutatingRequestsInflight | 可选范围 1~1000，默认为空。 |  |
| maxRequestsInflight | 可选范围 1~3000，默认为空。 |  |
| featureGates | 可选参数包括 ServerSideApply 、 TTLAfterFinished 、 EphemeralContainers 、 RemoveSelfLink 、 HPAScaleToZero ，默认为空。 说明 支持在 1.18 及以上集群中使用 HPAScaleToZero ，不支持在 1.24 及以上集群中修改 RemoveSelfLink 。 |  |
| oidcIssuerURL | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcClientId | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcUsernameClaim | 默认值为 sub 。支持 1.18 以上集群。 |  |
| oidcUsernamePrefix | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcGroupsPrefix | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcGroupsClaim | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcRequiredClaim | 默认为空。 支持 1.18 及以上集群。 |  |
| oidcCAContent | 默认为空。 支持 1.18 及以上集群。 |  |
| Kube Controller Manager | horizontalPodAutoscalerSyncPeriod | 默认为空。 |
| horizontalPodAutoscalerTolerance | 默认为空。 |  |
| concurrentTTLAfterFinishedSyncs | 默认为空。 |  |
| largeClusterSizeThreshold | 默认为空。 |  |
| unhealthyZoneThreshold | 默认为空。 |  |
| secondaryNodeEvictionRate | 默认为空。 |  |
| nodeEvictionRate | 默认为空。 |  |
| podEvictionTimeout | 默认为空。 |  |
| kubeAPIQPS | 可选范围 1~1000，默认为空。 |  |
| kubeAPIBurst | 可选范围 1~1000，默认为空。 |  |
| featureGates | 可选参数为 TTLAfterFinished ，默认为空。 |  |
| Cloud Controller Manager | routeTableIDs | 默认为空。如果 VPC 内有多个路由表，可以手动设置 CCM 支持多个路由表 ID，以半角逗号（,）分隔，例如 vtb-**,vtb*** 。 |
| Kube Scheduler | 关于通过 Kube Scheduler 自定义参数，请参见 [自定义调度器参数](customize-the-scheduler-parameters.md) 。 |  |
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
