# ACK Edge快速入门-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/quick-start

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

# 快速入门

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

容器服务 Edge 版是阿里云容器服务针对边缘计算场景推出的云边一体化协同托管方案，让您轻松高效地在云端实现对边缘侧资源和应用的统一管理。本文介绍ACK Edge集群使用前须知、快速使用流程、快速使用方式，帮助您快速上手。

## 使用前须知

使用ACK Edge集群前，您需要了解的信息以及注意事项，包括动态与公告、产品发布记录、使用须知、高危操作说明、开服地域等。

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

| 信息项 | 说明 | 相关文档 |
| --- | --- | --- |
| 动态与公告 | ACK Edge 集群 的产品动态与公告。 | [产品变更](products/ack/documents/product-overview/product-changes.md) [产品维护](products/ack/documents/product-overview/product-maintenance.md) [K8s](https://help.aliyun.com/zh/document_detail/2361875.html) [版本](https://help.aliyun.com/zh/document_detail/2361875.html) [组件变更](products/ack/documents/product-overview/components.md) [系统恢复](products/ack/documents/product-overview/system-restoration.md) [CVE](products/ack/documents/product-overview/security-bulletins.md) [漏洞修复](products/ack/documents/product-overview/security-bulletins.md) |
| 产品发布记录 | ACK Edge 集群 的产品功能、Kubernetes 版本、操作系统镜像、组件等的发布记录。 | [功能发布记录](products/ack/documents/product-overview/release-notes.md) [版本发布说明](products/ack/documents/ack-edge/user-guide/release-notes-for-kubernetes-versions-supported-by-ack-edge.md) [操作系统镜像发布记录](products/ack/documents/product-overview/release-notes-for-os-images.md) [组件介绍与发布记录](products/ack/documents/product-overview/release-notes-for-components.md) |
| 开服地域 | ACK Edge 集群 支持的地域。 | [开服地域](products/ack/documents/product-overview/supported-regions.md) |
| 支持时区 | ACK Edge 集群 支持的时区。 | [支持时区](products/ack/documents/product-overview/supported-time-zones.md) |
| 使用须知和高危操作说明 | 为了更好地预估和避免相关的操作风险，在使用 ACK Edge 集群 前，需了解本文的注意事项和高危操作说明。 | [使用须知及高危风险操作说明](products/ack/documents/product-overview/before-you-start.md) |
| 使用限制 | 使用 ACK Edge 集群 时涉及的限制，包括容量限制、配额限制等。 | [配额与限制](products/ack/documents/product-overview/limits.md) |


## 快速使用流程

ACK Edge集群支持将边缘侧的计算资源接入到同一Kubernetes集群中管理，同时还可以将云上已有的云产品能力下沉到边缘侧，从而提升边缘资源与业务的运维效率，保障业务的稳定运行。您可以参考以下方式，快速上手使用ACK Edge集群。

ACK Edge集群的快速使用流程如下所示：

### 环境准备

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

- 

| 流程 | 描述 | 参考文档 |
| --- | --- | --- |
| 准备网络环境 | 在创建 ACK Edge 集群 之前，需要先确认集群、节点接入所依赖的网络环境，以及确认所选用的网络插件。 | [如何选择网络插件](products/ack/documents/ack-edge/user-guide/how-to-choose-a-network-plug-in.md) [边缘节点访问域名和](products/ack/documents/ack-edge/user-guide/network-configuration-for-public-network-access.md) [IP](products/ack/documents/ack-edge/user-guide/network-configuration-for-public-network-access.md) [路由网段配置](products/ack/documents/ack-edge/user-guide/network-configuration-for-public-network-access.md) |
| 开通及授权 ACK | 在创建 ACK Edge 集群 之前，您需要免费开通相应服务。如果您在创建集群前没有开通容器服务 ACK，可能会导致集群无法创建或创建失败。 | [开通容器服务并为角色授权](products/ack/documents/ack-managed-and-ack-dedicated/getting-started/quick-start-for-first-time-users.md) |
| 创建集群 | 您可以通过容器服务控制台、OpenAPI 或 Terraform 的方式创建 ACK Edge 集群 。 | [创建](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md) [ACK Edge](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md) [集群](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md) [通过](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster.md) [OpenAPI](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster.md) [创建](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster.md) [ACK Edge](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster.md) [集群](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster.md) [通过](products/ack/documents/ack-edge/developer-reference/use-terraform-to-create-an-ack-edge-cluster.md) [Terraform](products/ack/documents/ack-edge/developer-reference/use-terraform-to-create-an-ack-edge-cluster.md) [创建](products/ack/documents/ack-edge/developer-reference/use-terraform-to-create-an-ack-edge-cluster.md) [ACK Edge](products/ack/documents/ack-edge/developer-reference/use-terraform-to-create-an-ack-edge-cluster.md) [集群](products/ack/documents/ack-edge/developer-reference/use-terraform-to-create-an-ack-edge-cluster.md) |
| 添加边缘节点 | ACK Edge 集群 支持纳管多种类型的资源，包括 IDC 节点、不同地域及云厂商的 ECS 节点、ENS 节点等，使用相关功能之前，您需要先将边缘侧节点添加到 ACK Edge 集群 中。 | [添加边缘节点](products/ack/documents/ack-edge/user-guide/add-an-edge-node.md) [添加](products/ack/documents/ack-edge/user-guide/add-a-gpu-node.md) [GPU](products/ack/documents/ack-edge/user-guide/add-a-gpu-node.md) [节点](products/ack/documents/ack-edge/user-guide/add-a-gpu-node.md) |


### 功能使用

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

| 类别 | 功能 | 描述 | 参考文档 |
| --- | --- | --- | --- |
| 边缘扩展能力 | 边缘网络自治 | 在边缘和云端网络断连状态下，您可以设置边缘网络自治，以确保边缘节点上的业务应用仍然可以持续稳定地运行，而不会被驱逐或者迁移到其他边缘节点。 | [设置边缘节点自治](products/ack/documents/ack-edge/user-guide/configure-node-autonomy.md) |
| 应用管理 | 在多地域节点和线下 IDC 等边缘场景中，您可以通过节点池应用集管理和 DaemonSet 升级扩展功能，增强边缘场景下的应用管理能力。 节点池应用集管理：通过 YurtAppSet，对多个工作负载（例如 Deployment）进行统一管理。 DaemonSet 升级扩展：通过配置扩展的 DaemonSet 升级模型 AdvancedRollingUpdate 和 OTA 以解决云边网络中断导致的升级阻塞以及 OTA 升级问题。 | [节点池应用集管理](products/ack/documents/ack-edge/user-guide/node-pool-yurtappset-management.md) [DaemonSet](products/ack/documents/ack-edge/user-guide/daemonset-upgrade-model.md) [升级模型](products/ack/documents/ack-edge/user-guide/daemonset-upgrade-model.md) |  |
| 跨地域通信 | 当云边资源不在同一个网络域时，您可以通过跨地域通信组件 Raven，实现多地域高效云边运维。 | [使用跨域运维通信组件](products/ack/documents/ack-edge/user-guide/using-the-cloud-side-communication-raven-component.md) [Raven](products/ack/documents/ack-edge/user-guide/using-the-cloud-side-communication-raven-component.md) |  |
| 离线运维 | 当您设置了边缘节点自治时，云端控制面无法对边缘业务做运维变更，在紧急情况下，您可以通过离线运维工具，对离线节点上的业务进行运维操作，例如业务回滚，资源变配，业务配置修改等。 | [边缘节点离线运维](products/ack/documents/ack-edge/user-guide/edge-node-offline-operation-and-maintenance-tool.md) |  |
| 云上弹性 | ECS 节点以及 ECI 和 ACS 实例弹性能力 | 当本地资源不足时， ACK Edge 集群 可以快速弹性扩容云上节点，支持基于 ECS 的云端节点池的弹性，以及基于 ECI、ACS 实例的弹性能力。 | [云端](products/ack/documents/ack-edge/user-guide/overview-of-node-scaling.md) [ECS](products/ack/documents/ack-edge/user-guide/overview-of-node-scaling.md) [节点弹性](products/ack/documents/ack-edge/user-guide/overview-of-node-scaling.md) [启用节点自动伸缩](products/ack/documents/ack-edge/user-guide/auto-scaling-of-nodes.md) [虚拟节点](products/ack/documents/ack-edge/user-guide/serverless-elastic-virtual-nodes.md) [Serverless](products/ack/documents/ack-edge/user-guide/serverless-elastic-virtual-nodes.md) [弹性](products/ack/documents/ack-edge/user-guide/serverless-elastic-virtual-nodes.md) |
| 云上能力下沉 | 可观测 | ACK Edge 集群 能够与监控、日志、NPD 等能力无缝融合，保障边缘业务的稳定运行。 | [通过阿里云](products/ack/documents/ack-edge/user-guide/monitor-ack-edge-clusters-with-managed-service-for-prometheus.md) [Prometheus](products/ack/documents/ack-edge/user-guide/monitor-ack-edge-clusters-with-managed-service-for-prometheus.md) [监控](products/ack/documents/ack-edge/user-guide/monitor-ack-edge-clusters-with-managed-service-for-prometheus.md) [ACK Edge](products/ack/documents/ack-edge/user-guide/monitor-ack-edge-clusters-with-managed-service-for-prometheus.md) [集群](products/ack/documents/ack-edge/user-guide/monitor-ack-edge-clusters-with-managed-service-for-prometheus.md) [通过日志服务采集](products/ack/documents/ack-edge/user-guide/use-log-service-to-collect-log-data-from-containers-of-ack-edge-clusters.md) [ACK Edge](products/ack/documents/ack-edge/user-guide/use-log-service-to-collect-log-data-from-containers-of-ack-edge-clusters.md) [集群的容器日志](products/ack/documents/ack-edge/user-guide/use-log-service-to-collect-log-data-from-containers-of-ack-edge-clusters.md) [收集](products/ack/documents/ack-edge/user-guide/collect-ack-edge-cluster-control-plane-component-logs.md) [ACK Edge](products/ack/documents/ack-edge/user-guide/collect-ack-edge-cluster-control-plane-component-logs.md) [集群控制平面组件日志](products/ack/documents/ack-edge/user-guide/collect-ack-edge-cluster-control-plane-component-logs.md) |
| AI 套件 | 在 AI 场景中， ACK Edge 集群 结合云上 AI 套件，提供了 AI 套件控制台、GPU 共享调度、KServe 以及 Fluid 加速等功能。 | [使用](products/ack/documents/ack-edge/user-guide/use-fluid-to-accelerate-access-to-oss-files-from-edge-nodes.md) [Fluid](products/ack/documents/ack-edge/user-guide/use-fluid-to-accelerate-access-to-oss-files-from-edge-nodes.md) [加速边缘节点访问](products/ack/documents/ack-edge/user-guide/use-fluid-to-accelerate-access-to-oss-files-from-edge-nodes.md) [OSS](products/ack/documents/ack-edge/user-guide/use-fluid-to-accelerate-access-to-oss-files-from-edge-nodes.md) [文件](products/ack/documents/ack-edge/user-guide/use-fluid-to-accelerate-access-to-oss-files-from-edge-nodes.md) [使用共享](products/ack/documents/ack-edge/user-guide/enable-gpu-sharing.md) [GPU](products/ack/documents/ack-edge/user-guide/enable-gpu-sharing.md) [调度能力](products/ack/documents/ack-edge/user-guide/enable-gpu-sharing.md) [使用](products/ack/documents/ack-edge/user-guide/user-guide-for-ack-kserve.md) [ack-kserve](products/ack/documents/ack-edge/user-guide/user-guide-for-ack-kserve.md) [组件](products/ack/documents/ack-edge/user-guide/user-guide-for-ack-kserve.md) [使用](products/ack/documents/ack-edge/user-guide/use-fluid-to-accelerate-access-to-oss-files-from-edge-nodes.md) [Fluid](products/ack/documents/ack-edge/user-guide/use-fluid-to-accelerate-access-to-oss-files-from-edge-nodes.md) [加速边缘节点访问](products/ack/documents/ack-edge/user-guide/use-fluid-to-accelerate-access-to-oss-files-from-edge-nodes.md) [OSS](products/ack/documents/ack-edge/user-guide/use-fluid-to-accelerate-access-to-oss-files-from-edge-nodes.md) [文件](products/ack/documents/ack-edge/user-guide/use-fluid-to-accelerate-access-to-oss-files-from-edge-nodes.md) |  |
| 镜像加速 | 通过镜像加速，能够大幅度提升镜像的拉取速度，减少应用的部署时间。 ACK Edge 集群 支持按需加载镜像和 P2P 加载两种镜像加速方式。 | [按需加载容器镜像](products/ack/documents/ack-edge/user-guide/load-resources-of-a-container-image-on-demand.md) [使用](products/ack/documents/ack-edge/user-guide/use-p2p-acceleration-feature.md) [P2P](products/ack/documents/ack-edge/user-guide/use-p2p-acceleration-feature.md) [加速](products/ack/documents/ack-edge/user-guide/use-p2p-acceleration-feature.md) |  |
| 安全管理 | 借助云上的安全能力，帮您提升云上资源和业务应用的安全治理效率。 ACK Edge 集群 支持集群审计、自定义 API Server 证书 SAN、Secret 落盘加密、RRSA 等。 | [使用集群](products/ack/documents/ack-edge/security-and-compliance/work-with-cluster-auditing.md) [API Server](products/ack/documents/ack-edge/security-and-compliance/work-with-cluster-auditing.md) [审计功能](products/ack/documents/ack-edge/security-and-compliance/work-with-cluster-auditing.md) [自定义集群](products/ack/documents/ack-edge/security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md) [API Server](products/ack/documents/ack-edge/security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md) [证书](products/ack/documents/ack-edge/security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md) [SAN](products/ack/documents/ack-edge/security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md) [使用阿里云](products/ack/documents/ack-edge/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) [KMS](products/ack/documents/ack-edge/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) [进行](products/ack/documents/ack-edge/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) [Secret](products/ack/documents/ack-edge/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) [的落盘加密](products/ack/documents/ack-edge/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md) [通过](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [RRSA](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [配置](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [ServiceAccount](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [RAM](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [权限实现](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [Pod](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [权限隔离](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) |  |


[上一篇：ACK Edge集群计费说明](products/ack/documents/ack-edge/product-overview/billing-of-ack-edge-clusters.md)[下一篇：操作指南](products/ack/documents/ack-edge/user-guide.md)

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
