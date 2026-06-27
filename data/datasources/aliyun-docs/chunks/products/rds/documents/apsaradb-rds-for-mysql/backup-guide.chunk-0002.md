## 备份方式
常用的数据备份方式为逻辑备份、物理备份与快照备份，三者的主要区别如下：

| 维度 | 逻辑备份 | 物理备份 | 快照备份 |
| --- | --- | --- | --- |
| 备份粒度 | 数据库对象级（表、索引、存储过程等） | 数据库文件级（如 InnoDB 数据文件） | 云盘块级（整个实例存储卷） |
| 典型工具 | mysqldump | XtraBackup | 基于 ESSD 云盘快照服务 |
| 恢复精度 | 可恢复到单表/库，但不支持时间点恢复（除非结合 binlog） | 支持全量 + 日志备份 → 任意时间点恢复（秒级） | 支持时间点恢复（依赖日志备份） |
| 适用场景 | 跨版本迁移、单表恢复、导出到自建库 | 全量快速恢复、灾备、跨地域备份 | 极速恢复（RTO 最短）、业务连续性要求高的场景 |
| 相关操作 | [RDS MySQL](restore-the-data-of-an-apsaradb-rds-for-mysql-instance-from-a-logical-backup-file-to-a-self-managed-mysql-instance.md) [逻辑备份文件恢复到自建数据库](restore-the-data-of-an-apsaradb-rds-for-mysql-instance-from-a-logical-backup-file-to-a-self-managed-mysql-instance.md) | [RDS MySQL](restore-the-data-of-an-apsaradb-rds-for-mysql-instance-from-a-physical-backup-file-to-a-self-managed-mysql-database.md) [物理备份文件恢复到自建数据库](restore-the-data-of-an-apsaradb-rds-for-mysql-instance-from-a-physical-backup-file-to-a-self-managed-mysql-database.md) | [RDS MySQL](restore-the-data-of-an-apsaradb-rds-for-mysql-instance-to-a-self-managed-mysql-instance-by-using-a-csv-file-or-an-sql-file.md) [快照备份文件恢复到自建数据库](restore-the-data-of-an-apsaradb-rds-for-mysql-instance-to-a-self-managed-mysql-instance-by-using-a-csv-file-or-an-sql-file.md) |
