## 方案一
此方案为直接转换引擎，最简单直接，但过程中会全程阻塞DML操作且大表转换时间比较久。
[通过](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[DMS](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[登录](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[RDS](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[数据库](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)。
在上方选择SQL操作>SQL窗口。
执行如下命令：
Alter table test.testfs engine innodb
