建议设置为大于1的整数 server_id=2 # 当自建MySQL的版本大于5.6时，则必须设置该项。 binlog_row_image=full # 当自建数据库为双主集群时，需打开此参数 # log_slave_updates=ON
修改完成后，重启MySQL服务。 您可以通过Windows中的服务管理器重启服务，或使用如下命令重启服务：
net stop mysql net start mysql
