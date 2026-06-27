# 可弹性伸缩的在线数据库-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/product-overview/what-is-apsaradb-rds-what-is-apsaradb-rds

# 云数据库RDS简介
阿里云关系型数据库RDS（Relational Database Service）是一种安全稳定可靠、高性价比、可弹性伸缩的在线数据库服务。RDS支持[MySQL](../apsaradb-rds-for-mysql/overview-3.md)、[SQL Server](../apsaradb-rds-for-sql-server/overview-of-apsaradb-rds-for-sql-server.md)、[PostgreSQL](../apsaradb-rds-for-postgresql/what-is-apsaradb-rds-for-postgresql.md)和[MariaDB](../apsaradb-rds-for-mariadb/what-is-apsaradb-rds-for-mariadb.md)引擎，并且提供了容灾、备份、恢复、监控、迁移等方面的全套解决方案，帮助您解决数据库运维的烦恼。
## 为什么选择云数据库RDS
### 安全稳定可靠
历经考验：已支撑数十万用户的业务稳定运行，且经过双十一高并发、大数据量的考验。
高可用性：支持主备容灾架构、自动故障切换、跨可用区容灾，最高可保障99.99%可用性。
备份恢复：提供自动备份，支持异地备份、按时间点恢复等。
高安全性：支持网络隔离、静态数据加密、传输数据加密、访问权限控制等多项安全能力。
### 解决运维烦恼
快速部署：无需提前购置硬件和软件，只需点击鼠标或调用API，数分钟即可生成数据库实例。
轻量运维：阿里云自动完成修复软件、备份、监控、故障切换、主从复制等，让您专注于业务而不是繁琐的日常维护。
弹性伸缩：扩缩容操作简单灵活，通常仅约30秒闪断或无闪断。Serverless实例扩缩容为自动、秒级、无闪断。
### 有效降低成本
灵活计费：短期使用，可选择按量付费，用完释放。长期使用，可选择包年包月享受折扣。
节省计划：针对RDS按量付费项的折扣权益计划，对比按量付费，RDS MySQL可降低20%到70%的费用，RDS PostgreSQL和RDS SQL Server可降低15%到60%的费用。
Serverless：支持Serverless计费方式。
自动扩缩容，计费粒度精确到1秒，最高节省成本70%。
通过信通院Serverless能力分级测试，获最高评级“先进级”。
当前新老用户开通RDS Serverless实例均享受5折优惠。
实例可停：部分实例支持暂停实例，暂停期间只需付存储费用。Serverless实例还支持自动启停。
倚天版：新增RDS MySQL基础系列1核 1GB和1核 2GB规格，RDS实例包月价格分别仅18元和24元，包年价格更优惠。[点此购买](https://rdsbuy.console.aliyun.com/newCreate/rds/mysql)。
弹性IO：支持高性能云盘，存储空间不变也可自动提升和降低IOPS上限。让您无需为了提升IOPS而升级存储，导致资源和成本浪费。
备库可读：集群系列备库可读，提高实例利用率。
免费试用：为新用户提供[免费试用](https://free.aliyun.com/?searchKey=rds)。目前已有数万人免费试用。
### 自研增强特性
阿里云自研的AliSQL与AliPG在开源数据库的基础上，进行了一系列创新与优化，以满足企业级的性能和稳定性需求。
AliSQL提供了类似于MySQL企业版的诸多功能。例如，Binlog in Redo在事务提交时同步Binlog至Redo Log，以减少磁盘操作和提升性能；Statement Queue确保执行计划的稳定性；Inventory Hint快速提交/回滚事务以提高业务吞吐能力；Thread Pool优化了并发控制机制，保证了数据库在高并发环境下的高性能；Faster DDL提升了在线DDL的并发处理性能。
AliPG在开源PostgreSQL的基础上进行了许多增强。例如，Ganos时空引擎提供室内外、地上下、动静态全空间数据处理能力；TDE支持表级别加密；全密态数据库支持数据在存储、计算、传输的全程加密；Babelfish插件提供解析和执行SQL Server T-SQL语句的能力。rds_ccl插件通过SQL限流避免过高的负载，保障数据库稳定性。
更多选择理由，请参见[RDS](competitive-advantages-of-apsaradb-rds-instances-over-self-managed-databases.md)[与自建数据库对比优势](competitive-advantages-of-apsaradb-rds-instances-over-self-managed-databases.md)。
## RDS视频简介
## 如何使用RDS
您可以通过以下方式管理RDS实例，进行实例创建、网络设置、数据库创建、账号创建等操作：
控制台：提供图形化的Web界面，操作方便。[点此登录控制台](https://rdsnew.console.aliyun.com)。
CLI：控制台上所有的操作都可以通过CLI实现。[查看](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)[CLI](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)[介绍](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)。
SDK：控制台上所有的操作都可以通过SDK实现。[查看](../sdk-reference.md)[SDK](../sdk-reference.md)[参考](../sdk-reference.md)。
API：控制台上所有的操作都可以通过API实现。[查看](../list-of-operations-by-function.md)[API](../list-of-operations-by-function.md)[概览](../list-of-operations-by-function.md)。
说明
如果业务复杂，您可以购买[支持计划](https://www.aliyun.com/support/supportplans)，获取由IM企业群、技术服务经理（TAM）、服务经理等提供的专属支持。
## 入门视频
[RDS](../videos/create-an-rds-instance.md)[实例创建](../videos/create-an-rds-instance.md)
[账号及数据库管理](../videos/account-and-database-management.md)
[只读实例与读写分离](../videos/read-only-instance-management-and-read-or-write-splitting.md)
[监控、备份及克隆实例](../videos/monitor-back-up-and-clone-an-rds-instance.md)
## RDS相关内容
相关服务
| 服务 | 说明 |
| --- | --- |
| [ECS](../../../ecs/documents/user-guide/what-is-ecs.md) | ECS 是云服务器，通过内网访问同一地域的 RDS 时，可实现 RDS 的最佳性能。ECS 搭配 RDS 是典型的业务访问架构。 |
| [Redis](../../../redis/documents/product-overview/what-is-apsaradb-for-redis.md) | Redis 提供持久化的内存数据库服务。当业务访问量较大时，ECS 、RDS 和 Redis 的组合可以支持更多的读请求，同时减少响应时间。 |
| [MongoDB](https://help.aliyun.com/zh/mongodb/product-overview/what-is-apsaradb-for-mongodb) | 提供稳定可靠、弹性伸缩、完全兼容 MongoDB 协议的数据库服务。数据结构多样时，可以选择将结构化数据存储在 RDS，将非结构化数据存储在 MongoDB，满足业务的多样化存储需求。 |
| [MaxCompute](https://help.aliyun.com/zh/maxcompute/product-overview/what-is-maxcompute) | 大数据计算服务 MaxCompute（原名 ODPS）是一种快速、完全托管的 TB/PB 级数据仓库解决方案，提供了完善的数据导入方案以及多种经典的分布式计算模型，能够快速地解决海量数据计算问题。通过数据集成服务，可将 RDS 数据导入 MaxCompute，实现大规模的数据计算 |
| [DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts) | 您可以使用数据传输服务 DTS 将本地数据库迁移到云上的 RDS，以及实现 RDS 的异地容灾。 |
| [OSS](../../../oss/documents/user-guide/what-is-oss.md) | 对象存储服务 OSS 是阿里云提供的海量、安全、低成本、高可靠的云存储服务。 |
相关链接
| 项目 | 链接 |
| --- | --- |
| RDS 定价 | 请参见 [计费项](billable-items-billing-methods-and-pricing.md) 。 |
| 提交建议 | 产品、功能或文档建议，请您通过 [聆听平台](https://connect.console.aliyun.com/create?spm=a2c4g.11186623.0.0.1b854dbe1Nh6Ah) 提交建议。 |
| 常见问题和故障处理 | 使用 RDS 时遇到的各类问题，例如 CPU 过高、实例锁定等，您可以在 [Q&A](faq.md) 或 [常见问题](../faq-overview.md) 内搜索查看，可以解决您的绝大部分问题。 |
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
