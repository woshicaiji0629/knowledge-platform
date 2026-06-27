# 计费项构成与详细计费说明-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/product-overview/billable-items-billing-methods-and-pricing

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/product-overview.md)

- [快速入门](products/rds/documents/getting-started.md)

- [操作指南](products/rds/documents/user-guide.md)

- [实践教程](products/rds/documents/use-cases.md)

- [安全合规](products/rds/documents/security-compliance.md)

- [开发参考](products/rds/documents/developer-reference.md)

- [服务支持](products/rds/documents/support.md)

[首页](https://help.aliyun.com/zh)

# 计费项

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

使用云数据库 RDS可能涉及的计费项包括RDS实例计费项、增值服务计费项以及与RDS相关的其他云服务计费项。本文介绍这些计费项的定义、计费公式、计费方式等。

您可以前往[RDS](https://rdsbuy.console.aliyun.com/pricing)[定价详情](https://rdsbuy.console.aliyun.com/pricing)查看RDS MySQL各计费项的定价说明和价格，也可以前往[RDS](https://www.aliyun.com/price/product?spm=5176.28228749.J_cBmqkGxzGK2_MpfhV9BAu.5.19c755262b67m4#/commodity/bards)[价格计算器](https://www.aliyun.com/price/product?spm=5176.28228749.J_cBmqkGxzGK2_MpfhV9BAu.5.19c755262b67m4#/commodity/bards)估算RDS的费用。

说明

RDS价格计算器仅支持估算部分计费项的费用。

## RDS实例

RDS根据实例的[计费方式](products/rds/documents/product-overview/billing-overview.md)，RDS实例可以分为两类：

- 

包年包月或按量付费的RDS实例，购买此类RDS实例时需指定计算资源和存储空间的规格，购买后产生RDS规格费用和存储空间费用。

- 

Serverless实例，Serverless实例的计算资源会在您指定的范围内根据业务负载自动弹性伸缩，存储空间也根据数据量自动扩容。Serverless实例会产生RCU费用和存储空间费用。

### RDS规格

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 定义 | 包年包月或按量付费的 RDS 实例（包括常规实例、只读实例、灾备实例 、DuckDB 分析实例 ）的计算资源规格费用。计费项名称为 RDS 规格（rds_class） 或 规格（ClassCode） 。 创建实例后，会产生该计费项。实例的计算资源规格 或节点数 增加或减少，一般会导致该计费项的费用发生变化。 |
| 计费公式 | 基础系列、 高可用系列：RDS 规格费用=RDS 规格的实例单价 * 时长 MySQL、PostgreSQL 集群系列：RDS 规格费用=RDS 规格单节点单价 * 节点数 * 时长 SQL Server 集群系列：RDS 规格费用=RDS 主实例规格费用+RDS 只读实例规格费用 说明 RDS 规格单价与地域、引擎、规格大小相关，请参考售卖页和账单。 |
| 计费方式 | 包年包月或按量付费。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [计算包](products/rds/documents/product-overview/compute-plans.md) 和 [通用型节省计划](products/rds/documents/product-overview/savings-plan-introduction.md) 可以抵扣 按量付费 的 RDS 规格费用。 |


### Serverless实例的RCU

- 

- 

| 类别 | 说明 |
| --- | --- |
| 定义 | RDS Serverless 实例计算资源的费用。计费项名称为 计算单元 RCU（rds_serverless_rcu） 。 创建 Serverless 实例后，会产生该计费项。根据实际使用的 RCU 计费。如果暂停实例，该计费项也会暂停计费。 |
| 计费公式 | RDS MySQL、PostgreSQL：RCU 费用=单节点 RCU 单价 * 单节点 RCU 用量 * 节点数 * 使用时长 RDS SQL Server：RCU 费用=RCU 单价 * RCU 用量 * 使用时长 说明 RCU 单价请参见 [MySQL Serverless](https://help.aliyun.com/zh/document_detail/447753.html) [费用](https://help.aliyun.com/zh/document_detail/447753.html) 、 [PostgreSQL Serverless](products/rds/documents/apsaradb-rds-for-postgresql/pricing-of-serverless-apsaradb-rds-for-sql-server-instances.md) [费用](products/rds/documents/apsaradb-rds-for-postgresql/pricing-of-serverless-apsaradb-rds-for-sql-server-instances.md) 、 [SQL Server Serverless](products/rds/documents/apsaradb-rds-for-sql-server/pricing-of-serverless-apsaradb-rds-for-sql-server-instances.md) [费用](products/rds/documents/apsaradb-rds-for-sql-server/pricing-of-serverless-apsaradb-rds-for-sql-server-instances.md) 。 |
| 计费方式 | Serverless。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [弹性型（特惠版）节省计划](products/rds/documents/apsaradb-rds-for-mysql/elastic-savings-plan.md) 和 [通用型节省计划](products/rds/documents/product-overview/savings-plan-introduction.md) 可以抵扣 RDS Serverless 实例的 RCU 费用。 |


### 存储空间

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

| 类别 | 说明 |
| --- | --- |
| 定义 | 包年包月、按量付费 或 Serverless 的 RDS 实例（包括常规实例、只读实例、灾备实例、 、DuckDB 分析实例 ）的存储空间的费用。计费项名称为 存储空间（rds_storage 或 Storage） 。 创建实例后，会产生该计费项。实例的存储空间增加或减少，会导致该计费项的费用变化。 |
| 计费公式 | 包年包月或按量付费的基础系列、高可用系列：存储空间费用=实例存储空间单价 * 实例存储空间容量 * 时长 包年包月或按量付费的集群系列：存储空间费用=单节点存储空间单价 * 单节点存储空间容量 * 节点数 * 时长 RDS MySQL Serverless 实例、RDS PostgreSQL Serverless 实例：存储空间费用=单节点存储空间单价*单节点存储空间容量 * 节点数 * 时长 RDS SQL Server Serverless 实例：存储空间费用=实例存储空间单价 * 实例存储空间容量 * 时长 说明 RDS 存储空间单价与地域、产品系列、存储类型和计费方式相关，具体价格请以控制台为准。 不同计费方式下，计算公式中的时长会有所不同。 包年包月实例：计算时长为购买时长。 按量付费 或 Serverless 实例：计算时长为计费时长，计费周期为 1 小时。 开启存储压缩功能后，实例的单位存储空间的计费公式会发生变化，详情请参见 [存储压缩](products/rds/documents/product-overview/billable-items-billing-methods-and-pricing.md) 。 |
| 计费方式 | 包年包月、按量付费 和 Serverless 。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [存储包](products/rds/documents/product-overview/storage-plans.md) 可以抵扣 按量付费 的 RDS 实例（不包括高性能云盘和 SSD 云盘）的存储空间费用。 [通用型节省计划](products/rds/documents/product-overview/savings-plan-introduction.md) 可以抵扣 按量付费 和 Serverless 的 RDS 实例的存储空间费用。 [弹性型（特惠版）节省计划](products/rds/documents/apsaradb-rds-for-mysql/elastic-savings-plan.md) 可以抵扣 Serverless 的 RDS 实例的存储空间费用。 |


## RDS增值服务

RDS增值服务是RDS提供的付费功能。开通或使用了功能，才会产生费用。RDS增值服务的账单产品是云数据库 RDS。

### 存储压缩

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 定义 | 开启 [存储压缩](products/rds/documents/apsaradb-rds-for-mysql/storage-compression.md) 功能后，实例的单位存储空间的计费公式会发生变化。 |
| 计费公式 | 包年包月或按量付费的高可用系列：存储空间费用 = 1.25 * 实例存储空间单价 * 实例存储空间 * 使用时长 包年包月或按量付费的集群系列：存储空间费用 = 1.25 * 单节点存储空间单价 * 单节点存储空间 * 节点数 * 使用时长 |
| 计费方式 | 包年包月、按量付费。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [存储包](products/rds/documents/product-overview/storage-plans.md) 可以抵扣 按量付费 的 RDS 实例（不包括高性能云盘和 SSD 云盘）的存储空间费用。 [通用型节省计划](products/rds/documents/product-overview/savings-plan-introduction.md) 可以抵扣 按量付费 和 Serverless 的 RDS 实例的存储空间费用。 [弹性型（特惠版）节省计划](products/rds/documents/apsaradb-rds-for-mysql/elastic-savings-plan.md) 可以抵扣 Serverless 的 RDS 实例的存储空间费用。 |


### 性能自动扩容

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 定义 | 开启 [性能自动扩容](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-scale-up-feature-for-an-apsaradb-rds-for-mysql-instance.md) 功能不收费。但开启后，如果当 CPU 使用率达到阈值，会触发 RDS MySQL 实例计算资源的变配，增加的计算资源会按量计费。 云盘实例，性能自动扩容时会变配到其他 RDS 规格，系统会按新的规格收取实例的 [RDS](products/rds/documents/product-overview/billable-items-billing-methods-and-pricing.md) [规格](products/rds/documents/product-overview/billable-items-billing-methods-and-pricing.md) 费用。费用变化规则与变更配置相同，详情请参见 [变更配置](products/rds/documents/product-overview/specification-changes.md) 。 高性能本地盘实例，性能自动扩容时会自动增加 CPU 核数，产生新的计费项，名称为 弹性计算资源（CPU+IOPS） ，计费项 Code 为 cpu_cores_flexible。 |
| 计费公式 | 高性能本地盘实例弹性计算资源费用=CPU 单价 * 增加的 CPU 核数 * 时长 云盘实例新的 RDS 规格费用=RDS 规格实例单价 * 时长 说明 高性能本地盘实例性能自动扩容的 CPU 单价，请参见 [设置性能自动扩容](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-scale-up-feature-for-an-apsaradb-rds-for-mysql-instance.md) 。 云盘实例 RDS 规格实例单价与售卖页的 RDS 规格实例单价相同。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [计算包](products/rds/documents/product-overview/compute-plans.md) 和 [通用型节省计划](products/rds/documents/product-overview/savings-plan-introduction.md) 可以抵扣 按量付费的 RDS 云盘实例的 RDS 规格（rds_class） 费用。 |


### 高性能云盘IO性能突发

| 类别 | 说明 |
| --- | --- |
| 定义 | RDS 高性能云盘实例的 IO 性能突发量的费用。开启高性能云盘 IO 性能突发不收费。但开启后，如果 IO 性能突发量超过免费额度，会产生 IO 性能突发（io_burst） 的费用。 功能详情，请参见 [MySQL IO](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) [性能突发](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) 、 [PostgreSQL IO](products/rds/documents/apsaradb-rds-for-postgresql/io-performance-burst.md) [性能突发](products/rds/documents/apsaradb-rds-for-postgresql/io-performance-burst.md) 或 [SQL Server IO](products/rds/documents/apsaradb-rds-for-sql-server/i-o-performance-burst-for-premium-essds.md) [性能突发](products/rds/documents/apsaradb-rds-for-sql-server/i-o-performance-burst-for-premium-essds.md) 。 |
| 计费公式 | 高性能云盘 IO 性能突发费用=（实例各节点 IO 性能突发量总和-免费额度）* IO 性能突发单价 * 时长 说明 实例各节点 IO 性能突发量总和、免费额度、IO 性能突发单价请参见 [MySQL IO](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) [性能突发计费说明](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) 、 [PostgreSQL IO](products/rds/documents/apsaradb-rds-for-postgresql/io-performance-burst.md) [性能突发计费说明](products/rds/documents/apsaradb-rds-for-postgresql/io-performance-burst.md) 、 [SQL Server IO](products/rds/documents/apsaradb-rds-for-sql-server/i-o-performance-burst-for-premium-essds.md) [性能突发计费说明](products/rds/documents/apsaradb-rds-for-sql-server/i-o-performance-burst-for-premium-essds.md) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | 不支持。 |


### 高性能云盘数据归档

| 类别 | 说明 |
| --- | --- |
| 定义 | 开启数据归档不收费。但开启后，归档至 OSS 的数据会产生 OSS 存储空间（rds_oss_storage） 的费用。 功能详情，请参见 [MySQL](products/rds/documents/apsaradb-rds-for-mysql/rds-mysql-data-archiving-function.md) [数据归档](products/rds/documents/apsaradb-rds-for-mysql/rds-mysql-data-archiving-function.md) 、 [PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/data-archiving.md) [数据归档](products/rds/documents/apsaradb-rds-for-postgresql/data-archiving.md) 或 [SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/archive-data-to-an-oss-bucket.md) [数据归档](products/rds/documents/apsaradb-rds-for-sql-server/archive-data-to-an-oss-bucket.md) 。 说明 RDS SQL Server 同时支持 ESSD 云盘数据归档功能，高性能云盘数据归档功能需手动开启，ESSD 云盘数据归档功能默认处于开启状态。 |
| 计费公式 | 高性能 云盘数据归档费用=归档数据量 * 数据归档单价 * 时长 说明 数据归档单价，请参见 [MySQL](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) [数据归档计费说明](products/rds/documents/apsaradb-rds-for-mysql/i-o-performance-burst.md) 、 [PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/data-archiving.md) [数据归档计费说明](products/rds/documents/apsaradb-rds-for-postgresql/data-archiving.md) 、 [SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/archive-data-to-an-oss-bucket.md) [数据归档计费说明](products/rds/documents/apsaradb-rds-for-sql-server/archive-data-to-an-oss-bucket.md) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | 不支持。 |


### 常规备份、归档备份

### 常规备份空间

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 定义 | 数据备份和日志备份存放于阿里云提供的备份空间。阿里云提供免费的备份额度，当备份空间超过免费额度时，超出部分将按量计费，产生的计费项名称为 RDS 基础备份费用（backup_charged） 。 功能详情，请参见 [备份](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md) [MySQL](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md) [数据](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md) 、 [备份](products/rds/documents/apsaradb-rds-for-postgresql/back-up-an-apsaradb-rds-for-postgresql-instance.md) [PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/back-up-an-apsaradb-rds-for-postgresql-instance.md) [数据](products/rds/documents/apsaradb-rds-for-postgresql/back-up-an-apsaradb-rds-for-postgresql-instance.md) 、 [备份](products/rds/documents/apsaradb-rds-for-sql-server/back-up-an-apsaradb-rds-for-sql-server-instance.md) [SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/back-up-an-apsaradb-rds-for-sql-server-instance.md) [数据](products/rds/documents/apsaradb-rds-for-sql-server/back-up-an-apsaradb-rds-for-sql-server-instance.md) 、 [备份](products/rds/documents/apsaradb-rds-for-mariadb/back-up-an-apsaradb-rds-for-mariadb-instance.md) [MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/back-up-an-apsaradb-rds-for-mariadb-instance.md) [数据](products/rds/documents/apsaradb-rds-for-mariadb/back-up-an-apsaradb-rds-for-mariadb-instance.md) 。 |
| 账单产品 | 关系型数据库。 |
| 计费公式 | 备份空间费用=（备份总大小-免费备份额度）* 备份空间单价 * 时长 说明 未开启存储压缩功能的 免费备份空间额度： 云盘实例 的免费额度为存储空间的 200%； 高性能本地盘实例 的免费额度为存储空间的 50%。 开启 [存储压缩](products/rds/documents/apsaradb-rds-for-mysql/storage-compression.md) 功能的免费备份空间额度： 云盘实例 的免费额度为存储空间的 400%； 高性能本地盘实例 的免费额度为存储空间的 100%。 备份空间单价，请参见 [MySQL](products/rds/documents/apsaradb-rds-for-mysql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md) [备份费用](products/rds/documents/apsaradb-rds-for-mysql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md) 、 [PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-postgresql-instance.md) [备份费用](products/rds/documents/apsaradb-rds-for-postgresql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-postgresql-instance.md) 、 [SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-sql-server-instance.md) [备份费用](products/rds/documents/apsaradb-rds-for-sql-server/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-sql-server-instance.md) 、 [RDS MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/view-the-free-quota-for-backup-storage-of-an-apsaradb-rds-for-mariadb-instance.md) [备份费用](products/rds/documents/apsaradb-rds-for-mariadb/view-the-free-quota-for-backup-storage-of-an-apsaradb-rds-for-mariadb-instance.md) 。 如何减少备份费用和大小，请参见 [减少](products/rds/documents/apsaradb-rds-for-mysql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md) [RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md) [备份费用](products/rds/documents/apsaradb-rds-for-mysql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md) 、 [减少](products/rds/documents/apsaradb-rds-for-sql-server/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-sql-server-instance.md) [RDS SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-sql-server-instance.md) [备份费用](products/rds/documents/apsaradb-rds-for-sql-server/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-sql-server-instance.md) 、 [减少](products/rds/documents/apsaradb-rds-for-postgresql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-postgresql-instance.md) [RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-postgresql-instance.md) [备份费用](products/rds/documents/apsaradb-rds-for-postgresql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-postgresql-instance.md) 、 [通过扩容存储空间提高](products/rds/documents/apsaradb-rds-for-mariadb/change-the-specifications-of-an-apsaradb-rds-for-mariadb-instance.md) [MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/change-the-specifications-of-an-apsaradb-rds-for-mariadb-instance.md) [免费额度](products/rds/documents/apsaradb-rds-for-mariadb/change-the-specifications-of-an-apsaradb-rds-for-mariadb-instance.md) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [存储包](products/rds/documents/product-overview/storage-plans.md) 可以抵扣 包年包月或按量付费 的 RDS 实例超出免费额度的备份空间（不包括高性能云盘和 SSD 云盘）。 [通用型节省计划](products/rds/documents/product-overview/savings-plan-introduction.md) 可以抵扣 包年包月、按量付费以及 Serverless RDS 实例的备份空间费用。 |


## 归档备份空间

- 

- 

| 类别 | 说明 |
| --- | --- |
| 定义 | 备份天数超过 730 天的数据备份自动转为归档备份，产生的计费项名称为 长期备份（ArchivedBackupCharged） 。 功能详情，请参见 [自动备份](products/rds/documents/apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md) 。 |
| 账单产品 | 关系型数据库。 |
| 计费公式 | 归档备份空间费用= 归档备份空间单价 * 归档备份空间用量 * 时长 说明 归档备份空间单价，请参见 [备份费用](products/rds/documents/apsaradb-rds-for-mysql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [存储包](products/rds/documents/product-overview/storage-plans.md) 可以抵扣 包年包月或按量付费 的 RDS 实例的归档备份空间。 [通用型节省计划](products/rds/documents/product-overview/savings-plan-introduction.md) 可以抵扣 包年包月、按量付费以及 Serverless RDS 实例的归档备份空间费用。 |


说明

- 

跨地域备份产生的计费项，账单产品包括关系型数据库和数据库备份，详情请参见[数据灾备：跨地域备份、已删除实例备份空间、下载备份](products/rds/documents/product-overview/billable-items-billing-methods-and-pricing.md)。

- 

已删除实例的备份空间、下载备份产生的计费项，账单产品是数据库备份，详情请参见[数据灾备：跨地域备份、已删除实例备份空间、下载备份](products/rds/documents/product-overview/billable-items-billing-methods-and-pricing.md)。

### 全量恢复、常规库表恢复

## 恢复全量数据（克隆实例）

使用原实例的数据备份和日志备份进行数据恢复，恢复至新实例时需要收取新实例的[RDS](products/rds/documents/product-overview/billable-items-billing-methods-and-pricing.md)[规格](products/rds/documents/product-overview/billable-items-billing-methods-and-pricing.md)费用和[存储空间](products/rds/documents/product-overview/billable-items-billing-methods-and-pricing.md)费用。

功能详情，请参见[恢复](products/rds/documents/apsaradb-rds-for-mysql/restore-full-data-of-an-apsaradb-rds-for-mysql-instance.md)[MySQL](products/rds/documents/apsaradb-rds-for-mysql/restore-full-data-of-an-apsaradb-rds-for-mysql-instance.md)[数据](products/rds/documents/apsaradb-rds-for-mysql/restore-full-data-of-an-apsaradb-rds-for-mysql-instance.md)、[恢复](products/rds/documents/apsaradb-rds-for-sql-server/restore-the-data-of-an-apsaradb-rds-for-sql-server-instance.md)[SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/restore-the-data-of-an-apsaradb-rds-for-sql-server-instance.md)[数据](products/rds/documents/apsaradb-rds-for-sql-server/restore-the-data-of-an-apsaradb-rds-for-sql-server-instance.md)、[恢复](products/rds/documents/apsaradb-rds-for-postgresql/restore-data-of-an-apsaradb-rds-for-postgresql-instance.md)[PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/restore-data-of-an-apsaradb-rds-for-postgresql-instance.md)[数据](products/rds/documents/apsaradb-rds-for-postgresql/restore-data-of-an-apsaradb-rds-for-postgresql-instance.md)、[恢复](products/rds/documents/apsaradb-rds-for-mariadb/restore-the-data-of-an-apsaradb-rds-for-mariadb-instance.md)[MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/restore-the-data-of-an-apsaradb-rds-for-mariadb-instance.md)[数据](products/rds/documents/apsaradb-rds-for-mariadb/restore-the-data-of-an-apsaradb-rds-for-mariadb-instance.md)。

## 常规库表恢复

将指定的库、表按备份集或时间点恢复至新实例时需要收取新实例的[RDS](products/rds/documents/product-overview/billable-items-billing-methods-and-pricing.md)[规格](products/rds/documents/product-overview/billable-items-billing-methods-and-pricing.md)费用和[存储空间](products/rds/documents/product-overview/billable-items-billing-methods-and-pricing.md)费用。恢复至原实例，不会产生费用。

功能详情，请参见[MySQL](products/rds/documents/apsaradb-rds-for-mysql/restore-individual-databases-and-tables-of-an-apsaradb-rds-for-mysql-instance.md)[恢复库表](products/rds/documents/apsaradb-rds-for-mysql/restore-individual-databases-and-tables-of-an-apsaradb-rds-for-mysql-instance.md)、[PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/restore-individual-databases-and-tables-of-an-apsaradb-rds-for-postgresql-instance.md)[恢复库表](products/rds/documents/apsaradb-rds-for-postgresql/restore-individual-databases-and-tables-of-an-apsaradb-rds-for-postgresql-instance.md)。

### SQL审计（DAS企业版V0）

| 类别 | 说明 |
| --- | --- |
| 定义 | SQL 审计日志的存储费用。开启 SQL 审计后，根据 SQL 审计日志占用的存储空间和存储时长计费。计费项名称为 SQL 审计（sql_collected） 。 功能详情，请参见 [RDS MySQL SQL](products/rds/documents/use-sql-explorer-features-on-apsaradb-rds-for-mysql-instances.md) [洞察和审计](products/rds/documents/use-sql-explorer-features-on-apsaradb-rds-for-mysql-instances.md) 、 [RDS SQL Server SQL](products/rds/documents/apsaradb-rds-for-sql-server/use-the-sql-explorer-and-audit-feature-on-an-apsaradb-rds-for-sql-server-instance.md) [洞察和审计](products/rds/documents/apsaradb-rds-for-sql-server/use-the-sql-explorer-and-audit-feature-on-an-apsaradb-rds-for-sql-server-instance.md) 、 [RDS PostgreSQL SQL](products/rds/documents/apsaradb-rds-for-postgresql/sql-insight-or-audit.md) [洞察和审计](products/rds/documents/apsaradb-rds-for-postgresql/sql-insight-or-audit.md) 。 |
| 账单产品 | 关系型数据库。 |
| 计费公式 | SQL 审计费用 = 单价 * 存储空间 * 时长 说明 SQL 审计单价，请参见 [MySQL SQL](products/rds/documents/use-sql-explorer-features-on-apsaradb-rds-for-mysql-instances.md) [洞察计费](products/rds/documents/use-sql-explorer-features-on-apsaradb-rds-for-mysql-instances.md) 、 [PostgreSQL SQL](products/rds/documents/use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) [洞察计费](products/rds/documents/use-the-sql-audit-feature-on-an-apsaradb-rds-for-postgresql-instance.md) 、 [SQL Server SQL](https://help.aliyun.com/zh/document_detail/95712.html#fa863db04812d) [洞察计费](https://help.aliyun.com/zh/document_detail/95712.html#fa863db04812d) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [存储包](products/rds/documents/product-overview/storage-plans.md) 和 [通用型节省计划](products/rds/documents/product-overview/savings-plan-introduction.md) 可以抵扣 按量付费 和 包年包月 RDS 实例产生的 DAS 企业版 V0 SQL 审计 费用。 |


说明

由DAS 企业版V3/V2/V1提供的SQL洞察与审计功能，账单产品为数据库自治服务，详情请参见[DAS：SQL](products/rds/documents/product-overview/billable-items-billing-methods-and-pricing.md)[洞察和审计](products/rds/documents/product-overview/billable-items-billing-methods-and-pricing.md)。

### 性能监控

| 类别 | 说明 |
| --- | --- |
| 定义 | 设置 RDS MySQL 实例性能监控频率为 5 秒/次时，产生 性能监控（advanced_monitor） 费用。性能监控频率为 60 秒/次和 300 秒/次时，性能监控免费。RDS PostgreSQL、SQL Server 和 MariaDB 实例性能监控免费。 功能详情，请参见 [设置旧版监控的频率](products/rds/documents/apsaradb-rds-for-mysql/set-the-monitoring-frequency-of-an-apsaradb-rds-for-mysql-instance.md) 。 |
| 计费公式 | 性能监控费用=性能监控单价 * 时长 说明 性能监控单价，请参见 [费用](products/rds/documents/apsaradb-rds-for-mysql/set-the-monitoring-frequency-of-an-apsaradb-rds-for-mysql-instance.md) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [通用型节省计划](products/rds/documents/product-overview/savings-plan-introduction.md) 可以抵扣固定规格的 RDS 实例的性能监控费用。 |


### 数据库代理

| 类别 | 说明 |
| --- | --- |
| 定义 | 数据库代理的费用。开通数据库代理且代理类型为 独享型代理 时，按代理规格和使用时长计费，计费项名称为 数据库代理实例分片数（MaxscaleChargedSliceNum） 。通用型代理免费。 功能详情，请参见 [RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/what-are-database-proxies.md) [数据库代理](products/rds/documents/apsaradb-rds-for-mysql/what-are-database-proxies.md) 、 [RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/what-are-database-proxies.md) [数据库代理](products/rds/documents/apsaradb-rds-for-postgresql/what-are-database-proxies.md) 。 说明 关于 RDS 数据库代理的使用问题和更多相关信息，欢迎加入用户钉钉群（106730000316）进行咨询、反馈和交流 。 |
| 计费公式 | 数据库代理费用=单价 * 代理数量 * 时长 说明 数据库代理单价，请参见 [MySQL](products/rds/documents/apsaradb-rds-for-mysql/billing-rules-for-the-dedicated-proxy-feature-of-apsaradb-rds-for-mysql.md) [独享型代理价格](products/rds/documents/apsaradb-rds-for-mysql/billing-rules-for-the-dedicated-proxy-feature-of-apsaradb-rds-for-mysql.md) 、 [PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/billing-rules-for-the-database-proxy-of-an-apsaradb-rds-for-postgresql-instance.md) [独享型代理价格](products/rds/documents/apsaradb-rds-for-postgresql/billing-rules-for-the-database-proxy-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [计算包](products/rds/documents/product-overview/compute-plans.md) 和 [通用型节省计划](products/rds/documents/product-overview/savings-plan-introduction.md) 可以抵扣固定规格的 RDS 实例的数据库代理规格费用。 |


### 外网连接地址流量

申请外网地址并使用外网地址连接RDS，会产生外网流量。当前通过外网地址连接RDS实例产生的外网流量（流入和流出）享受零折优惠，不收费。

功能详情，请参见[RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/apply-for-or-release-a-public-endpoint-for-an-apsaradb-rds-for-mysql-instance.md)[开通或关闭外网地址](products/rds/documents/apsaradb-rds-for-mysql/apply-for-or-release-a-public-endpoint-for-an-apsaradb-rds-for-mysql-instance.md)、[RDS SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/apply-for-or-release-a-public-endpoint-for-an-apsaradb-rds-for-sql-server-instance.md)[开通或关闭外网地址](products/rds/documents/apsaradb-rds-for-sql-server/apply-for-or-release-a-public-endpoint-for-an-apsaradb-rds-for-sql-server-instance.md)、[RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/apply-for-or-release-a-public-endpoint-on-an-apsaradb-rds-for-postgresql-instance.md)[开通或关闭外网地址](products/rds/documents/apsaradb-rds-for-postgresql/apply-for-or-release-a-public-endpoint-on-an-apsaradb-rds-for-postgresql-instance.md)、[RDS MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/apply-for-or-release-a-public-endpoint-for-an-apsaradb-rds-for-mariadb-instance.md)[开通或关闭外网地址](products/rds/documents/apsaradb-rds-for-mariadb/apply-for-or-release-a-public-endpoint-for-an-apsaradb-rds-for-mariadb-instance.md)。

## 其他云产品提供服务与计费

RDS集成了其他阿里云产品的服务。您在使用下列功能时，会产生其他云产品的计费项。

### 数据灾备：跨地域备份、已删除实例备份空间、下载备份

### 跨地域备份

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

| 类别 | 说明 |
| --- | --- |
| 定义 | 跨地域备份产生的备份存储费用和网络费用。具体计费项如下： 异地备份空间（DdrOssStorageSize） 和 跨地域备份网络流量（NetworkOutDuplicationSize）。 RDS MySQL 高性能本地盘、RDS PostgreSQL、SQL Server： 异地备份空间（DdrOssStorageSize） 和 跨地域备份网络流量（NetworkOutDuplicationSize） 。 RDS MySQL 云盘版： 云数据库备份存储容量（BackupStorageSize） 和 跨地域备份网络流量（NetworkOutDuplicationSize）。 功能详情，请参见 [MySQL](products/rds/documents/apsaradb-rds-for-mysql/use-the-cross-region-backup-feature-of-an-apsaradb-rds-for-mysql-instance.md) [跨地域备份](products/rds/documents/apsaradb-rds-for-mysql/use-the-cross-region-backup-feature-of-an-apsaradb-rds-for-mysql-instance.md) 、 [PostgreSQL](products/rds/documents/apsaradb-rds-for-sql-server/enable-the-cross-region-backup-feature-for-an-apsaradb-rds-for-sql-server-instance.md) [跨地域备份](products/rds/documents/apsaradb-rds-for-sql-server/enable-the-cross-region-backup-feature-for-an-apsaradb-rds-for-sql-server-instance.md) 、 [SQL Server](products/rds/documents/apsaradb-rds-for-postgresql/use-the-cross-region-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) [跨地域备份](products/rds/documents/apsaradb-rds-for-postgresql/use-the-cross-region-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 账单产品 | 异地备份空间（DdrOssStorageSize）： 关系型数据库。 云数据库备份存储容量（BackupStorageSize） ：数据库备份。 跨地域备份网络流量（NetworkOutDuplicationSize） ：数据库备份。 |
| 计费公式 | 异地备份空间费用=异地备份空间单价*异地存储空间大小*时长 云数据库备份存储容量费用=云数据库备份存储空间单价*云数据库备份存储空间大小*时长 跨地域备份网络费用=网络流量单价*流量用量 说明 异地备份空间单价，请参见 [MySQL](products/rds/documents/apsaradb-rds-for-mysql/use-the-cross-region-backup-feature-of-an-apsaradb-rds-for-mysql-instance.md) [高性能本地盘跨地域备份](products/rds/documents/apsaradb-rds-for-mysql/use-the-cross-region-backup-feature-of-an-apsaradb-rds-for-mysql-instance.md) 、 [PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/use-the-cross-region-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) [跨地域备份](products/rds/documents/apsaradb-rds-for-postgresql/use-the-cross-region-backup-feature-for-an-apsaradb-rds-for-postgresql-instance.md) 、 [SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/enable-the-cross-region-backup-feature-for-an-apsaradb-rds-for-sql-server-instance.md) [跨地域备份](products/rds/documents/apsaradb-rds-for-sql-server/enable-the-cross-region-backup-feature-for-an-apsaradb-rds-for-sql-server-instance.md) 。 云数据库备份存储空间单价，请参见 [MySQL](products/rds/documents/apsaradb-rds-for-mysql/use-the-cross-region-backup-feature-of-an-apsaradb-rds-for-mysql-instance.md) [云盘跨地域备份](products/rds/documents/apsaradb-rds-for-mysql/use-the-cross-region-backup-feature-of-an-apsaradb-rds-for-mysql-instance.md) 。 网络流量单价，请参见 [网络费用](https://help.aliyun.com/zh/dms/product-overview/network-fees) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [RDS](products/rds/documents/product-overview/storage-plans.md) [存储包](products/rds/documents/product-overview/storage-plans.md) 和 [通用型节省计划](products/rds/documents/product-overview/savings-plan-introduction.md) 可以抵扣 包年包月或按量付费 RDS MySQL 高性能本地盘 实例、RDS SQL Server 实例、RDS PostgreSQL 实例的 异地备份空间（DdrOssStorageSize） 费用。 [DBS](https://help.aliyun.com/zh/dbs/getting-started/use-network-plans#task-1953491) [网络包](https://help.aliyun.com/zh/dbs/getting-started/use-network-plans#task-1953491) 可以抵扣 包年包月或按量付费 RDS 实例的 跨地域备份网络流量（NetworkOutDuplicationSize） 费用。 |


### 已删除实例备份空间

- 

- 

| 类别 | 说明 |
| --- | --- |
| 定义 | RDS MySQL 已删除实例的备份集存储费用。7 天内存储免费，超过 7 天将按备份集大小和存储时长计费。具体计费项名称如下。 RDS MySQL 高性能本地盘： 标准型存储容量（StandardStorageSize） RDS MySQL 云盘： 云数据库备份存储容量（BackupStorageSize） 功能详情，请参见 [设置实例释放后备份保留策略](products/rds/documents/apsaradb-rds-for-mysql/configure-backup-retention-policies-for-released-instances.md) 。 |
| 账单产品 | 数据库备份。 |
| 计费公式 | 已删除实例的备份存储空间费用=已删除实例备份存储单价 * 已删除实例的备份大小 * 使用时长 说明 已删除实例备份存储单价，请参见 [费用说明](products/rds/documents/apsaradb-rds-for-mysql/retain-the-backup-files-of-an-apsaradb-rds-for-mysql-instance-for-a-long-period-of-time.md) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | [DBS](https://help.aliyun.com/zh/dbs/getting-started/use-storage-plans#multiTask382) [云数据库备份存储包](https://help.aliyun.com/zh/dbs/getting-started/use-storage-plans#multiTask382) 可以抵扣 包年包月或按量付费 RDS MySQL 云盘 实例的 云数据库备份存储容量（BackupStorageSize） 费用。 |


### 下载备份

- 

- 

| 类别 | 说明 |
| --- | --- |
| 定义 | 下载 RDS 实例备份时产生的 费用，包括 外网流出流量（NetworkOutSize） 费用和使用高级下载功能时产生的 备份计算数据量（BackupAnalyticSize） 费用 。 功能详情，请参见 [RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance-download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance.md) [下载备份](products/rds/documents/apsaradb-rds-for-mysql/download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance-download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance.md) 、 [RDS SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/download-the-data-backup-files-and-log-backup-files-of-an-apsaradb-rds-for-sql-server-instance.md) [下载备份](products/rds/documents/apsaradb-rds-for-sql-server/download-the-data-backup-files-and-log-backup-files-of-an-apsaradb-rds-for-sql-server-instance.md) 、 [RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/download-the-backup-files-of-an-apsaradb-rds-for-postgresql-instance.md) [下载备份](products/rds/documents/apsaradb-rds-for-postgresql/download-the-backup-files-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 账单产品 | 数据库备份。 |
| 计费公式 | 备份计算数据量费用=单价 * 备份计算数据量 外网流出流量费用=单价 * （流量用量-免费额度） 说明 下载备份产生的备份计算数据量单价（又叫备份转换费用单价）和外网流出流量单价，请参见 [下载备份](products/rds/documents/apsaradb-rds-for-mysql/download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance-download-the-backup-files-of-an-apsaradb-rds-for-mysql-instance.md) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | [DBS](https://help.aliyun.com/zh/dbs/getting-started/use-network-plans#task-1953491) [网络包](https://help.aliyun.com/zh/dbs/getting-started/use-network-plans#task-1953491) 可以抵扣 包年包月或按量付费 RDS 实例的 外网流出流量（NetworkOutSize） 费用。 |


### 数据灾备：极速库表（5min）恢复、应急恢复

### 极速库表恢复&极速库表5min恢复

重要

极速库表5min恢复已暂停新增。

- 

- 

| 类别 | 说明 |
| --- | --- |
| 定义 | RDS MySQL 高性能本地盘实例的极速库表恢复功能分免费版和付费版两种。详情如下： 免费版：开启及使用极速库表恢复（免费版），不收取任何费用。 付费版：开启及使用极速库表恢复（付费版）后，将根据数据量计费，产生的计费项名称为 CDM 本地盘存储容量（CapacitySandboxStorageSize） 。 |
| 账单产品 | 数据库备份。 |
| 计费公式 | 费用 = CDM 本地盘存储单价 * CDM 本地盘存储容量 * 使用时长 说明 CDM 本地盘存储单价，请参见 [恢复库表](products/rds/documents/apsaradb-rds-for-mysql/restore-individual-databases-and-tables-of-an-apsaradb-rds-for-mysql-instance.md) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | [CDM](https://help.aliyun.com/zh/dbs/product-overview/dbs-sandbox-fees#7b28e1cf9fpmy) [沙箱存储包](https://help.aliyun.com/zh/dbs/product-overview/dbs-sandbox-fees#7b28e1cf9fpmy) 可以抵扣 包年包月或按量付费 RDS MySQL 高性能本地盘 实例的 CDM 本地盘存储容量（CapacitySandboxStorageSize） 费用。 |


### 应急恢复

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 定义 | RDS MySQL 高性能本地盘实例的应急恢复功能涉及的计费项如下： CDM 本地盘存储容量（CapacitySandboxStorageSize） ：开启 数据灾备 沙箱功能后，每个数据库实例将对应一个沙箱存储。系统会自动将对应数据库实例的数据同步至沙箱存储中，生成多个沙箱快照。 数据灾备 将根据沙箱存储中的数据量收取沙箱存储费用。 CDM 沙箱实例规格（SandboxDatabaseSpec） ：恢复到临时沙箱实例后， 数据灾备 将根据临时沙箱实例的规格和使用时长收取临时沙箱实例费用（按小时扣费）。如果您没有恢复临时沙箱实例，则不会产生临时沙箱实例费用。 功能详情，请参见 [RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/create-an-rds-emergency-instance.md) [应急恢复](products/rds/documents/apsaradb-rds-for-mysql/create-an-rds-emergency-instance.md) 。 |
| 账单产品 | 数据库备份。 |
| 计费公式 | CDM 本地盘存储容量费用 = CDM 本地盘存储容量单价 * 使用时长 * CDM 本地盘存储容量 CDM 沙箱实例规格费用 = 沙箱实例规格单价 * 使用时长 说明 CDM 本地盘存储容量单价，请参见 [沙箱存储费用](https://help.aliyun.com/zh/dbs/product-overview/dbs-sandbox-fees#section-zem-2el-l1d) 。 沙箱实例规格单价，请参见 [临时沙箱实例费用](https://help.aliyun.com/zh/dbs/product-overview/dbs-sandbox-fees#section-kbj-aba-mlq) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | [CDM](https://help.aliyun.com/zh/dbs/product-overview/dbs-sandbox-fees#7b28e1cf9fpmy) [沙箱存储包](https://help.aliyun.com/zh/dbs/product-overview/dbs-sandbox-fees#7b28e1cf9fpmy) 可以抵扣 包年包月或按量付费 RDS MySQL 高性能本地盘 实例的 CDM 本地盘存储容量（CapacitySandboxStorageSize） 费用。 |


### DAS：SQL洞察和审计

DAS企业版V3、V2、V1的计费项账单产品为数据库自治服务。不能用RDS的节省计划或资源包抵扣。

计费详情

企业版 V3

重要

企业版 V3按使用的功能细分了计费项，使计费更加灵活，使用成本大大降低。

- 

开通企业版 V3后，默认收取日志流量费用，其他计费将根据对应功能的使用情况进行收取。

- 

支持企业版 V1和V2免费迁移至企业版 V3，迁移完成前按照当前版本计费，迁移完成后按照迁移目标版本计费。详情请参见[DAS](https://help.aliyun.com/zh/das/user-guide/faq#a3a950500f3s3)[企业版间数据如何迁移？](https://help.aliyun.com/zh/das/user-guide/faq#a3a950500f3s3)

企业版 V3计费方式简介

计费案例

根据服务使用场景、选用功能可分为以下2个案例：

运维场景

支持全量SQL日志记录和聚类分析，可用于快速查询定位分析问题SQL，对受影响业务应急处理和后续深度优化，功能详见[SQL](https://help.aliyun.com/zh/das/user-guide/sql-explorer-and-audit-5/)[洞察和审计](https://help.aliyun.com/zh/das/user-guide/sql-explorer-and-audit-5/)。本场景可选开启功能如下：

假设您的实例每天都有10GB写入流量，设置SQL日志存储为30天，日志索引热存储为7天。

说明

SQL日志存储时长即为您的SQL日志存储总时间，默认为冷存储。例如，在以上场景，开通日志索引后，新产生的日志会先以7天热存储形式存储，超过7天之后，剩余23天则转入冷存储。

| 功能 | 计费项 | 日单价（中国内地公有云为例） | 日用量 | 日费用 |
| --- | --- | --- | --- | --- |
| SQL 日志 | 日志流量（DataIngestion） | 0.24 元/GB | 10GB | 2.4 元 |
| 冷存储（SqlInsightColdDataSize） | 0.003 元/GB/天 | 从转冷存储起 第 1 天 10GB 第 2 天 20GB …… 第 23 天为 230GB | 0 （30 天内冷存储部分免费） |  |
| 日志索引 | 日志索引（RealTimeSearchAnalytics） | 0.24 元/GB | 10GB | 2.4 元 |
| 热存储（SqlInsightHotDataSize） | 0.01 元/GB/天 | 开通后 第 1 天为 10GB 第 2 天为 20GB …… 第 7 天为 70GB （7 天之后热数据到期部分转到冷存储） | 存够 7 天及以上 10*（7-1）*0.01=0.6 元 （首日热存储免费） |  |
| SQL 洞察 | SQL 洞察（InsightAnalysis） | 0.08 元/GB | 10GB | 0.8 元 |


审计合规场景

支持银行级安全合规能力以及中国内地等保法规要求，长周期透明监控数据库行为，提供实时告警；数据安全方面全方位检测异常访问、漏洞攻击、数据泄露、基线检测等，以避免数据库业务受到影响。功能详见[安全审计（新版）](https://help.aliyun.com/zh/das/user-guide/security-audit-new-version/)，本场景可选开启功能如下：

假设您的实例每天都有10GB写入流量，设置SQL日志存储为180天满足中国内地合规法规。

说明

- 

SQL日志存储时长即为您的SQL日志储总时间，默认为冷存储。

- 

为满足中国内地合规法规设置冷存储时间不能低于180天。

| 功能 | 计费项 | 日单价（中国内地公有云为例） | 日用量 | 日费用 |
| --- | --- | --- | --- | --- |
| SQL 日志 | 日志流量（DataIngestion） | 0.24 元/GB | 10GB | 2.4 元 |
| 冷存储（SqlInsightColdDataSize） | 0.003 元/GB/天 | 第 1 天 10GB 第 2 天 20GB …… 第 180 天为 1800GB | 10*（180-30）*0.003=4.5 元 说明 已经减免 30 天内冷存储费用，4.5 元为超过 30 天之后，150 天的存储费用。 |  |
| 安全审计 | 安全审计（SecurityAudit） | 0.48 元/GB | 10GB | 4.8 元 |


公共云

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

| 计费项 | 计费方式 | 中国内地定价 | 中国香港和海外定价 | 说明 |
| --- | --- | --- | --- | --- |
| 日志流量 （DataIngestion） | 按量计费 | 0.24 元/GB | 0.36 元/GB | 默认费用。 日志引入到存储（包含采集、传输和写入等基本过程）时按量收取该费用。 |
| 日志索引 （RealTimeSearchAnalytics） | 0.24 元/GB | 0.36 元/GB | 开启日志索引功能时收取该费用。 日志索引的数据采用热存储，会自动适应并创建优化索引，以提高数据的读取速度。 日志引入到热存储后， 1 天内不收存储费 ； |  |
| SQL 洞察 （InsightAnalysis） | 0.08 元/GB | 0.12 元/GB | 使用 SQL 洞察自动聚合分析时按日志量收取该费用。 |  |
| 热存储 （SqlInsightHotDataSize） | 0.01 元/GB/天 | 0.015 元/GB/天 | 热日志存储的费用，按日志量和存储时长收取。 日志引入到热存储后， 1 天内不收存储费 ； 如果开启了冷存储，日志热存储到期后自动免费转入冷存储。 热存储日志最多存储 7 天。 |  |
| 冷存储 （SqlInsightColdDataSize） | 0.003 元/GB/天 | 0.0045 元/GB/天 | 默认费用。 冷日志存储的费用，按日志量和存储时长收取。 如果未开启热存储，日志只存储在冷存储， 30 天内不收存储费 。 如果开启热存储： 新引入的日志将先存储于热存储（热存储首日免费），在热存储期间（ 热存储时长-首日 ）收取日志热存储的费用。 热存储到期后，自动免费转入冷存储，在冷存储期间（ 30 天-热存储时长 ）不收费。 |  |
| 冷查询 （SqlScanDataSize） | 0.015 元/GB | 0.0225 元/GB | 离线查询冷存储日志时，按查询量收取该费用。 |  |
| 下载（免费） | 0.0 元/GB | 0.0 元/GB | 当前属于公测期间，下载免费。 数据导出、转储时收取该费用。 |  |
| 安全审计 （SecurityAudit） | 0.48 元/GB | 0.72 元/GB | 使用新版安全审计时，按日志量收取该费用。 |  |


政务云、金融云

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

| 计费项 | 计费方式 | 政务云定价 | 金融云定价 | 说明 |
| --- | --- | --- | --- | --- |
| 日志流量 （DataIngestion） | 按量计费 | 0.48 元/GB | 0.456 元/GB | 默认费用。 日志引入到存储（包含采集、传输和写入等基本过程）时按量收取该费用。 |
| 日志索引 （RealTimeSearchAnalytics） | 0.48 元/GB | 0.456 元/GB | 开启日志索引功能时收取该费用。 日志索引的数据采用热存储，会自动适应并创建优化索引，以提高数据的读取速度。 日志引入到热存储后， 1 天内不收存储费 ； |  |
| SQL 洞察 （InsightAnalysis） | 0.16 元/GB | 0.152 元/GB | 使用 SQL 洞察自动聚合分析时按日志量收取该费用。 |  |
| 热存储 （SqlInsightHotDataSize） | 0.02 元/GB/天 | 0.019 元/GB/天 | 热日志存储的费用，按日志量和存储时长收取。 日志引入到热存储后， 1 天内不收存储费 ； 如果开启了冷存储，日志热存储到期后自动免费转入冷存储。 热存储日志最多存储 7 天。 |  |
| 冷存储 （SqlInsightColdDataSize） | 0.006 元/GB/天 | 0.0057 元/GB/天 | 默认费用。 冷日志存储的费用，按日志量和存储时长收取。 如果未开启热存储，日志只存储在冷存储，30 天内不收费。 如果开启热存储： 新引入日志将先存储于热存储（热存储首日免费），在热存储期间（ 热存储时长-首日 ）收取日志热存储的费用。 热存储到期后，自动免费转入冷存储，在冷存储期间（ 30 天-热存储时长 ）不收费。 |  |
| 冷查询 （SqlScanDataSize） | 0.03 元/GB | 0.0285 元/GB | 离线查询冷存储日志时，按查询量收取该费用。 |  |
| 下载（免费） | 0.0 元/GB | 0.0 元/GB | 当前属于公测期间，下载免费。 数据导出、转储时收取该费用。 |  |
| 安全审计 （SecurityAudit） | 0.96 元/GB | 0.912 元/GB | 使用新版安全审计时，按日志量收取该费用。 |  |


企业版 V2

公共云

- 

- 

| 计费项 | 计费方式 | 中国内地、马来西亚（吉隆坡）和印度尼西亚（雅加达）定价 | 中国香港和新加坡定价 | 说明 |
| --- | --- | --- | --- | --- |
| 热存储（SqlInsightHotDataSize） | 按量计费 | 0.01 元/GB/小时 | 0.015 元/GB/小时 | 数据存储在高性能的存储设备中，提供查询加速和 SQL 聚合信息的能力。最近 7 天的 SQL 洞察和审计数据使用热存储模式。 |
| 冷存储（SqlInsightColdDataSize） | 0.00125 元/GB/小时 | 0.001875 元/GB/小时 | 数据存储在低成本的存储设备中，减少使用成本，超出最近 7 天的 SQL 洞察和审计数据自动从热存储转为冷存储。查询冷存储的数据时，查询速度比查询热存储的数据慢。 |  |
| 数据查询费用（SqlScanDataSize） | 0.2 元/GB | 0.3 元/GB | 查询冷存储的数据时，按量收取数据查询费用。 |  |
| 安全审计（SecurityAudit） | 0.48 元/GB | 0.72 元/GB | 可选，可单独开通关闭。 使用新版安全审计时，按日志量收取该费用。 |  |


企业版 V1和V0

重要

仅企业版 V1收取包年包月的费用。

公共云

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

| 计费项 | 计费方式 | 定价 | 说明 |
| --- | --- | --- | --- |
| 包年包月的费用 | 包年包月 | 40 元/实例/月 | 用于计费的实例数量指企业版 V1 配额，即能够开启 DAS 专业版 V1 的数据库实例总数。 例如，当前账号的企业版 V1 配额为 3，已开启 DAS 专业版的数据库实例数量为 1，那么该账号 DAS 专业版包年包月的费用为 40 元/月×3=120 元/月 。 说明 如果您实际开通企业版 V1 的数据库实例数量小于购买的企业版 V1 配额，您可以通过减少配额来降低实际费用。详情请参见 [管理企业版 V1](https://help.aliyun.com/zh/das/user-guide/purchase-das-professional-edition#261bebb5dcypr) 。 仅企业版 V1 收取包年包月的费用。 |
| SQL 洞察的存储费用（sql_storage_used） | 按量计费 | 免费额度：DAS 赠送 5 GB 的免费存储空间。 重要 仅企业版 V1 赠送免费存储空间。 超出部分计费：0.008 元/GB/小时。 | 中国内地、马来西亚（吉隆坡）和印度尼西亚（雅加达）定价。 |
| 免费额度：DAS 赠送 3 GB 的免费存储空间。 重要 仅企业版 V1 赠送免费存储空间。 超出部分计费：0.0122 元/GB/小时。 | 中国香港和新加坡定价。 |  |  |
| 安全审计（SecurityAudit） | 中国内地：0.48 元/GB。 中国香港和海外：0.72 元/GB。 | 可选，可单独开通关闭。 使用新版安全审计时，按日志量收取该费用。 |  |


政务云、金融云

- 

- 

- 

- 

- 

- 

| 计费项 | 计费方式 | 定价 | 说明 |
| --- | --- | --- | --- |
| 包年包月的费用 | 包年包月 | 80 元/实例/月 | 用于计费的实例数量指您在购买页配置的能够开启 DAS 专业版的数据库实例总数。 例如，当前账号能够开启 DAS 专业版的数据库实例总数为 3，已开启 DAS 专业版的数据库实例数量为 1，那么该账号 DAS 专业版包年包月的费用为 80 元/月×3=240 元/月 。 重要 仅企业版 V1 收取包年包月的费用。 |
| SQL 洞察的存储费用（sql_storage_used） | 按量计费 | 政务云：0.016 元/GB/小时 金融云：0.0152 元/GB/小时 | 无 |
| 安全审计（SecurityAudit） | 政务云：0.96 元/GB 金融云：0.96 元/GB | 可选，可单独开通关闭。 使用新版安全审计时，按日志量收取该费用。 |  |


经济版

| 计费项 | 计费方式 | 定价 | 说明 |
| --- | --- | --- | --- |
| 初级包 | 包年包月 | 53 元/月 | 最多支持接入 10 个数据库实例。 |
| 中级包 | 150 元/月 | 最多支持接入 50 个数据库实例。 |  |
| 高级包 | 300 元/月 | 支持接入的数据库实例数无上限。 |  |


基础版

不收费。

安全中心

- 

- 

- 

- 

| 计费项 | 计费对象 | 规格 | 定价 | 说明 |
| --- | --- | --- | --- | --- |
| 敏感识别 （DCG_Amount） | 数据库表数（X） | 0 万张<=Z<=5 万张 | 400 元/万张/月 | 识别任务中扫描表，每扫描一张消耗 1 配额，用完为止，不结转次月。 阶梯费用，量越大单价越低。 提示：敏感识别为您赠送 100 张表的免费配额，畅享安全体验。 |
| 6 万张<=Z<=10 万张 | 300 元/万张/月 |  |  |  |
| 11 万张<=Z<=50 万张 | 200 元/万张/月 |  |  |  |
| 51 万张<=Z<=9999999999999 万张 | 100 元/万张/月 |  |  |  |
| 列加密 (CLE_Amount) | 数据库列数（Y） | 5 | 2688 元/月 | 为识别后存在敏感数据的列加密，某列被加密时消耗 1 配额，取消加密后该配额恢复。 阶梯费用，量越大单价越低。 |
| 10 | 3688 元/月 |  |  |  |
| 15 | 4680 元/月 |  |  |  |
| 20 | 5688 元/月 |  |  |  |
| 25 | 6688 元/月 |  |  |  |
| 30 | 7680 元/月 |  |  |  |
| 35 | 8680 元/月 |  |  |  |
| 40 | 9688 元/月 |  |  |  |
| 45 | 10665 元/月 |  |  |  |
| 50 | 11688 元/月 |  |  |  |
| 50<N<=100 | 156.88 元/个/月 |  |  |  |
| 100<N<=200 | 88.44 元/个/月 |  |  |  |
| 200<N<=300 | 65.6 元/个/月 |  |  |  |
| 300<N<=400 | 54.22 元/个/月 |  |  |  |
| 400<N<=500 | 47.37 元/个/月 |  |  |  |
| 500<N<=600 | 42.81 元/个/月 |  |  |  |
| 600<N<=700 | 39.55 元/个/月 |  |  |  |
| 700<N<=800 | 37.11 元/个/月 |  |  |  |
| 800<N<=900 | 35.2 元/个/月 |  |  |  |
| 900<N<=1000 | 33.68 元/个/月 |  |  |  |
| 1000<N<=9999999999999 | 25 元/个/月 |  |  |  |


[上一篇：计费概览](products/rds/documents/product-overview/billing-overview.md)[下一篇：RDS节省计划](products/rds/documents/product-overview/savings-plans.md)

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
