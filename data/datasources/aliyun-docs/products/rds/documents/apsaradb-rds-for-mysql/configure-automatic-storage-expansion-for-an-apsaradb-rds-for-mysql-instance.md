# RDS MySQL存储空间自动扩容-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-mysql-instance

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

# 设置存储空间自动扩容

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当数据库存储空间不足时，可能会无法写入数据，导致数据丢失甚至数据库崩溃，严重影响业务运行。RDS MySQL支持在存储空间达到阈值时自动进行扩容。在扩容期间无需重启实例，对业务无影响。

## 前提条件

- 

实例的计费方式为包年包月或按量付费。

说明

如果计费方式为Serverless，则实例存储空间会自动扩容，无需设置。

- 

实例的产品系列为高可用系列或集群系列。

说明

对于基础系列（云盘）实例，支持在DAS控制台开启存储空间自动扩容，详情请参见[自动空间扩展](https://help.aliyun.com/zh/das/user-guide/automatic-space-expansion)。

- 

实例的存储类型为云盘。

- 

实例的状态为运行中。

- 

账户内需要有足够的余额支撑扩容。

## 功能说明

当数据库实例存在只读实例，且主实例触发存储空间自动扩容时，系统会自动检查主实例下每个只读实例的存储空间大小，如果只读实例的存储空间小于主实例的扩容目标空间，会先扩容只读实例的存储空间。所有只读实例扩容完成后，再扩容主实例存储空间。详情请参见[【产品/功能变更】RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/optimization-of-automatic-storage-expansion-for-apsaradb-rds-for-mysql-instances-and-apsaradb-rds-for-postgresql-instances.md)[和](products/rds/documents/apsaradb-rds-for-mysql/optimization-of-automatic-storage-expansion-for-apsaradb-rds-for-mysql-instances-and-apsaradb-rds-for-postgresql-instances.md)[RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-mysql/optimization-of-automatic-storage-expansion-for-apsaradb-rds-for-mysql-instances-and-apsaradb-rds-for-postgresql-instances.md)[实例存储空间自动扩容规则优化](products/rds/documents/apsaradb-rds-for-mysql/optimization-of-automatic-storage-expansion-for-apsaradb-rds-for-mysql-instances-and-apsaradb-rds-for-postgresql-instances.md)。

## 操作步骤

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在基本信息页面的实例资源区域单击存储空间自动扩展右侧的设置。

说明

如果未找到设置按钮，请确认实例是否符合[前提条件](products/rds/documents/apsaradb-rds-for-mysql/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-mysql-instance.md)。

- 

设置如下参数。

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 自动存储扩容 | 存储空间自动扩容的开关。 |
| 可用空间<= | 当剩余存储空间百分比达到设定的值时，会触发自动扩容。 说明 扩容的存储空间大小取下列二者中的最大值： 5 GB 存储空间。当实例存储总空间小于 50 GB，并且可用存储空间小于 10%时，扩容步长调整为 10 GB。 当前实例存储空间的 15%（结果取最近的 5 的倍数）。 例如，如果您当前存储总空间为 100 GB，其 15%为 15 GB，大于 5 GB，那么达到阈值触发扩容时将在原来存储空间的基础上扩容 15 GB，扩容成功后的总空间为 115 GB |
| 存储自动扩展上限 | 扩容后 实例总存储空间 的上限，需要大于等于实例当前存储空间总大小。 不同的云盘存储空间上限如下，您可以在此范围内进行设置： ESSD 云盘上限：32000 GB 高性能云盘上限：64000 GB SSD 云盘上限：6000 GB 说明 SSD 云盘已下线，建议升级至 [ESSD](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md) [云盘](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md) 。 |


- 

单击确认。

## 相关文档

- 

存储空间扩容后，暂不支持自动缩容，如需缩容，请通过变更配置手动缩容，更多信息请参见[变更配置](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。

- 

您可以开通[空间碎片自动回收](products/rds/documents/apsaradb-rds-for-mysql/use-the-automatic-fragment-reclamation-feature-for-an-apsaradb-rds-for-mysql-instance.md)，清理表空间碎片，减少存储空间浪费。

- 

您可以使用[空间分析](products/rds/documents/apsaradb-rds-for-mysql/use-the-storage-analysis-feature-for-an-apsaradb-rds-for-mysql-instance.md)和[容量评估](products/rds/documents/apsaradb-rds-for-mysql/use-the-capacity-assessment-feature-for-an-apsaradb-rds-for-mysql-instance.md)功能，查看和分析存储空间的使用情况。

- 

其他引擎存储空间自动扩容请参见：

- 

RDS PostgreSQL：[存储自动扩容](products/rds/documents/apsaradb-rds-for-postgresql/use-the-automatic-storage-expansion-feature-for-an-apsaradb-rds-for-postgresql-instance.md)。

- 

RDS SQL Server：[设置自动空间扩展](products/rds/documents/apsaradb-rds-for-sql-server/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-sql-server-instance.md)。

## 相关API

| API | 描述 |
| --- | --- |
| [ModifyDasInstanceConfig](products/rds/documents/api-configure-automatic-storage-expansion.md) | 设置实例存储空间自动扩容。 |


## 常见问题

Q：为什么实例使用量统计区域找不到存储空间自动扩展的设置按钮？

A：实例需满足本文所述的前提条件。高性能本地盘实例需[手动扩容](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)，或[变更高性能本地盘至云盘](products/rds/documents/apsaradb-rds-for-mysql/change-the-storage-type-from-local-ssd-to-essd.md)后设置自动扩容。

[上一篇：存储/性能自动扩容](products/rds/documents/apsaradb-rds-for-mysql/automatic-expansion-of-cloud-disk.md)[下一篇：设置性能自动扩容](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-scale-up-feature-for-an-apsaradb-rds-for-mysql-instance.md)

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
