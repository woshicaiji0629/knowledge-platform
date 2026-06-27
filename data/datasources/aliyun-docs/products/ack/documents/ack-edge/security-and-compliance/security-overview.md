# 如何使用安全概览-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/security-overview

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

# 安全概览

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

容器服务ACK提供安全概览功能，支持对节点、容器镜像、容器运行时、工作负载配置进行风险识别及安全加固，可以帮助您提升云上资源和业务应用的安全治理效率。本文介绍如何使用容器服务ACK的安全概览功能。

## 使用说明

该功能目前处于邀测中，如需使用，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)。

除了容器运行时风险，由于其他节点漏洞、容器镜像风险、工作负载配置风险数据会有24小时延时，在初次授权开启使用或风险修复完成后，需等待24小时，才可以在安全概览页面看到最新数据。

## 查看安全概览

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。

- 

在集群信息页面，单击安全概览页签。

安全概览会展示两个维度的风险。其中红框部分的数据表示从风险视角分析的结果，蓝框部分的数据表示从资产视角分析的结果。例如，节点漏洞中，从风险视角看，该集群共出现5个高危风险，从资产视角看，该集群共有2个节点池，该高危风险存在1个节点池中。页面右侧容器安全能力概览区域列出集群审计、策略管理、容器运行时安全、容器镜像安全、节点池安全五项能力入口，每项提供使用和文档链接。页面下方可按风险类别切换查看具体漏洞详情，包含漏洞名称、关联CVE编号、影响节点数及修复操作。

| 类别 | 说明 |
| --- | --- |
| [集群安全风险](products/ack/documents/ack-edge/security-and-compliance/security-overview.md) | 展示集群整体安全状态。 |
| [节点漏洞](products/ack/documents/ack-edge/security-and-compliance/security-overview.md) | 展示节点漏洞风险，默认开启。 |
| [容器镜像风险](products/ack/documents/ack-edge/security-and-compliance/security-overview.md) | 用于识别来自容器镜像服务企业版 ACR EE 上容器镜像的安全风险，需授权后使用。 |
| [容器运行时风险](products/ack/documents/ack-edge/security-and-compliance/security-overview.md) | 用于实时查看容器运行时风险并进行运行时实时防护。容器运行时风险基于云安全中心来做相关诊断，需 开通云安全中心 旗舰版 。 |
| [工作负载配置风险](products/ack/documents/ack-edge/security-and-compliance/security-overview.md) | 帮您实时了解当前状态下运行应用的配置是否有安全隐患，需开启配置巡检功能后使用。 |


## 集群安全风险

集群安全风险用于展示容器集群的安全风险等级，具体定义如下。

- 

健康

当节点漏洞无高危风险时，集群中已开启容器镜像风险、容器运行时风险、工作负载配置风险扫描，且扫描结果无高危风险，则集群安全风险等级为健康。

- 

高危

当节点漏洞出现高危或者容器运行时出现高危时，集群安全风险等级为高危。

- 

中危

其他情况均为中危。

## 节点漏洞

节点漏洞检查默认开启。

在安全概览页面下方，单击节点漏洞页签，查看节点漏洞列表，包含对应的节点池以及影响该节点池中的节点数，然后单击修复即可跳转至节点池详情页面进行漏洞修复。关于节点池CVE漏洞修复，请参见[修复节点池操作系统](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cve-patching.md)[CVE](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cve-patching.md)[漏洞](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cve-patching.md)。

说明

漏洞修复完成后，安全概览页面的相关数据还需等待24小时才会刷新。

## 容器镜像风险

您需要提前给ACR授权，单击容器镜像风险卡片上的去授权，根据提示完成授权相关操作。您也可以单击移除权限关闭容器镜像风险分析能力。

说明

授权完成后，会有24小时延时，才会显示当前集群下正在运行的容器镜像个数，并关联对应来自ACR EE的容器镜像的安全风险。

在安全概览页面下方，单击容器镜像风险页签，查看容器镜像风险列表项，包含对应容器镜像的地址、受影响容器、扫描时间等详情，然后单击修复即可跳转至ACR EE对应的镜像风险详情页面，查看风险详情并修复。

说明

风险修复完成后，安全概览页面的相关数据还需等待24小时才会刷新。

## 容器运行时风险

容器运行时风险基于云安全中心来做相关诊断，您需要提前购买云安全中心的高级版及以上版本。更多信息，请参见[购买云安全中心](https://help.aliyun.com/zh/security-center/user-guide/purchase-security-center#task-lxj-3bc-zdb)。云安全中心购买完成后，可实时查看容器运行时风险并进行运行时实时防护。

在安全概览页面下方，单击容器运行时风险页签，查看容器运行时风险列表项，包含对应的告警名称、告警描述，然后单击处理即可跳转至安全监控页面进行风险治理。

## 工作负载配置风险

您需要提前开启配置巡检功能。开启配置巡检后，会有24小时延时，才会显示当前集群下的工作负载配置情况及风险情况。具体操作，请参见[执行巡检](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-the-inspection-feature-to-detect-security-risks-in-the-workloads-of-an-ack-cluster.md)。

在安全概览页面下方，单击工作负载配置风险页签，查看对应的风险描述以及对应的加固建议，然后单击查看详情即可跳转至集群的配置巡检页面进行风险修复。

说明

风险修复完成后，安全概览页面的相关数据还需等待24小时才会刷新。

[上一篇：安全责任共担模型](products/ack/documents/ack-edge/security-and-compliance/shared-responsibility-model.md)[下一篇：基础设施安全](products/ack/documents/ack-edge/security-and-compliance/infrastructure-security.md)

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
