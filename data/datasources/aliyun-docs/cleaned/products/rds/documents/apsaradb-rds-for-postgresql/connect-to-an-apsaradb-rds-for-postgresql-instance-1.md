# 连接RDS PostgreSQL实例-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/connect-to-an-apsaradb-rds-for-postgresql-instance-1

# 连接RDS PostgreSQL实例
购买RDS PostgreSQL实例并完成必要配置（创建账号、设置白名单）后，您就可以通过数据管理DMS、pgAdmin客户端、PostgreSQL命令行工具或应用程序等方式连接RDS PostgreSQL实例，实现您的业务目标。本文介绍这些连接方法的具体操作。
## 前提条件
已创建RDS PostgreSQL实例。更多信息，请参见[创建](create-an-apsaradb-rds-for-postgresql-instance-1.md)[RDS PostgreSQL](create-an-apsaradb-rds-for-postgresql-instance-1.md)[实例](create-an-apsaradb-rds-for-postgresql-instance-1.md)。
已创建账号和数据库。更多信息，请参见[创建账号和数据库](create-a-database-and-an-account-on-an-apsaradb-rds-for-postgresql-instance.md)。
已设置白名单，允许客户端所在的ECS或本地设备访问RDS PostgreSQL实例。更多信息，请参见[设置白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance.md)。
如果使用ECS通过内网访问RDS PostgreSQL，ECS与RDS PostgreSQL实例必须位于同一阿里云账号下的同一地域及同一VPC内，同时应将ECS的私网IP地址添加至白名单。
如果使用本地设备访问RDS PostgreSQL，则将本地设备的公网IP添加到白名单。
## 操作步骤
### 数据管理DMS连接
数据管理DMS是一种集数据管理、结构管理、用户授权、安全审计、数据趋势、数据追踪、BI图表、性能与优化和服务器管理于一体的数据管理服务。关于数据库管理DMS的更多信息，请参见[什么是数据管理](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582)[DMS](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582)。
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在基本信息页面单击登录数据库。在实例的基本信息页面上方，单击登录数据库。
在DMS的登录实例页面，选择访问方式和管控模式。
| 配置项 | 说明 |
| --- | --- |
| 访问方式 | 通过 DMS 访问 RDS 实例的方式。本文以 账号+密码登录 为例。 账号+密码登录 ：使用 拥有目标数据库的权限 的数据库账号和密码登录。 KMS 凭据登录 ：DMS 会自动为实例开启安全托管，但您需要手动选择在 KMS 创建的 RDS 凭据以登录数据库。 说明 KMS 凭据登录 的访问方式登录 RDS 时，DMS 会自动为实例免费开启 [安全托管](https://help.aliyun.com/zh/dms/product-overview/security-hosting) 。 您也可以单击 一键开启安全托管 ，输入账号和密码，为实例免费开启 [安全托管](https://help.aliyun.com/zh/dms/product-overview/security-hosting) ，实现安全可控的 免密登录。 |
| 管控模式 | 数据管理 DMS 提供三种实例级别的 [管控模式](https://help.aliyun.com/zh/dms/product-overview/control-modes) ，您可以根据实际业务场景进行设置。 自由操作 稳定变更 安全协同 |
登录后请刷新页面。随后，您可以在左侧已登录实例菜单中看到实例内已登录的实例及其数据库。
说明
如果开启了安全托管，您可以在左侧免登录实例菜单中看到已登录的实例及其数据库。
在DMS控制台，只能通过双击目标数据库的方式切换数据库，不支持使用USE命令切换。
如果实例存在，但实例展开后未找到目标数据库，可能是：
登录账号无目标数据库的访问权限，请更换具有相关权限的账号进行登录。
元数据未同步导致目录无法显示：请将鼠标悬浮在目标数据库所属实例上，单击实例名右侧的按钮，即可刷新数据库列表，显示目标数据库。
如需快速同步数据库的库表结构，可以通过DMS[空库初始化](https://help.aliyun.com/zh/dms/initialize-empty-databases)功能实现。
说明
除了通过RDS控制台跳转到DMS进行登录，您还可以登录DMS控制台直接录入RDS实例，录入后可以在DMS控制台快速登录数据库。详情请参见[云数据库录入](https://help.aliyun.com/zh/dms/register-an-apsaradb-instance-1#multiTask2179)。
如果重置了账号密码，需要重新登录DMS。
### pgAdmin客户端连接
pgAdmin客户端是PostgreSQL官方推荐的数据库连接工具，在[PostgreSQL](https://www.postgresql.org/download/)[官方网站](https://www.postgresql.org/download/)下载并安装PostgreSQL时，将会自动安装pgAdmin 4客户端。下文以pgAdmin 4 V6.2.0为例，介绍如何连接RDS PostgreSQL实例。
如果您不想安装PostgreSQL，也可以单独下载[pgAdmin](https://www.pgadmin.org/download/)[客户端](https://www.pgadmin.org/download/)，仅用于连接远程数据库。
启动pgAdmin 4客户端。
说明
高版本客户端首次登录需要设置Master Password用于保护保存的密码和其他凭据。
右键单击Servers，选择Register>Server...。
在General页签设置连接名称。 在General标签页的Name字段中输入自定义的服务器名称。
选择Connection标签页，输入要连接的实例信息。 在Connection标签页，填写以下连接参数，完成后单击Save。
| 参数 | 说明 |
| --- | --- |
| Host name/address | RDS PostgreSQL 实例的连接地址及对应的端口。 若通过内网连接，需输入 RDS 实例的内网地址和内网端口。 若使用外网连接，需输入 RDS 实例的外网地址和外网端口。 您可以在 RDS PostgreSQL 实例的数据库连接页面查看。 更多信息，请参见 [查看或修改连接地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| Port |  |
| Username | RDS PostgreSQL 实例的账号和密码。 创建 RDS 实例的账号请参见 [创建账号和数据库](create-a-database-and-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| Password |  |
单击Save。
若连接信息无误，会出现如下界面，则表示连接成功。连接成功后，pgAdmin 4 主界面显示Dashboard监控面板，左侧Browser面板可展开查看服务器下的Databases、Login/Group Roles、Tablespaces等对象。
重要
postgres是RDS实例默认的系统数据库，请勿在该数据库中进行任何操作。
### PostgreSQL命令行工具连接
通过[PostgreSQL](https://www.postgresql.org/download/)[官方网站](https://www.postgresql.org/download/)下载并安装PostgreSQL时，将会自动安装PostgreSQL命令行终端工具（Command Line Tools）。
在命令行终端中输入如下命令连接RDS PostgreSQL数据库。
psql -h <实例连接地址> -U <用户名> -p <端口号> [-d <数据库名>]
C:\Users\Administrator>psql -h pgm-xxx.pg.rds.aliyuncs.com -p 5432 -U xxx -d postgres 用户 xxx 的口令; psql (13.4, 服务器 11.9) 输入 "help" 来获取帮助信息. postgres=>
| 参数 | 说明 |
| --- | --- |
| 实例连接地址 | RDS PostgreSQL 实例的连接地址及对应的端口。 若通过内网连接，需输入 RDS 实例的内网地址和内网端口。 若使用外网连接，需输入 RDS 实例的外网地址和外网端口。 您可以在 RDS PostgreSQL 实例的数据库连接页面查看。 更多信息，请参见 [查看或修改连接地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 端口号 |  |
| 用户名 | RDS PostgreSQL 实例的账号。 创建 RDS 实例的账号请参见 [创建账号和数据库](create-a-database-and-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 数据库名 | 可选，需要连接的数据库名，postgres 是 RDS PostgreSQL 实例默认的系统数据库，请勿在该数据库中进行任何操作，建议配置 RDS 实例下已创建的其他数据库。 如何创建和查看数据库，请参见 [创建数据库](create-a-database-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |
### 应用程序连接
说明
本文以Maven项目JDBC连接RDS PostgreSQL实例为例，其它编程语言连接方式类似。
pom.xml中添加依赖。
<dependency> <groupId>postgresql</groupId> <artifactId>postgresql</artifactId> <version>8.2-504.jdbc3</version> </dependency>
连接实例示例代码如下：
public class DatabaseConnection { public static void main( String[] args ){ try { Class.forName("org.postgresql.Driver"); } catch (ClassNotFoundException e) { e.printStackTrace(); } //实例连接地址 String hostname = "pgm-bp1i3kkq7321o9****.pg.rds.aliyuncs.com"; //实例连接端口 int port = 5432; //数据库名称 String dbname = "postgres"; //用户名 String username = "username"; //密码 String password = "password"; String dbUrl = "jdbc:postgresql://" + hostname + ":" + port + "/" + dbname + "?binaryTransfer=true"; Connection dbConnection; try { dbConnection = DriverManager.getConnection(dbUrl, username, password); Statement statement = dbConnection.createStatement(); //输入需要执行的SQL语句。 String selectSql = "SELECT * FROM information_schema.sql_features LIMIT 10"; ResultSet resultSet = statement.executeQuery(selectSql); while (resultSet.next()) { System.out.println(resultSet.getString("feature_name")); } } catch (SQLException e) { e.printStackTrace(); } } }
### 第三方报表工具连接
Microsoft Power BI
RDS PostgreSQL支持接入[Power BI](https://powerbi.microsoft.com/)，在Power BI中对数据进行获取、清洗、建模和可视化展示等操作，实现数据分析。下文以Power BI 2.112.1161.0 64-bit版本为例，介绍如何连接RDS PostgreSQL实例。
下载并安装Power BI Desktop客户端。下载方法请参见[获取 Power BI Desktop](https://learn.microsoft.com/power-bi/fundamentals/desktop-get-the-desktop)。
启动Power BI Desktop客户端。
在顶部菜单栏选择主页页签，然后单击获取数据>更多...。在主页选项卡中，单击获取数据按钮，在下拉菜单底部单击更多...。
在获取数据对话框中选择数据库>PostgreSQL数据库，然后单击连接。在左侧分类列表中选择数据库，然后在右侧列表中选择PostgreSQL 数据库，单击连接。
在PostgreSQL数据库对话框中，分别设置服务器和数据库后，单击确定。在数据连接模式中选择导入，然后单击确定。
| 参数 | 说明 |
| --- | --- |
| 服务器 | RDS PostgreSQL 实例的连接地址和对应的端口。 格式： 连接地址:端口 若通过内网连接，需输入 RDS 实例的内网地址和内网端口。 若使用外网连接，需输入 RDS 实例的外网地址和外网端口。 您可以在 RDS PostgreSQL 实例的数据库连接页面查看。 更多信息，请参见 [查看或修改连接地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 数据库 | postgres 是 RDS PostgreSQL 实例默认的系统数据库，请勿在该数据库中进行任何操作，建议配置 RDS 实例下已创建的其他数据库。 如何创建和查看数据库，请参见 [创建数据库](create-a-database-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |
设置用户名和密码后，单击连接。在弹出的身份验证对话框中，输入 RDS PostgreSQL 实例的用户名和密码，然后单击连接。
说明
创建RDS实例的账号请参见[创建账号和数据库](create-a-database-and-an-account-on-an-apsaradb-rds-for-postgresql-instance.md)。
在加密支持对话框中单击确定。在弹出的加密支持对话框中，单击确定以使用不加密连接访问数据源。
连接成功后，即可在导航器窗口中查看数据库中的表信息，您可以根据业务需求，选中目标表后，选择加载或转换数据操作。在导航器对话框左侧导航树中，展开已连接的 RDS PostgreSQL 实例，勾选需要导入的目标表（例如public.tb_test2），右侧将自动预览该表的数据。确认无误后，单击加载直接导入数据，或单击转换数据在导入前进行数据编辑。
Smartbi
RDS PostgreSQL支持接入Smartbi，在Smartbi中对数据进行分析处理，满足您在企业级报表、数据可视化分析、自助探索分析、数据挖掘建模、AI 智能分析等大数据分析需求。下文以Smartbi V10.5版本为例，介绍如何连接RDS PostgreSQL实例。
根据Smartbi官方安装指导，完成申请License、Smartbi客户端的下载、安装以及启动Smartbi服务。
在开始菜单，单击访问Smartbi。在 Windows 开始菜单中找到Smartbi文件夹，单击访问Smartbi打开 Smartbi 登录页面。
输入账号和密码后，单击登录，进入Smartbi。
说明
管理员默认登录账号为admin，密码为manager。
如果是首次登录，则需要修改管理员密码。
在左侧单击
在新建关系数据库对话框中配置相关参数，然后单击测试连接(T)。驱动程序存放目录选择产品内置，链接方式选择用户名密码，验证类型选择静态，填写完成后单击测试连接(T)验证连接是否正常。
| 参数 | 说明 |
| --- | --- |
| 名称 | 数据库连接的名称，自定义。 |
| 驱动程序类型 | 固定选择为 PostgreSQL。 |
| 驱动程序类 | 选择 驱动程序类型 后自动选择，无需修改。 |
| 连接字符串 | 连接 RDS PostgreSQL 实例的 JDBC 连接串，格式如下： jdbc:postgresql://<servername>:<port>/<dbName>?defaultRowFetchSize=10000 <servername>:<port> ：RDS PostgreSQL 实例的连接地址和对应的端口。 若通过内网连接，需输入 RDS 实例的内网地址和内网端口。 若使用外网连接，需输入 RDS 实例的外网地址和外网端口。 您可以在 RDS PostgreSQL 实例的数据库连接页面查看。 更多信息，请参见 [查看或修改连接地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) 。 <dbName> ：postgres 是 RDS PostgreSQL 实例默认的系统数据库，请勿在该数据库中进行任何操作。 建议配置 RDS 实例下已创建的其他数据库。如何创建和查看数据库，请参见 [创建数据库](create-a-database-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 用户名 、 密码 | 创建 RDS 实例的账号请参见 [创建账号](create-an-account-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |
测试通过后，单击保存，出现如下信息，表示连接成功。连接成功后，左侧导航面板的数据连接列表中将显示RDS_PostgreSQL节点，展开该节点可查看表关系视图、计算字段和过滤器三个子项。
### SSL连接
RDS PostgreSQL支持设置SSL链路加密，对网络连接进行加密，保证传输链路的安全。具体配置请参见[使用](connect-to-an-apsaradb-rds-for-postgresql-instance-over-ssl-connections.md)[SSL](connect-to-an-apsaradb-rds-for-postgresql-instance-over-ssl-connections.md)[链路连接](connect-to-an-apsaradb-rds-for-postgresql-instance-over-ssl-connections.md)[RDS PostgreSQL](connect-to-an-apsaradb-rds-for-postgresql-instance-over-ssl-connections.md)[数据库](connect-to-an-apsaradb-rds-for-postgresql-instance-over-ssl-connections.md)。
## 连接失败的解决办法
请参见[解决无法连接实例问题](../support/what-do-i-do-if-i-fail-to-connect-to-an-apsaradb-rds-instance.md)。
## 常见问题
Q：如果ECS与RDS不位于同一地域或同一账号下，如何进行连接？
A：可以使用如下两种方法中的一种进行连接。
使用[VPC](../../../vpc/documents/vpc-peer-to-peer-connection.md)[对等连接](../../../vpc/documents/vpc-peer-to-peer-connection.md)实现同账号或跨账号、同地域或跨地域的两个VPC间的私网互通，且同地域的VPC对等连接免费。
使用云企业网实现内网互通，具体请根据实际情况参照[同地域](../../../cen/documents/getting-started/connect-vpcs-in-same-region-with-transit-router.md)[VPC](../../../cen/documents/getting-started/connect-vpcs-in-same-region-with-transit-router.md)[互通](../../../cen/documents/getting-started/connect-vpcs-in-same-region-with-transit-router.md)、[跨地域](../../../cen/documents/getting-started/inter-region-vpc-interworking.md)[VPC](../../../cen/documents/getting-started/inter-region-vpc-interworking.md)[互通](../../../cen/documents/getting-started/inter-region-vpc-interworking.md)或[跨账号](../../../cen/documents/getting-started/use-enterprise-edition-transit-routers-to-connect-vpcs-across-regions-and-accounts.md)[VPC](../../../cen/documents/getting-started/use-enterprise-edition-transit-routers-to-connect-vpcs-across-regions-and-accounts.md)[互通](../../../cen/documents/getting-started/use-enterprise-edition-transit-routers-to-connect-vpcs-across-regions-and-accounts.md)实现。
Q：我使用函数计算，想获取RDS的数据，要怎么操作呢？
A：您可以为函数安装第三方依赖，使用内置模块获取RDS数据，详情请参见[为函数安装第三方依赖](https://help.aliyun.com/zh/functioncompute/fc-2-0/user-guide/install-third-party-dependencies-on-function-compute)。
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
