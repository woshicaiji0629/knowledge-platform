# 创建PostgreSQL只读实例以扩展读取能力-云数据库RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/create-a-read-only-apsaradb-rds-for-postgresql-instance

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

# 创建RDS PostgreSQL只读实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当您面临数据库读取压力大幅增加时，云数据库RDS PostgreSQL支持创建只读实例来扩展读取能力，提高应用的整体吞吐量。只读实例使用物理复制技术，能够实时同步主实例数据，确保数据的一致性。

关于只读实例的更多介绍，请参见[PostgreSQL](products/rds/documents/overview-of-read-only-apsaradb-rds-for-postgresql-instances.md)[只读实例简介](products/rds/documents/overview-of-read-only-apsaradb-rds-for-postgresql-instances.md)。

## 前提条件

您已创建PostgreSQL主实例，主实例满足以下条件：

- 

实例版本：需为在售版本，[停售版本](products/rds/documents/apsaradb-rds-for-postgresql/lifecycles-of-major-engine-versions.md)不支持创建只读实例。

- 

实例系列：高可用系列。

- 

实例规格：

- 

云盘：无特殊要求。

- 

高性能本地盘：如果使用高性能本地盘，规格为独享套餐（8核32 GB及以上）。

- 

计费方式：包年包月或按量付费，Serverless计费方式的实例暂不支持创建只读实例。

说明

- 

创建PostgreSQL只读实例前，请在基本信息页面确认实例系列及规格信息。如果不满足要求，且需要创建只读实例时，请单击变更配置，将[基础系列变更为高可用系列](products/rds/documents/apsaradb-rds-for-postgresql/upgrade-an-apsaradb-rds-for-postgresql-instance-from-basic-edition-to-high-availability-edition.md)后再创建只读实例。

- 

支持创建[高可用系列](products/rds/documents/apsaradb-rds-for-postgresql/rds-high-availability-edition.md)或[基础系列](products/rds/documents/apsaradb-rds-for-postgresql/rds-basic-edition.md)的只读实例；其中高可用系列的只读实例为高可用架构（由主节点和备节点组成）。

## 注意事项

- 

创建只读实例时，必须选择与主实例相同的VPC，否则将会创建失败并且退款。

- 

只能在主实例内创建只读实例，不能将已有实例切换为只读实例。

- 

由于创建只读实例时是从备实例复制数据，因此不会影响主实例。

- 

只读实例的参数不继承主实例上的参数设置，会生成默认的参数值，可以在只读实例的控制台上进行修改。

重要

新通用型只读实例的参数会继承主实例上的参数设置。新通用型只读实例的更多信息，请参见[RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/read-only-apsaradb-rds-for-postgresql-instance-types.md)[只读实例规格列表](products/rds/documents/apsaradb-rds-for-postgresql/read-only-apsaradb-rds-for-postgresql-instance-types.md)。

- 

创建的只读实例存储类型与主实例一致。

- 

高性能本地盘只读实例的规格和存储空间不能低于主实例。

- 

云盘版只读实例的规格建议与主实例保持一致，或大于等于主实例规格的1/2，避免只读实例性能与主实例相差过大而导致的复制延迟、OOM等情况。

- 

云盘版只读实例存储空间不能低于主实例，且如果主实例内存大于只读实例内存，主实例变配时会重启只读实例。

- 

创建的只读实例内存需满足如下要求：

| 主实例内存范围 | 只读实例内存要求 |
| --- | --- |
| (0 GB~64 GB] | 至少为主实例内存的 1/4 |
| (64 GB~256 GB] | 至少为主实例内存的 1/6 |
| (256 GB~9999 GB] | 至少为主实例内存的 1/8 |


- 

高性能本地盘主实例最多创建5个只读实例，云盘主实例最多创建32个只读实例。

- 

高性能本地盘实例的只读实例为高可用系列，云盘实例的只读实例包含基础系列和高可用系列。

说明

基础系列为单节点架构没有备节点，因此无法保障可用性。建议您购买多个只读实例，使用libpq或JDBC实现[自动故障转移](products/rds/documents/apsaradb-rds-for-postgresql/configure-automatic-failover-and-read-or-write-splitting.md)，或者通过[数据库代理](products/rds/documents/apsaradb-rds-for-postgresql/what-are-database-proxies.md)实现读写自动分离。您也可以直接购买高可用系列只读实例。

- 

创建只读实例会产生费用，支持包年包月和按量付费两种方式计费。费用请以实际购买页为准。

