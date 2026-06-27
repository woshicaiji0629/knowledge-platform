# SQL Server数据迁移或上云方案概览-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-sql-server/data-migration-and-synchronization/

# SQL Server数据迁移或上云方案概览
RDS SQL Server提供了多种数据迁移方案，可满足不同上云或迁云的业务需求。帮助您在不影响业务的情况下，平滑地将部署于不同环境中的SQL Server数据库（如ECS自建SQL Server、线下自建SQL Server、Azure平台SQL Server、AWS平台SQL Server）与阿里云RDS SQL Server之间进行互相迁移。
## 场景一：RDS间的数据迁移
[RDS SQL Server](restore-the-data-of-an-apsaradb-rds-for-sql-server-instance.md)[备份恢复到新实例或已有实例](restore-the-data-of-an-apsaradb-rds-for-sql-server-instance.md)
[RDS SQL Server](migrate-data-between-apsaradb-rds-for-sql-server-instances.md)[迁移到](migrate-data-between-apsaradb-rds-for-sql-server-instances.md)[RDS SQL Server](migrate-data-between-apsaradb-rds-for-sql-server-instances.md)
[跨阿里云账号迁移](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-rds-instances-of-different-alibaba-cloud-accounts)[RDS](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-rds-instances-of-different-alibaba-cloud-accounts)[实例](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-rds-instances-of-different-alibaba-cloud-accounts)
## 场景二：自建SQL Server迁移到RDS SQL Server
[全量备份数据上云](migrate-the-full-backup-data-of-a-self-managed-sql-server-instance-to-an-apsaradb-rds-for-sql-server-instance.md)（数据库级别的迁移上云方案）
[增量备份数据上云](migrate-the-incremental-backup-data-of-a-self-managed-sql-server-instance-to-an-apsaradb-rds-for-sql-server-instance.md)（数据库级别的迁移上云方案）
[SQL Server](migrate-data-from-a-self-managed-sql-server-instance-to-an-apsaradb-rds-for-sql-server-instance.md)[实例级别迁移上云](migrate-data-from-a-self-managed-sql-server-instance-to-an-apsaradb-rds-for-sql-server-instance.md)（实例级别的迁移上云方案）
[自建](migrate-data-from-a-self-managed-sql-server-database-to-an-apsaradb-rds-for-sql-server-instance.md)[SQL Server](migrate-data-from-a-self-managed-sql-server-database-to-an-apsaradb-rds-for-sql-server-instance.md)[迁移至](migrate-data-from-a-self-managed-sql-server-database-to-an-apsaradb-rds-for-sql-server-instance.md)[RDS SQL Server](migrate-data-from-a-self-managed-sql-server-database-to-an-apsaradb-rds-for-sql-server-instance.md)（采用JDBC逻辑协议获取SQL并写入到目标端）
[自建](migrate-data-from-a-self-managed-sql-server-database-to-an-apsaradb-rds-for-sql-server-instance-by-using-a-physical-gateway.md)[SQL Server](migrate-data-from-a-self-managed-sql-server-database-to-an-apsaradb-rds-for-sql-server-instance-by-using-a-physical-gateway.md)[通过物理网关迁移上云](migrate-data-from-a-self-managed-sql-server-database-to-an-apsaradb-rds-for-sql-server-instance-by-using-a-physical-gateway.md)（采用数据库原生物理备份协议写入数据块到目标端）
[使用](use-ssms-to-migrate-data-to-an-rds-for-sql-server-instance.md)[SSMS](use-ssms-to-migrate-data-to-an-rds-for-sql-server-instance.md)[迁移数据至](use-ssms-to-migrate-data-to-an-rds-for-sql-server-instance.md)[RDS SQL Server](use-ssms-to-migrate-data-to-an-rds-for-sql-server-instance.md)
[通过](how-to-import-multiple-data-entries-to-apsaradb-for-rds-sql-server.md)[BCP](how-to-import-multiple-data-entries-to-apsaradb-for-rds-sql-server.md)[命令/JDBC SQLBulkCopy/ADO.NET SQLBulkCopy](how-to-import-multiple-data-entries-to-apsaradb-for-rds-sql-server.md)[向](how-to-import-multiple-data-entries-to-apsaradb-for-rds-sql-server.md)[RDS SQL Server](how-to-import-multiple-data-entries-to-apsaradb-for-rds-sql-server.md)[批量导入数据](how-to-import-multiple-data-entries-to-apsaradb-for-rds-sql-server.md)
[通过](https://help.aliyun.com/zh/dms/import-data)[DMS](https://help.aliyun.com/zh/dms/import-data)[数据导入功能批量导入](https://help.aliyun.com/zh/dms/import-data)（仅支持SQL、CSV、Excel格式）
## 场景三：第三方云SQL Server迁移到RDS SQL Server
[Azure](migrate-data-from-a-sql-server-database-on-microsoft-azure-to-apsaradb-rds-for-sql-server.md)[平台的](migrate-data-from-a-sql-server-database-on-microsoft-azure-to-apsaradb-rds-for-sql-server.md)[SQL Server](migrate-data-from-a-sql-server-database-on-microsoft-azure-to-apsaradb-rds-for-sql-server.md)[迁移至](migrate-data-from-a-sql-server-database-on-microsoft-azure-to-apsaradb-rds-for-sql-server.md)[RDS SQL Server](migrate-data-from-a-sql-server-database-on-microsoft-azure-to-apsaradb-rds-for-sql-server.md)
[AWS](migrate-data-from-a-sql-server-database-on-aws-to-apsaradb-rds-for-sql-server.md)[平台的](migrate-data-from-a-sql-server-database-on-aws-to-apsaradb-rds-for-sql-server.md)[SQL Server](migrate-data-from-a-sql-server-database-on-aws-to-apsaradb-rds-for-sql-server.md)[迁移至](migrate-data-from-a-sql-server-database-on-aws-to-apsaradb-rds-for-sql-server.md)[RDS SQL Server](migrate-data-from-a-sql-server-database-on-aws-to-apsaradb-rds-for-sql-server.md)
## 场景四：阿里云其他SQL Server迁移到RDS SQL Server
[MyBase SQL Server](https://help.aliyun.com/zh/dts/user-guide/migrate-mybase-sql-server-to-rds-sql-server)[迁移至](https://help.aliyun.com/zh/dts/user-guide/migrate-mybase-sql-server-to-rds-sql-server)[RDS SQL Server](https://help.aliyun.com/zh/dts/user-guide/migrate-mybase-sql-server-to-rds-sql-server)
## 场景五：RDS SQL Server迁移到本地SQL Server
[RDS SQL Server](migrate-data-from-an-apsaradb-rds-for-sql-server-instancce-to-a-local-sql-server-database.md)[迁移至本地](migrate-data-from-an-apsaradb-rds-for-sql-server-instancce-to-a-local-sql-server-database.md)[SQL Server](migrate-data-from-an-apsaradb-rds-for-sql-server-instancce-to-a-local-sql-server-database.md)
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
