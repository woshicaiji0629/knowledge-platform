### 已删除实例备份空间

| 类别 | 说明 |
| --- | --- |
| 定义 | RDS MySQL 已删除实例的备份集存储费用。7 天内存储免费，超过 7 天将按备份集大小和存储时长计费。具体计费项名称如下。 RDS MySQL 高性能本地盘： 标准型存储容量（StandardStorageSize） RDS MySQL 云盘： 云数据库备份存储容量（BackupStorageSize） 功能详情，请参见 [设置实例释放后备份保留策略](../apsaradb-rds-for-mysql/configure-backup-retention-policies-for-released-instances.md) 。 |
| 账单产品 | 数据库备份。 |
| 计费公式 | 已删除实例的备份存储空间费用=已删除实例备份存储单价 * 已删除实例的备份大小 * 使用时长 说明 已删除实例备份存储单价，请参见 [费用说明](../apsaradb-rds-for-mysql/retain-the-backup-files-of-an-apsaradb-rds-for-mysql-instance-for-a-long-period-of-time.md) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | [DBS](https://help.aliyun.com/zh/dbs/getting-started/use-storage-plans#multiTask382) [云数据库备份存储包](https://help.aliyun.com/zh/dbs/getting-started/use-storage-plans#multiTask382) 可以抵扣 包年包月或按量付费 RDS MySQL 云盘 实例的 云数据库备份存储容量（BackupStorageSize） 费用。 |
