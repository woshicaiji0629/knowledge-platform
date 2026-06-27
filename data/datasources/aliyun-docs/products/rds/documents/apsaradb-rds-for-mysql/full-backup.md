# 数据库备份的自动配置与手动执行-云数据库 RDS-阿里云-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/full-backup

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

# 全量备份

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文主要介绍如何通过自动与手动两种方式为数据库执行全量备份，内容涵盖自动备份策略的配置方法和手动备份的即时操作步骤，以满足数据保护与灾难恢复的需求。

## 使用场景

- 

自动备份：用于日常数据保护与灾难恢复。系统依据预设策略，自动执行全量备份并结合日志备份，为实现按时间点恢复（Point-in-Time Recovery, PITR）提供数据基础，从而在发生意外时最大限度地减少数据损失。

- 

手动备份：在执行数据库结构变更（DDL）、应用升级或数据迁移等高风险操作前，手动创建一份即时的数据快照。该备份可作为一个明确、可靠的恢复点，一旦变更引发问题，能够快速将数据回滚至操作前的状态，保障业务的稳定性和连续性。

## 前提条件

初次使用RDS备份服务，请使用阿里云主账号完成[数据灾备服务关联角色授权（AliyunServiceRoleForDBS）](products/rds/documents/support/how-do-i-create-a-service-linked-role-for-dbs.md)。

## 费用说明

如果备份使用量在免费额度内，备份不收费。若超出备份免费额度，将按使用量计费。免费额度以及计费标准详情请参见[备份费用](products/rds/documents/apsaradb-rds-for-mysql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md)。

## 注意事项

- 

默认开启：数据备份（全量备份）默认开启且无法关闭，最少保留7天，频率最低每周两次。

- 

内核版本限制：以下内核小版本的实例锁定后无法发起备份。

- 

RDS MySQL 5.1、5.5：所有小版本。

- 

RDS MySQL 5.6、5.7、8.0：20190815之前的小版本。

说明

- 

如需升级实例的大版本或内核小版本，请参见[升级数据库版本](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)或[升级内核小版本](products/rds/documents/apsaradb-rds-for-mysql/update-the-minor-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)。

- 

更多详情，请参见[实例状态显示“锁定中”时如何解决](products/rds/documents/support/what-do-i-do-if-my-apsaradb-rds-instance-is-in-the-locking-state.md)。

- 

只读实例：仅支持设置[本地日志保留策略](products/rds/documents/apsaradb-rds-for-mysql/view-and-delete-the-binary-log-files-of-an-apsaradb-rds-for-mysql-instance.md)，不支持设置自动备份策略。

- 

DDL 操作：备份期间不要执行DDL操作，避免锁表导致备份失败。

- 

避免业务高峰期：尽量选择业务低峰期进行备份。

- 

备份恢复异常：备份的表数量超过5万张将无法进行库表恢复，数据库恢复（原克隆实例）功能不受影响。

- 

无法备份：备份的表数量超过60万将无法进行备份。

- 

备份策略修改：会立即触发一次全量备份。

## 执行备份

## 自动备份操作步骤

### Step 1: 进入配置页面

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏选择备份恢复。

- 

点击备份策略标签页。正常情况下，控制台会展示常规备份策略页面（未升级），如您已升级为高级备份，则控制台会展示高级备份策略页面（升级后）。

如何按照页面内容区分常规备份策略和高级备份策略？

- 

常规备份策略页面（未升级）

- 

页面包含基础备份区域。

- 

点击编辑按钮，参数以表单形式直接展示。

该区域包含以下参数：全量备份保留天数、全量备份开始时间、全量备份周期、预计下次备份时间、日志备份、日志备份保留天数、高频增量备份、任意时间点恢复、库表恢复及实例释放后保留备份文件。

- 

高级备份策略页面（升级后）

- 

页面顶部有MySQL和一级备份标签。

- 

中间有带数字的圆形图标，点击弹出参数设置页面。

- 

支持[稀疏备份](products/rds/documents/apsaradb-rds-for-mysql/sparse-backup-2.md)等高级功能。

在备份策略页签中，页面分为左侧数据源区域和右侧极速存储池区域，数据流向为从 MySQL 数据源经中间带数字的备份节点连接至极速存储池中的一级备份。

说明

如何升级到高级版？

如果你是常规版界面，但希望使用高级功能（如稀疏备份），请在页面上查找“升级至高级版本”的链接（部分地域的实例现已支持将备份策略页面[升级至高级版本](products/rds/documents/apsaradb-rds-for-mysql/sparse-backup-2.md)）。升级后，备份策略设置入口及部分参数设置方法会略有不同，请根据实际情况选择设置方法。

