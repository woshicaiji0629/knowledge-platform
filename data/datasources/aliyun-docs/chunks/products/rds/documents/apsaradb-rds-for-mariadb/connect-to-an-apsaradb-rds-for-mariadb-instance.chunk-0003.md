单击打开。
若连接信息无误，即会成功连接实例。
常见报错说明如下：
Unknown MySQL server hose 'xxxxxxxxx'(11001)
请检查主机名/IP地址是否填写正确，常见错误是填写为实例ID或IP地址。应该填写内网或外网连接地址。
Access denied for user 'xxxxx'@'xxxxx'(using password:YES)
请检查账号密码是否填写正确，常见错误为填写阿里云账号。应该填写实例的账号管理页面创建的账号。
响应很慢并返回Can't connect to MySQL server on 'rm-bp1xxxxxxxxxxxxxx.mysql.rds.aliyuncs.com'(10060)
请检查白名单是否设置正确，需要将该软件所在主机的对外公网IP填写在白名单中。如何设置白名单，请参见[设置白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mariadb-instance.md)。
说明
您可以临时设置白名单为0.0.0.0/0，用来排查是否是白名单设置问题导致的连接报错，如果确定是白名单设置问题，再定位正确的IP地址。具体操作，请参见[外网无法连接](../support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[RDS MySQL](../support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[或](../support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[MariaDB：如何正确填写本地设备的公网](../support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[IP](../support/why-am-i-un
