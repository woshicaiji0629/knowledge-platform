## 常见IP白名单设置错误案例
白名单与安全组 > 白名单设置中只有默认地址127.0.0.1。
该地址表示不允许任何设备访问RDS实例。因此需在白名单中添加对端的IP地址。
白名单设置为0.0.0.0。
正确格式为0.0.0.0/0。
重要
0.0.0.0/0表示允许任何设备访问RDS实例，请谨慎使用。
白名单中添加的设备公网IP地址并非设备真正的出口IP地址。
原因如下：
公网IP地址不固定，可能会变动。
IP地址查询工具或网站查询的公网IP地址不准确。
解决办法请参见[外网无法连接](../support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[RDS MySQL](../support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[或](../support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[MariaDB：如何正确填写本地设备的公网](../support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[IP](../support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[地址](../support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)。