### Step 2: 配置核心参数

无论备份策略是否升级，核心参数的含义是相同的。

数据备份设置

数据备份（全量备份）默认开启且无法关闭，最少保留7天，频率最低每周两次。

- 

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 备份周期 | 最低为每周 2 次。云盘实例开启高频快照后，最高可设置为每 15 分钟 1 次。 |
| 备份保留天数 | 默认为 7 天。可选范围： 云盘实例：7~730 天。 说明 5.7 基础系列固定为 7 天，无法修改。 高性能本地盘实例：7 天或以上。 保留不超过 730 天的数据备份为常规备份。 保留超过 730 天的数据备份为归档备份， [备份费用](products/rds/documents/apsaradb-rds-for-mysql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md) 较低。 说明 如果设置超过 730 天，或者勾选 实例释放前长期保留 ，则还需设置归档备份的保留个数，例如保留每个月最早的 2 个归档备份。 |
| 备份开始时间 | 选择业务低峰期，以减少对业务的潜在影响。 |
| 实例释放后保留备份文件 | 选择实例释放后是否保留备份文件。 说明 建议您选择 保留最后一个 或 全部保留 。当实例释放后，您可以在 [已删除实例备份](https://rdsnext.console.aliyun.com/backupManage/cn-hangzhou/delInsBack) 页面下载备份进行恢复。具体详情，请参见 [长期保留备份](products/rds/documents/apsaradb-rds-for-mysql/retain-the-backup-files-of-an-apsaradb-rds-for-mysql-instance-for-a-long-period-of-time.md) 。 |


日志备份设置

日志备份（增量备份）用于实现任意时间点恢复（PITR）。

- 

- 

| 参数 | 说明 |
| --- | --- |
| 日志备份 | 开启后可以实现按时间点恢复。默认为开启。 |
| 任意时间点恢复 | 开启后可以实现按任意时间点（PITR）恢复数据。 |
| 日志备份保留天数 | 设置日志备份保留天数。 可选范围：7~730 天。默认为 7 天。 必须小于等于全量备份保留天数。 说明 5.7 基础系列固定为 7 天。 |


重要

为实现任意时间点的恢复能力，实例会在您设置的日志备份保留天数外额外保留一部分备份集。

示例：以日志备份保留天数设置为7天为例，实际会保留7~9天的备份数据。具体来说，系统会额外保留一个7天外最晚的全量备份，以及7天外最晚的全量备份到第7天间的所有连续日志备份，但只对一个全量备份和最多额外一周日志备份计费。

高级功能（可选）

- 

- 

| 参数 | 适用实例 | 说明 |
| --- | --- | --- |
| 秒级备份 | 云盘实例（高可用/集群版） | 开启后，快照备份的执行速度会提升至秒级。 |
| 增加快照频率 | 云盘实例（高可用/集群版） | 开启 [高频快照备份](products/rds/documents/apsaradb-rds-for-mysql/use-the-high-frequency-snapshot-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md) 功能可缩短秒级快照周期，增加秒级快照密度。开启后，可设置每 N 小时备份 1 次，甚至每 15 分钟备份一次。 说明 本功能与 秒级备份 必须同步开启，若在秒级备份关闭的情况下开启本功能，则系统会自动开启秒级备份。 |
| 库表恢复 | 所有实例 | 开启后，生成的备份文件支持恢复单个库或表，而无需恢复整个实例。 |
| 极速库表恢复 | 高性能本地盘实例（部分地域） | [开启极速库表恢复](products/rds/documents/apsaradb-rds-for-mysql/restore-individual-databases-and-tables-of-an-apsaradb-rds-for-mysql-instance.md) 表示选择库表恢复速度为极速，否则默认为常规。 常规 ：正常情况下的库表恢复速度。 极速 ：在常规库表恢复速度的基础上，提升约 50%~95%的恢复速度。 说明 开启极速库表恢复后，还需选择 CDM 付费类型 和 CDM 保留时长 。 |
| 备份加密状态 | 高性能本地盘实例（高级备份策略） | 对备份文件进行加密，提升数据安全性。 |


### Step 3: 保存并验证

- 

点确定或保存。

- 

系统会立即根据新策略触发一次全量备份。

- 

稍后可以在备份恢复→数据备份列表中查看新生成的备份集。首次备份成功后，系统将按新策略自动执行后续备份。

## 手动备份操作步骤

## 执行备份

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在页面右上角，单击备份实例。

- 

在备份实例对话框中，备份所有库或者特定库表，单击确定。

说明

备份方式的区别，请参见[逻辑备份、物理备份与快照](https://help.aliyun.com/zh/dbs/product-overview/backup-modes#multiTask1034)。

- 

- 

| [实例存储类型](products/rds/documents/product-overview/storage-types.md) | 备份所有库 | 备份特定库表 |
| --- | --- | --- |
| 高性能本地盘实例 | 两种方式： 物理备份 （备份与恢复速度比逻辑备份快） 逻辑备份 > 实例备份 | 逻辑备份 > 单库备份 |
| 云盘实例 | 快照备份 | 不支持 |


## 查看备份进度

执行备份后系统将生成一个备份任务，您可在[任务中心](https://rdsnext.console.aliyun.com/jobCenter/cn-hangzhou)页面筛选任务类型为手动备份实例、状态为等待执行和执行中的任务，查看备份进度。在备份任务列表中，确认任务类型为手动备份实例，任务状态为执行成功，任务进度为100%，表示手动备份已完成。

说明

- 

手动备份集的保留时长与备份策略无关，由用户自定义，支持7～730天和永久保留，不指定保留时长时默认永久保留。

- 

备份完成后才会显示备份集，您可以在备份恢复>基础备份列表页面下载备份文件。具体操作，请参见[下载备份](products/rds/documents/apsaradb-rds-for-mysql/download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance-download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance.md)。

## 相关操作

- 

备份完成后您可以在备份恢复>基础备份列表页面下载备份文件。具体操作，请参见[下载备份](products/rds/documents/apsaradb-rds-for-mysql/download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance-download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance.md)。

- 

除了本文介绍的RDS自动备份功能外，您也可以使用[数据灾备](https://help.aliyun.com/zh/dbs/product-overview/what-is-dbs)的逻辑备功能（支持跨账号备份、单库或单表备份、异地备份、将备份存储于OSS等）实现[RDS MySQL](https://help.aliyun.com/zh/dbs/user-guide/back-up-apsaradb-rds-for-mysql-or-self-managed-mysql-instances-by-using-logical-backup#task-1964148)[或自建](https://help.aliyun.com/zh/dbs/user-guide/back-up-apsaradb-rds-for-mysql-or-self-managed-mysql-instances-by-using-logical-backup#task-1964148)[MySQL](https://help.aliyun.com/zh/dbs/user-guide/back-up-apsaradb-rds-for-mysql-or-self-managed-mysql-instances-by-using-logical-backup#task-1964148)[自动备份](https://help.aliyun.com/zh/dbs/user-guide/back-up-apsaradb-rds-for-mysql-or-self-managed-mysql-instances-by-using-logical-backup#task-1964148)。关于两者的具体差异，请参见[RDS](products/rds/documents/apsaradb-rds-for-mysql/differences-between-default-rds-backups-and-data-disaster-recovery.md)[默认备份与数据灾备的区别](products/rds/documents/apsaradb-rds-for-mysql/differences-between-default-rds-backups-and-data-disaster-recovery.md)。

- 

除了本文介绍的RDS自动备份功能外，RDS还支持您[手动备份](products/rds/documents/apsaradb-rds-for-mysql/manually-back-up-an-apsaradb-rds-for-mysql-instance.md)所有库或者特定库表。

- 

您可以[下载备份](products/rds/documents/apsaradb-rds-for-mysql/download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance-download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance.md)到本地或上传到OSS。

- 

您可通过[数据恢复方案](https://help.aliyun.com/zh/document_detail/157519.html)将数据备份和日志备份恢复到已有实例、新实例或本地数据库中。

- 

默认备份文件存储于实例所在地域。如需备份至其它地域，请参见[跨地域备份](products/rds/documents/apsaradb-rds-for-mysql/use-the-cross-region-backup-feature-of-an-apsaradb-rds-for-mysql-instance.md)。

- 

您可以通过API管理RDS实例备份策略或配置数据灾备备份计划，具体如下：

| 分类 | API | 描述 |
| --- | --- | --- |
| RDS 默认备份 | [ModifyBackupPolicy](products/rds/documents/api-modify-backup-settings.md) | 修改 RDS 实例备份设置。 |
| [DescribeBackupPolicy](products/rds/documents/api-query-backup-settings.md) | 查询实例备份设置。 |  |
| [DescribeBackups](products/rds/documents/api-query-data-backup-files.md) | 查看备份集列表。 |  |
| [DescribeBackupTasks](products/rds/documents/api-query-backup-tasks.md) | 查询实例的备份任务列表。 |  |
| 数据灾备备份 | [CreateBackupPlan](https://help.aliyun.com/zh/dms/developer-reference/api-dbs-2019-03-06-createbackupplan#main-107864) | 创建一个备份计划。 |
| [ConfigureBackupPlan](https://help.aliyun.com/zh/dms/developer-reference/api-dbs-2019-03-06-configurebackupplan#main-107864) | 配置备份计划。 |  |


## 备份常见问题

- 

Q：备份会影响实例性能吗？

| 实例系列 | 备份的影响 |
| --- | --- |
| [高可用系列](products/rds/documents/apsaradb-rds-for-mysql/rds-high-availability-edition.md) 或 [集群系列](products/rds/documents/apsaradb-rds-for-mysql/rds-cluster-edition.md) | 备份在备实例执行，不占用主实例 CPU，不影响主实例性能。 说明 少数情况下，备实例不可用时，备份会在主实例执行。 |
| [基础系列](products/rds/documents/apsaradb-rds-for-mysql/rds-basic-edition.md) | 由于是单节点架构，备份时会影响实例性能。 |


- 

Q：数据备份或日志备份是否可以关闭？

A：数据备份不可以关闭，但可以减少备份频率（一周至少2次），保留天数最少7天；日志备份可以关闭，在备份策略页面可以关闭日志备份开关。具体请参考[删除或减少备份](products/rds/documents/apsaradb-rds-for-mysql/delete-the-backup-files-or-reduce-the-size-of-backup-files-of-an-apsaradb-rds-for-mysql-instance.md)教程减少RDS MySQL备份。

- 

Q：按量付费实例进入欠费状态后，是否仍会进行自动备份？

A：在延期免停额度内（即欠费7天内），自动备份功能将继续执行。超过7天的延期额度后，阿里云将暂停该实例的服务（即停服），并停止计费。同时，自动备份功能将立即终止。更多信息请参见[欠费说明](products/rds/documents/apsaradb-rds-for-mysql/overdue-payments.md)。

- 

Q：为什么有时候备份任务会失败？

A：备份过程中执行耗时长的DDL或更新语句，会导致锁表，进而导致备份失败。

- 

Q：为什么数据只有几GB，快照备份有几十GB？

A：单次备份文件的大小可能比数据量大，也可能比数据量小。云盘实例采用快照备份，单次快照备份文件的大小可能远大于数据的大小。云盘实例备份免费额度为实例存储容量的200%，高性能本地盘实例备份免费额度为实例存储容量的50%。

说明

计算单次快照备份文件的大小时，会计算所有非空块的大小。如果写入时比较分散（例如3MB的数据可能占用2个、3个甚至4个块），会导致较多非空块，因此快照备份较大。

因此控制台备份恢复页面显示的所有备份集的备份文件大小总和，可能会与显示的备份使用量不一致。

- 

Q：数据库的备份文件占用实例磁盘空间吗？

A：数据备份和日志备份存放于阿里云提供的备份空间，不占用实例的存储空间。

说明

- 

备份空间不对外开放访问。如需下载备份，请参见[下载备份](products/rds/documents/apsaradb-rds-for-mysql/download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance-download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance.md)。

- 

备份空间提供免费额度，超出额度时需付费，具体请参见[备份费用](products/rds/documents/apsaradb-rds-for-mysql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md)。

## 其他引擎

- 

[备份](products/rds/documents/apsaradb-rds-for-sql-server/back-up-an-apsaradb-rds-for-sql-server-instance.md)[SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/back-up-an-apsaradb-rds-for-sql-server-instance.md)[数据](products/rds/documents/apsaradb-rds-for-sql-server/back-up-an-apsaradb-rds-for-sql-server-instance.md)

- 

[备份](products/rds/documents/apsaradb-rds-for-postgresql/back-up-an-apsaradb-rds-for-postgresql-instance.md)[PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/back-up-an-apsaradb-rds-for-postgresql-instance.md)[数据](products/rds/documents/apsaradb-rds-for-postgresql/back-up-an-apsaradb-rds-for-postgresql-instance.md)

- 

[备份](products/rds/documents/apsaradb-rds-for-mariadb/back-up-an-apsaradb-rds-for-mariadb-instance.md)[MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/back-up-an-apsaradb-rds-for-mariadb-instance.md)[数据](products/rds/documents/apsaradb-rds-for-mariadb/back-up-an-apsaradb-rds-for-mariadb-instance.md)

[上一篇：备份指引](products/rds/documents/apsaradb-rds-for-mysql/backup-guide.md)[下一篇：库表级备份](products/rds/documents/apsaradb-rds-for-mysql/back-up-the-individual-databases-and-tables-of-an-apsaradb-rds-for-mysql-instance.md)

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
