# 产品使用限制与各项规格配额-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/quotas-and-limits

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

# RDS PostgreSQL使用限制

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库PostgreSQL在配额和使用上有一些限制，用来提高实例的稳定性和安全性。本文介绍PostgreSQL配额与使用限制的具体内容。

## 规格与性能

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

| 资源 | 规格 | 说明 |
| --- | --- | --- |
| 磁盘空间大小 | 高性能本地盘：最大 6,000 GB SSD 云盘：最大 6,000 GB ESSD 云盘：最大 64,000 GB 高性能云盘：最大 64,000 GB | 基于高性能本地盘的实例存储空间大小与实例规格绑定，云盘版实例的存储空间可购买大小不受实例规格限制。具体请参见 [主实例规格列表](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md) 。 |
| 连接数 | 最大 76,800 | 不同实例规格的连接数不同，请参见 [主实例规格列表](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md) 。 |
| IOPS | 高性能本地盘：最大 50,000 云盘：请参见 [关于云盘](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md) [IOPS](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md) | 无 |
| 内存大小 | 高性能本地盘：最大 512GB 云盘：最大 768GB | 云盘实例的底层操作系统以及相关管理服务会占用一部分内存，因此实例实际可用的内存不会达到规格显示的内存大小。占用内存详情如下： 底层操作系统：约 500~700 MB。 RDS 相关管理服务：约 500 MB。 |


## 配额

- 

- 

- 

- 

- 

- 

- 

- 