## 创建只读实例

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在实例分布区域，单击只读实例后的添加。

- 

设置只读实例的参数。

- 

- 

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 计费方式 | 包年包月 ：适合长期使用（一次性付费）。 按量付费 ：适合短期使用（按小时付费）。您可以先创建按量付费的只读实例，确认实例符合要求后再转包年包月。 |
| 产品系列 | 基础系列 ：单节点的只读实例，性价比高，适用于学习或测试。故障恢复和重启耗时较长。 高可用系列 （默认）：拥有一个主节点和一个备节点，可实现只读实例的高可用，适用于生产环境，适合 80%以上的用户场景。 说明 如果 产品系列 选择高可用系列，则还需选择主节点可用区、部署方案（多可用区部署或单可用区部署）以及备节点可用区。 |
| 产品类型 | 仅当主实例 存储类型 为 ESSD 云盘 或 高性能云盘 时，才支持选择 倚天版 。 标准版 和 倚天版 的更多信息，请参见 [产品类型](products/rds/documents/product-overview/product-types.md) 。 |
| 可用区 | 可用区是地域中的一个独立物理区域，不同可用区之间没有实质性区别。相比单可用区，多可用区能提供可用区级别的容灾。 |
| 实例规格 | 通用规格 ：通用型的实例规格，独享被分配的内存和 I/O 资源，与同一服务器上的其他通用型实例共享 CPU 和存储资源。 独享规格 ：独享或独占型的实例规格。独享型指独享被分配的 CPU、内存、存储和 I/O 资源。独占型是独享型的顶配，独占整台服务器的 CPU、内存、存储和 I/O 资源。 说明 每种规格都有对应的 CPU 核数、内存、最大连接数和最大 IOPS。高性能本地盘主实例的只读实例规格不能低于主实例。规格详情请参见 [RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/read-only-apsaradb-rds-for-postgresql-instance-types.md) [只读实例规格列表](products/rds/documents/apsaradb-rds-for-postgresql/read-only-apsaradb-rds-for-postgresql-instance-types.md) 。 |
| 存储空间 | 存储空间包括数据空间、系统文件空间、WAL 文件空间和事务文件空间。调整存储空间时最小单位为 5 GB。 说明 只读实例存储空间不能低于主实例。各规格的存储空间大小，请参见 [RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/read-only-apsaradb-rds-for-postgresql-instance-types.md) [只读实例规格列表](products/rds/documents/apsaradb-rds-for-postgresql/read-only-apsaradb-rds-for-postgresql-instance-types.md) 。 |


- 

单击下一步：实例配置，设置如下参数。

