## 配额

| 配额 | 限制 |
| --- | --- |
| 只读实例 | PG 10 或以上版本才支持只读实例，且只读实例必须创建在与主实例相同的地域内。 高性能本地盘： 主实例最多创建 5 个只读实例。 规格必须大于 8 核 32 GB（独享套餐），才支持只读实例。 云盘： 主实例最多创建 32 个只读实例。 只读实例为单节点架构，没有备节点。 只读实例的更多信息，请参见 [PostgreSQL](../overview-of-read-only-apsaradb-rds-for-postgresql-instances.md) [只读实例简介](../overview-of-read-only-apsaradb-rds-for-postgresql-instances.md) 。 |
| 标签 | 标签键必须唯一，最大设置 20 个。每次最多设置 50 个实例进行批量标签绑定。创建标签，请参见 [创建标签](add-tags-to-apsaradb-rds-instances-1.md) 。 |
| 备份空间免费额度 | PostgreSQL 云盘实例仅支持快照备份，PostgreSQL 高性能本地盘实例仅支持物理备份。超出免费额度的部分 = 数据备份量 + 日志备份量 - 免费额度，单位为 GB，只入不舍。 高性能本地盘：物理备份空间的免费额度=50%×实例购买的存储空间。 云盘：快照备份空间的免费额度=200%×实例购买的存储空间。 备份的更多信息，请参见 [备份](back-up-an-apsaradb-rds-for-postgresql-instance.md) [PostgreSQL](back-up-an-apsaradb-rds-for-postgresql-instance.md) [数据](back-up-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 实例备份保留天数 | 默认为 7 天，最大 730 天。 |
| 错误日志保留天数 | 30 天。查看错误日志，请参见 [查看日志](view-the-logs-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 慢日志明细保留天数 | 30 天。查看慢日志明细，请参见 [查看日志](view-the-logs-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
