# ACK集群生命周期及异常状态说明-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/cluster-abnormal-states

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

# ACK集群生命周期及异常状态说明

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ACK集群的生命周期涉及多个阶段和状态，从集群的创建部署、运行维护（扩容缩容、更新升级、排水移除等），到最终的删除。本文介绍ACK集群的全生命周期，帮助您更好地理解和管理集群。

## 集群生命周期

ACK集群在不同状态下的含义和状态流转如下。

重要

- 

ACK会定时检测集群运行状态。如符合特定异常条件，集群将自动变为不活跃（inactive）或不可用（unavailable）。届时，ACK会通过短信、邮件、站内信的方式发送相关通知。

- 

对于ACK托管集群Pro版，可参见下表了解对应状态的集群是否收取集群管理费用。ACK计费说明，请参见[计费概述](products/ack/documents/ack-managed-and-ack-dedicated/product-overview/ack-pro-cluster-billing.md)。

- 

集群关联云产品的计费策略以各云产品为准，请参见[云产品资源费用](products/ack/documents/ack-managed-and-ack-dedicated/product-overview/billing-of-cloud-services.md)。

| 阶段 | 集群状态 | 说明 | 集群管理费 （ ACK 托管集群 Pro 版 ） |
| --- | --- | --- | --- |
| 创建部署 | 初始化中（initial） | 集群创建中。 | 不收取 |
| 创建失败（failed） | 集群创建失败。 |  |  |
| 运行维护 | 运行中（running） | 集群运行中。 | 收取 |
| 升级中（upgrading） | 集群升级中。 |  |  |
| 节点排水中（draining） | 正在将节点上的 Pod 驱逐并在其他节点上重建；完成后该节点将处于不可调度状态。 |  |  |
| 节点移除中（removing） | 正在移除集群中的节点。 |  |  |
| 配置变更中（updating） | 集群元信息更新中。 |  |  |
| 不活跃（inactive） | 特定异常条件下，集群暂时无法使用。详见 [不活跃（inactive）](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cluster-abnormal-states.md) 。 | 不收取 |  |
| 不可用（unavailable） | 集群基础云资源异常，集群不再可用。详见 [不可用（unavailable）](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cluster-abnormal-states.md) 。 |  |  |
| 删除释放 | 删除中（deleting） | 集群删除中。 | 不收取 |
| 删除失败（delete_failed） | 删除集群失败。 |  |  |
| 已删除（deleted） | 成功删除集群。该状态下集群不再可见。 |  |  |


## 集群异常状态说明

### 不活跃（inactive）

不活跃（inactive）状态可能由不同原因导致，您可以通过状态码判断具体的异常原因。

- 

- 

- 

- 

- 

| 状态码 | 异常状态 | 解决方案 |
| --- | --- | --- |
| KMSUnhealthy | 集群开启了使用阿里云密钥管理服务 KMS 进行 Secret 的落盘加密功能，且由于阿里云账号欠费或其他原因导致 KMS 服务暂停，使得集群控制面无法正常运行。 | 登录 [密钥管理服务控制台](https://kms.console.aliyun.com) 。 查看 KMS 服务暂停的原因，并恢复 KMS 服务。 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) ，联系技术支持人员恢复集群状态。 |
| NoNodeForLongTime | ACK 托管集群基础版 中没有节点，且集群中连续 14 天没有节点。 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 恢复集群的状态，恢复后将集群升级为 ACK 托管集群 Pro 版 。 |
| AssumeRoleNotFound | 系统无法找到 容器服务 Kubernetes 版 的服务角色，导致集群控制面异常。 | 参见 [容器服务](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ack-default-roles.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ack-default-roles.md) [服务角色](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ack-default-roles.md) 排查 容器服务 Kubernetes 版 所需的角色。 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) ，联系技术支持人员恢复集群状态。 |
| AssumeUserNotFound | 系统无法找到 容器服务 Kubernetes 版 对应的 RAM 用户，导致集群控制面异常。 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 获取技术支持。 |
| SecurityGroupNotFound | 系统无法找到 容器服务 Kubernetes 版 的安全组，导致集群控制面异常。 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 获取技术支持。 |
| UnderMaintenance | 集群控制面处于后台维护中。 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 获取技术支持。 |
| ServiceInDebt | 当账号可用额度（含阿里云账户余额和代金券）小于待结算的账单时，会被判断为账号欠费。欠费后，您的 ACK 托管集群 Pro 版 会处于不活跃状态，您将无法访问集群的 API Server ，且涉及 API Server 访问的操作都将无法进行。 如果超过 15 天仍处于欠费状态， 容器服务 Kubernetes 版 将暂停为您提供服务，并删除集群的控制面资源。但 ACK 不会主动释放集群关联的其他云产品资源实例（包括但不限于 NAT 网关、SLB 实例、ECS 实例、ESS 伸缩组等）。届时，关联云产品资源可能产生非预期行为，请及时处理。 | 请您及时充值，并结清账单。欠费结清后，集群将自动恢复正常状态。 |


### 不可用（unavailable）

- 

- 

- 

| 异常原因 | 解决方案 |
| --- | --- |
| 集群 API Server 的 CLB 实例被释放，可能包括以下情况： 实例被手动释放 包年包月实例到期自动释放 自 2024 年 12 月 01 日起，新建 CLB 实例 不再支持 包年包月 付费类型，同时 将新增收取实例费，请参见 [【产品公告】关于取消新增集群](products/ack/documents/product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [API Server](products/ack/documents/product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [负载均衡](products/ack/documents/product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [CLB](products/ack/documents/product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) [包年包月付费的公告](products/ack/documents/product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types.md) 、 [传统型负载均衡](products/slb/documents/product-overview/announcement-on-adjustment-of-traditional-load-balancing-clb-billing-items.md) [CLB](products/slb/documents/product-overview/announcement-on-adjustment-of-traditional-load-balancing-clb-billing-items.md) [计费项调整公告](products/slb/documents/product-overview/announcement-on-adjustment-of-traditional-load-balancing-clb-billing-items.md) 。 阿里云账号欠费导致按量付费实例被释放 | 集群已无法恢复，请删除集群或重新创建集群。具体操作，请参见 [删除集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/delete-a-cluster-1.md) 、 [创建](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md) [托管集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md) 。 |


### 异常状态的影响

- 

计费影响

集群处于不活跃（inactive）或不可用（unavailable）状态时，集群控制面会进行缩容。缩容后，不再收取集群管理费用，但仍会继续收取关联的云产品资源费用。

- 

集群操作限制

集群处于不活跃（inactive）或不可用（unavailable）状态时，仅允许执行以下集群管理操作：

- 

变更集群删除保护状态

- 

删除集群

- 

其他影响

集群处于不活跃（inactive）或不可用（unavailable）状态时，为了避免弹出新的ECS实例，产生预期外的费用，ACK会停用集群关联的伸缩组。待集群状态恢复正常后，如果集群关联的伸缩组仍处于停用状态，您可以在[弹性伸缩控制台](https://essnew.console.aliyun.com/)手动启用伸缩组。

[上一篇：查看集群信息](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/view-cluster-information.md)[下一篇：容器服务系统事件](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ack-system-event.md)

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
