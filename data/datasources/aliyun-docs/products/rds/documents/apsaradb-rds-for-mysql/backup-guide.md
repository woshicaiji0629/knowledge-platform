# 备份指引-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/backup-guide

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

# 备份指引

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

介绍阿里云RDS MySQL备份的功能特性、使用量计算、计费方式、性能影响及数据保护策略，帮助用户全面了解并有效使用RDS备份服务。

## 备份功能介绍

| 类别 | 功能名称 | 描述 | 主要用途/场景 |
| --- | --- | --- | --- |
| 基础备份能力 | 自动备份 | 系统提供的核心自动化保护机制，可配置备份周期、时间窗口及保留时长。 | 常规运维，系统将依据策略自动执行全量备份，并结合日志备份，为按时间点恢复（PITR）提供数据基础。 |
| 手动备份 | 提供按需创建即时备份的能力。 | 在执行应用升级、数据迁移等重大变更前，创建可明确追溯的恢复点。 |  |
| 高级备份能力 | 库表级备份 | 无需恢复整个实例，可以恢复指定的单个或多个库、表。 | 应对误删表、误更新数据等细粒度恢复场景，最大限度减少业务影响。 |
| 高频备份（物理/快照） | 可迅速恢复至特定时间段，大幅缩短数据可能丢失的时间窗口。 | 满足 RPO（恢复点目标）要求极为苛刻的业务场景。 |  |
| 灾备与成本优化 | 跨地域备份 | 将备份数据自动备份到另一个地理区域。 | 实现地域级灾难恢复，保障业务的最高可用性。 |
| 稀疏备份 | 灵活设置备份策略，保留最少的备份集。 | 在保证数据可用的前提下，降低备份存储成本。 |  |
| 设置实例释放后备份保留策略 | 实例被释放（删除）后，其备份数据仍可再保留一段时间。 | 防止因误操作导致数据永久丢失，提供最后的恢复机会。 |  |


综上，通过对上述功能的组合运用，用户可以构建出一个多维度、可灵活配置的数据保护体系，以满足在日常运维、高级容灾、性能与成本管理等方面的综合性需求。

说明

