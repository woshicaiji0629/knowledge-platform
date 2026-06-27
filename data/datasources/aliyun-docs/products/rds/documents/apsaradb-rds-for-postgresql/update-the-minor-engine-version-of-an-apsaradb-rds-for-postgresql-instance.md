# RDS PostgreSQL升级内核小版本-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance

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

# RDS PostgreSQL升级内核小版本

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库RDS PostgreSQL提供内核小版本升级功能。通过升级，您将获得包含性能提升、新功能支持和安全问题解决的最新版本，能够确保数据库服务的持续优化和安全。

RDS PostgreSQL内核小版本功能详情请参见[AliPG](products/rds/documents/apsaradb-rds-for-postgresql/release-notes-for-alipg.md)[内核小版本发布记录（PostgreSQL 14~18）](products/rds/documents/apsaradb-rds-for-postgresql/release-notes-for-alipg.md)。

## 注意事项

- 

升级内核小版本会重启实例，RDS服务可能会出现一次30秒的闪断，请您尽量在业务低峰期执行升级操作，或确保您的应用有自动重连机制。

- 

升级内核小版本后无法降级。

- 

小版本升级通常不会出现兼容性问题，但因插件的升级有可能会有兼容性问题，如果涉及到插件升级（如Ganos插件版本升级），建议先使用[恢复](products/rds/documents/apsaradb-rds-for-postgresql/restore-data-of-an-apsaradb-rds-for-postgresql-instance.md)[PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/restore-data-of-an-apsaradb-rds-for-postgresql-instance.md)[数据](products/rds/documents/apsaradb-rds-for-postgresql/restore-data-of-an-apsaradb-rds-for-postgresql-instance.md)功能，在恢复的新实例上测试新版本插件的兼容性。

- 

相关插件升级注意事项：

- 

如果您的业务已经使用了PostGIS或Ganos插件，在升级内核小版本后，还需要手动升级PostGIS或Ganos插件，升级方法，请参见[时空引擎插件升级](products/rds/documents/apsaradb-rds-for-postgresql/how-do-i-update-the-plug-ins-of-ganos.md)。

- 

如果您的实例大版本为PostgreSQL 14，在20230330内核小版本前已使用了[TimescaleDB](products/rds/documents/apsaradb-rds-for-postgresql/use-the-timescaledb-extension.md)插件（插件版本小于等于2.5.0），在升级内核小版本到20230330或以上版本后，必须手动执行ALTER EXTENSION timescaledb UPDATE;命令进行手动升级插件后，才能继续使用TimescaleDB插件。

## 查看内核小版本

您可以通过如下两种方法查看实例当前的内核小版本。

- 

