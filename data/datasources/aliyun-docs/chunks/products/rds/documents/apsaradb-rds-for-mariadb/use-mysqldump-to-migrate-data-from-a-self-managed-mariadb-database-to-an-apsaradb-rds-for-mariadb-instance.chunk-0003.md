testdb -R | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' > /tmp/testdb_trigger.sql
说明
若数据库中没有使用存储过程、触发器和函数，可跳过此步骤。在导出存储过程、触发器和函数时，需要将definer去掉，以兼容RDS。
通过如下命令将数据文件和存储过程文件导入到目标RDS MariaDB实例中。
mysql -h <RDS实例外网地址> -P <RDS实例外网端口> -u <RDS实例高权限账号> -p <RDS上数据库名> < /tmp/<想要迁移的数据库名>.sql mysql -h <RDS实例外网地址> -P <RDS实例外网端口> -u <RDS实例高权限账号> -p <RDS上数据库名> < /tmp/<想要迁移的数据库名>trigger.sql
示例
mysql -h rm-bpxxxxx.mariadb.rds.aliyuncs.com -P 3306 -u testuser -p test001 < /tmp/testdb.sql mysql -h rm-bpxxxxx.mariadb.rds.aliyuncs.com -P 3306 -u testuser -p test001 < /tmp/testdb_trigger.sql
刷新远程工具后查看表，已经有了数据，说明已经迁移成功。
该文章对您有帮助吗？
反馈
