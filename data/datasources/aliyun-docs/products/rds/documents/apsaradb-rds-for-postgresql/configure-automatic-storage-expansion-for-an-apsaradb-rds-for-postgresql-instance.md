# RDS PostgreSQL存储空间自动扩容-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-postgresql-instance

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-postgresql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-postgresql/getting-started.md)

- [DuckDB分析加速](products/rds/documents/apsaradb-rds-for-postgresql/duckdb-analytics-acceleration.md)

- [RDS for AI](products/rds/documents/apsaradb-rds-for-postgresql/rds-for-ai.md)

- [自研内核 AliPG](products/rds/documents/apsaradb-rds-for-postgresql/proprietary-alipg.md)

- [插件](products/rds/documents/apsaradb-rds-for-postgresql/plug-ins-1.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-postgresql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-postgresql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-postgresql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-postgresql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-postgresql/support.md)

[首页](https://help.aliyun.com/zh)

# 设置存储空间自动扩容

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍RDS PostgreSQL云盘实例的存储空间如何自动扩容。

## 前提条件

- 

RDS PostgreSQL云盘实例，且实例状态为运行中。

- 

账户内需要有足够的余额支撑扩容。

## 注意事项

- 

您可以通过[WAL](products/rds/documents/apsaradb-rds-for-postgresql/use-the-wal-log-management-feature-for-an-apsaradb-rds-for-postgresql-instance.md)[日志管理](products/rds/documents/apsaradb-rds-for-postgresql/use-the-wal-log-management-feature-for-an-apsaradb-rds-for-postgresql-instance.md)功能查看是否存在冗余的Replication Slot，您可以手动删除非活跃Replication Slot来让RDS PostgreSQL内核自动清理WAL日志，然后再查看存储空间是否满足业务需求，如仍不满足再设置自动扩容。

- 

2023年02月28日起，系统逐步优化各地域实例的存储自动扩容规则，当数据库实例存在只读实例，且主实例触发自动扩容时，系统会自动检查主实例下每个只读实例的存储空间大小，如果只读实例的存储空间小于主实例的扩容目标空间，会先扩容只读实例的存储空间。所有只读实例扩容完成后，再扩容主实例存储空间。详情请参见[【产品/功能变更】RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/optimization-of-automatic-storage-expansion-for-apsaradb-rds-for-mysql-instances-and-apsaradb-rds-for-postgresql-instances.md)[和](products/rds/documents/apsaradb-rds-for-mysql/optimization-of-automatic-storage-expansion-for-apsaradb-rds-for-mysql-instances-and-apsaradb-rds-for-postgresql-instances.md)[RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-mysql/optimization-of-automatic-storage-expansion-for-apsaradb-rds-for-mysql-instances-and-apsaradb-rds-for-postgresql-instances.md)[实例存储空间自动扩容规则优化](products/rds/documents/apsaradb-rds-for-mysql/optimization-of-automatic-storage-expansion-for-apsaradb-rds-for-mysql-instances-and-apsaradb-rds-for-postgresql-instances.md)。

- 

如果实例当前正在进行备份，存储空间自动扩容任务需等待备份完成后再进行。

## 费用

计费规则与手动升级RDS实例存储空间相同，详情请参见[变配的计费规则](products/rds/documents/product-overview/specification-changes.md)。

## 操作步骤

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在实例资源区域单击存储空间自动扩展右侧的设置。

- 

设置如下参数。

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 自动存储扩容 | 存储空间自动扩容的开关。 |
| 可用空间<= | 当剩余存储空间百分比达到设定的值时，会触发自动扩容。 说明 扩容的存储空间大小取下列两者中的最大值： 5 GB 存储空间。当实例存储总空间小于 50 GB，并且可用存储空间小于 10%时，扩容步长调整为 10 GB。 当前实例存储空间的 15%（结果取最近的 5 的倍数）。 |
| 存储自动扩展上限 | 自动扩容上限，需要大于等于实例当前存储空间总大小。 ESSD 云盘上限：32000 GB SSD 云盘上限：6000 GB |


- 

单击确认。

## 查看扩容历史

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在实例资源区域单击存储空间自动扩展右侧的扩容历史，进入数据库自治服务控制台。

- 

在自治中心页面，将类型切换为弹性伸缩事件，查看已触发的存储空间扩容历史。

- 

单击目标弹性伸缩事件中的详情，查看扩容具体信息。弹性伸缩事件详情页展示事件的异常级别、持续时间等基本信息。在建议Tab页签中，问题与建议区域显示磁盘空间使用情况及扩容建议，存储建议区域显示原存储容量与推荐存储容量（例如原存储20 GB、推荐存储25 GB），执行情况区域显示扩容任务的执行状态及各步骤（调用RDS OpenAPI、管控执行规格变更）的执行细节。

## 常见问题

Q：触发存储空间自动扩容后，扩容过程通常需要多长时间才能完成？

A：扩容所需时间无法准确预测，因为它与实例负载、数据量等多个因素密切相关。您可以前往[任务中心](products/rds/documents/apsaradb-rds-for-postgresql/task-list.md)查看任务进度。

## 相关API

| API | 描述 |
| --- | --- |
| [ModifyDasInstanceConfig](products/rds/documents/api-configure-automatic-storage-expansion.md) | 设置实例存储空间自动扩容。 |


[上一篇：设置可维护时间段](products/rds/documents/apsaradb-rds-for-postgresql/set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md)[下一篇：云盘版RDS PostgreSQL实例存储空间缩容](products/rds/documents/apsaradb-rds-for-postgresql/reduce-the-storage-capacity-of-an-apsaradb-rds-for-postgresql-instance-that-uses-essds.md)

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