| 配额 | 限制 |
| --- | --- |
| 只读实例 | PG 10 或以上版本才支持只读实例，且只读实例必须创建在与主实例相同的地域内。 高性能本地盘： 主实例最多创建 5 个只读实例。 规格必须大于 8 核 32 GB（独享套餐），才支持只读实例。 云盘： 主实例最多创建 32 个只读实例。 只读实例为单节点架构，没有备节点。 只读实例的更多信息，请参见 [PostgreSQL](products/rds/documents/overview-of-read-only-apsaradb-rds-for-postgresql-instances.md) [只读实例简介](products/rds/documents/overview-of-read-only-apsaradb-rds-for-postgresql-instances.md) 。 |
| 标签 | 标签键必须唯一，最大设置 20 个。每次最多设置 50 个实例进行批量标签绑定。创建标签，请参见 [创建标签](products/rds/documents/apsaradb-rds-for-postgresql/add-tags-to-apsaradb-rds-instances-1.md) 。 |
| 备份空间免费额度 | PostgreSQL 云盘实例仅支持快照备份，PostgreSQL 高性能本地盘实例仅支持物理备份。超出免费额度的部分 = 数据备份量 + 日志备份量 - 免费额度，单位为 GB，只入不舍。 高性能本地盘：物理备份空间的免费额度=50%×实例购买的存储空间。 云盘：快照备份空间的免费额度=200%×实例购买的存储空间。 备份的更多信息，请参见 [备份](products/rds/documents/apsaradb-rds-for-postgresql/back-up-an-apsaradb-rds-for-postgresql-instance.md) [PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/back-up-an-apsaradb-rds-for-postgresql-instance.md) [数据](products/rds/documents/apsaradb-rds-for-postgresql/back-up-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 实例备份保留天数 | 默认为 7 天，最大 730 天。 |
| 错误日志保留天数 | 30 天。查看错误日志，请参见 [查看日志](products/rds/documents/apsaradb-rds-for-postgresql/view-the-logs-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 慢日志明细保留天数 | 30 天。查看慢日志明细，请参见 [查看日志](products/rds/documents/apsaradb-rds-for-postgresql/view-the-logs-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |


## 命名限制

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

| 限制项 | 限制说明 |
| --- | --- |
| 实例名 | 长度为 2~256 个字符。 由大小写字母、中文、数字、下划线（_）或短横线（-）组成。 以大小写字母或中文开头。 |
| 用户名 | 长度为 2~63 个字符。 由小写字母、数字或下划线组成。 以字母开头，以字母或数字结尾。 不能和已有的账号名重复。 不能以 pg 开头。 不能使用 SQL 关键字。具体请参见 [SQL](https://www.postgresql.org/docs/14/sql-keywords-appendix.html) [关键字](https://www.postgresql.org/docs/14/sql-keywords-appendix.html) 。 |
| 数据库名 | 长度不超过 63 个字符。 由小写字母、数字、下划线（_）或短横线（-）组成。 以字母开头，以字母或数字结尾。 不能和已有的数据库名重复。 不能使用 SQL 关键字。具体请参见 [SQL](https://www.postgresql.org/docs/14/sql-keywords-appendix.html) [关键字](https://www.postgresql.org/docs/14/sql-keywords-appendix.html) 。 |


## 安全限制

- 

- 

- 

- 

| 限制项 | 限制说明 |
| --- | --- |
| 密码 | 密码需要满足以下要求： 长度为 8~32 个字符。 由大写字母、小写字母、数字、特殊字符中的至少三种组成。特殊字符为： !@#$%^&*()_+-= 。 |
| 端口 | RDS PostgreSQL 实例的默认端口为 5432，允许用户手动修改端口号。 |
| 实例参数 | 出于安全和稳定性考虑，部分参数不支持修改。大部分实例参数可以使用控制台或 API 进行修改，修改参数方法请参见 [设置实例参数](products/rds/documents/apsaradb-rds-for-postgresql/modify-the-parameters-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 云盘加密 | 云盘加密只能在创建实例时开启且不能关闭。设置云盘加密，请参见 [云盘加密](products/rds/documents/apsaradb-rds-for-postgresql/configure-disk-encryption-for-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 实例可加入安全组数量 | 最大 10 个。 如果云数据库 RDS 实例与云服务器处于不同的安全组，云服务器不能访问 RDS。 RDS 实例只能添加与自身网络类型相同的安全组，即实例为专有网络 VPC 时，只能添加 VPC 类型的安全组；实例为经典网络时，只能添加经典网络类型的安全组。 设置安全组，请参见 [设置安全组](products/rds/documents/apsaradb-rds-for-postgresql/configure-a-security-group-for-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 实例可添加白名单分组数量 | 最大 50 个。添加白名单，请参见 [设置白名单](products/rds/documents/apsaradb-rds-for-postgresql/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance-1.md) 。 |
| root 权限账号 | 不可创建，RDS 无法向用户提供 superuser 权限。 |
| 高权限账号 | 高权限账号只能通过控制台或 API 创建和管理。支持多个高权限账号，可以断开任意账号的连接。 创建账号，请参见 [创建账号](products/rds/documents/apsaradb-rds-for-postgresql/create-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 普通账号 | 普通账号可以通过控制台、API 或者 SQL 语句创建和管理。需要手动给普通账号授予特定数据库的权限。不能创建和管理其他账号，也不能断开其他账号的连接。 创建账号，请参见 [创建账号](products/rds/documents/apsaradb-rds-for-postgresql/create-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |


## SQL使用限制

RDS PostgreSQL实例中SQL的使用限制与官方保持一致，请参见[PostgreSQL SQL](https://www.postgresql.org/docs/14/sql-commands.html)[命令参考](https://www.postgresql.org/docs/14/sql-commands.html)和[PostgreSQL](https://www.postgresql.org/docs/14/limits.html)[限制](https://www.postgresql.org/docs/14/limits.html)。

## 其它限制

| 限制项 | 限制说明 |
| --- | --- |
| 外网地址 | 外网地址需要手动申请。申请外网地址，请参见 [查看或修改连接地址和端口](products/rds/documents/apsaradb-rds-for-postgresql/view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 搭建数据库复制 | 提供主备复制架构（基础系列除外），其中的备（slave）实例不对用户开放，用户应用不能直接访问。 |
| 重启 RDS 实例 | 必须通过控制台或 OpenAPI 操作重启实例。 |
| 创建表空间 | 不支持。 |


[上一篇：计费常见问题](products/rds/documents/apsaradb-rds-for-postgresql/billing-faq.md)[下一篇：动态与公告](products/rds/documents/apsaradb-rds-for-postgresql/announcements-and-updates-of-apsaradb-rds-for-postgresql.md)

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
