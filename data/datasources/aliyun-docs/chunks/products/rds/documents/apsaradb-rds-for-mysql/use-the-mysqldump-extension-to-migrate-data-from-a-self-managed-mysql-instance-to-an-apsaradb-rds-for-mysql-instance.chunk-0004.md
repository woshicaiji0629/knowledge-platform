## 操作步骤
本文以Linux系统为例。在macOS的终端或者Windows的命令提示符下也可执行mysqldump命令。
使用mysqldump导出自建数据库的数据、存储过程、触发器和函数。
重要
导出期间请勿进行数据更新，耐心等待导出完成。
下文中的user用户需要具备本文介绍的操作的相关权限。权限设置的详细操作，请参见[权限设置](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)。
在Linux命令行下导出自建数据库的数据，命令如下：
mysqldump -h 127.0.0.1 -u user -p --opt --default-character-set=utf8 --hex-blob <自建数据库名> --skip-triggers --skip-lock-tables > /tmp/<自建数据库名>.sql
说明
如果需要使用mysqldump导出RDS MySQL数据库的数据，请将命令中的连接地址、账号、密码及数据库名替换为RDS MySQL实例的信息。
示例
mysqldump -h 127.0.0.1 -u user -p --opt --default-character-set=utf8 --hex-blob testdb --skip-triggers --skip-lock-tables > /tmp/testdb.sql
在Linux命令行下导出存储过程、触发器和函数，命令如下：
mysqldump -h 127.0.0.1 -u user -p --opt --default-character-set=utf8 --hex-blob <自建数据库名> -R | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' > /tmp/<自建数据库名>Trigger.sql
示例
mysqldump -h 127.0.0.1 -u user -p --opt --default-character-set=utf8 --hex-blob testdb -R | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' > /tmp/testdbTrigger.sql
说明
若数据库中没有使用存储过程、触发器和函数，可跳过此步骤。
将导出的两个文件上传到ECS实例上，本例路径为/tmp。
说明
如果自建数据库原本就在ECS实例上，可跳过本步骤。
将导出的文件导入到目标RDS中，命令如下：
mysql -h <RDS实例连接地址> -P <RDS实例端口> -u <RDS实例账号> -p <RDS数据库名称> < /tmp/<自建数据库名>.sql mysql -h <RDS实例连接地址> -P <RDS实例端口> -u <RD
