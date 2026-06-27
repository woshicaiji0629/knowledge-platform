# 变更RDS PostgreSQL实例的规格与存储空间-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance

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

# 变更配置

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍如何变更RDS PostgreSQL实例配置，包括系列、规格和存储空间。

## 前提条件

- 

实例的计费方式为包年包月或按量付费。

说明

如果实例的计费方式为Serverless，变更Serverless配置请参见[Serverless](products/rds/documents/apsaradb-rds-for-postgresql/serverless-apsaradb-rds-for-postgresql-instances.md)[实例](products/rds/documents/apsaradb-rds-for-postgresql/serverless-apsaradb-rds-for-postgresql-instances.md)。

- 

实例状态为运行中。

- 

您的阿里云账号没有未支付的续费订单。

## 变更项

如您需要横向扩展数据库的读取能力，请参见[PostgreSQL](products/rds/documents/overview-of-read-only-apsaradb-rds-for-postgresql-instances.md)[只读实例简介](products/rds/documents/overview-of-read-only-apsaradb-rds-for-postgresql-instances.md)和[创建](products/rds/documents/apsaradb-rds-for-postgresql/create-a-read-only-apsaradb-rds-for-postgresql-instance.md)[PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/create-a-read-only-apsaradb-rds-for-postgresql-instance.md)[只读实例](products/rds/documents/apsaradb-rds-for-postgresql/create-a-read-only-apsaradb-rds-for-postgresql-instance.md)，通过只读实例来分担主实例的压力。

警告

根据变更项不同，切换过程中可能会出现业务闪断或实例重启，而且与数据库、账号、网络等相关的大部分操作都无法执行，请选择在[可维护时间段](products/rds/documents/apsaradb-rds-for-postgresql/set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md)内执行变配操作。

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

