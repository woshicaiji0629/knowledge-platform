# 如何快速上手连接MariaDB实例功能-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mariadb/connect-to-an-apsaradb-rds-for-mariadb-instance

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-mariadb/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-mariadb/getting-started.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-mariadb/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-mariadb/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-mariadb/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-mariadb/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-mariadb/support.md)

[首页](https://help.aliyun.com/zh)

# 连接MariaDB实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

初始化配置后，您可以让ECS连接MariaDB实例，也可以本地连接到MariaDB实例，实现业务目标。

## 前提条件

已完成如下操作：

- 

[快速创建](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance.md)[RDS MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance.md)[实例](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance.md)

- 

[设置白名单](products/rds/documents/apsaradb-rds-for-mariadb/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mariadb-instance.md)

- 

[创建账号](products/rds/documents/apsaradb-rds-for-mariadb/create-a-database-and-an-account-on-an-apsaradb-rds-for-mariadb-instance.md)

## 方法一：使用DMS连接实例

DMS是阿里云提供的图形化的数据管理工具，可用于管理关系型数据库和NoSQL数据库，支持数据管理、结构管理、用户授权、安全审计、数据趋势、数据追踪、BI图表、性能与优化等功能。

您可以在数据库管理页面右侧单击SQL查询登录数据库。

## 方法二：使用客户端连接实例

RDS与原生的数据库服务完全兼容，所以您可以使用任何通用的数据库客户端连接到RDS实例，且连接方法类似。下文以[HeidiSQL](https://www.heidisql.com/)为例。

- 

启动HeidiSQL客户端。

- 

在左下角单击新建。

- 

输入要连接的RDS实例信息，参数说明如下。

- 

- 

| 参数 | 说明 |
| --- | --- |
| 网络类型 | 连接数据库的形式。选择 MariaDB or MySQL（TCP/IP） 。 |
| Library | 动态链接库。保持默认值即可。 |
| 主机名/IP 地址 | 输入 RDS 实例的内网地址或外网地址，例如 rm-bp1xxxxxxxxxxxxxx.mysql.rds.aliyuncs.com 。 关于如何查看地址信息，请参见 [查看或修改内外网地址和端口](products/rds/documents/apsaradb-rds-for-mariadb/view-and-change-the-internal-and-public-endpoints-and-port-numbers-of-an-apsaradb-rds-for-mariadb-instance.md) 。 若您的客户端部署在 ECS 实例上，且 ECS 实例与要访问的 RDS 实例的地域、网络类型相同，请使用内网地址。例如 ECS 实例和 RDS 实例都是华东 1 的专有网络实例，使用内网地址连接能提供安全高效的访问。 其它情况只能使用外网地址。 |
| 用户 | RDS 实例中创建的账号名称。关于如何创建账号，请参见 [创建数据库和账号](products/rds/documents/apsaradb-rds-for-mariadb/create-a-database-and-an-account-on-an-apsaradb-rds-for-mariadb-instance.md) 。 |
| 密码 | 账号对应的密码。 |
| 端口 | 若使用内网连接，需输入 RDS 实例的内网端口。若使用外网连接，需输入 RDS 实例的外网端口。更多信息，请参见 [查看或修改内外网地址和端口](products/rds/documents/apsaradb-rds-for-mariadb/view-and-change-the-internal-and-public-endpoints-and-port-numbers-of-an-apsaradb-rds-for-mariadb-instance.md) 。 |


- 

单击打开。

若连接信息无误，即会成功连接实例。

常见报错说明如下：

- 

Unknown MySQL server hose 'xxxxxxxxx'(11001)

请检查主机名/IP地址是否填写正确，常见错误是填写为实例ID或IP地址。应该填写内网或外网连接地址。

- 

Access denied for user 'xxxxx'@'xxxxx'(using password:YES)

请检查账号密码是否填写正确，常见错误为填写阿里云账号。应该填写实例的账号管理页面创建的账号。

- 

响应很慢并返回Can't connect to MySQL server on 'rm-bp1xxxxxxxxxxxxxx.mysql.rds.aliyuncs.com'(10060)

请检查白名单是否设置正确，需要将该软件所在主机的对外公网IP填写在白名单中。如何设置白名单，请参见[设置白名单](products/rds/documents/apsaradb-rds-for-mariadb/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mariadb-instance.md)。

说明

您可以临时设置白名单为0.0.0.0/0，用来排查是否是白名单设置问题导致的连接报错，如果确定是白名单设置问题，再定位正确的IP地址。具体操作，请参见[外网无法连接](products/rds/documents/support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[RDS MySQL](products/rds/documents/support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[或](products/rds/documents/support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[MariaDB：如何正确填写本地设备的公网](products/rds/documents/support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[IP](products/rds/documents/support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[地址](products/rds/documents/support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)。

## 连接失败的解决办法

请参见[解决无法连接实例问题](products/rds/documents/support/what-do-i-do-if-i-fail-to-connect-to-an-apsaradb-rds-instance.md)。

## 操作视频

[ECS（Linux）连接](products/rds/documents/videos/connect-an-ecs-instance-running-linux-to-an-rds-instance.md)[RDS](products/rds/documents/videos/connect-an-ecs-instance-running-linux-to-an-rds-instance.md)

## 常见问题

Q：我使用函数计算，想获取RDS的数据，要怎么操作呢？

A：您可以为函数安装第三方依赖，使用内置模块获取RDS数据，详情请参见[为函数安装第三方依赖](https://help.aliyun.com/zh/functioncompute/fc-2-0/user-guide/install-third-party-dependencies-on-function-compute)。

[上一篇：创建数据库和账号](products/rds/documents/apsaradb-rds-for-mariadb/create-a-database-and-an-account-on-an-apsaradb-rds-for-mariadb-instance.md)[下一篇：操作指南](products/rds/documents/apsaradb-rds-for-mariadb/user-guide.md)

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
