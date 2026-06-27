# 自动或手动备份-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/automatic-or-manual-backup

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/redis/documents/product-overview.md)

- [快速入门](products/redis/documents/getting-started.md)

- [Tair AI能力](products/redis/documents/tair-ai-ability.md)

- [操作指南](products/redis/documents/user-guide.md)

- [实践教程](products/redis/documents/use-cases.md)

- [安全合规](products/redis/documents/security-compliance.md)

- [开发参考](products/redis/documents/developer-reference.md)

- [服务支持](products/redis/documents/support.md)

- [视频专区](products/redis/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 自动或手动备份

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库 Tair（兼容 Redis）实例使用RDB快照存储实现持久化，它会将某一时刻的内存数据压缩、保存到硬盘的文件中，备份期间不会影响数据的读写性能。实例默认每天备份一次，您可以根据业务需求修改自动备份策略，也可以手动发起临时的备份。

## 功能概述

云数据库 Tair（兼容 Redis）的RDB快照备份，提供两种触发方式。

- 

自动备份：根据您配置的自动备份策略（默认每天备份一次），触发备份。

不允许删除自动备份的备份集，也不允许修改过期时间，仅会在到期后将自动删除，以保证数据的安全性。

- 

手动备份：随时手动触发备份（上限为30次/实例/天）。

云原生版实例支持自定义设置单次手动备份的过期策略，也支持删除手动备份的备份集、支持修改过期时间。

云原生实例删除（到期或释放）后，实例所有的备份集会修改为不过期，您可以按需恢复或删除。而经典实例删除后，会同时删除备份集。

### 费用

每个实例都有免费备份额度，免费备份额度为该实例规格默认内存量，例如实例内存规格容量为8 GB，则该免费备份额度为8 GB。当备份数据量超过免费备份额度后，超出的部分将按量计费，单价为0.15元/GB/月。

实例删除后，免费备份额度随即失效，将根据备份容量计费。

说明

您可以在控制台的备份与恢复页签中看到该实例的免费备份额度与当前已备份的总量。

## 注意事项

- 

若实例类型为单节点，则不支持备份、恢复功能。

- 

若实例的备份任务正在进行时，则无法启动新的备份任务，请在当前备份任务完成后重试。

- 

默认情况下，实例会在备库上进行数据备份，但实例若开启[数据闪回功能](products/redis/documents/user-guide/use-data-flashback-to-restore-data-by-point-in-time.md)，则会在实例主库进行数据备份。

## 操作步骤

- 

访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏，单击备份与恢复。

- 

根据业务需求，选择执行下述步骤：

### 修改自动备份策略

- 

单击页面右上角的备份设置。

- 

在弹出的对话框中，设置备份周期和备份时间段。

- 

保留天数：备份文件的保留天数为3~730天。

- 

备份周期：可以设置为一星期中的某一天或者某几天，默认为每天备份一次。

- 

备份时间：可以设置为任意时段，以小时为单位，建议设置为业务的低峰期。

说明

控制台显示的时间为您电脑的时区。

- 

单击确定。

## 手动发起备份

- 

单击页面右上角的手动创建备份。

- 

在弹出的对话框中，选择备份过期策略，单击确定。

仅云原生版实例支持自定义设置手动备份的过期策略（经典版不支持），支持选择：

- 

当前设置（默认）：表示与当前自动备份策略一致。

- 

独立设置：设置本次手动备份数据的保留时长，范围为3~730。

- 

不过期：设置本次手动备份数据不过期（实例生命周期内）。例如您可以在每周一或每月初进行手动备份，并将该备份数据设置为不过期，从而长久地保持数据。

说明

- 

单个实例每天最多允许手动备份30次，超过后将报错Exceeding the daily backup times of this DB instance.，该限制将于24小时后自动解除，但该限制不会影响自动备份的执行。

- 

手动备份数据支持延长过期时间。

## 常见问题

- 

Q：如何删除备份数据？

A：对于云原生实例，可以直接单击目标手动备份数据右侧的删除按钮进行删除。但所有自动备份数据均不支持删除，自动备份数据在到期后将自动删除。

- 

Q：修改备份策略会影响实例运行吗？

A：不会。

- 

Q：实例是否支持执行SAVE或BGSAVE命令备份数据？

A：不支持，您可以在控制台单击手动创建备份或调用[CreateBackup](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-createbackup-redis.md)接口，手动备份数据。

- 

Q：每天多次备份需要怎么做？

A：自动备份策略最多支持每天一次。如需进行更高频率的备份，您可以编写代码，定时调用[CreateBackup](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-createbackup-redis.md)接口，模拟手动创建备份，更多信息请参见[CreateBackup](https://next.api.aliyun.com/api/R-kvstore/2015-01-01/CreateBackup)集成示例。备份后的数据也在备份列表中。

说明

您也可以考虑使用Tair（企业版）实例提供的数据闪回功能。开启数据闪回功能后，Tair（企业版）实例可实现7x24小时数据备份，也支持恢复至7天内的任意时间时（PITR，point-in-time recovery），更多信息请参见[数据闪回](products/redis/documents/user-guide/use-data-flashback-to-restore-data-by-point-in-time.md)。

- 

Q：实例到期或被释放后，备份的数据还会保留吗？

A：云原生实例备份数据支持保留，您可以在[备份管理](https://kvstore.console.aliyun.com/Redis/backupManage/cn-beijing)中进行查询、恢复。但经典版实例的备份集会被删除，如需长期保存，请提前[下载备份集](products/redis/documents/user-guide/download-a-backup-file.md)。

## 相关API

| API 接口 | 说明 |
| --- | --- |
| [CreateBackup](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-createbackup-redis.md) | 为实例手动创建数据备份。 |
| [DescribeBackupPolicy](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-describebackuppolicy-redis.md) | 查询实例的备份策略，包括备份周期、备份时间等信息。 |
| [ModifyBackupPolicy](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-modifybackuppolicy-redis.md) | 修改实例的自动备份策略。 |
| [ModifyBackupExpireTime](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-modifybackupexpiretime-redis.md) | 延长手动备份数据的过期时间。 |


## 相关文档

- 

如需恢复数据，请参见[从备份集恢复至新实例](products/redis/documents/user-guide/restore-data-from-a-backup-set-to-a-new-instance.md)。

- 

如需下载备份文件至本地，请参见[下载备份集](products/redis/documents/user-guide/download-a-backup-file.md)。

[上一篇：备份与恢复](products/redis/documents/user-guide/backup-and-restoration-solutions.md)[下一篇：从备份集恢复至新实例](products/redis/documents/user-guide/restore-data-from-a-backup-set-to-a-new-instance.md)

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
