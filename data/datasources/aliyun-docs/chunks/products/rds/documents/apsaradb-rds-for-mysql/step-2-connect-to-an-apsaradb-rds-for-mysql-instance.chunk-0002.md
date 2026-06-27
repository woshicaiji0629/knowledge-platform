## 准备工作
您需要先购买RDS MySQL实例，在实例中创建MySQL数据库和对应的高权限账号，详细教程请参见[第一步：创建](step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[RDS MySQL](step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[实例与配置数据库](step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)。
重要
本教程中所使用的RDS MySQL实例、数据库、账号及密码等均来自教程[第一步：创建](step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[RDS MySQL](step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[实例与配置数据库](step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)中通过控制台方式创建与配置，您也可以根据自身需求进行修改。
如果您准备通过DMS登录数据库，则无需后续的准备工作，可以直接按步骤完成登录操作。
如果您准备通过命令行或客户端登录数据库，则需要预先为实例设置IP白名单，并根据访问类型获取实例对应的内网连接地址或外网连接地址，详细操作如下：
设置IP白名单与获取实例内外网访问地址
1. 设置IP白名单
您需要将您的IP地址或应用服务器的IP地址[写入](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[实例的](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[IP](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[白名单](configure-an-ip-address-whitelist-for-an-apsaradb
