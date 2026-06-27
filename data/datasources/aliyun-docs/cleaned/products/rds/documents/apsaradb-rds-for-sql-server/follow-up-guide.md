# 深入使用RDS SQL Server-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-sql-server/follow-up-guide

# 深入使用RDS SQL Server
当您掌握了实例的创建、配置、连接等基本操作后，您可以通过以下教程深入使用RDS SQL Server，体验更多功能和产品特色。
## 冷热数据分离
实践教程：[冷热数据分离最佳实践](hot-and-cold-data-separation-best-practices.md)
功能简介：通过将低频访问的冷数据归档至成本更低的对象存储服务OSS，同时将高频访问的热数据保留在云盘上，从而达到数据管理的成本效益和高效率。适用于数据量庞大、对成本敏感或对数据访问性能有分层需求等业务场景。
涉及功能：[数据归档](archive-data-to-an-oss-bucket.md)[OSS](archive-data-to-an-oss-bucket.md)
## 快照备份
功能简介：相对于常规的物理备份方式，快照备份可大幅缩短数据库的恢复时间，同时支持更大的备份数据量。快照备份不占用实例的CPU和内存资源，对实例I/O的占用也远远小于传统的物理备份，整个备份过程对实例性能几乎无影响。
涉及功能：[快照备份](enable-the-snapshot-backup-feature-for-an-apsaradb-rds-for-sql-server-instance.md)
## 透明数据加密TDE
实践教程：[TDE](tde-best-practices.md)[使用的最佳实践](tde-best-practices.md)
功能简介：通过设置透明数据加密（Transparent Data Encryption，简称TDE）阻止可能的攻击者绕过数据库直接从存储中读取敏感信息，有效提高您数据库中敏感数据的安全性；同时将指导您将开启了TDE后生成的SQL Server备份数据从阿里云RDS恢复到本地环境中。
涉及功能：[设置透明数据加密](configure-tde-for-an-apsaradb-rds-for-sql-server-instance.md)[TDE](configure-tde-for-an-apsaradb-rds-for-sql-server-instance.md)
## 只读实例与读写分离（集群系列）
功能简介：在对数据库有少量写请求，但有大量读请求的应用场景下，单个实例可能无法承受读取压力，甚至对业务产生影响。为了实现读取能力的弹性扩展，分担数据库压力，您可以在集群系列的主实例中创建一个或多个只读实例分散数据库读取压力，增加应用的吞吐量。且当前对于满足条件的主实例支持[只读实例快速初始化能力](../overview-of-read-only-apsaradb-rds-for-sql-server-instances.md)，该能力将有效缩短只读实例的创建时间至分钟级别，且该过程对主实例I/O无任何影响。
只读实例创建后开通只读地址，并在应用程序中配置主实例地址和只读地址，可以实现写请求转发到主实例，读请求转发到只读地址，只读地址会根据权重将读请求自动转发给各个只读实例。
涉及功能：[RDS SQL Server](rds-cluster-edition.md)[集群系列](rds-cluster-edition.md)、[创建](create-a-read-only-apsaradb-rds-for-sql-server-instance.md)[SQL Server](create-a-read-only-apsaradb-rds-for-sql-server-instance.md)[只读实例](create-a-read-only-apsaradb-rds-for-sql-server-instance.md)、[读写分离简介/开通读写分离](enable-the-read-or-write-splitting-endpoint-for-an-apsaradb-rds-for-sql-server-instance.md)
## 实例参数管理
功能简介：通过RDS控制台/API修改实例级别参数，并查询参数修改历史，可有效提升您的数据库运维效率和体验。
涉及功能：[通过控制台管理实例参数](manage-instance-parameters-in-the-apsaradb-rds-console.md)
## 配置Serverless实例弹性伸缩
实践教程：[定时配置](configure-scheduled-tasks-to-adjust-the-number-of-rcus-for-serverless-apsaradb-rds-instances.md)[Serverless](configure-scheduled-tasks-to-adjust-the-number-of-rcus-for-serverless-apsaradb-rds-instances.md)[实例的](configure-scheduled-tasks-to-adjust-the-number-of-rcus-for-serverless-apsaradb-rds-instances.md)[RCU](configure-scheduled-tasks-to-adjust-the-number-of-rcus-for-serverless-apsaradb-rds-instances.md)
功能简介：Serverless实例RCU弹性伸缩的耗时通常为秒级，极小概率下可能因为跨机弹性扩容而耗时3~5分钟。如果您对特定时段的稳定性有严格要求，您可以定时配置Serverless实例的RCU，提前增加RCU数量。
涉及功能：[RDS SQL Server Serverless](https://help.aliyun.com/zh/document_detail/604344.html)[实例](https://help.aliyun.com/zh/document_detail/604344.html)
## WebShell登录RDS SQL Server主机
实践教程：[通过](webshell-to-log-on-to-the-host.md)[WebShell](webshell-to-log-on-to-the-host.md)[登录](webshell-to-log-on-to-the-host.md)[SQL Server](webshell-to-log-on-to-the-host.md)[主机并使用](webshell-to-log-on-to-the-host.md)[SSRS](webshell-to-log-on-to-the-host.md)[报表服务](webshell-to-log-on-to-the-host.md)
功能简介：通过创建主机账号并登录到RDS SQL Server实例主机中，您可以在登录主机后使用SSRS（SQL Server Reporting Services）服务管理和操作SQL Server数据库。
涉及功能：[创建主机账号并登录](create-a-host-account-for-an-apsaradb-rds-for-sql-server-instance-and-use-the-host-account-for-logons.md)
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
