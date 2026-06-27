## 方法三：通过客户端连接RDS MySQL实例
如果您不熟悉复杂的服务器命令，也可以通过通用的第三方客户端连接RDS MySQL实例。本教程以MySQL Workbench 8.0.29版本为例，向您详细展示如何通过客户端连接RDS MySQL实例。
重要
使用客户端方式连接实例需要[提前设置实例](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)[IP](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)[白名单并根据自身需求获取对应实例连接地址](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)。
您需要提前下载并安装[MySQL Workbench 8.0.29](https://downloads.mysql.com/archives/workbench/)[版本客户端](https://downloads.mysql.com/archives/workbench/)。
打开MySQL Workbench，选择Database > Connect to Database。
在Connect to Database页面，填入所需的地址与账号信息。
选择Connection Method，本教程以Standard(TCP/IP)为例。
填写Hostname。您需要根据自身情况判断是否符合内网访问条件，并填入对应的[实例连接地址](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)，本教程以内网连接地址为例。
填写Port，本教程端口号以3306为例。
填写Username，本教程以高权限账号dbuser为例。
填写Password，您需要自定义密码。
单击确定连接至RDS MySQL实例，后续您可以进行相应的数据库操作。
