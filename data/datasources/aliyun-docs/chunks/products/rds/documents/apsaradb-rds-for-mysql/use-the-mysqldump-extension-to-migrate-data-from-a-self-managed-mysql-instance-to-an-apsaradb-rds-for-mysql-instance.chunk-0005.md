就在ECS实例上，可跳过本步骤。
将导出的文件导入到目标RDS中，命令如下：
mysql -h <RDS实例连接地址> -P <RDS实例端口> -u <RDS实例账号> -p <RDS数据库名称> < /tmp/<自建数据库名>.sql mysql -h <RDS实例连接地址> -P <RDS实例端口> -u <RDS实例账号> -p <RDS数据库名称> < /tmp/<自建数据库名>Trigger.sql
说明
RDS数据库名称需要是RDS实例上已创建的数据库。创建数据库操作，请参见[管理数据库](create-a-database-for-an-apsaradb-rds-for-mysql-instance.md)。
RDS实例账号需要是高权限账号或具有读写权限的账号。
示例
mysql -h rm-bpxxxxx.mysql.rds.aliyuncs.com -P 3306 -u testuser -p testdb < /tmp/testdb.sql mysql -h rm-bpxxxxx.mysql.rds.aliyuncs.com -P 3306 -u testuser -p testdb < /tmp/testdbTrigger.sql
导入成功后[通过](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[DMS](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[登录](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[RDS](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[数据库](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)查看数据是否正常。
