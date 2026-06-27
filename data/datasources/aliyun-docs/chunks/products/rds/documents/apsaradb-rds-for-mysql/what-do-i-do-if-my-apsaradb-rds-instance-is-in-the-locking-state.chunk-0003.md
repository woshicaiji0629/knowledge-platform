-because-its-storage-capacity-is-exhausted-by-temporary-files.md)。
日志文件（标准监控中对应binlog_size和general_log_size）
产生原因：数据库管理系统会生成查询日志、慢查询日志、错误日志等，帮助管理员监控数据库的性能和健康状况。

| 引擎 | 处理办法 |
| --- | --- |
| MySQL | 根据 监控与报警 中，磁盘空间的占用信息，清理对应的日志文件。 [MySQL Binlog](what-do-i-do-if-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-is-exhausted-by-binary-log-files.md) [文件导致实例空间满的解决办法](what-do-i-do-if-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-is-exhausted-by-binary-log-files.md) [General log](handle-the-issue-that-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-is-exhausted-by-the-general-log-file.md) [导致实例空间满的解决办法](handle-the-issue-that-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-is-exhausted-by-the-general-log-file.md) |
| PostgreSQL | RDS PostgreSQL 日志文件不支持手动删除。 您可以通过手动删除非活跃的 Replication Slot 来让 RDS PostgreSQL 内核自动清理 WAL 日志。具体方法，请参见 [WAL](../apsaradb-rds-for-postgresql/use-the-wal-log-management-feature-for-an-apsaradb-rds-for-postgresql-instance.md) [日志管理](../apsaradb-rds-for-postgresql/use-the-wal-log-management-feature-for-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| SQL Server | RDS SQL Server 日志文件不支持手动删除，但可以通过控制台 [收缩事务日志](../apsaradb-rds-for-sql-server/troubleshoot-insufficient-storage-space-issues-on-an-apsaradb-rds-for-sql-server-instance.md) 。 |
