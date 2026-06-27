### 释放存储空间
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
单击左侧导航栏的监控与报警，查看实例各类数据占用的磁盘空间信息。
根据不同数据库类型，清理对应磁盘空间。
警告
数据无价，请您谨慎清理，如非必要，不推荐清理数据，请采用扩容存储空间方式解除锁定；如果必须清理，请在清理前对数据库进行备份，避免数据丢失。
临时文件（标准监控中对应temp_file_size）
产生原因：MySQL实例可能会由于查询语句的排序、分组、关联表产生的临时表文件，或者大事务未提交前产生的binlog cache文件，导致实例磁盘空间满。
解决方法：请参见[RDS MySQL](../support/what-do-i-do-if-an-apsaradb-rds-for-mysql-instance-is-in-the-locked-state-because-its-storage-capacity-is-exhausted-by-temporary-files.md)[临时文件导致实例磁盘空间满且出现“锁定中”状态](../support/what-do-i-do-if-an-apsaradb-rds-for-mysql-instance-is-in-the-locked-state-because-its-storage-capacity-is-exhausted-by-temporary-files.md)。
日志文件（标准监控中对应binlog_size和general_log_size）
产生原因：数据库管理系统会生成查询日志、慢查询日志、错误日志等，帮助管理员监控数据库的性能和健康状况。
