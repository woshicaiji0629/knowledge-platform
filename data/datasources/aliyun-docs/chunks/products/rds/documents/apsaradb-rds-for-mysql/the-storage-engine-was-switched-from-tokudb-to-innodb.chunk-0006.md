| --postpone-cut-over-flag-file | 切换文件。指定时间删除此文件立刻进行表切换。 |
| --panic-flag-file | 生成此文件，ghost 进程立刻停止。 |
| --serve-socket-file | 用于接收交互命令。 |
| --execute | 直接执行。 |

前提条件
已在本地主机或ECS安装gh-ost。
已在RDS实例的IP白名单中添加本地主机或ECS的IP。
操作步骤
在本地主机或ECS上执行如下命令进行转换，等待转换完成。
gh-ost --user="test01" --password="Test123456" --host="rm-bpxxxxx.mysql.rds.aliyuncs.com" --database="test" --table="testfs" --alter="engine=innodb" --initially-drop-old-table --initially-drop-ghost-table --aliyun-rds --assume-rbr --allow-on-master --assume-master-host="rm-bpxxxxx.mysql.rds.aliyuncs.com" --chunk-size=500 --postpone-cut-over-flag-file="/tmp/ghostpost.postpone" --panic-flag-file="/tmp/stop.flag" --serve-socket-file="/tmp/ghost.sock" --execute
[通过](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[DMS](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[登录](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[RDS](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[数据库](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)。
在左侧查看表，会发现存在以_gho、_ghc结尾的临时表。
执行rm /tmp/ghostpost.postpone命令开始切换表。结果如下。
说明
请忽略显示的error（错误），实际已经切换完成。
检查表并验证数据。
说明
验证数据没有问题后删除_del表即可。
