## 操作步骤
使用远程工具[登录](connect-to-an-apsaradb-rds-for-mariadb-instance.md)[RDS MariaDB](connect-to-an-apsaradb-rds-for-mariadb-instance.md)[实例](connect-to-an-apsaradb-rds-for-mariadb-instance.md)，创建空数据库（例如test001）。在 MySQL-Front 工具中连接 MariaDB 实例，在SQL编辑器中执行create database test001;创建目标数据库，执行成功后左侧数据库列表中出现test001数据库。
登录本地Linux服务器，使用自带的mysqldump工具将本地数据库数据导出为数据文件。
mysqldump -h localhost -u <本地数据库用户名> -p --opt --default-character-set=utf8 --hex-blob <想要迁移的数据库名> --skip-triggers > /tmp/<想要迁移的数据库名>.sql
示例
说明
下文中的user用户需要具备相关权限，权限设置的详细操作，请参见[权限设置](https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html)。
mysqldump -h localhost -u user -p --opt --default-character-set=utf8 --hex-blob testdb --skip-triggers > /tmp/testdb.sql
重要
导出期间请勿进行数据更新。本步骤仅仅导出数据，不包括存储过程、触发器及函数。
使用mysqldump导出存储过程、触发器和函数。
mysqldump -h localhost -u <本地数据库用户名> -p --opt --default-character-set=utf8 --hex-blob <想要迁移的数据库名> -R | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' > /tmp/<想要迁移的数据库名>_trigger.sql
示例
mysqldump -h localhost -u user -p --opt --default-character-set=utf8 --hex-blob testdb -R | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' > /tmp/testdb_trigger.sql
说明
若数据库中没有使用存储过程、触发器和函数，可跳过此步骤。在导出存储过程、触发器和函数时，需要将definer去掉，以兼容RDS。
通过如下命令将数据文件和存储过
