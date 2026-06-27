### 操作步骤
使用客户端工具[登录目标](connect-to-an-apsaradb-rds-for-mariadb-instance.md)[MariaDB](connect-to-an-apsaradb-rds-for-mariadb-instance.md)[实例](connect-to-an-apsaradb-rds-for-mariadb-instance.md)，创建空数据库。在目标 RDS MariaDB 实例的数据库管理工具（如 MySQL-Front）中，执行 SQL 语句create database test001;创建目标数据库test001。创建成功后，可在左侧数据库对象树中看到test001节点。
在CentOS 7使用自带的mysqldump工具将源MariaDB实例的数据库导出为数据文件。
mysqldump -h <源实例外网地址> -P <源实例端口> -u <源实例高权限账号> -p<源实例高权限账号密码> --opt --default-character-set=utf8 --hex-blob <要迁移的数据库名称> --skip-triggers > /tmp/<要迁移的数据库名称>.sql
示例
mysqldump -h rm-xxx.mariadb.rds.aliyuncs.com -P 3306 -u test -pTestxxx --opt --default-character-set=utf8 --hex-blob testdb --skip-triggers > /tmp/testdb.sql
重要
导出期间请勿进行数据更新。本步骤仅导出数据，不包括存储过程、触发器及函数。
使用mysqldump导出存储过程、触发器和函数。
mysqldump -h <源实例外网地址> -P <源实例端口> -u <源实例高权限账号> -p<源实例高权限账号密码> --opt --default-character-set=utf8 --hex-blob <要迁移的数据库名称> -R > /tmp/<要迁移的数据库名称>trigger.sql
示例如下：
mysqldump -h rm-xxx.mariadb.rds.aliyuncs.com -P 3306 -u test -pTestxxx --opt --default-character-set=utf8 --hex-blob testdb -R > /tmp/testdbtrigger.sql
说明
若数据库中没有使用存储过程、触发器和函数，可跳过此步骤。
通过如下命令将数据文件、存储过程、触发器和函数导入目标RDS MariaDB实例中。
mysql -h <目的实例外网地址> -P <目的实例端口> -u <目的实例高权限账号> -p<目的实例高权
