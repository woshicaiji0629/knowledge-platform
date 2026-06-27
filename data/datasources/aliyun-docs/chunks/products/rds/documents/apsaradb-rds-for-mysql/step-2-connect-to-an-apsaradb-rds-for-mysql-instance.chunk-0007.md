## 方法二：通过命令行连接RDS MySQL实例
如果您偏向于使用服务器命令操作数据库，希望从阿里云ECS实例或本地服务器连接数据库，您可以通过命令行的方式连接RDS MySQL实例。本教程以Linux系统为例，向您展示如何使用命令行连接实例。
重要
使用命令行方式连接需要[提前设置实例](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)[IP](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)[白名单并根据自身需求获取对应实例连接地址](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)。
您需要提前在应用服务器中安装MySQL，不同版本Linux系统安装命令如下：
CentOS安装MySQL命令
sudo yum install mysql
Ubuntu安装MySQL命令
sudo apt-get update sudo apt install mysql-server
登录到需要连接RDS实例的应用服务器。您可以从本地服务器连接，也可以[登录阿里云](../../../ecs/documents/getting-started/create-and-manage-an-ecs-instance-by-using-the-ecs-console.md)[ECS](../../../ecs/documents/getting-started/create-and-manage-an-ecs-instance-by-using-the-ecs-console.md)[实例](../../../ecs/documents/getting-started/create-and-manage-an-ecs-instance-by-using-the-ecs-console.md)进行连接。
执行数据库连接命令，输入密码后访问RDS MySQL实例。数据库连接命令如下所示，其中-h表示需要输入RDS实例连接地址，-P表示需要输入RDS实例端口号，-u表示需要输入用户名，-p表示执行命令后需要输入密码。
