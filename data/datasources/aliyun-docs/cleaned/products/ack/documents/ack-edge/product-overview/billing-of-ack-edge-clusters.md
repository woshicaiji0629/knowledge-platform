# ACK Edge集群如何收费-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/product-overview/billing-of-ack-edge-clusters

# ACK Edge集群计费说明
本文介绍ACK Edge集群计费说明、欠费说明和计费常见问题等相关信息。
## 计费说明
| 集群类型 | 集群管理费用 | 节点管理费用 | 云产品资源费用 |
| --- | --- | --- | --- |
| ACK Edge 集群 Pro 版 |  |  |  |
| ACK Edge 集群基础版 |  |  |  |
说明
以下计费示例仅供参考，实际费用以购买产品的控制台页面（或购买页面）为准。
### 集群管理计费
阿里云容器服务 Edge 版整合阿里云虚拟化、存储、网络和安全等能力，并简化集群运维工作，专注于容器化应用的开发与管理，所以针对ACK Edge集群Pro版会收取集群的管理费用。
| 计费方式 | 价格 |
| --- | --- |
| 按量计费 | 每个集群 0.64 元/小时 |
### 节点管理计费
阿里云容器服务 Edge 版支持丰富的异构边缘节点资源，包括自建IDC资源、[ENS](https://www.aliyun.com/product/ens)、IoT设备、X86、ARM架构等；并支持异构资源的混合调度，所以会收取非云端ECS的节点管理费用。例如，集群下有3台4 vCPU 8 GB的节点（其中1台是ECS，另外2台是ENS或者线下节点），边缘容器服务收取的费用为0.2元/vCPU/天∗2∗4vCPU=1.6元/天，使用时间不足一天，按一天计算。
默认情况下，节点管理费用采用按量付费的方式，也可以购买[容器服务边缘节点资源包](billing-of-ack-edge-clusters.md)来抵扣。
按量付费
| 计费方式 | 价格 |
| --- | --- |
| 按量计费 | 0.2 元/vCPU/天 |
容器服务边缘节点资源包
购买资源包
购买[容器服务边缘节点资源包](https://common-buy.aliyun.com/?commodityCode=csk_edgevcore_dp_cn)，以此抵扣ACK Edge集群对边缘节点的管理费用。
容器服务边缘节点资源包仅一种规格，支持购买多个，可叠加抵扣。
| 规格 | 说明 | 价格 | 有效期 |
| --- | --- | --- | --- |
| 500 vCPU | 按天抵扣，单个资源包可固定抵扣边缘节点 500 个 vCPU 365 天的按量计费账单。 | 12000 元 | 365 天。 开通时间可以选择购买后立即生效，也可以指定 6 个月内任意一天生效。 |
使用资源包
购买容器服务边缘节点资源包后，会自动抵扣阿里云账号下ACK Edge集群的边缘节点管理费用，无需进行操作。
抵扣时，遵循以下规则：
每天会固定抵扣掉500 vCPU核数的边缘节点（非云端ECS节点）的管理费。
本资源包不能抵扣已经产生的用量。
资源包耗尽或过期失效后，边缘节点管理费用将自动转为按量付费。
如果边缘节点的vCPU核数过多，可以叠加购买多个资源包。例如，如果边缘节点为1000 vCPU，可以购买2个边缘节点资源包，抵扣时会按下单顺序依次抵扣。请注意资源包生效日期。
查看资源包使用情况
购买容器服务边缘节点资源包后，可以通过以下操作查询资源包使用情况，并设置余量预警。
登录费用与成本页面。
说明
以下操作以新版（蓝色版）控制台为例。
在左侧导航栏，选择账户>资源包。
在资源维度处，选中资源包，然后在资源包列表中，筛选资源包类型为容器服务边缘节点资源包。
说明
单击列表右上角的图标可以设置列表显示的列；单击图标可以将列表信息导出为CSV文件。
根据需要进行以下操作。
## 查询整体用量
在实例汇总页签下，找到要操作的容器服务边缘节点资源包，单击对应操作列中的统计。
在弹出页面查看容器服务边缘节点的信息以及使用情况，包括失效时间、剩余量、实例抵扣情况等。
## 查看使用明细
单击使用明细页签。
设置查询条件，单击搜索。
查看容器服务边缘节点资源包的使用明细，包括抵扣量、被抵扣的集群ID、抵扣时间段等。
## 设置余量预警
在页面右上角单击余量预警设置。
在弹出的对话框中找到容器服务边缘节点资源包，开启预警并设置额度比例，然后单击确定。
### 云产品资源计费
如果在使用ACK Edge集群过程中使用了其他的阿里云云产品资源，需要按照各云产品规定的计费规则，为使用的这些资源付费，费用由各云产品收取。如果未使用其他阿里云云产品，则不收取云产品资源费用。
| 云产品名称 | 开通类型 | 产品说明 | 是否支持包年包月 | 是否支持资源包 | 计费说明 |
| --- | --- | --- | --- | --- | --- |
| [云服务器](../../../../ecs/documents/user-guide/what-is-ecs.md) [ECS](../../../../ecs/documents/user-guide/what-is-ecs.md) | 必选项 | 用于为 ACK Edge 集群 创建节点。 | 支持 | 不支持 | [计费概述](../../../../ecs/documents/billing-overview.md) |
| [边缘节点服务](https://help.aliyun.com/zh/ens/product-overview/what-is-ens) [ENS](https://help.aliyun.com/zh/ens/product-overview/what-is-ens) | 可选项 | 用于为 ACK Edge 集群 添加边缘节点。 | 支持 | 不支持 | [边缘节点服务](https://help.aliyun.com/zh/ens/product-overview/overview-5#concept-1828715) [ENS](https://help.aliyun.com/zh/ens/product-overview/overview-5#concept-1828715) [计费概览](https://help.aliyun.com/zh/ens/product-overview/overview-5#concept-1828715) |
| [专有网络](../../../../vpc/documents/what-is-vpc.md) [VPC](../../../../vpc/documents/what-is-vpc.md) | 必选项 | 用于构建集群网络环境和路由规则。 | 不支持 | 不支持 | [产品计费](../../../../vpc/documents/product-overview/product-billing.md) |
| [传统型负载均衡](../../../../slb/documents/classic-load-balancer/product-overview/what-is-clb.md) [CLB](../../../../slb/documents/classic-load-balancer/product-overview/what-is-clb.md) | 必选项 | 用于为 ACK Edge 集群 创建负载均衡。 | 不支持 说明 自 2024 年 12 月 01 日起，创建 ACK Edge 集群 时，API Server 关联的 CLB 实例不再支持包年包月。更多信息，请参见 [【产品公告】关于取消新增集群](../../product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [API Server](../../product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [负载均衡](../../product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [CLB](../../product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [包年包月付费的公告](../../product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) 。 | 不支持 | [CLB](../../../../slb/documents/classic-load-balancer/product-overview/billing-overview.md) [计费概述](../../../../slb/documents/classic-load-balancer/product-overview/billing-overview.md) |
| [弹性伸缩](https://help.aliyun.com/zh/auto-scaling/product-overview/what-is-auto-scaling#concept-25857-zh) [ESS](https://help.aliyun.com/zh/auto-scaling/product-overview/what-is-auto-scaling#concept-25857-zh) | 必选项 | 用于为 ACK Edge 集群 创建节点和实现自动伸缩。 | 不支持 | 不支持 | [产品计费](https://help.aliyun.com/zh/auto-scaling/product-overview/billing-rules#concept-nw2-h3m-qfb) |
| [容器镜像服务](https://help.aliyun.com/zh/acr/product-overview/what-is-container-registry#concept-2058233) [ACR](https://help.aliyun.com/zh/acr/product-overview/what-is-container-registry#concept-2058233) | 建议项 | 用于云原生资产的安全托管和全生命周期管理。 | 支持 说明 ACR 企业版实例仅支持按照实例的包年包月计费方式。更多信息，请参见 [企业版实例计费说明](https://help.aliyun.com/zh/acr/product-overview/billing-of-container-registry-enterprise-edition-instances#task-2273187) 。 | 不支持 | [计费说明](https://help.aliyun.com/zh/acr/product-overview/billing-description#concept-2047822) |
| [弹性公网](../../../../eip/documents/product-overview/what-is-eip.md) [IP](../../../../eip/documents/product-overview/what-is-eip.md) | 建议项 | 用于云资源与公网通信。 | 不支持 | 不支持 | [计费概述](../../../../eip/documents/billing-overview.md) |
| [弹性容器实例](https://help.aliyun.com/zh/eci/product-overview/what-is-elastic-container-instance#topic-1860079) | 建议项 | 用于部署集群。 | 不支持 | 不支持 | [计费概述](https://help.aliyun.com/zh/eci/product-overview/billing-overview#topic-1860085) |
| [服务网格](https://help.aliyun.com/zh/asm/product-overview/what-is-asm#concept-2366983) [ASM](https://help.aliyun.com/zh/asm/product-overview/what-is-asm#concept-2366983) | 建议项 | 基于 服务网格 实现多个集群应用的统一流量管理。 | 不支持 | 支持 说明 请参见 [网格管理计费（资源包）](https://help.aliyun.com/zh/asm/product-overview/billing-rules#section-tvp-y6a-85h) ，根据业务需要选购合适的资源包。 | [计费说明](https://help.aliyun.com/zh/asm/product-overview/billing-rules#concept-2370573) |
| [日志服务](../../../../sls/documents/what-is-log-service.md) [SLS](../../../../sls/documents/what-is-log-service.md) | 建议项 | 用于集群组件和应用的日志采集和检索。 | 不支持 | 支持 说明 可参考如下文档，根据业务需要选购合适的资源包： [选购资源包](../../../../sls/documents/purchase-a-resource-plan.md) 。 | [计费概述](../../../../sls/documents/billing-overview.md) |
| [CMS](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/what-is-cloudmonitor#concept-2452587) [云监控服务](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/what-is-cloudmonitor#concept-2452587) | 建议项 | 用于监控集群节点和应用运行状态。 | 不支持 | 支持 说明 可参考如下文档，根据业务需要选购合适的资源包： [计费概述](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/billing-overview) | [计费概述](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/billing-overview) |
| [可观测监控 Prometheus 版](../../../../arms/documents/prometheus-monitoring/product-overview/what-is-prometheus.md) | 建议项 | 基于 Prometheus 实现对集群的监控和告警。 | 不支持 | 不支持 | [按量计费](../../../../arms/documents/prometheus-monitoring/product-overview/pay-as-you-go.md) |
| [NAT 网关服务](../../../../nat-gateway/documents/product-overview/what-is-nat-gateway.md) | 可选项 | 用于为集群开启公网访问和公网镜像拉取。 | 不支持 | 支持 说明 可参考如下文档，根据业务需要选购合适的资源包： [NAT 网关资源包](../../../../nat-gateway/documents/nat-resource-plans.md) 。 | [NAT 网关计费](../../../../nat-gateway/documents/nat-gateway-billing.md) |
| [云安全中心](https://help.aliyun.com/zh/security-center/product-overview/what-is-security-center#concept-bjv-y5w-ydb) | 可选项 | 用于监控集群应用运行时的安全事件和告警。 | 不支持 | 不支持 | [计费说明](https://help.aliyun.com/zh/security-center/product-overview/billing-overview#concept-z2v-2bc-zdb) |
| [文件存储](https://help.aliyun.com/zh/nas/product-overview/what-is-nas#concept-qpg-wrt-1fb) [NAS](https://help.aliyun.com/zh/nas/product-overview/what-is-nas#concept-qpg-wrt-1fb) | 可选项 | 基于 NAS 实现集群应用数据的文件存储方案。 | 不支持 | 支持 说明 可参考如下文档，根据业务需要选购合适的资源包： [选购资源包](https://help.aliyun.com/zh/nas/product-overview/purchase-resource-plans#concept-53974-zh) 。 | [通用型](https://help.aliyun.com/zh/nas/product-overview/billing-of-general-purpose-nas-file-systems#task-2567548) [NAS](https://help.aliyun.com/zh/nas/product-overview/billing-of-general-purpose-nas-file-systems#task-2567548) [计费](https://help.aliyun.com/zh/nas/product-overview/billing-of-general-purpose-nas-file-systems#task-2567548) 和 [极速型](https://help.aliyun.com/zh/nas/product-overview/billing-of-extreme-nas-file-systems#task-2567605) [NAS](https://help.aliyun.com/zh/nas/product-overview/billing-of-extreme-nas-file-systems#task-2567605) [计费](https://help.aliyun.com/zh/nas/product-overview/billing-of-extreme-nas-file-systems#task-2567605) |
| [对象存储](../../../../oss/documents/user-guide/what-is-oss.md) [OSS](../../../../oss/documents/user-guide/what-is-oss.md) | 可选项 | 基于 OSS 实现集群应用数据的对象存储方案。 | 不支持 | 支持 说明 可参考如下文档，根据业务需要选购合适的资源包： [资源包购买指南](../../../../oss/documents/purchase-resource-plans.md) 。 | [计费概述](../../../../oss/documents/billing-overview.md) |
| [KMS](../../../../kms/documents/key-management-service/support/what-is-key-management-service.md) [密钥管理服务](../../../../kms/documents/key-management-service/support/what-is-key-management-service.md) | 可选项 | 用于集群应用密钥的管理以及 Pro 版集群开启密钥的落盘加密能力。 | 不支持 | 不支持 | [KMS 1.0](../../../../kms/documents/key-management-service/support/billing-of-kms.md) [计费说明](../../../../kms/documents/key-management-service/support/billing-of-kms.md) |
| [云备份](https://help.aliyun.com/zh/cloud-backup/product-overview/what-is-hbr#concept-62362-zh) | 可选项 | 提供备份、容灾保护以及策略化归档管理。 | 支持 | 支持 说明 可参考如下文档，根据业务需要选购合适的资源包： [资源包购买指南](https://help.aliyun.com/zh/cloud-backup/product-overview/purchase-resource-plans#concept-2531739) 。 | [计费方式与计费项](https://help.aliyun.com/zh/cloud-backup/product-overview/billing-methods-and-billable-items#concept-89062-zh) |
| [云企业网](../../../../cen/documents/product-overview/what-is-cen.md) | 可选项 | 用于在跨地域专有网络之间，以及专有网络与本地数据中心间搭建私网通信通道。 | 支持 说明 带宽包支持包年包月。 | 支持带宽包 说明 可参考如下文档，根据需求选择合适的带宽包操作： [使用带宽包](../../../../cen/documents/user-guide/work-with-a-bandwidth-plan.md) 。 | [计费说明](../../../../cen/documents/product-overview/billing-rules.md) |
## 欠费说明
如果账户余额不足以支付账单金额，ACK Edge集群会处于欠费状态，将无法访问集群API Server，但节点上的业务仍可继续运行。如果超过15天仍处于欠费状态，阿里云将暂停提供服务，从集群中移除相应节点（但不会释放）并删除ACK Edge集群及集群中的容器实例。因ACK Edge集群删除而释放的容器实例，将不可被恢复。
说明
阿里云提供延期免停权益，即当按量付费的资源发生欠费后，提供一定额度或时长继续使用云服务的权益，延停期间正常计费。具体使用说明和规则，请参见[延期免停权益](https://help.aliyun.com/zh/user-center/exemption-of-suspension-after-delinquency)。
## 退款说明
按量计费方式不涉及退款相关内容。
## 计费周期
容器服务 Edge 版费用的计费周期为24小时，即阿里云将在下一个自然日就上一个自然日的服务使用进行计量、出具账单，出具账单后从阿里云账户中按账单金额扣划服务费用。账单出账时间通常在当前计费周期结束后8至10个小时内。
## 查看账单
关于查看账单的具体操作，请参见[查看账单](../../ack-managed-and-ack-dedicated/product-overview/view-your-bills.md)。
## 计费常见问题
为什么会突然增加或减少每天的账单金额？
如果在使用过程中扩容或缩容了节点，系统会按照集群所管理的节点的总vCPU数调整计费，在第二天的出账中体现新的费用。
当未通过容器服务控制台移除节点时（如：使用kubectl delete node移除节点），被移除的节点在移除当天有可能还会被计费。因此请通过容器服务控制台移除节点。
删除了ACK Edge集群，为什么今天还会收到账单并被扣费？
ACK Edge集群管理费用以每天0时0分0秒至23时59分59秒为周期进行计费，第二天收费。所以昨天删除ACK Edge集群，昨天的计费系统已经计入，今天会出账单进行扣费，次日就不会出账单扣费了。
如何停止ACK Edge集群的计费？
删除所有地域的ACK Edge集群，删除集群前请注意备份应用和数据。
NotReady状态的节点是否会计费？
节点状态不论是Ready还是NotReady，ACK Edge集群都会对节点进行管理，因此NotReady状态的节点仍然会计费。必须通过容器服务控制台移除节点，相关节点才不会计费。
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
