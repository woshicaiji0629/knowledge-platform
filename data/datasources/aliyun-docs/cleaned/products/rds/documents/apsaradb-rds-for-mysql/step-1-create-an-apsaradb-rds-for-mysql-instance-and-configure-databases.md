# 入门第一步：快捷创建RDS MySQL实例与配置数据库-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases

# 第一步：创建RDS MySQL实例与配置数据库
一个RDS MySQL实例是一台数据库服务器，您可以在其上创建多个数据库，帮助您管理海量的业务数据。本教程将向您介绍如何快速通过控制台创建RDS MySQL实例，并在实例中配置数据库与账号信息。
## 流程概述
在体验云数据库RDS丰富的功能前，您需要创建并配置一个RDS MySQL实例。推荐您使用阿里云主账号完成以下流程，避免RAM账号带来的权限问题：
通过标准创建页面购买一个RDS MySQL实例。
在实例内创建数据库。
在实例内创建一个高权限账号。
## 一、创建RDS MySQL实例
访问[RDS](https://rdsbuy.console.aliyun.com/newCreate/rds/mysql)[实例标准创建页面](https://rdsbuy.console.aliyun.com/newCreate/rds/mysql)。
配置核心参数
您可以通过配置以下核心参数快速完成实例选型，其他参数保持默认值即可。
选择计费方式（示例值：按量付费）
短期使用建议选择按量付费，按小时付费，能随时释放实例。
长期使用建议选择包年包月，预付费模式，费用比按量付费更低。
业务波动大时建议选择Serverless，实例无固定规格，性能随业务负载自动调整。
选择地域（示例值：华东1（杭州））
如需通过ECS连接：选择ECS实例所在地域，可实现内网互通。
如需通过其他设备连接：选择离该设备较近的地域，可以降低网络时延，后续通过外网访问。
实例购买后地域不可更改，请谨慎选择。
选择引擎（示例值：MySQL 8.0）
支持MySQL 5.6、5.7、8.0，建议与业务侧数据库大版本保持一致。
如无版本需求，建议选择MySQL 8.0，可体验更丰富的功能。
选择产品系列与存储类型
不同[产品系列](https://help.aliyun.com/zh/document_detail/2787304.html)和[存储类型](https://help.aliyun.com/zh/document_detail/2545944.html)的实例会限制[部分产品功能](features.md)的使用。
如需体验RDS MySQL产品或短期试用，推荐选择高可用系列，存储类型为本地SSD盘或高性能云盘，以较低成本体验更多产品功能。
选择VPC
如需与同地域下的ECS实例内网互连，则需选择与ECS相同的VPC。其他情况下，保持默认值即可。
选择实例规格（示例值：通用规格 2核4 GB）
RDS MySQL提供了多种实例规格，您可以根据实际业务需要进行选择。如果购买后发现此规格无法满足需求，可以[变更规格配置](change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。
确认配置与下单支付
您可以在页面右侧查看与确认待购买实例的配置，将鼠标悬浮在查看明细上时，可以在弹窗中查看实例的费用明细。[RDS](billable-items-billing-methods-and-pricing.md)[实例费用](billable-items-billing-methods-and-pricing.md)与其付费方式、系列、规格、存储类型和存储空间大小等参数相关。
确认配置无误后，单击去支付按钮并支付。
说明
创建按量付费的RDS实例时，您的阿里云账户余额（即现金余额）和代金券的总值必须大于等于100.00元人民币，否则会下单失败并提示“可用金不足”。
查看实例
支付成功后，可以单击返回控制台或直接访问[RDS](https://rdsnext.console.aliyun.com/rdsList/cn-hangzhou)[实例列表](https://rdsnext.console.aliyun.com/rdsList/cn-hangzhou)，在页面上方选择地域，查看已购买的实例。实例创建需要1～10分钟左右，当实例状态变为运行中时，表示实例已创建成功。
说明
从订单支付成功到控制台显示实例间有一定的延迟，如您支付成功后控制台未显示相关实例，请等待一段时间后刷新控制台。
## 二、创建数据库
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。在本教程中，您需要选择上一步中创建的RDS实例与该实例所在的地域。
在左侧导航栏中单击数据库管理，然后单击创建数据库按钮打开创建数据库页签。
设置参数：
本教程设置数据库（DB）名称为db_test1，支持字符集为utf8，然后单击创建。
如您需要存储4字节的宽字符（例如表情和不常用汉字），可以使用utf8mb4字符集。
高权限账号默认拥有所有数据库权限，无需单独授权，因此不在授权账号下拉框中展示。
您可以在数据库管理页面中查看新建的数据库。
## 三、创建账号
在[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)中单击实例ID，选择左侧导航栏账号管理，单击创建账号打开创建账号页签。
设置账号参数：本教程设置数据库账号为dbuser，账号类型选择高权限账号。
填写新密码与确认密码，单击确定按钮，完成账号创建。
说明
如您创建账号失败，请检查是否存在账号重名、创建过于频繁或实例中已有高权限账号等问题，解决后重新创建。
您可以刷新账号管理页面查看新建的高权限账号。
说明
RDS MySQL支持创建普通账号和高权限账号，两者区别如下：
高权限账号：云数据库RDS MySQL内最高权限账号（RDS MySQL不支持创建root账号），拥有实例下所有数据库的权限，可通过控制台或API创建，每个实例仅允许创建一个高权限账号。
普通账号：仅对被授权数据库有部分操作权限，可通过[控制台、API](create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)[和](create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)[SQL](create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)[命令创建](create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)。如您需要使用SQL命令创建普通账号（如CREATE USER），需要先创建高权限账号，再通过高权限账号登录数据库执行命令。
## 下一步
[第二步：连接](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)[实例](step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)
## 常见问题
## 实例查询
Q1：如何查看阿里云账号下的RDS实例总数量，以及阿里云账号下是否还有运行中的RDS实例？
登录[RDS](https://rdsnext.console.aliyun.com/dashboard/cn-hangzhou)[概览页](https://rdsnext.console.aliyun.com/dashboard/cn-hangzhou)，即可查看当前阿里云账号下所有数据库引擎的RDS实例总数量。在该页面您还可以看到实例的地域分布情况，以及各地域下正在运行中的RDS实例数量。
该页面同时展示即将到期和已过期的实例数量，并可在下方表格中按地域查看各状态实例的详细分布。
Q2：为什么创建实例后，实例列表看不到创建中的实例？
| 可能原因 | 说明 | 建议 |
| --- | --- | --- |
| 地域错误 | 您所在地域和您创建实例时选择的地域不一致。 | 在页面左上角切换地域。 |
| 可用区内资源不足 | 可用区内资源不足，导致创建失败。 创建失败您可以在 [订单列表](https://usercenter2.aliyun.com/order/list?pageIndex=1&pageSize=20) 里看到退款。 | 选择其它可用区后重试。 |
| RAM 权限策略禁止创建未加密的 RDS 实例 | 已配置 RAM 权限策略，禁止 RAM 用户创建未加密的 RDS 实例。 RAM 用户尝试创建高性能本地盘实例，实例创建失败（高性能本地盘实例无法在创建时设置磁盘加密）。 RAM 用户尝试创建云盘实例，但未设置云盘加密，实例创建失败。 更多信息，请参见 [通过](use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) [RAM](use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) [权限策略限制](use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) [RAM](use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) [用户权限](use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) 。 | 创建实例时，存储类型选择云盘，选中云盘加密并设置密钥后重试。 |
## 账号与权限
Q1：账号可以实现更细粒度的管理吗？例如限制账号访问源地址、限制访问表等。
请参见[指定账号从特定](authorize-an-account-to-access-its-authorized-databases-from-specified-ip-addresses-in-an-apsaradb-rds-for-mysql-instance.md)[IP](authorize-an-account-to-access-its-authorized-databases-from-specified-ip-addresses-in-an-apsaradb-rds-for-mysql-instance.md)[地址访问数据库](authorize-an-account-to-access-its-authorized-databases-from-specified-ip-addresses-in-an-apsaradb-rds-for-mysql-instance.md)或[限制账号只能访问指定表、视图、字段](authorize-accounts-to-manage-tables-views-and-fields.md)。
Q2：RDS提供root账号或super权限吗？
RDS不提供root账号或具有super权限的账号，避免您误操作导致数据丢失泄露等无法挽回的损失。
## 相关文档
通过API创建RDS实例：[创建](api-rds-2014-08-15-createdbinstance-mysql.md)[RDS](api-rds-2014-08-15-createdbinstance-mysql.md)[实例](api-rds-2014-08-15-createdbinstance-mysql.md)
创建其他类型实例请参见：
[快速创建并使用](../apsaradb-rds-for-sql-server/create-an-apsaradb-rds-for-sql-server-instance.md)[RDS SQL Server](../apsaradb-rds-for-sql-server/create-an-apsaradb-rds-for-sql-server-instance.md)[实例](../apsaradb-rds-for-sql-server/create-an-apsaradb-rds-for-sql-server-instance.md)
[快速创建](../apsaradb-rds-for-postgresql/create-an-apsaradb-rds-for-postgresql-instance.md)[RDS PostgreSQL](../apsaradb-rds-for-postgresql/create-an-apsaradb-rds-for-postgresql-instance.md)[实例](../apsaradb-rds-for-postgresql/create-an-apsaradb-rds-for-postgresql-instance.md)
[快速创建](../apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance.md)[RDS MariaDB](../apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance.md)[实例](../apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance.md)
创建其它引擎数据库和账号请参见：
[SQL Server](../apsaradb-rds-for-sql-server/create-a-database-and-account.md)[创建数据库和账号](../apsaradb-rds-for-sql-server/create-a-database-and-account.md)
[PostgreSQL](../apsaradb-rds-for-postgresql/create-a-database-and-an-account-on-an-apsaradb-rds-for-postgresql-instance.md)[创建数据库和账号](../apsaradb-rds-for-postgresql/create-a-database-and-an-account-on-an-apsaradb-rds-for-postgresql-instance.md)
[MariaDB](../apsaradb-rds-for-mariadb/create-a-database-and-an-account-on-an-apsaradb-rds-for-mariadb-instance.md)[创建数据库和账号](../apsaradb-rds-for-mariadb/create-a-database-and-an-account-on-an-apsaradb-rds-for-mariadb-instance.md)
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
