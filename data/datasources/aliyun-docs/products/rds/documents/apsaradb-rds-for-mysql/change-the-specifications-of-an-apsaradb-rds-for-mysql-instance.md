# RDS MySQL变更配置-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance

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

# 变更配置

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍如何变更RDS MySQL实例配置，包括变更实例系列、升降级实例规格以及扩缩容存储空间。

RDS MySQL实例支持的全量变更项请参见[实例变更项](products/rds/documents/apsaradb-rds-for-mysql/configuration-items-for-an-apsaradb-rds-for-mysql-instance.md)。

其他引擎变更配置请参见：

- 

[SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/change-the-specifications-of-an-apsaradb-rds-for-sql-server-instance.md)[变更配置](products/rds/documents/apsaradb-rds-for-sql-server/change-the-specifications-of-an-apsaradb-rds-for-sql-server-instance.md)

- 

[PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)[变更配置](products/rds/documents/apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)

- 

[MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/change-the-specifications-of-an-apsaradb-rds-for-mariadb-instance.md)[变更配置](products/rds/documents/apsaradb-rds-for-mariadb/change-the-specifications-of-an-apsaradb-rds-for-mariadb-instance.md)

## 前提条件

- 

实例的计费方式为包年包月或按量付费。

说明

如果实例的计费方式为Serverless，请参见[配置](https://help.aliyun.com/zh/document_detail/421557.html#task-2202683)[Serverless](https://help.aliyun.com/zh/document_detail/421557.html#task-2202683)[实例](https://help.aliyun.com/zh/document_detail/421557.html#task-2202683)。

- 

您的阿里云账号下没有未支付的续费订单。

- 

实例状态为运行中。如您的实例已进入“锁定中”，请先[解锁实例](products/rds/documents/apsaradb-rds-for-mysql/what-do-i-do-if-my-apsaradb-rds-instance-is-in-the-locking-state.md)，再进行变更配置操作。

## 限制

- 

变配订单操作限制：提交配置变更订单后无法取消，请在执行变配前详细评估业务需求。

- 

只读实例变配限制：

- 

变更只读实例配置时，其所属主实例必须处于运行中状态。

- 

只读实例的存储空间必须大于或等于主实例当前存储空间。建议先完成所有只读实例的存储扩容，再扩容主实例存储空间。

- 

DuckDB分析只读实例的存储空间需要大于等于主实例的一半。

- 

存储空间缩容限制：

- 

高性能本地盘实例缩容

- 

缩容后的空间必须大于或等于当前已使用存储空间的120%。

示例：实例存储空间100 GB（已用50 GB），缩容后至少需保留60 GB（50×120%）。

- 

通用缩容限制

- 

基础系列或高可用系列：支持同一系列、同一架构下缩容。

- 

最小缩容值计算：min{当前使用量×1.3, 当前使用量+400 GB}，且需大于或等于当前规格支持的最小存储空间。

- 

调整步长：存储空间调整单位为5 GB。

- 

当实例Binlog产生较快时，需要本地保留足够多的日志，才允许实例进行缩容。日志备份的开启方法，请参见[修改](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)[RDS](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)[备份策略](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)。

- 

产品类型变配限制：

- 

可用区兼容性：相比标准版，倚天版[支持的可用区](products/rds/documents/product-overview/product-types.md)更少。如果因可用区限制导致无法变更，请先[变更实例可用区](products/rds/documents/apsaradb-rds-for-mysql/migrate-an-apsaradb-rds-for-mysql-instance-across-zones-in-the-same-region.md)，再变更产品类型。

- 

内核版本约束：变更后内核小版本必须大于或等于当前版本。若当前版本更高，则不支持变更。

- 

系列约束：基础系列仅支持从倚天版变更为标准版，高可用和集群系列可在倚天版与标准版间互相变更。

- 

[历史规格实例](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)变配限制：无法直接变配，需先升级配置至线上售卖规格，才能进行后续变更操作。

- 

如果实例使用的是SSD云盘，需先将存储类型升级为ESSD云盘，否则变配时会报Commodity.InvalidComponent错误。具体操作请参见[变更存储类型](products/rds/documents/support/how-do-i-change-the-storage-type-from-standard-ssd-to-premium-local-ssd.md)。

- 

其他限制：仅支持对[实例变更项](products/rds/documents/apsaradb-rds-for-mysql/configuration-items-for-an-apsaradb-rds-for-mysql-instance.md)中列出的项目进行变更。

## 影响

- 

- 

- 

- 

- 

- 

| [实例存储类型](products/rds/documents/product-overview/storage-types.md) | 变配项目 | 影响 |
| --- | --- | --- |
| 高性能本地盘实例 | 规格、系列、存储空间 | 本地无资源可用的情况下执行变更规格或系列会引发自动数据迁移，迁移完成后根据您选择的切换时间进行切换（期间保持增量同步）。 重要 变配会出现实例切换，通常切换影响时间约 15 秒（但若客户端配置不合理或驱动版本太低可能导致影响时间较久），请在业务低峰期进行变配，并确保您的应用有 [自动重连机制](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md) 。 实例切换期间，与数据库、账号、网络等相关的大部分操作都无法执行，详情请参见 [实例切换的影响](products/rds/documents/apsaradb-rds-for-mysql/untitled-document-1701914031929.md) 。 |
| 云盘实例 | 规格或系列 | 变配耗时为分钟级别，不受数据量大小的影响。 重要 变配会出现实例切换，通常切换影响时间约 15 秒（但若客户端配置不合理或驱动版本太低可能导致影响时间较久），请在业务低峰期进行变配，并确保您的应用有 [自动重连机制](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md) 。 实例切换期间，与数据库、账号、网络等相关的大部分操作都无法执行，详情请参见 [实例切换的影响](products/rds/documents/apsaradb-rds-for-mysql/untitled-document-1701914031929.md) 。 |
| 存储空间 | 扩容时：SSD 云盘扩容会有闪断，ESSD 云盘和高性能云盘扩容没有闪断。 缩容时：云盘缩容会有闪断影响，详情请参见 [云盘存储空间缩容（SSD](products/rds/documents/support/reduce-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-that-uses-essds.md) [云盘不支持缩容）](products/rds/documents/support/reduce-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-that-uses-essds.md) 。 说明 当云盘存在快照任务时，云盘扩容和云盘性能等级变更会等待快照任务执行结束后才执行。 |  |


说明

- 

变配操作无需您手动重启实例，且变配操作不会导致已存储数据的丢失。

- 

变配操作不会导致实例ID和连接地址改变，但如果实例发生了跨机迁移，连接地址对应的IP会发生变化，建议业务侧使用RDS连接地址访问数据库。

## 计费规则

请参见[变配的计费规则](products/rds/documents/product-overview/specification-changes.md)。

## 操作步骤

重要

提交配置变更订单后无法取消，请在执行变配前详细评估业务需求。

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在配置信息区域单击变更配置。

- 

（仅包年包月实例需要执行此步骤）在弹出的对话框中，选择变更方式，单击下一步。

变更方式说明如下：

立即升配或立即降配：变配后，新的配置立即生效。包年包月实例和按量付费实例都支持立即升降配。

变更任务下达后，系统将磁盘数据同步到一个新实例，然后根据变配确定的切换时间，到时间后系统将原实例的实例ID和连接地址等信息切换到新实例，实例ID、连接地址等不会改变。

- 

修改实例的配置。

说明

- 

所有实例类型都支持[变更规格](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)和存储空间，[历史规格实例](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)需要先升级配置至线上售卖规格后，再进行存储空间扩容。

- 

当前支持高可用系列高性能本地盘实例、基础系列或高可用系列云盘（不包括SSD云盘）实例对存储空间进行缩容，其他实例不支持降低存储空间。

- 

MySQL 8.4、8.0、5.7高可用系列的高性能本地盘实例可以变更存储类型到ESSD云盘。

- 

MySQL 5.7基础系列实例可以升级为高可用系列高性能本地盘实例。

- 

MySQL 8.4、8.0、5.7高可用系列的ESSD云盘实例可以变更为集群系列实例。

- 

变配实例页面的实例规格默认为当前规格，请确保调整后的实例规格相关参数满足您的需求，避免相关风险。

- 

选择切换时间。

- 

立即切换：数据迁移后立即切换。

- 

可维护时间内进行切换：在[可维护时间段](products/rds/documents/apsaradb-rds-for-mysql/set-the-maintenance-window-of-an-apsaradb-rds-for-mysql-instance.md)内执行切换操作。

重要

- 

RDS MySQL实例变配任务下发后，如果任务本身不涉及切换或闪断影响，则系统会忽略指定的运维时间配置，并立即完成任务。因此，只有在任务存在切换或闪断影响时，才会严格按照指定的运维时间执行。

- 

如选择可维护时间内进行切换，则实例会一直保持升降配中状态直到完成切换，在此期间无法对该实例执行升降配、版本升级、跨可用区迁移等实例级别的操作。

- 

仅增加存储空间或ESSD存储类型变更时，绝大多数情况下对业务无影响，变配后立即执行，无需选择可维护时间内进行切换。

- 

基础系列只有一个数据库节点，没有备节点作为热备份，因此当该节点变更配置时，会出现较长时间中断。请在非高峰期内进行变更配置，避免影响业务。

- 

非基础系列在变更配置生效期间，可能会出现一到两次实例切换，虽然不影响正常使用，但是请尽量在非高峰期进行变更配置，或确保您的应用有自动重连机制。实例切换的影响，请参见[实例切换的影响](products/rds/documents/apsaradb-rds-for-mysql/untitled-document-1701914031929.md)。

- 

在变配实例页面中确认变配前后的实例信息，单击去支付并完成支付。

警告

- 

变配订单提交后无法取消，请在执行变配前详细评估业务需求。

- 

为确保变配的稳定进行，在提交变配订单至变配完成期间，请勿执行DDL操作。

## 常见问题

### 磁盘扩缩容问题

- 

Q：实例已扩容磁盘，为何仍显示锁定？

A：磁盘满导致锁定时，扩容后需等待升配任务完成自动解锁。您可在实例基本信息页右上角单击按钮跳转至任务列表页面，查看扩容任务进度。

- 

Q：存储扩容为何会闪断？

A：存储扩容需实例切换，闪断影响详见[实例切换的影响](products/rds/documents/apsaradb-rds-for-mysql/untitled-document-1701914031929.md)。

- 

Q：扩容磁盘，免费备份额度是否扩大？

A：是。详见[免费备份额度](products/rds/documents/apsaradb-rds-for-mysql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md)。

- 

Q：缩容磁盘时出现错误提示“操作失败，日志备份未开启，无法按时间点恢复。”如何解决？

A：当实例Binlog产生较快时，需要本地保留足够多的日志，才允许实例进行缩容。您可以先短暂[开启日志备份](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)，若缩容完无需保留日志再[关闭日志备份](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)即可。更多限制，请参见[限制](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。

### 存储类型变更

- 

Q：如何变更存储类型（高性能本地盘、SSD云盘和ESSD云盘）？

A：请参见[云盘如何变更为高性能本地盘](products/rds/documents/support/how-do-i-change-the-storage-type-from-standard-ssd-to-premium-local-ssd.md)。

- 

Q：高性能本地盘实例如何实现自动扩容？

A：可以[变更高性能本地盘至云盘](products/rds/documents/apsaradb-rds-for-mysql/change-the-storage-type-from-local-ssd-to-essd.md)后设置自动扩容，或者新购云盘实例并[迁移数据](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-between-apsaradb-rds-for-mysql-instances.md)。

- 

Q：RDS MySQL高性能本地盘实例的存储空间已达上限，还需要增加存储空间大小，应该怎么操作？

A：RDS MySQL 8.4、8.0、5.7高可用系列高性能本地盘实例的存储空间范围，请参见[RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)[高可用系列（高性能本地盘）](products/rds/documents/apsaradb-rds-for-mysql/primary-apsaradb-rds-for-mysql-instance-types.md)。如需增加存储空间可[变更高性能本地盘至云盘](products/rds/documents/apsaradb-rds-for-mysql/change-the-storage-type-from-local-ssd-to-essd.md)，获得更大的存储上限。

### 存储空间管理

- 

Q：升级存储空间提示库存不足怎么办？

A：建议[迁移可用区](products/rds/documents/apsaradb-rds-for-mysql/migrate-an-apsaradb-rds-for-mysql-instance-across-zones-in-the-same-region.md)后扩容。迁移后连接地址不变但IP会改变，需设置应用自动重连。

- 

Q：仅扩容存储空间需迁移数据到新实例吗？

A：云盘实例（非基础系列）扩容存储空间，绝大多数情况无闪断。高性能本地盘实例扩容存储空间，有如下两种情形：

- 

主机存储足够：直接扩容，无影响。

- 

主机存储不足：自动新建主备实例并同步数据，切换时闪断约15秒。

说明

目前无法查询实例所在主机剩余存储空间。

- 

Q：RDS MySQL实例直接删除数据库，磁盘空间是否可以得到释放？

A：执行DROP语句会释放空间；DELETE语句会产生碎片，不释放磁盘空间。

### 配置升级影响

- 

Q：CPU、内存、磁盘同时升配，会导致多长时间的服务不可用？

A：无论单项目或多项目升配，不可用时间均为分钟级。升配过程中，可能会出现实例切换或实例重启，而且与数据库、账号、网络等相关的大部分操作都无法执行，请在可维护时间段内执行变配操作。各变更项的业务影响，请参见[变更项业务影响](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。

- 

Q：变配时长受哪些因素影响？

A：请参见[RDS MySQL](products/rds/documents/support/which-factors-affect-the-time-that-is-required-to-change-the-specifications-of-my-apsaradb-rds-for-mysql-instance.md)[实例变配时长受哪些因素影响](products/rds/documents/support/which-factors-affect-the-time-that-is-required-to-change-the-specifications-of-my-apsaradb-rds-for-mysql-instance.md)。

- 

Q：变更配置会影响线上业务吗？

A：请参见本文[影响](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。

### 只读实例相关

- 

Q：主实例升级，只读实例会同步升级吗？

A：不会，需手动升级只读实例配置。

- 

Q：主实例扩容会影响到只读实例的主从复制吗？

A：不影响。

### 连接与网络

- 

Q：变更配置后连接地址会变吗？

A：连接地址（如rm-bpxxxxx.mysql.rds.aliyuncs.com）不变，但IP可能变更。建议在应用程序中使用连接地址，而不是IP地址。

- 

Q：如何设置应用程序重连机制？

A：Java应用建议TTL不超过60秒，以确保在连接地址的VIP地址发生变更时，应用程序可以通过重新查询DNS来接收和使用资源的新VIP地址。Java中设置TTL的方法请参见[JDK](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/net/InetAddress.html)[官方文档](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/net/InetAddress.html)。

### 实例类型与计费

- 

Q：常规实例是否支持变更为Serverless实例？

A：按量付费实例支持变更为Serverless实例，详情请参见[按量付费转](products/rds/documents/apsaradb-rds-for-mysql/pay-as-you-go-to-serverless.md)[Serverless](products/rds/documents/apsaradb-rds-for-mysql/pay-as-you-go-to-serverless.md)。

- 

Q：存储自动扩容如何计费？

A：存储空间自动扩容功能默认关闭，不收费。开启后计费同手动扩容，详见[变更配置](products/rds/documents/product-overview/specification-changes.md)。

- 

Q：误操作降配后再立即升配为原配置，为什么退费与收费差额很大？

A：可能是实例购买时参加了优惠活动，再进行升级没有优惠活动，价格会升高。

### 自动扩容与缩容

- 

Q：存储空间自动扩容规则是什么？

A：详见[设置存储空间自动扩容](products/rds/documents/apsaradb-rds-for-mysql/configure-automatic-storage-expansion-for-an-apsaradb-rds-for-mysql-instance.md)。

- 

Q：云盘实例缩容存储空间有何影响？

A：云盘缩容会有闪断影响，详情请参见[云盘存储空间缩容](products/rds/documents/support/reduce-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-that-uses-essds.md)。

- 

Q：高性能本地盘实例能否缩容？

A：可以。实例处于运行中时，单击变更配置后选择立即降配。

### 可用区迁移

Q：单可用区部署变更为多可用区部署，应该如何操作？

A：详见[迁移可用区](products/rds/documents/apsaradb-rds-for-mysql/migrate-an-apsaradb-rds-for-mysql-instance-across-zones-in-the-same-region.md)。

## 相关API

| API | 描述 |
| --- | --- |
| [ModifyDBInstanceSpec](products/rds/documents/api-change-instance-configuration.md) | 变更 RDS 实例配置。 |


[上一篇：实例变更项](products/rds/documents/apsaradb-rds-for-mysql/configuration-items-for-an-apsaradb-rds-for-mysql-instance.md)[下一篇：极速变配](products/rds/documents/apsaradb-rds-for-mysql/rapid-instance-type-change.md)

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
