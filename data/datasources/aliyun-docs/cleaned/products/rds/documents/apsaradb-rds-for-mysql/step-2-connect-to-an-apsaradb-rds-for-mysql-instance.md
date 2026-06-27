# 入门第二步：连接RDS MySQL实例-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/step-2-connect-to-an-apsaradb-rds-for-mysql-instance

# 第二步：连接RDS MySQL实例
在创建RDS MySQL实例与数据库后，您需要手动连接至RDS MySQL实例管理数据或将应用服务器连接至数据库进行业务部署。本教程详细展示了如何通过DMS（数据管理服务）直接登录至MySQL数据库，或通过命令行与客户端远程连接至数据库，方便您根据自身的需求与偏好选择合适的连接与登录方式。
## 费用说明
创建RDS MySQL实例会产生[实例规格费用与存储费用](billable-items-billing-methods-and-pricing.md)，其与实例的付费方式、系列、规格、存储类型和存储空间大小等参数相关。
本教程所述费用不包含用于连接RDS实例的应用服务器和第三方客户端费用。
## 准备工作
您需要先购买RDS MySQL实例，在实例中创建MySQL数据库和对应的高权限账号，详细教程请参见[第一步：创建](step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[RDS MySQL](step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[实例与配置数据库](step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)。
重要
本教程中所使用的RDS MySQL实例、数据库、账号及密码等均来自教程[第一步：创建](step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[RDS MySQL](step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[实例与配置数据库](step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)中通过控制台方式创建与配置，您也可以根据自身需求进行修改。
如果您准备通过DMS登录数据库，则无需后续的准备工作，可以直接按步骤完成登录操作。
如果您准备通过命令行或客户端登录数据库，则需要预先为实例设置IP白名单，并根据访问类型获取实例对应的内网连接地址或外网连接地址，详细操作如下：
设置IP白名单与获取实例内外网访问地址
1. 设置IP白名单
您需要将您的IP地址或应用服务器的IP地址[写入](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[实例的](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[IP](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)后才能正常访问实例。设置IP白名单后才能进行后续获取内网或外网连接地址的操作。
2. 选择合适的访问类型
访问类型分为内网访问和外网访问，如果您符合内网访问条件，您需要使用实例的内网连接地址进行远程连接；如果您不符合内网访问条件或使用本地设备访问RDS MySQL实例，则需要使用实例的外网连接地址进行远程连接。内网访问条件与获取内外网连接地址的方法如下：
重要
如您需要通过内网访问实例，则需满足以下条件：
使用阿里云服务器访问，且服务器与RDS实例同一地域、同一VPC。
如果服务器与实例的网络类型均为专有网络，则专有网络ID也需要相同。
| 场景 | 需获取的 RDS 实例地址 | 如何获取 |
| --- | --- | --- |
| 满足内网访问条件 | RDS 内网地址 | 访问 [RDS](https://rdsnext.console.aliyun.com/rdsList/basic) [实例列表](https://rdsnext.console.aliyun.com/rdsList/basic) ，在上方选择地域，然后单击目标实例 ID。 单击 查看连接详情 ，即可查看 RDS 实例地址和端口号。在 基本信息 区域，单击 网络类型 右侧的 查看连接详情 。 说明 需要点击 申请外网地址 ，才会显示外网连接地址。 对于集群系列实例，修改主节点地址需要在 集群读写连接 区域操作，修改备节点地址需要在 集群可读连接 区域操作。 |
| 从 ECS 实例访问 RDS 实例，但不满足内网访问条件 | RDS 外网地址 |  |
| 从本地设备访问 RDS 实例 |  |  |
## 方法一：通过DMS登录RDS MySQL实例
[数据管理](https://help.aliyun.com/zh/dms/product-overview/what-is-dms)[DMS](https://help.aliyun.com/zh/dms/product-overview/what-is-dms)（Data Management）是一款支撑数据全生命周期的一站式数据管理平台，其提供全域数据资产管理、数据治理、数据库设计开发、数据集成、数据开发和数据消费等功能，同时DMS内置的数据灾备还提供了低成本高可靠的备份恢复能力，致力于帮助企业高效、安全地挖掘数据价值，助力企业数字化转型。
您可以使用DMS快速便捷地登录RDS MySQL实例进行数据的管理与使用，无需关注实例IP白名单的设置与实例访问类型的选择。
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
单击登录数据库进入DMS登录页面。
在登录实例弹窗中，填写登录信息，并单击登录。
选择访问方式，本教程以账号+密码登录为例。
若选择KMS凭证登录方式，请参见[数据管理](../../../kms/documents/key-management-service/user-guide/integrate-apsaradb-rds-secrets-into-dms.md)[DMS](../../../kms/documents/key-management-service/user-guide/integrate-apsaradb-rds-secrets-into-dms.md)[集成](../../../kms/documents/key-management-service/user-guide/integrate-apsaradb-rds-secrets-into-dms.md)[RDS](../../../kms/documents/key-management-service/user-guide/integrate-apsaradb-rds-secrets-into-dms.md)[凭据](../../../kms/documents/key-management-service/user-guide/integrate-apsaradb-rds-secrets-into-dms.md)。
填写数据库账号与数据库密码，本教程以高权限账号dbuser和用户自定义密码为例。
选择管控模式。本教程以自由操作 永久免费为例。
说明
稳定变更与安全协同[收费](https://help.aliyun.com/zh/dms/product-overview/pricing)。
相比于自由操作 永久免费的[管控模式](https://help.aliyun.com/zh/dms/product-overview/control-modes)，稳定变更与安全协同提供更多的功能支持和更强的数据库管控能力，如果您是试用或体验RDS MySQL产品，建议您选择自由操作模式。
查看数据库。登录成功后您可以在DMS页面左侧的已登录实例中查看新创建的数据库，本教程以db_test1数据库为例，您也可以双击其它数据库进行切换。
说明
information_schema、MySQL、performance_schema、sys、回收站均为系统库。
如果实例存在，但实例展开后未找到目标数据库，可能是：
登录账号无目标数据库的访问权限：您可前往RDS实例详情页的账号管理页面手动[调整账号权限](modify-the-permissions-of-a-standard-account-on-an-apsaradb-rds-for-mysql-instance.md)。
元数据未同步导致目录无法显示：请将鼠标悬浮在目标数据库所属实例上，单击实例名右侧的按钮，即可刷新数据库列表，显示目标数据库。
如需快速同步数据库的库表结构，可以通过DMS[空库初始化](https://help.aliyun.com/zh/dms/initialize-empty-databases)功能实现。
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
# mysql连接命令模版 mysql -h 连接地址 -P 端口号 -u 用户名 -p # mysql连接命令示例 mysql -h rm-bp**************.mysql.rds.aliyuncs.com -P 3306 -u dbuser -p
填入连接地址。您需要根据自身情况判断是否符合内网访问条件，并填入对应的实例连接地址，本教程以内网连接地址为例。如何获取实例内外网连接地址请见[本文准备工作](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)。
填入端口号，本教程以3306端口为例。
填入用户名，本教程以高权限账号dbuser为例。
按下回车键，在Enter password中填入对应高权限账号密码，然后执行连接命令。
当您在命令行中看到如下信息时，说明已经成功连接RDS MySQL实例，您可以进行后续的数据库操作。连接成功后，终端将显示如下欢迎信息：
Welcome to the MySQL monitor. Commands end with ; or \g. Your MySQL connection id is 51325 Server version: 8.0.18 Source distribution
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
## 常见问题
Q：我使用函数计算，想获取RDS的数据，要怎么操作呢？
A：您可以为函数安装第三方依赖，使用内置模块获取RDS数据，详情请参见[为函数安装第三方依赖](https://help.aliyun.com/zh/functioncompute/fc-2-0/user-guide/install-third-party-dependencies-on-function-compute)。
Q：连接数据库后，如何导入SQL文件？
A：当需要将大批量数据以附件（SQL、CSV、Excel）形式快速导入数据库时，可以使用[DMS](https://help.aliyun.com/zh/dms/import-data)[的数据导入功能](https://help.aliyun.com/zh/dms/import-data)。
## 相关文档
ECS实例连接RDS实例：[ECS（Linux）连接](../videos/connect-an-ecs-instance-running-linux-to-an-rds-instance.md)[RDS](../videos/connect-an-ecs-instance-running-linux-to-an-rds-instance.md)
数据库连接失败：[解决无法连接实例问题](../support/what-do-i-do-if-i-fail-to-connect-to-an-apsaradb-rds-instance.md)
连接其他引擎的实例：
[连接](../connect-to-sql-server-instance.md)[SQL Server](../connect-to-sql-server-instance.md)[实例](../connect-to-sql-server-instance.md)
[连接](../apsaradb-rds-for-postgresql/connect-to-an-apsaradb-rds-for-postgresql-instance-1.md)[PostgreSQL](../apsaradb-rds-for-postgresql/connect-to-an-apsaradb-rds-for-postgresql-instance-1.md)[实例](../apsaradb-rds-for-postgresql/connect-to-an-apsaradb-rds-for-postgresql-instance-1.md)
[连接](../apsaradb-rds-for-mariadb/connect-to-an-apsaradb-rds-for-mariadb-instance.md)[MariaDB](../apsaradb-rds-for-mariadb/connect-to-an-apsaradb-rds-for-mariadb-instance.md)[实例](../apsaradb-rds-for-mariadb/connect-to-an-apsaradb-rds-for-mariadb-instance.md)
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