| 参数 | 说明 |
| --- | --- |
| 网络类型 | 默认与主实例网络类型、 VPC 和 主节点交换机 保持一致。 |
| 实例释放保护 | 如果 计费方式 为 按量付费 ，则可以为按量付费实例开启 实例释放保护 ，防止按量付费实例被意外释放。更多信息，请参见 [开启和关闭实例释放保护](products/rds/documents/apsaradb-rds-for-postgresql/enable-or-disable-the-release-protection-feature-for-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 资源组 | 默认与主实例资源组相同，不支持修改。 |
| 时区 | 默认与主实例时区保持一致。 |
| SLR 授权 | 无需配置，购买主实例时已授权。SLR 授权的相关信息，请参见 [【产品/功能变更】2022](products/rds/documents/apsaradb-rds-for-postgresql/slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [年](products/rds/documents/apsaradb-rds-for-postgresql/slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [10](products/rds/documents/apsaradb-rds-for-postgresql/slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [月](products/rds/documents/apsaradb-rds-for-postgresql/slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [10](products/rds/documents/apsaradb-rds-for-postgresql/slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [日起创建](products/rds/documents/apsaradb-rds-for-postgresql/slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [实例需](products/rds/documents/apsaradb-rds-for-postgresql/slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [SLR](products/rds/documents/apsaradb-rds-for-postgresql/slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [授权](products/rds/documents/apsaradb-rds-for-postgresql/slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) 。 |
| 实例名称 | 设置实例名称，方便管理。 |
| 标签 | 支持创建实例时为实例绑定标签，实例创建后，可根据标签进行筛选。更多信息，请参见 [根据标签筛选实例](products/rds/documents/apsaradb-rds-for-postgresql/use-tags-to-filter-apsaradb-rds-for-mysql-instances-2.md) 。 |


- 

单击下一步：确认订单。

- 

确认参数配置，选择购买量和购买时长（仅包年包月实例）后，单击确认下单并完成支付。

只读实例创建时间与主实例存储类型及磁盘大小相关，请参考以下预估时间，耐心等待只读实例创建。

- 

主实例存储类型为SSD云盘，创建时间约为一次全量备份时间+20分钟。

- 

主实例存储类型为ESSD云盘或高性能云盘，创建时间约为20分钟。

说明

- 

创建只读实例期间对主实例无影响，创建成功后会在主实例中产生一个WAL Sender的进程，用于发送WAL日志到只读实例。

- 

RDS PostgreSQL通过快照的方式搭建只读实例，与数据量大小无关。

## 查看只读实例

### 方法一：在实例列表中查看只读实例

- 

登录[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[管理控制台](https://rdsnext.console.aliyun.com/rdsList/basic)，在左侧单击实例列表，然后在上方选择地域。

- 

在实例列表中找到主实例（带有标识），展开主实例的下拉列表。

- 

单击只读实例的ID。

### 方法二：在主实例的基本信息页面查看只读实例

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在主实例的基本信息页面，把鼠标悬停于只读实例的数量上，单击只读实例的ID。

## 查看只读实例的延迟时间

只读实例同步主实例的数据时，可能会有一定的延迟。您可以在只读实例的基本信息页面查看延迟时间。

## 相关API

| API | 描述 |
| --- | --- |
| [CreateReadOnlyDBInstance](products/rds/documents/apsaradb-rds-for-postgresql/api-rds-2014-08-15-createreadonlydbinstance-postgresql.md) | 创建 RDS 只读实例。 |


## 常见问题

- 

Q：只读实例的计费方式可以转化吗？

A：可以。具体操作，请参见[按量付费转包年包月](products/rds/documents/apsaradb-rds-for-postgresql/switch-an-apsaradb-rds-for-postgresql-instance-from-pay-as-you-go-to-subscription.md)或[包年包月转按量付费](products/rds/documents/apsaradb-rds-for-postgresql/package-year-package-month-to-pay-by-volume.md)。

- 

Q：变更只读实例的配置、释放只读实例、转化只读实例计费方式会影响主实例吗？

A：不会。

- 

Q：主实例上创建的账号在只读实例上可以用吗？

A：主实例创建的账号会同步到只读实例，只读实例无法管理账号。账号在只读实例上只能进行读操作，不能进行写操作。

- 

Q：只读实例可以转变为常规实例吗？比如作为容灾实例？

A：暂不支持。

- 

Q：能否对只读实例的数据进行备份？实例的自动备份能否在只读实例上进行？

A：无需对只读实例进行备份，备份在主实例上进行，由于RDS PostgreSQL的备份使用快照备份，对主实例没有性能开销。

- 

Q：只读实例是否支持并行复制？

A：RDS PostgreSQL采用的是物理流复制，基于WAL日志文件同步加回放来实现数据复制能力，效率高，无需使用并行复制。

- 

Q：事务日志的清除机制是怎样的？

A：RDS PostgreSQL的WAL日志备份完成后，由内核在Checkpoint操作中自动清理。

- 

Q：如何通过只读实例延迟时间判断复制是否正常？

A：通常情况下只读实例延迟时间在1秒以内，如果超过1秒，说明数据同步延迟，极端场景下也可能出现断开的场景。

- 

Q：复制延迟通常是什么原因引起的？

A：常见原因及解决办法如下：

- 

原因1：主实例规格大，只读实例规格过小，导致主备延迟过大。

解决方法：升级只读实例规格，更多信息，请参见[变更配置](products/rds/documents/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)。

- 

原因2：参数max_standby_streaming_delay设置不合理，导致复制延迟较高。参数设置方法，请参见[设置实例参数](products/rds/documents/apsaradb-rds-for-postgresql/modify-the-parameters-of-an-apsaradb-rds-for-postgresql-instance.md)。

解决办法：调整参数max_standby_streaming_delay取值：

- 

该值设置较小时可以减少只读实例与主实例之间数据复制延迟，但过小时可能会导致只读实例的事务被取消。

- 

该值设置过大时可能会造成复制延迟。

[上一篇：只读实例](products/rds/documents/apsaradb-rds-for-postgresql/rds-for-postgresql-read-only-instances.md)[下一篇：Serverless实例](products/rds/documents/apsaradb-rds-for-postgresql/serverless-apsaradb-rds-for-postgresql-instances.md)

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
