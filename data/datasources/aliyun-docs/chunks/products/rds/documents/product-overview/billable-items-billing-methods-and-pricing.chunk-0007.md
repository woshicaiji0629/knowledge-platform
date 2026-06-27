### 高性能云盘IO性能突发

| 类别 | 说明 |
| --- | --- |
| 定义 | RDS 高性能云盘实例的 IO 性能突发量的费用。开启高性能云盘 IO 性能突发不收费。但开启后，如果 IO 性能突发量超过免费额度，会产生 IO 性能突发（io_burst） 的费用。 功能详情，请参见 [MySQL IO](../apsaradb-rds-for-mysql/i-o-performance-burst.md) [性能突发](../apsaradb-rds-for-mysql/i-o-performance-burst.md) 、 [PostgreSQL IO](../apsaradb-rds-for-postgresql/io-performance-burst.md) [性能突发](../apsaradb-rds-for-postgresql/io-performance-burst.md) 或 [SQL Server IO](../apsaradb-rds-for-sql-server/i-o-performance-burst-for-premium-essds.md) [性能突发](../apsaradb-rds-for-sql-server/i-o-performance-burst-for-premium-essds.md) 。 |
| 计费公式 | 高性能云盘 IO 性能突发费用=（实例各节点 IO 性能突发量总和-免费额度）* IO 性能突发单价 * 时长 说明 实例各节点 IO 性能突发量总和、免费额度、IO 性能突发单价请参见 [MySQL IO](../apsaradb-rds-for-mysql/i-o-performance-burst.md) [性能突发计费说明](../apsaradb-rds-for-mysql/i-o-performance-burst.md) 、 [PostgreSQL IO](../apsaradb-rds-for-postgresql/io-performance-burst.md) [性能突发计费说明](../apsaradb-rds-for-postgresql/io-performance-burst.md) 、 [SQL Server IO](../apsaradb-rds-for-sql-server/i-o-performance-burst-for-premium-essds.md) [性能突发计费说明](../apsaradb-rds-for-sql-server/i-o-performance-burst-for-premium-essds.md) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | 不支持。 |