登录[RDS](https://rds.console.aliyun.com/)[管理控制台](https://rds.console.aliyun.com/)，在目标实例的基本信息页面查看。

说明

此方法仅适用于PostgreSQL云盘版实例。

- 

连接[目标](products/rds/documents/apsaradb-rds-for-postgresql/connect-to-an-apsaradb-rds-for-postgresql-instance.md)[PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/connect-to-an-apsaradb-rds-for-postgresql-instance.md)[实例](products/rds/documents/apsaradb-rds-for-postgresql/connect-to-an-apsaradb-rds-for-postgresql-instance.md)，通过show rds_release_date;命令查看。

说明

此方法适用于PostgreSQL云盘版和高性能本地盘版实例。

## 手动升级内核小版本

### 高性能本地盘实例升级内核小版本

高性能本地盘实例暂不支持手动升级内核小版本。您可以通过重启实例自动升级到最新的小版本。具体操作请参见[重启实例](products/rds/documents/apsaradb-rds-for-postgresql/restart-an-apsaradb-rds-for-postgresql-instance.md)。

说明

如果当前实例为主实例，拥有只读实例，请先逐个重启所有只读实例，再重启主实例。如果只重启主实例，则只读实例不会升级内核小版本。

### 云盘实例升级内核小版本

说明

如果当前实例为主实例，拥有只读实例，可以通过两种方式进行升级。

- 

对主实例发起内核小版本升级，该主实例下的所有只读实例都会先立即进行并发升级，然后再升级主实例。

- 

如果您不希望所有只读实例立即升级，请先逐个升级所有只读实例，然后再升级主实例。

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在配置信息区域中单击升级内核小版本。

- 

在弹出的对话框中，选择可升级到版本和升级时间，单击确定。

可升级到版本中各字段含义：

- 

rds：RDS实例。

- 

postgres：PostgreSQL数据库。

- 

1200：PostgreSQL大版本为12。

- 

20220830：AliPG内核小版本。各小版本的具体信息，请参见[AliPG](products/rds/documents/apsaradb-rds-for-postgresql/release-notes-for-alipg.md)[内核小版本发布记录（PostgreSQL 14~18）](products/rds/documents/apsaradb-rds-for-postgresql/release-notes-for-alipg.md)。

- 

12.11：PostgreSQL社区小版本号。

## 自动升级内核小版本

警告

自动升级仅为系统辅助升级手段，并不保证所有实例均能立即升级至最新内核版本。您可以在实例的基本信息页查看内核版本状态，并及时升级内核版本，以避免历史内核版本可能存在的潜在风险。如您取消了系统下发的版本升级任务，或查看控制台版本升级提示后仍未及时升级至最新稳定版本，因此造成的业务中断、数据丢失等损失和后果均由您承担。详情请参见[云数据库服务协议](http://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud201802112245_42129.html)。

购买RDS PostgreSQL云盘版实例时，默认选择小版本升级策略为自动升级，当您的内核小版本低于最新内核小版本时，系统将会不定期地下发主动运维任务来升级内核小版本。任务信息将通过短信、邮件、站内信等渠道通知您。自动升级操作将会在您设置的[可维护时间段](products/rds/documents/apsaradb-rds-for-postgresql/set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md)内进行。您可以在事件管理中修改升级时间，或在任务开始前取消任务，详情请参见[计划内事件](products/rds/documents/apsaradb-rds-for-postgresql/pending-events.md)。

说明

自动升级内核小版本功能仅支持云盘版实例。

### 修改自动升级设置

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在实例的基本信息页的配置信息区域查看小版本自动升级的设置情况。

- 

单击小版本自动升级右侧的设置。

- 

在弹出的对话框中，选择自动升级或手动升级，然后单击确认。

## 常见问题

升级内核小版本后，PostGIS和Ganos插件访问出错，如何处理？

在升级内核小版本后，还需要手动升级PostGIS或Ganos插件，升级方法，请参见[时空引擎插件升级](products/rds/documents/apsaradb-rds-for-postgresql/how-do-i-update-the-plug-ins-of-ganos.md)。

PostGIS在升级内核小版本时有哪些兼容性问题？

兼容性差异如下表所示：

说明

内核小版本在20211031前的RDS PostgreSQL实例，可能会遇到如下兼容性问题。

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

| PostGIS 插件版本 | 只升级 RDS PostgreSQL 内核小版本 | 升级 RDS PostgreSQL 内核小版本 + 升级 PostGIS 插件 |
| --- | --- | --- |
| 2.5.x | 使用如下函数时，可能导致数据库崩溃 ST_ClusterKMeans ST_GeomFromKML ST_AsKML 使用如下函数时，将会报错 ST_Buffer 报错 ： Invalid buffer parameter: uad_segs (accept: 'endcap', 'join', 'mitre_limit', 'miter_limit', 'quad_segs' and 'side') 解决办法 ：将 quadsegs 参数修改为 quad_segs 。 ST_Intersects 报错 ： ERROR: GetGenericCacheCollection: Could not find upper context 解决办法： 无。 如下函数将会被删除，无法使用 ST_Force_2D ST_Locate_Along_Measure ST_Estimated_Extent 如下函数的参数值或写法将与升级前不一致 ST_GeomFromGeoJSON：升级后会默认指定 SRID=4326 。 ST_AsGeoJSON：maxdecimaldigits 从 16 修改为 9。 MutliPoint 写法不一致： 升级前： MULTIPOINT(1 1,-1 1) 升级后： MULTIPOINT((1 1),(-1 1)) | 如下函数将会被删除，无法使用 ST_Force_2D ST_Locate_Along_Measure ST_Estimated_Extent 如下函数的参数值或写法将与升级前不一致 ST_GeomFromGeoJSON：升级后会默认指定 SRID=4326 。 ST_AsGeoJSON：参数 maxdecimaldigits 从 16 修改为 9。 MutliPoint 写法不一致： 升级前： MULTIPOINT(1 1,-1 1) 升级后： MULTIPOINT((1 1),(-1 1)) |
| 3.1.x | 使用如下函数时，可能导致数据库崩溃 ST_ClusterKMeans MutliPoint 写法将与升级前不一致 升级前： MULTIPOINT(1 1,-1 1) 升级后： MULTIPOINT((1 1),(-1 1)) | MutliPoint 写法将与升级前不一致 升级前： MULTIPOINT(1 1,-1 1) 升级后： MULTIPOINT((1 1),(-1 1)) |


## 相关文档

- 

如果您的业务已经使用了PostGIS或Ganos插件，在升级内核小版本后，还需要手动升级PostGIS或Ganos插件，升级方法，请参见[时空引擎插件升级](products/rds/documents/apsaradb-rds-for-postgresql/how-do-i-update-the-plug-ins-of-ganos.md)。

- 

各小版本的具体信息，请参见[AliPG](products/rds/documents/apsaradb-rds-for-postgresql/release-notes-for-alipg.md)[内核小版本发布记录（PostgreSQL 14~18）](products/rds/documents/apsaradb-rds-for-postgresql/release-notes-for-alipg.md)。

- 

您也可以使用API升级内核小版本：

| API | 描述 |
| --- | --- |
| [升级内核小版本](products/rds/documents/apsaradb-rds-for-postgresql/api-rds-2014-08-15-upgradedbinstancekernelversion-postgresql.md) | 升级数据库的内核小版本。 |
| [修改](products/rds/documents/developer-reference/api-rds-2014-08-15-modifydbinstanceautoupgrademinorversion.md) [RDS](products/rds/documents/developer-reference/api-rds-2014-08-15-modifydbinstanceautoupgrademinorversion.md) [升级内核小版本的方式](products/rds/documents/developer-reference/api-rds-2014-08-15-modifydbinstanceautoupgrademinorversion.md) | 设置内核小版本升级策略为自动或手动。 |


[上一篇：解读RDS PostgreSQL大版本升级检查报告](products/rds/documents/apsaradb-rds-for-postgresql/introduction-to-the-check-report-of-a-major-engine-version-upgrade-for-an-apsaradb-rds-for-postgresql-instance.md)[下一篇：管理参数](products/rds/documents/apsaradb-rds-for-postgresql/parameter-management.md)

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
