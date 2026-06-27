## redis-cli
本示例在ECS（Linux）上使用redis-cli访问处于同一专有网络的云数据库 Tair（兼容 Redis）。
说明
本地连接请[申请公网连接地址](../user-guide/apply-for-a-public-endpoint-for-an-apsaradb-for-redis-instance.md)后使用公网地址连接。
登录ECS实例，依次执行以下命令，下载、安装编译redis-cli。
sudo yum -y install gcc # 安装gcc依赖环境 wget https://download.redis.io/releases/redis-7.2.0.tar.gz tar xzf redis-7.2.0.tar.gz cd redis-7.2.0&&make
本文以redis-7.2.0版本为例演示操作流程，您也可以安装其他版本。编译安装通常需要2分钟~3分钟。
执行下述命令连接实例。
src/redis-cli -hhostname-apassword-pport
参数说明：
hostname：实例连接地址，您可以在控制台的连接信息区域获取实例的专有网络连接地址，例如r-8vbwds91ie1rdl****.redis.zhangbei.rds.aliyuncs.com，更多信息请参见[查看连接地址](../user-guide/view-endpoints.md)。
password：密码。
port：端口号，默认为6379。
连接示例：
src/redis-cli -h r-8vbwds91ie1rdl****.redis.zhangbei.rds.aliyuncs.com -a TestPassword123 -p 6379
写入与读写数据。
执行命令SET bar foo。
预计返回OK。
执行命令GET bar。
预计返回"foo"。
