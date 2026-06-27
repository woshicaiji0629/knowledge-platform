# 入门第三步：自建数据库迁移上云-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/step-3-migrate-a-user-created-database-to-an-rds-mysql-instance

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-mysql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-mysql/getting-started.md)

- [AI能力中心](products/rds/documents/apsaradb-rds-for-mysql/ai-capability-center.md)

- [自研内核AliSQL](products/rds/documents/apsaradb-rds-for-mysql/proprietary-alisql.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-mysql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-mysql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-mysql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-mysql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-mysql/support.md)

[首页](https://help.aliyun.com/zh)

# 第三步：自建数据库迁移至RDS MySQL实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

数据库迁移是一项复杂且耗时的工程，您不仅需要考虑迁移过程中数据的安全性和完整性，还需要评估因数据库迁移而导致的业务中断所带来的影响。为了更快捷、更平滑地完成数据库迁移任务，您可以使用阿里云数据传输服务DTS辅助您的迁移工作，其能在保证数据传输快速且完整的情况下，将应用停机时间降低到分钟级别，让您更专注于迁移后的业务发展。同时，您也可以对自建数据库进行全量备份，使用备份文件恢复数据库至RDS MySQL实例，实现数据库的间接迁移上云。

## 费用说明

- 

创建RDS MySQL实例会产生实例规格费用与存储费用，其与实例的付费方式、系列、规格、存储类型和存储空间大小等参数相关，详情请参见[RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/billable-items-billing-methods-and-pricing.md)[计费项](products/rds/documents/apsaradb-rds-for-mysql/billable-items-billing-methods-and-pricing.md)。

- 

（方法一：使用DTS迁移至RDS MySQL实例）使用DTS进行数据迁移时会产生链路配置费用，其与任务时间、链路规格等参数相关，详情请参见[数据传输服务](https://help.aliyun.com/zh/dts/product-overview/billable-items)[DTS](https://help.aliyun.com/zh/dts/product-overview/billable-items)[计费项](https://help.aliyun.com/zh/dts/product-overview/billable-items)。

- 

（方法二：使用全量备份恢复至RDS MySQL实例）自建数据库全量备份上传至OSS会产生存储费用，详情请参见[OSS](products/oss/documents/storage-fees.md)[存储费用](products/oss/documents/storage-fees.md)。

## 准备工作

您可以直接使用前两篇教程中创建的RDS MySQL实例进行本教程中的操作。如实例已释放，您可以再次购买RDS MySQL实例并创建高权限账号dbuser，详细教程请参见[第一步：创建](products/rds/documents/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[实例与配置数据库](products/rds/documents/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)。

## 方法一：使用DTS迁移至RDS MySQL实例

[数据传输服务](https://help.aliyun.com/zh/dts/product-overview/what-is-dts)[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts)（Data Transmission Service）是阿里云提供的实时数据流服务，支持关系型数据库（RDBMS）、非关系型的数据库（NoSQL）、数据多维分析（OLAP）等数据源间的数据交互，集数据同步、迁移、订阅、集成、加工于一体，助您构建安全、可扩展、高可用的数据架构。

本教程以ECS自建数据库为例，展示如何创建与配置DTS数据迁移任务，将自建数据库平滑迁移至RDS MySQL实例。

说明

- 

从自建数据库向RDS MySQL迁移时，建议保持ECS实例与RDS实例在同一地域与同一VPC下（实例满足[内网访问条件](products/rds/documents/apsaradb-rds-for-mysql/step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)），使数据迁移过程更快速且稳定。

- 

使用DTS进行数据迁移时的相关限制和注意事项请参见[从自建](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md)[MySQL](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md)[迁移至](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md)[实例](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md)。

- 

登录[DMS](https://dms.aliyun.com/new?spm=a2c4g.211596.0.0.99dc646bcQs6s4)[数据管理服务](https://dms.aliyun.com/new?spm=a2c4g.211596.0.0.99dc646bcQs6s4)。

- 

在顶部菜单栏选择Data + AI>数据传输 (DTS)>数据迁移。如果顶部没有菜单栏，可以点击右上角退出极简模式。

- 

单击创建任务跳转至任务配置页面。

- 

配置源库与目标库信息。

## 配置源库参数

本教程中的源库指您的原业务数据库，即ECS实例中的自建数据库。

- 

数据库类型：选择MySQL。

- 

接入方式：选择ECS自建数据库。根据部署位置的不同，自建数据库可以划分为部署在ECS的自建数据库与部署在本地的自建数据库。针对不同场景，DTS提供了多种接入方式满足数据库迁移需求，详情请参见[各接入方式准备工作](https://help.aliyun.com/zh/dts/user-guide/preparation-overview)：

| 自建库部署位置 | 公网访问 | DTS 接入方式（同迁移任务配置） |
| --- | --- | --- |
| ECS（已在云上） | 均可 | ECS 自建数据库 |
| 本地（未上云） | 具备公网地址 | 公网 IP |
| 不具备公网地址 | 云企业网 CEN 、 数据库网关 DG 、 专线/VPN 网关/智能网关 |  |


- 

实例地区：选择ECS实例所在地域。

- 

ECS实例ID：在下拉列表中选择待迁移的ECS实例。

- 

端口：默认为3306。

- 

数据库账号和数据库密码：填写ECS自建数据库中用于数据迁移或拥有相关权限的账号和密码。如未准备，您可以新建账号并授予相关权限，详细步骤请参见[为自建](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)[MySQL](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)[创建账号](https://help.aliyun.com/zh/dts/user-guide/create-an-account-for-a-self-managed-mysql-database-and-configure-binary-logging#concept-1198525)。

- 

连接方式：如果自建数据库未开启SSL加密，选择非加密连接；如果已开启SSL加密，选择SSL安全连接，并上传CA 证书和CA 密钥。

## 配置目标库参数

本教程中的目标库指云数据库RDS MySQL实例，您需要将源库迁移至该数据库。

- 

数据库类型：选择MySQL。

- 

接入方式：选择云实例。

- 

实例地区：选择RDS实例所在地域，本教程以华东1 （杭州）为例。

- 

RDS实例ID：在下拉列表中选择[准备工作](products/rds/documents/apsaradb-rds-for-mysql/step-3-migrate-a-user-created-database-to-an-rds-mysql-instance.md)中创建的RDS MySQL实例ID。

- 

数据库账号和数据库密码：填写RDS MySQL实例中高权限账号和密码，本教程以dbuser和用户自定义密码为例。

- 

连接方式：本教程以非加密连接为例。如果选择SSL安全连接，您需要提前开启RDS MySQL实例的SSL加密功能，详情请参见[使用云端证书快速开启](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md)[SSL](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md)[链路加密](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md)。

- 

单击测试连接以进行下一步。DTS会自动为ECS实例添加DTS安全组，并将DTS服务器IP添加至RDS实例白名单中，以允许DTS访问ECS实例和RDS实例。

- 

配置任务对象。

- 

选择迁移类型。为了实现数据库平滑迁移，您需要勾选库表结构迁移、全量迁移和增量迁移。三种迁移方式的区别请参见[迁移类型说明](https://help.aliyun.com/zh/dts/user-guide/overview-of-data-migration-scenarios#section-wda-pa7-g81)。

- 

在源库对象中选择待迁移的数据库（本教程以wordpressdb为例），单击将其移动至已选择对象，然后单击下一步高级配置。

- 

高级配置页面中您无需进行参数选择，您可以直接使用默认的参数配置并单击下一步数据校验。

- 

在数据校验页面中勾选全量校验、增量校验和结构校验，然后单击下一步保存任务并预检查。三种数据校验方式详情请参见[什么是数据校验](https://help.aliyun.com/zh/dts/user-guide/what-is-data-verification)。

- 

预检查通过率达到100%后，单击下一步购买。

- 

选择数据迁移实例的链路规格，本教程以small规格为例。阅读并选中《数据传输（按量付费）服务条款》，单击购买并启动。

- 

迁移任务正式开始，您可以单击迁移任务ID查看具体进度。当您看到如下界面，表示存量数据已迁移完成，增量数据会实时同步。任务启动后，在迁移任务详情页的实例进展区域可查看各阶段运行状态（增量数据采集、增量写入、全量校验、结构校验、增量校验）。下方基本信息页签显示任务状态、当前位点、RPS 速率及限速信息，右侧提供重启和暂停操作按钮。后续您可以验证全量数据和增量数据的迁移结果，确认无误后，您可以将业务流量切换至RDS MySQL实例，实现自建库迁移至RDS MySQL实例。

## 方法二：使用全量备份恢复至RDS MySQL实例

RDS MySQL支持全量备份导入与恢复功能。您可以使用[Percona XtraBackup](https://docs.percona.com/percona-xtrabackup/)与MySQL Backup Helper工具对自建数据库进行全量备份并上传至OSS，然后将全量备份文件从OSS导入RDS控制台，通过数据库恢复功能将其恢复至新实例中，实现自建数据库间接迁移至RDS MySQL实例。详细操作请参见[MySQL 5.7、8.0](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[自建数据库全量上云](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)。

## 相关文档

- 

[从](products/rds/documents/apsaradb-rds-for-mysql/import-data-from-csv-files-txt-files-or-sql-scripts-to-rds-instances.md)[CSV](products/rds/documents/apsaradb-rds-for-mysql/import-data-from-csv-files-txt-files-or-sql-scripts-to-rds-instances.md)[文件、TXT](products/rds/documents/apsaradb-rds-for-mysql/import-data-from-csv-files-txt-files-or-sql-scripts-to-rds-instances.md)[文件或](products/rds/documents/apsaradb-rds-for-mysql/import-data-from-csv-files-txt-files-or-sql-scripts-to-rds-instances.md)[SQL](products/rds/documents/apsaradb-rds-for-mysql/import-data-from-csv-files-txt-files-or-sql-scripts-to-rds-instances.md)[脚本导入数据到](products/rds/documents/apsaradb-rds-for-mysql/import-data-from-csv-files-txt-files-or-sql-scripts-to-rds-instances.md)[RDS](products/rds/documents/apsaradb-rds-for-mysql/import-data-from-csv-files-txt-files-or-sql-scripts-to-rds-instances.md)

- 

[将](products/rds/documents/apsaradb-rds-for-mysql/import-data-from-an-excel-file-to-apsaradb-rds-for-mysql.md)[Excel](products/rds/documents/apsaradb-rds-for-mysql/import-data-from-an-excel-file-to-apsaradb-rds-for-mysql.md)[的数据导入数据库](products/rds/documents/apsaradb-rds-for-mysql/import-data-from-an-excel-file-to-apsaradb-rds-for-mysql.md)

- 

[从自建](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-user-created-oracle-instance-to-an-rds.md)[Oracle](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-user-created-oracle-instance-to-an-rds.md)[迁移至阿里云](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-user-created-oracle-instance-to-an-rds.md)[RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-user-created-oracle-instance-to-an-rds.md)

- 

[从自建](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-db2-database-to-an-apsaradb-rds-for-mysql-instance.md)[Db2](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-db2-database-to-an-apsaradb-rds-for-mysql-instance.md)[迁移至](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-db2-database-to-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-db2-database-to-an-apsaradb-rds-for-mysql-instance.md)

- 

[从第三方云数据库迁移至](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-third-party-cloud-database-to-apsaradb-for-rds.md)[RDS](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-third-party-cloud-database-to-apsaradb-for-rds.md)

- 

[RDS](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-between-apsaradb-rds-for-mysql-instances.md)[实例间数据迁移](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-between-apsaradb-rds-for-mysql-instances.md)

[上一篇：第二步：连接RDS MySQL实例](products/rds/documents/apsaradb-rds-for-mysql/step-2-connect-to-an-apsaradb-rds-for-mysql-instance.md)[下一篇：后续指引](products/rds/documents/apsaradb-rds-for-mysql/follow-up-guide.md)

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
