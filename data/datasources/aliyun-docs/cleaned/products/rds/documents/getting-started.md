# 关系型数据库引擎-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/getting-started

# 快速入门
如果您初次使用阿里云关系型数据库RDS，请参见快速入门系列文档，帮助您快速上手RDS。
[RDS MySQL](create-an-apsaradb-rds-for-mysql-instance.md)[快速入门](create-an-apsaradb-rds-for-mysql-instance.md)
[RDS SQL Server](apsaradb-rds-for-sql-server/create-an-apsaradb-rds-for-sql-server-instance.md)[快速入门](apsaradb-rds-for-sql-server/create-an-apsaradb-rds-for-sql-server-instance.md)
[RDS PostgreSQL](apsaradb-rds-for-postgresql/create-an-apsaradb-rds-for-postgresql-instance.md)[快速入门](apsaradb-rds-for-postgresql/create-an-apsaradb-rds-for-postgresql-instance.md)
[RDS MariaDB](apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance.md)[快速入门](apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance.md)
## 数据库引擎简介
## RDS MySQL
| MySQL | MySQL 是全球受欢迎的开源数据库之一，作为开源软件组合 LAMP（Linux + Apache + MySQL + Perl/PHP/Python）中的重要一环，广泛应用于各类应用。 Web 2.0 时代，风靡全网的社区论坛软件系统 Discuz!和博客平台 WordPress 均基于 MySQL 实现底层架构。 Web 3.0 时代，阿里巴巴、Facebook、Google 等大型互联网公司都采用更为灵活的 MySQL 构建了成熟的大规模数据库集群。 |
| --- | --- |
| RDS MySQL | 阿里云数据库 RDS MySQL 基于阿里巴巴的 MySQL 源码分支，经过双 11 高并发、大数据量的考验，拥有优良的性能和吞吐量。此外，阿里云数据库 MySQL 版还拥有经过优化的 [读写分离](apsaradb-rds-for-mysql/enable-the-proxy-terminal-feature-for-an-apsaradb-rds-for-mysql-instance.md) 、 [数据库代理](apsaradb-rds-for-mysql/what-are-database-proxies.md) 、 [智能调优](https://help.aliyun.com/zh/document_detail/144875.html#concept-2338561) 等高级功能。 |
| 支持版本 | 支持 MySQL 5.5、5.6、5.7 和 8.0 版本。 |
## RDS SQL Server
| SQL Server | SQL Server 是发行最早的商用数据库产品之一，作为 Windows 平台（IIS + .NET + SQL Server）中的重要一环，支撑着大量的企业应用。SQL Server 自带的 Management Studio 管理软件内置了大量图形工具和丰富的脚本编辑器。您通过可视化界面即可快速上手各种数据库操作。 |
| --- | --- |
| RDS SQL Server | 阿里云数据库 RDS SQL Server 拥有高可用架构和任意时间点的 [数据恢复](apsaradb-rds-for-sql-server/restore-the-data-of-an-apsaradb-rds-for-sql-server-instance.md) 功能，强力支撑各种企业应用。同时，其还拥有 微软正版的 License 授权 ，实例费用中也包含了微软的 License 费用，您无需额外支出。 |
| 支持版本 | 企业集群版：2017、2019、2022 企业版：2012、 2014、 2016 企业版（单机）：2012 标准版：2012、 2014、 2016、2017、2019、2022 Web 版：2012、2016、2017、2019、2022 |
## RDS PostgreSQL
| PostgreSQL | PostgreSQL 是一个开源数据库。作为学院派关系型数据库管理系统的鼻祖，它的优点主要集中在对 SQL 规范的完整实现以及丰富多样的数据类型支持，包括 JSON 数据、IP 数据和几何数据等，而大部分商业数据库都不支持这些数据类型。 |
| --- | --- |
| RDS PostgreSQL | 阿里云数据库 RDS PostgreSQL 不仅完美支持事务、子查询、多版本控制（MVCC）、数据完整性检查等特性，还集成了高可用和备份恢复等重要功能，减轻您的运维压力。 |
| 支持版本 | RDS PostgreSQL 支持 11 及以上版本。 |
## RDS MariaDB
| MariaDB | MariaDB 是 MySQL 的一个分支，主要由开源社区维护，采用 GPL 授权许可。MariaDB 的目的是完全兼容 MySQL，包括 API 和命令行，使之能轻松成为 MySQL 的代替品。在存储引擎方面，MariaDB 10.0.9 版起使用 XtraDB（代号为 Aria）来代替 MySQL 的 InnoDB。 |
| --- | --- |
| RDS MariaDB | 阿里云关系型数据库 MariaDB 完全兼容社区版 MariaDB，良好兼容 Oracle，对 PL/SQL 有优秀的兼容性，提供技术支持以及专家服务，为您提供企业级数据库解决方案。 |
| 支持版本 | RDS MariaDB 支持 10.3 和 10.6 版本。 |
## 常见问题
Q：RDS的系统库有哪些？
A：阿里云RDS不同引擎自带的系统库不同，您可以[连接到](support/how-do-i-connect-to-an-apsaradb-rds-instance.md)[RDS](support/how-do-i-connect-to-an-apsaradb-rds-instance.md)[数据库](support/how-do-i-connect-to-an-apsaradb-rds-instance.md)后查看。各引擎系统库如下：
RDS MySQL：information_schema、mysql、performance_schema、sys、__recycle_bin__
RDS SQL Server：master、msdb、tempdb、model
RDS PostgreSQL：postgres、template1、rdsadmin
RDS MariaDB：information_schema、mysql、performance_schema、sys
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