| 变更项 | 说明 | 业务影响 |
| --- | --- | --- |
| 系列 | 当前支持： [PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/upgrade-an-apsaradb-rds-for-postgresql-instance-from-basic-edition-to-high-availability-edition.md) [基础系列升级高可用系列](products/rds/documents/apsaradb-rds-for-postgresql/upgrade-an-apsaradb-rds-for-postgresql-instance-from-basic-edition-to-high-availability-edition.md) [PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/upgrade-the-rds-edition-from-rds-basic-edition-or-rds-high-availability-edition-to-rds-cluster-edition.md) [基础系列或高可用系列升级集群系列](products/rds/documents/apsaradb-rds-for-postgresql/upgrade-the-rds-edition-from-rds-basic-edition-or-rds-high-availability-edition-to-rds-cluster-edition.md) | 会出现短暂业务闪断。 |
| 产品类型 | 支持将产品类型在标准版和倚天版间变更，标准版和倚天版间差异，请参见 [产品类型](products/rds/documents/product-overview/product-types.md) 。 说明 如果变更时无法选择目标产品类型，可能实例所在可用区暂无对应资源在售。 您可以先到实例售卖页查看目标产品类型的在售可用区情况，然后通过 [迁移可用区](products/rds/documents/apsaradb-rds-for-postgresql/migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region.md) 功能，将当前实例迁移至目标可用区后，再进行变更配置。 如果需要变更配置实例的产品类型，需要确保变更后内核小版本大于等于当前实例内核小版本，如果当前实例内核小版本高于变更后内核小版本，则不支持变更。 倚天版规格暂不支持 [plv8](https://plv8.github.io/) 和 [rdkit](products/rds/documents/apsaradb-rds-for-postgresql/use-the-rdkit-plug-in.md) 插件，由标准版变更为倚天版时，请确认未使用这几款插件。各产品类型支持情况请参见 [支持插件列表](products/rds/documents/apsaradb-rds-for-postgresql/extensions-supported-by-apsaradb-rds-for-postgresql.md) 。 | 会出现短暂业务闪断。 |
| 存储类型 | 支持变更存储类型。 云盘实例： 支持 SSD 云盘 升级为 ESSD 云盘 （ ESSD PL1 云盘 、 ESSD PL2 云盘 或 ESSD PL3 云 盘），不支持由 ESSD 云盘降级为 SSD 云盘。 支持 ESSD PL1 云盘 、 ESSD PL2 云盘 和 ESSD PL3 云盘 间的升级或降级。 支持 ESSD 云盘变更为 高性能云盘 ，不支持高性能云盘变更为 ESSD 云盘。 高性能本地盘实例：高性能本地盘实例不支持变更存储类型。 说明 不同存储类型间的性能差异，请参见 [存储类型](products/rds/documents/product-overview/storage-types.md) 。 | ESSD PL1 云盘 、 ESSD PL2 云盘 和 ESSD PL3 云盘 间升级或降级存储类型，不会造成业务闪断。 ESSD 云盘变更为 高性能云盘 时，不会造成业务闪断。 SSD 云盘 升级到 ESSD 云盘 时，将会出现短暂业务闪断。 |
| 实例规格 | 支持变更实例规格。 说明 高可用系列 [通用型规格](products/rds/documents/apsaradb-rds-for-postgresql/primary-apsaradb-rds-for-postgresql-instance-types.md) 支持变更为 CPU 16 核以上的独享规格。 由 [通用型规格](products/rds/documents/apsaradb-rds-for-postgresql/primary-apsaradb-rds-for-postgresql-instance-types.md) 变更为独享规格后，支持再次变更为通用型规格。 部分待停售的通用规格暂不支持变更，更多信息，请参见 [【停售/下线】2023](products/rds/documents/apsaradb-rds-for-postgresql/some-general-purpose-instance-types-are-no-longer-available-for-purchase.md) [年](products/rds/documents/apsaradb-rds-for-postgresql/some-general-purpose-instance-types-are-no-longer-available-for-purchase.md) [01](products/rds/documents/apsaradb-rds-for-postgresql/some-general-purpose-instance-types-are-no-longer-available-for-purchase.md) [月](products/rds/documents/apsaradb-rds-for-postgresql/some-general-purpose-instance-types-are-no-longer-available-for-purchase.md) [31](products/rds/documents/apsaradb-rds-for-postgresql/some-general-purpose-instance-types-are-no-longer-available-for-purchase.md) [日起](products/rds/documents/apsaradb-rds-for-postgresql/some-general-purpose-instance-types-are-no-longer-available-for-purchase.md) [RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/some-general-purpose-instance-types-are-no-longer-available-for-purchase.md) [部分基础系列通用规格停止售卖](products/rds/documents/apsaradb-rds-for-postgresql/some-general-purpose-instance-types-are-no-longer-available-for-purchase.md) 。 不支持 变更至 [基础系列倚天版规格](products/rds/documents/apsaradb-rds-for-postgresql/primary-apsaradb-rds-for-postgresql-instance-types.md) 。 | 实例规格升配，会出现短暂业务闪断。 实例规格降配，会导致实例主库重启，且重启后将有短暂业务闪断。 变配过程中部分内核参数需要保持只读实例和主实例一致，因此变配过程中只读实例会出现重启导致短暂业务闪断。 |
| 存储空间 | 支持存储空间扩容和缩容。 存储空间扩容：至少增加 5 GB，至多不能超过当前规格的存储空间限制，详情请参见 [主实例规格列表](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md) 。 存储空间缩容：云盘实例允许在同一系列、同一架构下缩容，缩容后的最小空间由公式 min{使用量*1.3，使用量+400 GB} 计算，不得低于当前规格允许的最小存储空间，存储空间调整步长 5 GB。更多信息，请参见 [ESSD](products/rds/documents/apsaradb-rds-for-postgresql/reduce-the-storage-capacity-of-an-apsaradb-rds-for-postgresql-instance-that-uses-essds.md) [云盘缩容](products/rds/documents/apsaradb-rds-for-postgresql/reduce-the-storage-capacity-of-an-apsaradb-rds-for-postgresql-instance-that-uses-essds.md) 。 存储空间缩容示例 假设实例的存储类型为 ESSD PL1 云盘（最小存储空间为 20 GB），存储空间为 2000 GB： 使用量为 10 GB，根据公式计算得 13 GB，低于 20 GB，最小可缩容至 20 GB。 使用量为 500 GB，根据公式计算得 650 GB，最小可缩容至 650 GB。 使用量为 1500 GB，根据公式计算得 1900 GB，最小可缩容至 1900 GB。 说明 如果您的 RDS 实例为高性能本地盘实例，建议使用大版本升级功能，将实例升级到云盘高版本，在升级的同时支持存储空间缩容。更多信息，请参见 [升级数据库大版本](products/rds/documents/apsaradb-rds-for-postgresql/upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) 。 如果您的云盘实例在 2022 年 10 月 10 日前（旧架构实例）创建，需要升级内核小版本到最新后，再缩容存储空间。更多信息，请参见 [升级内核小版本](products/rds/documents/apsaradb-rds-for-postgresql/update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) 。 云盘实例不仅可以通过变更配置手动调整存储空间，还支持 [设置存储空间自动扩容](products/rds/documents/apsaradb-rds-for-postgresql/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-postgresql-instance.md) ，当数据库实例的剩余存储空间百分比达到设定的扩容阈值时，实例将会触发自动扩容，保障您的业务稳定运行。 如果实例当前正在进行备份，扩容任务需等待备份完成后再进行，建议您在实例的备份时间之外进行存储空间扩容。 | 云盘： 扩容不会造成业务闪断。 缩容会出现短暂业务闪断。 高性能本地盘：会出现短暂业务闪断。 |


## 计费规则

请参见[变配的计费规则](products/rds/documents/product-overview/specification-changes.md)。

## 注意事项

- 

由于基础系列只有一个数据库节点，没有备节点作为热备份，因此当该节点意外宕机或者执行变更配置、版本升级等任务时，会出现较长时间的不可用。如果业务对数据库的可用性要求较高，不建议使用基础系列，可选择其他系列（如高可用系列）。

说明

变更配置是否会造成业务闪断，与变更配置项相关，具体请参见[变更项](products/rds/documents/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)的业务影响列。

- 

根据变更项不同，切换过程中可能会出现业务闪断或实例重启，而且与数据库、账号、网络等相关的大部分操作都无法执行，请选择在[可维护时间段](products/rds/documents/apsaradb-rds-for-postgresql/set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md)内执行变配操作。各变更项的业务影响，请参见[变更项](products/rds/documents/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)的业务影响列。

- 

变更配置不会导致实例ID和连接地址的改变。

- 

变更配置后无需您手动重启实例。

- 

如果目标实例下存在只读实例，变更存储空间时，需确保只读实例的存储空间大于等于主实例的存储空间。建议：

- 

扩容存储空间时，先扩容只读实例的存储空间。待所有只读实例的存储空间扩容完成后，再扩容主实例的存储空间。

- 

缩容存储空间时，先缩容主实例的存储空间。待主实例的存储空间缩容完成后，再缩容只读实例的存储空间。

- 

如果目标实例下存在只读实例，变更实例规格时，需确保高性能本地盘只读实例规格大于等于主实例规格；云盘版只读实例规格大于等于主实例规格的1/2。建议：

- 

升配实例规格时，先升配只读实例规格。待所有只读实例规格升配完成后，再升配主实例规格。

- 

降配实例规格时，先降配主实例规格。待主实例规格降配完成后，再降配只读实例规格。

- 

升级实例规格时，必须确保实例所在的交换机具有至少两个可用IP地址，否则会导致实例规格升级失败。您可以在[专有网络管理控制台](https://vpcnext.console.aliyun.com/vpc)查看目标交换机可用的IP地址数量。当交换机的IP地址不足时，请先切换至IP资源充足的交换机，然后再升级实例规格，详情请参见[切换虚拟交换机](products/rds/documents/apsaradb-rds-for-postgresql/switch-an-apsaradb-rds-for-postgresql-instance-to-a-different-vswitch.md)。

## 操作步骤

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在配置信息区域单击变更配置。

- 

（仅包年包月实例需要执行此步骤）在弹出的对话框中，选择变更方式，单击下一步。

立即升配或立即降配：变配后，新的配置立即生效。包年包月实例和按量付费实例都支持立即升降配。

变更任务下达后，系统将磁盘数据同步到一个新实例，然后根据立即升降配确定时间，到时间后系统将原实例的实例ID和连接地址等信息切换到新实例，实例ID、连接地址等不会改变。

警告

如果选择立即降配，切换过程中会导致实例主库重启，请选择在[可维护时间段](products/rds/documents/apsaradb-rds-for-postgresql/set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md)内执行变配操作。

- 

修改实例的配置。支持修改的变更项，请参见[变更项](products/rds/documents/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)。

- 

选择变更实例配置的执行时间。

- 

立即执行：变更实例配置会涉及到底层的数据迁移，您可以选择在数据迁移后立即切换。

- 

可维护时间内进行切换：在变更配置生效期间，可能会出现业务闪断或实例重启，而且与数据库、账号、网络等相关的大部分操作都无法执行，因此您可以选择在[可维护时间段](products/rds/documents/apsaradb-rds-for-postgresql/set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md)内执行切换的操作。

说明

- 

云盘实例：仅增加存储空间或ESSD存储类型变更时，对业务无影响，变配后立即执行，无需选择可维护时间内进行切换。

- 

高性能本地盘实例：建议选择可维护时间内进行切换，如果实例所在主机上有足够存储空间用于扩容，则立即升级，对业务无影响。如果存储空间不足，则会触发数据迁移，迁移完成后根据您选择的切换时间进行切换（期间保持增量同步）。

- 

在变配实例页面中确认变配前后的实例信息，阅读服务协议后，单击确认下单并完成支付。

警告

- 

变配订单提交后无法取消，请在执行变配前详细评估业务需求。

- 

为确保变配的稳定进行，在提交变配订单至变配完成期间，请勿执行DDL操作。

## 常见问题

- 

Q：云盘版实例如何变更为高性能本地盘实例？

A：请参见[云盘如何变更为高性能本地盘](products/rds/documents/support/how-do-i-change-the-storage-type-from-standard-ssd-to-premium-local-ssd.md)。

- 

Q：仅扩容存储空间，需要迁移数据到新实例吗？

A：

- 

云盘实例：不需要。

- 

高性能本地盘实例：需要检查实例所在主机上是否有足够存储空间用于扩容。

- 

如果有足够存储空间，则直接扩容，不需要迁移数据。

- 

如果没有足够存储空间，则需要迁移数据到拥有足够存储空间的主机上。

- 

Q：如何缩容存储空间？

A：

- 

本地盘实例，建议使用大版本升级功能，将实例升级到云盘高版本，在升级的同时支持存储空间缩容。更多信息，请参见[升级数据库大版本](products/rds/documents/apsaradb-rds-for-postgresql/upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md)。

- 

云盘实例，请参见[ESSD](products/rds/documents/apsaradb-rds-for-postgresql/reduce-the-storage-capacity-of-an-apsaradb-rds-for-postgresql-instance-that-uses-essds.md)[云盘缩容](products/rds/documents/apsaradb-rds-for-postgresql/reduce-the-storage-capacity-of-an-apsaradb-rds-for-postgresql-instance-that-uses-essds.md)。

- 

Q：CPU、内存、磁盘同时升配，会闪断多久？

A：无论是单独升配CPU、内存、磁盘中的一个，还是三个同时升配，闪断的时间都是一样的，一般是分钟级的。切换过程中，可能会出现业务闪断或实例重启，而且与数据库、账号、网络等相关的大部分操作都无法执行，请选择在可维护时间段内执行变配操作。各变更项的业务影响，请参见[变更项的业务影响](products/rds/documents/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)。

- 

Q：单独变更只读实例配置是否会对主实例产生影响？

A：单独变更只读实例配置通常不会对主实例产生影响。然而，仍需与主实例保持一定的关联，详情请参见本文[注意事项](products/rds/documents/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)。

## 相关API

| API | 描述 |
| --- | --- |
| [ModifyDBInstanceSpec](products/rds/documents/api-change-instance-configuration.md) | 变更 RDS 实例配置。 |


[上一篇：变更实例](products/rds/documents/apsaradb-rds-for-postgresql/instance-configuration-change.md)[下一篇：变更计费方式](products/rds/documents/apsaradb-rds-for-postgresql/change-a-billing-method.md)

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
