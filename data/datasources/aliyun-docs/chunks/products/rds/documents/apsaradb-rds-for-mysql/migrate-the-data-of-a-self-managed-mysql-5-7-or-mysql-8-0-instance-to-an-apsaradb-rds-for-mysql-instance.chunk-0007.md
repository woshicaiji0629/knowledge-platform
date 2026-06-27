/mysql-backup-helper)获取最新版的源码包。
解压MySQL Backup Helper源码包。
unzip master.zip
进入mysql-backup-helper-master文件夹，对main.go文件进行编译，获得backup_helper可执行文件。
cd mysql-backup-helper-master go build -a -o backup_helper main.go
说明
如无法正常完成编译，请参见[附录](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[4：设置](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[Go](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[代理](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)。
进入oss_stream文件夹，对oss_stream.go文件进行编译，获得oss_stream可执行文件。
cd oss_stream go build -a -o oss_stream oss_stream.go
说明
如无法正常完成编译，请参见[附录](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[4：设置](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[Go](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[代理](migrate-the-data-of-a-self-managed-mysql-5-7-
