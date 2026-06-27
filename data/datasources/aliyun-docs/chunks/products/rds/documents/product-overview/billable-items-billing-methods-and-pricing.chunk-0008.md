### 高性能云盘数据归档

| 类别 | 说明 |
| --- | --- |
| 定义 | 开启数据归档不收费。但开启后，归档至 OSS 的数据会产生 OSS 存储空间（rds_oss_storage） 的费用。 功能详情，请参见 [MySQL](../apsaradb-rds-for-mysql/rds-mysql-data-archiving-function.md) [数据归档](../apsaradb-rds-for-mysql/rds-mysql-data-archiving-function.md) 、 [PostgreSQL](../apsaradb-rds-for-postgresql/data-archiving.md) [数据归档](../apsaradb-rds-for-postgresql/data-archiving.md) 或 [SQL Server](../apsaradb-rds-for-sql-server/archive-data-to-an-oss-bucket.md) [数据归档](../apsaradb-rds-for-sql-server/archive-data-to-an-oss-bucket.md) 。 说明 RDS SQL Server 同时支持 ESSD 云盘数据归档功能，高性能云盘数据归档功能需手动开启，ESSD 云盘数据归档功能默认处于开启状态。 |
| 计费公式 | 高性能 云盘数据归档费用=归档数据量 * 数据归档单价 * 时长 说明 数据归档单价，请参见 [MySQL](../apsaradb-rds-for-mysql/i-o-performance-burst.md) [数据归档计费说明](../apsaradb-rds-for-mysql/i-o-performance-burst.md) 、 [PostgreSQL](../apsaradb-rds-for-postgresql/data-archiving.md) [数据归档计费说明](../apsaradb-rds-for-postgresql/data-archiving.md) 、 [SQL Server](../apsaradb-rds-for-sql-server/archive-data-to-an-oss-bucket.md) [数据归档计费说明](../apsaradb-rds-for-sql-server/archive-data-to-an-oss-bucket.md) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | 不支持。 |
