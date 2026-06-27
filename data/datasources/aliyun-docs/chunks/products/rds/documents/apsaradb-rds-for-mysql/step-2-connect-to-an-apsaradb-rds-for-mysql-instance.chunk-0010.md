## 常见报错
mysql command not found
原因是未安装MySQL。可按照如下方法快速安装：
CentOS：执行sudo yum install mysql。
Ubuntu：执行sudo apt-get update，并执行sudo apt install mysql-server。
SSL connection error: SSL is required but the server doesn't support it
使用部分版本MySQL Workbench时，Standard TCP/IP连接要求必须有SSL加密，可下载本教程中的版本（MySQL Workbench 8.0.29）进行常规连接。
错误码10060：Can't connect to MySQL server on 'rm-bpxxx.mysql.rds.aliyuncs.com'(10060)
（多数情况）RDS白名单设置错误，请参见[设置](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[IP](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)。
（少数情况）不满足内网互通的条件（ECS与RDS处于同一个专有网络VPC），却使用内网地址连接，[请获取外网地址并使用外网地址连接](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)。
Cannot Connect to Database Server
（多数情况）RDS白名单设置错误，请参见[设置](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[IP](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)。
（少数情况）不满足内网互通的条件（ECS与RDS处于同一个专有网络VPC），却使用内网地址连接，[请获取外网地址并使用外网地址连接](step-2-connect-to-an-apsaradb-rds-for-mys
