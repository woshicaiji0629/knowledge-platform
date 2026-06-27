-R > /tmp/testdbtrigger.sql
说明
若数据库中没有使用存储过程、触发器和函数，可跳过此步骤。
通过如下命令将数据文件、存储过程、触发器和函数导入目标RDS MariaDB实例中。
mysql -h <目的实例外网地址> -P <目的实例端口> -u <目的实例高权限账号> -p<目的实例高权限账号密码> <目的实例数据库名称> < /tmp/<要迁移的数据库名称>.sql mysql -h <目的实例外网地址> -P <目的实例端口> -u <目的实例高权限账号> -p<目的实例高权限账号密码> <目的实例数据库名称> < /tmp/<要迁移的数据库名称>trigger.sql
示例如下：
mysql -h rm-xxx.mariadb.rds.aliyuncs.com -P 3306 -u test2 -pTest2xxx test001 < /tmp/testdb.sql mysql -h rm-xxx.mariadb.rds.aliyuncs.com -P 3306 -u test2 -pTest2xxx test001 < /tmp/testdbtrigger.sql
该文章对您有帮助吗？
反馈