您也可以使用数据灾备的逻辑备份功能（支持跨账号备份、单库或单表备份、异地备份、将备份存储于OSS等）实现[RDS MySQL](https://help.aliyun.com/zh/dbs/user-guide/back-up-apsaradb-rds-for-mysql-or-self-managed-mysql-instances-by-using-logical-backup#task-1964148)[或自建](https://help.aliyun.com/zh/dbs/user-guide/back-up-apsaradb-rds-for-mysql-or-self-managed-mysql-instances-by-using-logical-backup#task-1964148)[MySQL](https://help.aliyun.com/zh/dbs/user-guide/back-up-apsaradb-rds-for-mysql-or-self-managed-mysql-instances-by-using-logical-backup#task-1964148)[自动备份](https://help.aliyun.com/zh/dbs/user-guide/back-up-apsaradb-rds-for-mysql-or-self-managed-mysql-instances-by-using-logical-backup#task-1964148)。

## 备份方式

常用的数据备份方式为逻辑备份、物理备份与快照备份，三者的主要区别如下：

| 维度 | 逻辑备份 | 物理备份 | 快照备份 |
| --- | --- | --- | --- |
| 备份粒度 | 数据库对象级（表、索引、存储过程等） | 数据库文件级（如 InnoDB 数据文件） | 云盘块级（整个实例存储卷） |
| 典型工具 | mysqldump | XtraBackup | 基于 ESSD 云盘快照服务 |
| 恢复精度 | 可恢复到单表/库，但不支持时间点恢复（除非结合 binlog） | 支持全量 + 日志备份 → 任意时间点恢复（秒级） | 支持时间点恢复（依赖日志备份） |
| 适用场景 | 跨版本迁移、单表恢复、导出到自建库 | 全量快速恢复、灾备、跨地域备份 | 极速恢复（RTO 最短）、业务连续性要求高的场景 |
| 相关操作 | [RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/restore-the-data-of-an-apsaradb-rds-for-mysql-instance-from-a-logical-backup-file-to-a-self-managed-mysql-instance.md) [逻辑备份文件恢复到自建数据库](products/rds/documents/apsaradb-rds-for-mysql/restore-the-data-of-an-apsaradb-rds-for-mysql-instance-from-a-logical-backup-file-to-a-self-managed-mysql-instance.md) | [RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/restore-the-data-of-an-apsaradb-rds-for-mysql-instance-from-a-physical-backup-file-to-a-self-managed-mysql-database.md) [物理备份文件恢复到自建数据库](products/rds/documents/apsaradb-rds-for-mysql/restore-the-data-of-an-apsaradb-rds-for-mysql-instance-from-a-physical-backup-file-to-a-self-managed-mysql-database.md) | [RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/restore-the-data-of-an-apsaradb-rds-for-mysql-instance-to-a-self-managed-mysql-instance-by-using-a-csv-file-or-an-sql-file.md) [快照备份文件恢复到自建数据库](products/rds/documents/apsaradb-rds-for-mysql/restore-the-data-of-an-apsaradb-rds-for-mysql-instance-to-a-self-managed-mysql-instance-by-using-a-csv-file-or-an-sql-file.md) |


## 备份使用量

### 备份组成

RDS的备份由数据备份和日志备份组成。

- 

数据备份：系统对数据进行备份，并生成备份集。默认开启，无法关闭。数据备份最少保留7天，备份频率最低每周2次。若您对数据备份需求较少，可通过修改备份频率和备份集保留时长来减少数据备份。

- 

日志备份：也称为增量备份，默认开启，可以关闭。日志备份最少保留7天，基于“数据备份+日志备份”，您可以恢复备份保留期限内第一个全量备份开始的任意时间点（PITR）的数据。若您对日志备份需求较少，可通过减少备份集保留时长或关闭日志备份来减少日志备份。

### 查看备份使用量

备份使用量 = 数据备份大小 + 日志备份大小

说明

- 

在实例基本信息页实例资源区域的备份使用量参数处查看。

- 

RDS MySQL或RDS MySQL Serverless基础系列实例升级小版本后，实例的基本信息页的备份使用量可能会显示为0，且在下一次定时备份完成后自动恢复。

例如，备份使用量为33.2 GB（数据备份）+ 20.19 MB（日志备份）。其中归档备份是指已保留超过2年（730天）的数据备份，数据是指非归档的数据备份。

### 备份使用量

与存储空间使用量的关系

| 日志 | 说明 | 作用 |
| --- | --- | --- |
| 数据备份 | 对数据进行备份，并生成备份集。存放于阿里云提供的备份空间， 不占用实例的存储空间 | 主要用于数据恢复，是按时间点恢复（PITR）的基础。 |
| 日志备份 | 开启日志备份后，本地日志会实时上传至阿里云提供的备份空间， 不占用实例的存储空间 | 实现按时间点恢复数据。 |
| 本地日志 | 实例的原始日志，存放于实例的存储空间。 | 例如，可用于自行搭建主从架构。 |


说明

- 

[清理本地日志](https://help.aliyun.com/zh/document_detail/96146.html#task-hsm-ycn-42b)会减少其占用的存储空间，但不会影响日志备份的大小。

- 

在实例的监控与报警页面可以查看本地日志占用的存储空间。更多详情，请参见[查看监控信息](products/rds/documents/apsaradb-rds-for-mysql/view-the-metrics-of-an-apsaradb-rds-for-mysql-instance.md)。其中MySQL存储空间使用量图表展示了各类日志的存储占用详情。

与数据大小的关系

单次备份文件的大小可能比数据量大，也可能比数据量小。

云盘实例采用快照备份。单次快照备份文件的大小可能大于数据的大小。云盘实例备份免费额度为实例存储容量的200%，高性能本地盘实例备份免费额度为实例存储容量的50%。

说明

计算单次快照备份文件大小时，会计算所有非空块的大小。如果写入时比较分散（例如3MB的数据可能占用2个、3个甚至4个块），会导致较多非空块，因此快照备份文件较大。

与实例架构的关系

备份大小与实例架构无关。例如，高可用实例和基础系列实例，如果数据一致，则备份大小一样，不会因为高可用就导致备份大小增加。

## 备份费用

### 备份计费项

- 

- 

- 

- 

| 计费项 | 计费项 Code | 计费归属产品 | 相关文档 |
| --- | --- | --- | --- |
| RDS 基础备份 | BackupCharged | 关系型数据库 RDS | [全量备份](products/rds/documents/apsaradb-rds-for-mysql/full-backup.md) [库表级备份](products/rds/documents/apsaradb-rds-for-mysql/back-up-the-individual-databases-and-tables-of-an-apsaradb-rds-for-mysql-instance.md) [高频物理备份](products/rds/documents/apsaradb-rds-for-mysql/use-the-high-frequency-physical-backup-feature-of-an-apsaradb-rds-for-mysql-instance.md) [高频快照备份](products/rds/documents/apsaradb-rds-for-mysql/use-the-high-frequency-snapshot-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md) |
| 高性能本地盘实例跨地域备份存储 | DdrOssStorageSize | [跨地域备份](products/rds/documents/apsaradb-rds-for-mysql/use-the-cross-region-backup-feature-of-an-apsaradb-rds-for-mysql-instance.md) |  |
| 云盘实例跨地域备份存储 | BackupStorageSize | 数据库备份 DBS |  |
| 跨地域备份网络流量 | NetworkOutDuplicationSize |  |  |
| 备份下载外网流量 | NetworkOutSize | [下载备份](products/rds/documents/apsaradb-rds-for-mysql/download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance-download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance.md) |  |
| 云盘实例备份转换 | BackupAnalyticSize |  |  |
| 高性能本地盘实例已删除实例备份集保留 | StandardStorageSize | [设置实例释放后备份保留策略](products/rds/documents/apsaradb-rds-for-mysql/retain-the-backup-files-of-an-apsaradb-rds-for-mysql-instance-for-a-long-period-of-time.md) |  |
| 云盘实例已删除实例备份集保留 | BackupStorageSize |  |  |
| 高性能本地盘实例库表恢复存储 | CapacitySandboxStorageSize | [恢复库表](products/rds/documents/apsaradb-rds-for-mysql/restore-individual-databases-and-tables-of-an-apsaradb-rds-for-mysql-instance.md) |  |


### 免费备份额度

免费备份额度与是否开启[存储压缩](products/rds/documents/apsaradb-rds-for-mysql/storage-compression.md)功能有关。

| 存储类型 | 存储压缩状态 | 免费额度说明 | 说明 |
| --- | --- | --- | --- |
| 高性能云盘 | 未开启压缩 | 存储空间的 200% | 在实例 基本信息 页 使用量统计 区域的 备份使用量 （即实际逻辑数据量）参数处查看。 |
| 开启压缩 | 存储空间的 400% |  |  |
| 高性能本地盘 | 未开启压缩 | 存储空间的 50% |  |
| 开启压缩 | 存储空间的 100% |  |  |


重要

免费备份额度仅抵扣常规备份（备份存储周期在730天内）部分，不抵扣超过730天的归档备份。

### 费用说明

如果[备份使用量](products/rds/documents/apsaradb-rds-for-mysql/view-and-manage-the-size-of-backup-files-of-an-apsaradb-rds-for-mysql-instance.md)未超过免费额度，备份不收费。超出部分将额外按使用量计费，每小时备份费用 = ( 备份使用量 - 免费备份额度 ) × 备份单价。

通用型节省计划或资源包抵扣详情

- 

[存储包](products/rds/documents/product-overview/storage-plans.md)可以抵扣包年包月或按量付费的RDS实例超出免费额度的备份空间（不包括高性能云盘和SSD云盘）。

- 

[通用型节省计划](products/rds/documents/product-overview/savings-plan-introduction.md)可以抵扣包年包月、按量付费以及ServerlessRDS实例的备份空间费用。

备份单价

常规备份与归档备份空间的单价，请前往[RDS](https://www.aliyun.com/price/product?spm=5176.28228749.J_cBmqkGxzGK2_MpfhV9BAu.5.19c755262b67m4#/commodity/bards)[定价详情](https://www.aliyun.com/price/product?spm=5176.28228749.J_cBmqkGxzGK2_MpfhV9BAu.5.19c755262b67m4#/commodity/bards)页查看。在该页面依次单击走价详情>备份与恢复。

备份计费示例

假设用户在华东1（杭州）地域有一个RDS MySQL 8.0版本的云盘实例，其存储空间为20 GB，当前实例的数据备份量为40 GB，日志备份量为20 GB。备份单价：0.00025 元/GB/小时。备份计费方式如下：

- 

免费备份额度为：20 GB x 200% = 40 GB

- 

当前备份使用量为：40 GB + 20 GB = 60 GB，已超出免费备份额度，超出部分将额外按使用量计费，每小时备份费用（最近730天内的备份）为：( 60 GB - 40 GB ) x 0.00025 = 0.005元/GB

### 注意事项

- 

备份费用和备份使用量有关，和存储空间使用量无关，因为备份不占用RDS实例的存储空间。

- 

分析备份费用时，请检查备份使用量的情况，而不是存储空间使用量。

- 

涉及云盘更换的管控操作（例如备库重搭），会对云盘实例产生如下影响：

- 

云盘实例的同地域备份存储量将增长，从而同地域备份存储费用会增加（计费项Code：BackupCharged）。

- 

云盘实例的跨地域备份网络流量将增长，从而跨地域备份网络流量费用会增加（计费项Code：NetworkOutDuplicationSize）。

- 

云盘实例的跨地域备份存储量将增长，从而跨地域备份存储费用会增加（计费项Code：BackupStorageSize）。

说明

例如，DDL操作导致备库延迟过长时，系统可能会自动触发备库重搭，增加费用。

### 如何减少备份费用

- 

减少备份使用量

即删除或减少备份，具体请参见[删除或减少备份](products/rds/documents/apsaradb-rds-for-mysql/delete-the-backup-files-or-reduce-the-size-of-backup-files-of-an-apsaradb-rds-for-mysql-instance.md)。

- 

提高免费额度

即扩容存储空间，具体请参见[变更配置](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。

免费额度与存储空间有关，例如，将存储空间从150 GB扩容至300 GB，免费额度会从75 GB升至150 GB。

- 

购买[RDS](products/rds/documents/product-overview/savings-plan-introduction.md)[节省计划](products/rds/documents/product-overview/savings-plan-introduction.md)、[RDS](products/rds/documents/product-overview/storage-plans.md)[存储包](products/rds/documents/product-overview/storage-plans.md)

若需长期保留备份且无扩容需求，可购买[RDS](products/rds/documents/product-overview/savings-plan-introduction.md)[节省计划](products/rds/documents/product-overview/savings-plan-introduction.md)、[RDS](products/rds/documents/product-overview/storage-plans.md)[存储包](products/rds/documents/product-overview/storage-plans.md)来抵扣备份费用。RDS存储包优先于RDS节省计划。

### 查看备份账单

- 

在[账单明细](https://usercenter2.aliyun.com/finance/expense-report/expense-detail-by-instance)页面，选中计费项和明细，输入实例名、实例ID或账单ID，单击搜索。

- 

查找计费项为实例备份的明细。

## 备份的存放位置

数据备份和日志备份存放于阿里云提供的备份空间，不占用实例的存储空间。

存放备份的地域是RDS实例所在的地域；存放备份的可用区不一定是RDS实例所在的可用区。如需实现跨地域的备份，请使用[跨地域备份](products/rds/documents/apsaradb-rds-for-mysql/use-the-cross-region-backup-feature-of-an-apsaradb-rds-for-mysql-instance.md)。

说明

- 

备份空间不对外开放访问。如需下载备份，请参见[下载备份](products/rds/documents/apsaradb-rds-for-mysql/download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance-download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance.md)。

- 

备份空间提供免费额度，超出额度时需付费，具体请参见[备份费用](products/rds/documents/apsaradb-rds-for-mysql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md)。

## 备份的影响

| 实例系列 | 备份的影响 |
| --- | --- |
| [高可用系列](products/rds/documents/apsaradb-rds-for-mysql/rds-high-availability-edition.md) 、 [集群系列](products/rds/documents/apsaradb-rds-for-mysql/rds-cluster-edition.md) 或 [三节点企业系列](products/rds/documents/rds-enterprise-edition.md) [高可用系列](products/rds/documents/apsaradb-rds-for-mysql/rds-high-availability-edition.md) 或 [集群系列](products/rds/documents/apsaradb-rds-for-mysql/rds-cluster-edition.md) | 备份在备实例执行，不占用主实例 CPU，不影响主实例性能。 说明 少数情况下，备实例不可用时，备份会在主实例执行。 |
| [基础系列](products/rds/documents/apsaradb-rds-for-mysql/rds-basic-edition.md) | 由于是单节点架构，备份时会影响实例性能。 |


## 备份的数据保护

- 

防篡改：

- 

RDS MySQL的全量物理备份和日志备份数据存储在OSS，全量快照备份存储在ESSD云盘快照服务，备份系统内部使用两种存储方式，都具备WORM（write once read many）不可篡改的特性。

- 

防恶意/误删除：

- 

用户手动删除：允许用户删除手动备份数据，但不允许用户删除自动备份的数据（参考文档：[删除或减少备份](products/rds/documents/apsaradb-rds-for-mysql/delete-the-backup-files-or-reduce-the-size-of-backup-files-of-an-apsaradb-rds-for-mysql-instance.md)）

- 

自动过期删除：可删除自动备份的数据。但同时限制了自动备份无法关闭，保留时长最低为7天，每周的备份次数最低为2次。（参考文档：[自动备份](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)）。因此用户自动备份的全量和日志数据，无法完全删除。

## 常见问题

- 

Q：RDS实例自动备份已经超出免费额度，目前备份在计费，怎么关闭备份功能？

A：RDS默认的备份功能默认开启，无法关闭。但您可以通过修改自动备份策略等方式来删除已有备份，或减少全新备份的产生，详情请参见[删除或减少备份](products/rds/documents/apsaradb-rds-for-mysql/delete-the-backup-files-or-reduce-the-size-of-backup-files-of-an-apsaradb-rds-for-mysql-instance.md)。

- 

Q：备份没有超出免费额度，为什么会扣费？

A：此项扣费可能是之前备份超出免费额度所产生的扣费项。

- 

Q：存储包是否可以抵扣备份超出免费额度产生的费用？

A：[存储包](products/rds/documents/product-overview/storage-plans.md)可以抵扣包年包月或按量付费的RDS实例超出免费额度的备份空间（不包括高性能云盘和SSD云盘）。

- 

Q：为什么备份大小比数据量大？

A：云盘实例采用快照备份，快照备份的大小可能远大于数据的大小。计算快照备份大小时，会计算所有非空块的大小。如果写入时比较分散，会导致较多非空块，因此快照备份较大。

- 

Q：备份保留时长从x天缩短为y天，为什么备份大小没有变？

A：如果原本没有超出y天的备份，则没有备份数据被删除，因此备份大小不会有变化。

- 

Q：我的RDS MySQL实例已经释放了，为什么还有备份费用产生？

A：即使RDS MySQL实例已被释放，但如果实例释放前[设置了实例删除后备份保留策略](products/rds/documents/apsaradb-rds-for-mysql/configure-backup-retention-policies-for-released-instances.md)，那么这些备份文件会继续存储在RDS控制台的备份管理页面中。根据功能规则，实例释放后7天内备份存储免费，超过7天将会开始计费。

因此，备份费用产生可能是因为备份保留时间超过了7天的免费期，此时根据实际存储量和所在地域计费。计费标准，请参见[费用说明](products/rds/documents/apsaradb-rds-for-mysql/configure-backup-retention-policies-for-released-instances.md)。若确认不需要备份，在已删除实例备份页签下将目标实例的保留策略改为不保留，可避免产生备份存储费用。

[上一篇：备份实例](products/rds/documents/apsaradb-rds-for-mysql/backup-instance.md)[下一篇：全量备份](products/rds/documents/apsaradb-rds-for-mysql/full-backup.md)

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
