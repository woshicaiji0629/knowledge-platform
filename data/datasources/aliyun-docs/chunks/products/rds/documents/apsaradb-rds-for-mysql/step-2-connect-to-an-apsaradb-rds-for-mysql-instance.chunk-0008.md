# mysql连接命令模版 mysql -h 连接地址 -P 端口号 -u 用户名 -p # mysql连接命令示例 mysql -h rm-bp**************.mysql.rds.aliyuncs.com -P 3306 -u dbuser -p
填入连接地址。您需要根据自身情况判断是否符合内网访问条件，并填入对应的实例连接地址，本教程以内网连接地址为例。如何获取实例内外网连接地址请见[本文准备工作](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)。
填入端口号，本教程以3306端口为例。
填入用户名，本教程以高权限账号dbuser为例。
按下回车键，在Enter password中填入对应高权限账号密码，然后执行连接命令。
当您在命令行中看到如下信息时，说明已经成功连接RDS MySQL实例，您可以进行后续的数据库操作。连接成功后，终端将显示如下欢迎信息：
Welcome to the MySQL monitor. Commands end with ; or \g. Your MySQL connection id is 51325 Server version: 8.0.18 Source distribution
