# 实例可变更配置项的范围与说明-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/configuration-items-for-an-apsaradb-rds-for-mysql-instance

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-mysql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-mysql/getting-started.md)

- [AI能力中心](products/rds/documents/apsaradb-rds-for-mysql/ai-capability-center.md)

- [自研内核AliSQL](products/rds/documents/apsaradb-rds-for-mysql/proprietary-alisql.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-mysql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-mysql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-mysql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-mysql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-mysql/support.md)

[首页](https://help.aliyun.com/zh)

# 实例变更项

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍RDS MySQL实例支持的变更项。

## 计算与存储

### 规格

- 

- 

- 

| 说明 | 变更方法 |
| --- | --- |
| 所有实例类型都支持变更规格。 集群系列实例的节点还支持单独变更规格，允许各节点规格不同。 说明 部分历史规格实例可能无法直接变更，您可以按如下步骤间接变更： [创建新实例](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md) ，选择目标规格。 [原实例数据迁移至新实例](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-between-apsaradb-rds-for-mysql-instances.md) [释放原实例](products/rds/documents/apsaradb-rds-for-mysql/release-or-unsubscribe-from-an-instance.md) | [变更配置](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md) [设置性能自动扩容](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-scale-up-feature-for-an-apsaradb-rds-for-mysql-instance.md) [变更节点配置](products/rds/documents/apsaradb-rds-for-mysql/change-node-specifications.md) |


### 存储类型

- 

- 

- 

- 

- 

- 

| 说明 | 变更方法 |
| --- | --- |
| 当前仅支持如下存储类型变更： MySQL 8.0、5.7 高可用系列或基础系列（SSD 云盘），可变更为 ESSD 云盘。 MySQL 8.0、5.7 高可用系列（高性能本地盘），可变更为 ESSD 云盘。 MySQL 5.7 基础系列（SSD 云盘）升级高可用系列时，可同步变更存储类型为高性能本地盘。 云盘空间不低于 40 GB 的 ESSD 云盘实例，可变更为高性能云盘。 基础系列支持 ESSD PL0 变更为 PL1，不支持 ESSD PL1 变更为 PL0。 高可用系列、集群系列实例节点支持在 ESSD PL1、PL2、PL3 云盘之间变更。 | [升级](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md) [SSD](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md) [云盘至](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md) [ESSD](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md) [云盘](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md) [变更高性能本地盘至云盘](products/rds/documents/apsaradb-rds-for-mysql/change-the-storage-type-from-local-ssd-to-essd.md) [基础系列升级为高可用系列](products/rds/documents/apsaradb-rds-for-mysql/upgrade-an-apsaradb-rds-for-mysql-instance-from-basic-edition-to-high-availability-edition.md) [ESSD](products/rds/documents/apsaradb-rds-for-mysql/essd-changed-to-universal-cloud-disk.md) [云盘变更为高性能云盘](products/rds/documents/apsaradb-rds-for-mysql/essd-changed-to-universal-cloud-disk.md) [变更节点配置](products/rds/documents/apsaradb-rds-for-mysql/change-node-specifications.md) |


### 存储空间

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

| 操作类型 | 说明 | 变更方法 |
| --- | --- | --- |
| 扩容 | 至少增加 5 GB，至多不能超过当前规格的存储空间限制，详情请参见 [主实例规格列表](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md) 。 说明 云盘实例（非基础系列）支持在线增加存储空间，绝大多数情况下不会闪断。 集群系列实例节点可通过 RDS 控制台或 [ModifyDBNode](products/rds/documents/developer-reference/api-rds-2014-08-15-modifydbnode.md) 接口增加存储空间。 | [变更配置](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md) [设置存储空间自动扩容](products/rds/documents/apsaradb-rds-for-mysql/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-mysql-instance.md) [变更节点配置](products/rds/documents/apsaradb-rds-for-mysql/change-node-specifications.md) |
| 缩容 | 高性能本地盘：高可用系列地盘实例支持降低存储空间。 云盘：基础系列、高可用系列、集群系列实例支持在同一系列、同一架构下缩容，可选择的最小缩容大小根据公式 min{使用量*1.3，使用量+400 GB} 计算所得，且不能小于当前规格支持的最小存储空间，存储空间调整步长 5 GB。 说明 存储类型为云盘的集群系列实例存储空间缩容，当前仅支持新加坡地域，其他地域逐步开放中，请以变配页为准。 当前仅支持 RDS MySQL 大版本为 5.7、8.0，内核小版本为 20210430 及之后的实例进行缩容。 集群系列实例节点仅可通过 [ModifyDBNode](products/rds/documents/developer-reference/api-rds-2014-08-15-modifydbnode.md) 接口降低存储空间。 存储空间缩容示例 假设当前实例规格的存储类型为 ESSD PL1 云盘（最小存储空间为 20 GB），存储空间为 2000 GB，根据不同实际存储空间使用量，可缩容的范围不同，具体如下： 如果存储空间实例使用量为 10 GB，根据公式计算 min{10×1.3, 10+400}=13 GB ，仍小于 20 GB，则最小可缩容至 20 GB。 如果存储空间实例使用量为 500 GB，根据公式计算 min{500×1.3, 500+400}=650 GB ，则最小可缩容至 650 GB。 如果存储空间实例使用量为 1500 GB，根据公式计算 min{1500×1.3, 1500+400}=1900 GB ，则最小可缩容至 1900 GB。 | 高性能本地盘： [变更配置](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md) 云盘： [ESSD](products/rds/documents/support/reduce-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-that-uses-essds.md) [云盘缩容](products/rds/documents/support/reduce-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-that-uses-essds.md) 、 [变更节点配置](products/rds/documents/apsaradb-rds-for-mysql/change-node-specifications.md) |


说明

- 

只读实例的存储空间必须大于或等于其所属主实例的存储空间。

- 

若当前规格对应的存储空间范围无法满足您的需求，请选择其它实例规格。

## 地域和可用区

- 

- 

| 变更项 | 说明 | 变更方法 |
| --- | --- | --- |
| 地域 | 实例的地域无法变更，您可以在目标地域创建实例后，通过数据传输服务 DTS 迁移数据，然后修改业务连接地址，确认业务正常后 [释放原实例](products/rds/documents/apsaradb-rds-for-mysql/release-or-unsubscribe-from-an-instance.md) 。 | [迁移数据](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-between-apsaradb-rds-for-mysql-instances.md) |
| 可用区 | 实例可以迁移至同一地域内的其它可用区。迁移可用区后，实例的所有属性、配置和连接地址都不会改变。 MySQL 5.7 从高可用系列升级到三节点企业系列（原金融版）时，需要变更实例所在的可用区。 说明 集群系列实例不支持迁移可用区。 迁移可用区需要迁移数据，数据量越大，所需时间越长。 | [迁移可用区](products/rds/documents/apsaradb-rds-for-mysql/migrate-an-apsaradb-rds-for-mysql-instance-across-zones-in-the-same-region.md) |


## 产品系列和产品类型

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 变更项 | 说明 | 变更方法 |
| --- | --- | --- |
| 产品系列 | 当前仅支持如下几种系列变更： MySQL 8.0 和 5.7 基础系列：变更为高可用系列。 MySQL 8.0 和 5.7 高可用系列：变更为集群系列。 说明 除上述场景外均不支持变更系列，如果需要进行其他系列变更，您可以执行如下步骤： [创建新实例](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md) ，选择目标系列。 [原实例数据迁移至新实例](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-between-apsaradb-rds-for-mysql-instances.md) [释放原实例](products/rds/documents/apsaradb-rds-for-mysql/release-or-unsubscribe-from-an-instance.md) | [基础系列升级为高可用系列](products/rds/documents/apsaradb-rds-for-mysql/upgrade-an-apsaradb-rds-for-mysql-instance-from-basic-edition-to-high-availability-edition.md) [高可用系列升级为集群系列](products/rds/documents/apsaradb-rds-for-mysql/upgrade-an-apsaradb-rds-for-mysql-instance-from-rds-high-availability-edition-to-rds-cluster-edition.md) |
| [产品类型](products/rds/documents/product-overview/product-types.md) | 高可用和集群系列：支持在标准版和倚天版间互相变更。 基础系列：仅支持倚天版变更为标准版。 说明 如果变更时无法选择目标类型，可能实例所在可用区暂无对应资源在售。 您可以先到实例售卖页查看目标类型的在售可用区情况，然后通过 [迁移可用区](products/rds/documents/apsaradb-rds-for-mysql/migrate-an-apsaradb-rds-for-mysql-instance-across-zones-in-the-same-region.md) 功能，将当前实例迁移至目标可用区后，再进行变更配置。 如果需要变更产品类型，需要确保变更后内核小版本大于等于当前实例内核小版本，如果当前实例内核小版本高于变更后内核小版本，则不支持变更。 | [变更配置](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md) |


## 网络

| 变更项 | 说明 | 变更方法 |
| --- | --- | --- |
| VPC 和虚拟交换机 | 部分实例支持切换 VPC 和虚拟交换机。 | [切换专有网络](products/rds/documents/apsaradb-rds-for-mysql/change-the-vpc-and-vswitch-for-an-apsaradb-rds-for-mysql-instance.md) [VPC](products/rds/documents/apsaradb-rds-for-mysql/change-the-vpc-and-vswitch-for-an-apsaradb-rds-for-mysql-instance.md) [和虚拟交换机](products/rds/documents/apsaradb-rds-for-mysql/change-the-vpc-and-vswitch-for-an-apsaradb-rds-for-mysql-instance.md) |


## 主备

| 变更项 | 说明 | 变更方法 |
| --- | --- | --- |
| 主备关系 | 实例可自动或手动切换主备，切换后原主实例变为备实例。 | [管理主备切换](products/rds/documents/apsaradb-rds-for-mysql/switch-workloads-over-between-primary-and-secondary-apsaradb-rds-for-mysql-instances.md) |
| 数据复制方式 | 修改主备实例之间的数据复制方式，可以提高数据库可用性。 | [查询和修改数据复制方式](products/rds/documents/apsaradb-rds-for-mysql/change-the-data-replication-mode-of-an-apsaradb-rds-for-mysql-instance.md) |


## 实例参数

| 说明 | 变更方法 |
| --- | --- |
| 支持对实例的部分参数值进行修改，以更好地满足业务需求。 | [设置实例参数](products/rds/documents/apsaradb-rds-for-mysql/modify-the-parameters-of-an-apsaradb-rds-for-mysql-instance.md) 或 [使用参数模板](products/rds/documents/apsaradb-rds-for-mysql/use-a-parameter-template-to-configure-the-parameters-of-apsaradb-rds-for-mysql-instances.md) |


## 数据库引擎版本

- 

- 

- 

| 说明 | 变更方法 |
| --- | --- |
| 支持在控制台进行如下形式的版本升级： RDS MySQL 5.7 → RDS MySQL 8.0 RDS MySQL 5.6 → RDS MySQL 5.7 RDS MySQL 5.5 → RDS MySQL 5.6 说明 不支持跨版本升级。例如 RDS MySQL 5.5 无法直接升级到 RDS MySQL 8.0。 | [升级数据库版本](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance.md) |


## 可维护时间段

| 说明 | 变更方法 |
| --- | --- |
| 实例可以修改可维护时间段。 | [设置可维护时间段](products/rds/documents/apsaradb-rds-for-mysql/set-the-maintenance-window-of-an-apsaradb-rds-for-mysql-instance.md) |


## 计费方式

| 说明 | 变更方法 |
| --- | --- |
| 实例的计费方式可以在按量付费和包年包月之间切换。 | [按量付费转包年包月](products/rds/documents/apsaradb-rds-for-mysql/change-the-billing-method-of-an-apsaradb-rds-for-mysql-instance-from-pay-as-you-go-to-subscription.md) [包年包月转按量付费](products/rds/documents/apsaradb-rds-for-mysql/change-the-billing-method-of-an-apsaradb-rds-for-mysql-instance-from-subscription-to-pay-as-you-go.md) |
| 实例的计费方式可以在按量付费和 Serverless 之间切换。 | [按量付费转](products/rds/documents/apsaradb-rds-for-mysql/pay-as-you-go-to-serverless.md) [Serverless](products/rds/documents/apsaradb-rds-for-mysql/pay-as-you-go-to-serverless.md) [Serverless](products/rds/documents/apsaradb-rds-for-mysql/transfer-serverless-instances-to-pay-as-you-go-billing.md) [转按量付费](products/rds/documents/apsaradb-rds-for-mysql/transfer-serverless-instances-to-pay-as-you-go-billing.md) |


[上一篇：变更实例](products/rds/documents/apsaradb-rds-for-mysql/instance-change.md)[下一篇：变更配置](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)

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
