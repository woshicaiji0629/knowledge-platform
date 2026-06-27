# 创建RDS PostgreSQL账号和数据库-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/create-a-database-and-an-account-on-an-apsaradb-rds-for-postgresql-instance

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

# 创建账号和数据库

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

若要使用云数据库RDS，您需要在实例中创建账号和数据库。本文介绍如何为RDS PostgreSQL实例创建账号和数据库。

## 账号类型

RDS PostgreSQL实例支持两种数据库账号：高权限账号和普通账号。详细说明如下。

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

| 账号类型 | 说明 |
| --- | --- |
| 高权限账号 | 只能通过控制台或 API 创建和管理。 可以创建多个高权限账号，管理所有普通账号和数据库。 开放了更多权限，可满足个性化和精细化的权限管理需求，例如可按用户分配不同表的查询权限。 可以断开任意账号的连接。 说明 当创建的高权限账号是该实例的第一个高权限账号时，这个账号将是标准系统数据库 template1 中默认模式 Public Schema 的 Owner。 CREATE DATABASE 命令默认通过复制 template1 来创建数据库。通过该方式创建的数据库，Public Schema 的 Owner 均为第一个高权限账号。 第一个高权限账号的备注默认为 template1 public schema owner ，您可以根据需要进行自定义。 |
| 普通账号 | 可以通过控制台、API 或者 SQL 语句创建和管理。 一个实例可以创建多个普通账号 。 需要手动给普通账号授予特定数据库的权限。 普通账号不能创建和管理其他账号，也不能断开其他账号的连接。 |


## 注意事项

- 

支持在控制台创建多个高权限账号和普通账号，也可以通过SQL命令创建、管理普通账号。

- 

如果您要迁移本地数据库到RDS，请在RDS实例中创建与本地数据库一致的迁移账号和数据库。

- 

分配数据库账号权限时，请按最小权限原则和业务角色创建账号，并合理分配只读和读写权限。必要时可以把数据库账号和数据库拆分成更小粒度，使每个数据库账号只能访问其业务范围内的数据。如果不需要数据库写入操作，请分配只读权限。

- 

为保障数据库的安全，请将数据库账号的密码设置为强密码，并定期更换。

## 创建账号

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏中选择账号管理。

- 

单击创建账号。

- 

设置如下参数。

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

| 参数 | 说明 |
| --- | --- |
| 数据库账号 | 长度为 2~63 个字符。 由小写字母、数字或下划线组成。 以字母开头，以字母或数字结尾。 不能和已有的账号名重复。 不能以 pg 开头。 不能使用 SQL 关键字。具体请参见 [SQL](https://www.postgresql.org/docs/14/sql-keywords-appendix.html) [关键字](https://www.postgresql.org/docs/14/sql-keywords-appendix.html) 。 |
| 账号类型 | RDS PostgreSQL 实例支持两种数据库账号：高权限账号和普通账号。 高权限账号拥有所有数据库的所有操作权限。 普通账号拥有已授权数据库（owner）的所有操作权限。 说明 操作权限包括 SELECT、INSERT、UPDATE、DELETE、TRUNCATE、REFERENCES、TRIGGER。 如需对账号权限进行精细化管理，例如创建只读账号，请参见 [RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/manage-permissions-in-an-apsaradb-rds-for-postgesql-instance.md) [权限管理最佳实践](products/rds/documents/apsaradb-rds-for-postgresql/manage-permissions-in-an-apsaradb-rds-for-postgesql-instance.md) 。 |
| 新密码 | 长度为 8~32 个字符。 由大写字母、小写字母、数字、特殊字符中的任意三种组成。 特殊字符为!@#$%^&*()_+-= |
| 确认密码 | 再次输入相同的密码。 |
| 备注 | 填写备注信息。 |


- 

单击确定。

## 创建数据库

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏单击数据库管理。

- 

单击创建数据库。

- 

设置如下参数。

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 数据库（DB）名称 | 最长 63 个字符。 由小写字母、数字、中划线、下划线组成。 以字母开头，以字母或数字结尾。 |
| 支持字符集 | 数据库的字符集。 重要 RDS PostgreSQL 数据库的字符集在数据库创建后不支持修改。 |
| Collate | 字符串排序规则。 |
| Ctype | 字符分类。 |
| 授权账号 | 设置数据库的所有者，对数据库拥有 ALL 权限。 |
| 备注 | 填写备注信息。 |


- 

单击创建。

创建成功后，即可在数据库管理中查看已创建的数据库及其相关信息。

| 参数 | 说明 |
| --- | --- |
| 限制并发量 | 指对应数据库并发请求执行的上限量，默认不限制，您也可以使用高权限账号登录数据库后，使用 ALTER DATABASE <数据库名> CONNECTION LIMIT <并发量>; 命令修改。 |
| 表空间 | 指数据库所属的表空间，默认为 pg_default ，表空间路径不支持查看和修改。 如果您使用 [一键上云](products/rds/documents/apsaradb-rds-for-postgresql/use-the-cloud-migration-feature-for-an-apsaradb-rds-for-postgresql-instance.md) 等迁移方式将本地自建数据库迁移上云时，表空间将与本地自建数据库表空间名称相同，支持将数据库和表的表空间修改为 pg_default 。 |


## 常见问题

创建的账号在只读实例上可以用吗？

答：主实例创建的账号会同步到只读实例，只读实例无法管理账号。账号在只读实例上只能进行读操作，不能进行写操作。

## 相关API

| API | 描述 |
| --- | --- |
| [创建数据库账号](products/rds/documents/api-create-an-account.md) | 创建账号 |


[上一篇：快速创建RDS PostgreSQL实例](products/rds/documents/apsaradb-rds-for-postgresql/create-an-apsaradb-rds-for-postgresql-instance.md)[下一篇：设置白名单](products/rds/documents/apsaradb-rds-for-postgresql/set-the-whitelist-1.md)

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
