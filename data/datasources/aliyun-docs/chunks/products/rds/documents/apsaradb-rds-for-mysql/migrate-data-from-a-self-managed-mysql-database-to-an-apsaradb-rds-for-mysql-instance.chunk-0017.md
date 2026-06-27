### （如需增量迁移）配置源库Binlog
如果您需要使用增量迁移，源库Binlog需完成以下配置并重启MySQL使配置生效：
源库需开启本地Binlog日志，且Binlog日志需保留7天及以上。
源库binlog_format参数需设置为row，binlog_row_image参数需设置为full。
如果自建MySQL是双主集群（两者互为主从），为保障DTS能获取全部的Binlog日志，您需开启参数log_slave_updates。
您可以通过以下命令配置源库Binlog：
Linux命令
使用vim命令，修改配置文件my.cnf中的如下参数。
log_bin=mysql_bin binlog_format=row # MySQL 8.0以下版本通过expire_logs_days设置binlog保存时长，默认为0（永不过期） # MySQL 8.0以上版本通过binlog_expire_logs_seconds设置binlog保存时长，默认为2592000秒（30天） # 如果您修改过MySQL中Binlog保留时长且小于7天，可以通过以下参数重新设置Binlog保存时长为7天及以上 # expire_logs_days=7 # binlog_expire_logs_seconds=604800 # 建议设置为大于1的整数 server_id=2 # 当自建MySQL的版本大于5.6时，则必须设置该项。 binlog_row_image=full # 当自建数据库为双主集群时，需打开此参数 # log_slave_updates=ON
修改完成后，重启MySQL进程。
/etc/init.d/mysqld restart
Windows命令
修改配置文件my.ini中的如下参数。
log_bin=mysql_bin binlog_format=row # MySQL 8.0以下版本通过expire_logs_days设置binlog保存时长，默认为0（永不过期） # MySQL 8.0以上版本通过binlog_expire_logs_seconds设置binlog保存时长，默认为2592000秒（30天） # 如果您修改过MySQL中Binlog保留时长且小于7天，可以通过以下参数重新设置Binlog保存时长为7天及以上 # expire_logs_days=7 # binlog_expire_logs_seconds=604800 # 建议设置为大于1的整数 server_id=2 # 当自建MySQL的版本大于5.6时，则必须设置该项。 binlog_row_image=full # 当自建数据库为双主集群时，需打开此参数 # log_slave_updates=ON
修改完成后，重启MySQL服务。 您可以通过Windows中的服务管理器重启服
