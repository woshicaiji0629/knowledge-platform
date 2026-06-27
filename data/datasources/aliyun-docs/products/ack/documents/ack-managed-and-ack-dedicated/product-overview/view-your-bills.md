# 查询ACK集群管理费用及关联云产品账单-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/product-overview/view-your-bills

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

# 账单查询

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以在费用与成本页面查看ACK集群相关的费用账单和消费明细，以了解费用情况。

## 查询账单

- 

登录[费用与成本](https://usercenter2.aliyun.com/home)页面。

说明

以下操作以新版（蓝色版）控制台为例。

- 

在左侧导航栏，选择账单>账单详情。

- 

选择统计项和统计周期，设置查询条件，然后查看账单。

| 账单筛选条件 | 说明 |
| --- | --- |
| 统计项 | 账单按指定分类展示。例如选择 实例 表示将账单按实例分类。 |
| 统计周期 | 账单按指定周期展示。例如选择 明细 表示按照计费周期，展示每小时的明细账单。 |
| 查询条件 | 支持按账单月份、产品名称、实例名称、实例 ID 等条件查询账单。 |


说明

在查询结果列表的右上角，单击图标可以设置列表显示的列；单击图标可以将列表信息导出为CSV文件。

示例一：查看集群管理费用账单

ACK托管集群Pro版会收取集群管理费用，对应计费项为ACK Pro定价。

查询账单时，请在产品名称处选择容器服务Kubernetes版。如需查询具体某个集群的管理费用，可进一步通过集群名称或者ID进行查询。账单示例如下：

示例二：查看集群关联云产品资源的账单

如需查询集群关联的云产品资源的账单，可在产品名称处选择对应的产品名称，通过实例ID或者名称进行查询。

例如查询ECS的账单时，可使用以下条件：

- 

产品名称处选择云服务器 ECS。

- 

（可选）资源实例名称/ID处选择资产/资源实例ID，并输入要查询的ECS实例ID（不支持多个）。

您可以从集群管理页的节点页面获取该集群包含的所有ECS实例ID，然后通过ID分别查询某个ECS实例的账单。由于该筛选项不支持输入多个ID，如需查询集群包含的所有ECS实例的账单，您可以保持该筛选项为空，仅通过产品名称查询出所有ECS实例的账单，将账单导出到本地CSV文件，然后再通过实例ID筛选出账单。

说明

通过ACK创建的ECS实例的名称默认为worker-k8s-for-cs-<集群ID>，您也可以通过筛选实例名称为worker-k8s-for-cs-<集群ID>的方式进行批量查询，但如果您的集群中存在其他名称的ECS节点，这种方式无法查询到全部账单。

账单示例如下：

## 相关文档

- 

ACK支持成本洞察功能，可以帮助您多维度了解集群资源使用量及成本分布，获取成本节约建议。更多信息，请参见[成本洞察](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cost-analysis-overview.md)。

- 

如需了解更多关于账单的信息，请参见[账单详情](https://help.aliyun.com/zh/user-center/billing-details-1)。

- 

如需了解消费汇总信息，可在月账单概览页面查看。更多信息，请参见[账单概览](https://help.aliyun.com/zh/user-center/bill-overview-1)。

[上一篇：云产品资源费用](products/ack/documents/ack-managed-and-ack-dedicated/product-overview/billing-of-cloud-services.md)[下一篇：欠费说明](products/ack/documents/ack-managed-and-ack-dedicated/product-overview/overdue-payments.md)

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
