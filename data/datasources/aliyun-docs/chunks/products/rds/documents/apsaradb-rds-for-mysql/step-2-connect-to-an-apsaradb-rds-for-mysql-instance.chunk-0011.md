itelist-for-an-apsaradb-rds-for-mysql-instance.md)。
（少数情况）不满足内网互通的条件（ECS与RDS处于同一个专有网络VPC），却使用内网地址连接，[请获取外网地址并使用外网地址连接](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)。
Your connection attempt failed for user 'xx" to the MySQL server
（多数情况）RDS白名单设置错误，请参见[设置](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[IP](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)。
（少数情况）不满足内网互通的条件（ECS与RDS处于同一个专有网络VPC），却使用内网地址连接，[请获取外网地址并使用外网地址连接](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)。
ping RDS内网地址时，报错Destination Host Unreachable
路由冲突。参考[无法](../support/destination-host-unreachable.md)[ping](../support/destination-host-unreachable.md)[通](../support/destination-host-unreachable.md)[RDS](../support/destination-host-unreachable.md)[内网地址处理方法](../support/destination-host-unreachable.md)解决。
Access denied for user 'xxx'@'xxx'(using password:YES)
输入的账号密码错误。可以在RDS控制台账号管理页面管理账号和密码。
Unknown MySQL server host 'xxx'(11001)
输入的RDS实例地址错误。正确格式为rm-xxxxxx.mysql.rds.aliyuncs.com。
