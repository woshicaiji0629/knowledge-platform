# RDS SQL Server配置变更-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-sql-server/change-the-specifications-of-an-apsaradb-rds-for-sql-server-instance

# 变更配置
本文介绍如何变更RDS SQL Server常规实例的配置，包括存储类型PL等级（如ESSD PL1变更为ESSD PL2）、实例规格、存储空间，以提升实例性能，解决因业务增长导致的数据存储瓶颈等问题。变更配置后您无需手动重启实例，同时部分实例已支持无损扩容能力，不会造成数据库访问中断。
说明
RDS SQL Server Serverless实例的配置变更，请参见[变更计算资源扩缩范围（RCU）](change-the-scaling-range-of-rcus-for-a-serverless-apsaradb-rds-for-sql-server-instance.md)和[增加存储空间](expand-storage-capacity.md)。
## 变更项
变更下述配置不会导致实例连接地址的改变。如果您需要横向扩展数据库的读取能力，可以通过[创建只读实例](create-a-read-only-apsaradb-rds-for-sql-server-instance.md)并[配置读写分离](read-only-instances-and-read-write-splitting.md)来分担主实例的压力（但需确保主实例为[集群系列实例](rds-cluster-edition.md)）。
| 变更项 | 说明 |
| --- | --- |
| 版本 | 支持 [升级数据库大版本](upgrade-the-major-engine-version-and-rds-edition-of-an-apsaradb-rds-for-sql-server-instance.md) 到更高版本。 |
| 系列 | 支持 [基础系列升级到高可用系列/集群系列、高可用系列升级到集群系列](upgrade-the-major-engine-version-and-rds-edition-of-an-apsaradb-rds-for-sql-server-instance.md) 。 |
| 规格 | 若 [实例规格族](../product-overview/instance-families.md) 不变，仅需变更规格代码 ：可通过 [变更配置](change-the-specifications-of-an-apsaradb-rds-for-sql-server-instance.md) 入口实现。 例如，实例规格族为通用型保持不变，但需将规格从 mssql.s2.medium.s2 变更为 mssql.s2.large.s2 若需变更实例规格族 ：可通过 [升级版本](upgrade-the-major-engine-version-and-rds-edition-of-an-apsaradb-rds-for-sql-server-instance.md) 入口操作实现，支持向同规格族或更高规格族的变更（ [部分情况](upgrade-the-major-engine-version-and-rds-edition-of-an-apsaradb-rds-for-sql-server-instance.md) 除外），具体以控制台显示为准。规格族自低到高：共享型<通用型<独享型（不支持高规格族降级） 例如，实例规格族从通用型变更为独享型。 说明 高可用系列共享规格不能直接升级为集群系列独享规格。 若控制台找不到目标规格族，可通过 [创建](create-an-apsaradb-rds-for-sql-server-instance-1.md) 一个目标规格族的新实例，再将原实例的数据 [迁移](migrate-data-between-apsaradb-rds-for-sql-server-instances.md) 到新实例的方式实现。 |
| 存储类型 | ESSD 云盘实例支持升级 PL 等级（不支持降级）。例如 ESSD PL1 升级为 ESSD PL2。 非集群系列的 SSD 云盘实例支持升级为 ESSD 云盘，但不支持再降级回 SSD。 说明 集群系列实例暂不支持从 SSD 云盘升级为 ESSD 云盘。但可通过 [创建](create-an-apsaradb-rds-for-sql-server-instance-1.md) 一个 ESSD 云盘新实例，再将原实例的数据 [迁移](migrate-data-between-apsaradb-rds-for-sql-server-instances.md) 到新实例的方式实现。 |
| 存储空间 | 所有实例仅支持增加存储空间， 不支持减少存储空间 。 增加存储空间时，最小增加量为 5 GB，最大不能超过当前 [实例规格的存储空间限制](../product-overview/primary-apsaradb-rds-instance-types.md) 。 说明 若主实例有只读实例，由于只读实例存储空间不能小于主实例存储空间，因此需要先增加只读实例存储空间，才能增加主实例的存储空间。 若当前规格对应的存储空间范围无法满足您的需求，请选择其它实例规格。 |
## 前提条件
您的阿里云账号没有未支付的续费订单。
## 注意事项
变配时升级大版本等场景将涉及跨机迁移，会导致主机账号及原主机中部署的程序或文件（SSIS、SSAS、SSRS等）都被清空，请务必提前迁移或备份数据。
重要
阿里云RDS SQL Server基于微软SQL Server原生内核，专注于提供稳定高效的数据库托管服务。若您的业务需要使用SSIS、SSAS、SSRS等功能时，更依赖您具备专业的运维能力，以确保业务连续性。
变更配置可能会进行数据迁移，迁移完成后根据您选择的切换时间进行切换（期间保持增量同步），切换过程中会出现一次约30秒的闪断，而且与数据库、账号、网络等相关的大部分操作都无法执行。请在业务低峰期执行变配操作，并确保您的应用有自动重连机制。
由于基础系列只有一个数据库节点，没有备节点作为热备份，因此当该节点意外宕机或者执行变更配置、版本升级等任务时，会出现较长时间的不可用。如果业务对数据库的可用性要求较高，不建议使用基础系列，可选择其他系列（如高可用系列）。
若RDS主实例下包含只读实例，在扩容主实例存储空间时，请确保只读实例的存储空间大于等于主实例的存储空间，否则将扩容失败。建议您先扩容只读实例的存储空间，所有只读实例扩容完成后，再扩容主实例存储空间。
## 计费规则
请参见[变配的计费规则](../product-overview/specification-changes.md)。
## 操作步骤
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在基本信息页的配置信息区域单击变更配置。
（仅包年包月实例需要执行此步骤）在弹出的对话框中，选择变更方式（立即升配或立即降配：变配后，新的配置立即生效），单击下一步。
变更任务下达后，系统将磁盘数据同步到一个新实例，然后根据切换时间，到时间后系统将原实例的实例ID和连接地址等信息切换到新实例，实例ID、连接地址等不会改变。
修改实例的配置。具体请参见[变更项](change-the-specifications-of-an-apsaradb-rds-for-sql-server-instance.md)。
重要
RDS SQL Server部分实例支持无损扩容能力，在仅变更存储类型等级（PL等级，例如ESSD PL1变更为ESSD PL2）或扩容存储空间时，由于无损扩容不会造成数据库访问中断，因此您无需设置实例的切换时间。但如果您同时更改了实例规格，则仍需配置切换时间。
若您未更改任何配置项但变配实例页面仍显示切换时间选项，则说明您的RDS实例尚不支持无损扩容。您可以[升级实例大版本或小版本](upgrade-the-major-engine-version-and-rds-edition-of-an-apsaradb-rds-for-sql-server-instance.md)后再进行变更配置操作，以实现无损扩容。
选择变更实例配置的执行时间。
数据迁移结束后立即切换：变更实例配置会涉及到底层的数据迁移，您可以选择在数据迁移后立即切换。
可维护时间内进行切换：在变更配置生效期间，可能会出现一次约30秒的闪断，而且与数据库、账号、网络等相关的大部分操作都无法执行，因此您可以选择在[可维护时间段](set-the-maintenance-window-of-an-apsaradb-rds-for-sql-server-instance.md)内执行切换的操作。
说明
部分实例支持无损扩容，不显示该配置项，因此无需配置实例的切换时间。
如果选择可维护时间内进行切换，则在变配任务下发至实例完成变配的过程中，实例的常规备份将被禁用。
在变配实例页面中确认变配前后的实例信息，单击去支付并完成支付。
警告
变配订单提交后无法取消，请在执行变配前详细评估业务需求。
为确保变配的稳定进行，在提交变配订单至变配完成期间，请勿执行DDL操作。
## 常见问题
变更存储类型PL等级操作，是否会造成数据库访问中断？
RDS SQL Server部分实例支持无损扩容能力，在仅变更存储类型等级（PL等级，例如ESSD PL1变更为ESSD PL2）或扩容存储空间时，由于无损扩容不会造成数据库访问中断，因此您无需设置实例的切换时间。但如果您同时更改了实例规格，则仍需配置切换时间。
若您未更改任何配置项但变配实例页面仍显示切换时间选项，则说明您的RDS实例尚不支持无损扩容。您可以[升级实例大版本或小版本](upgrade-the-major-engine-version-and-rds-edition-of-an-apsaradb-rds-for-sql-server-instance.md)后再进行变更配置操作，以实现无损扩容。
可用区和版本可以变更吗？
非SQL Server 2008 R2实例：支持通过API（[ModifyDBInstanceSpec](api-rds-2014-08-15-modifydbinstancespec-sqlserver.md)）升级数据库大版本，并变更实例的可用区和交换机；也支持通过RDS控制台[升级数据库大版本](upgrade-the-major-engine-version-and-rds-edition-of-an-apsaradb-rds-for-sql-server-instance.md)。
SQL Server 2008 R2（高性能本地盘）实例：支持通过RDS控制台[升级版本](upgrade-an-apsaradb-rds-for-sql-server-instance-with-local-disks-from-sql-server-2008-r2-to-sql-server-2012-or-sql-server-2016.md)的同时变更可用区。
说明
您也可以单独[迁移可用区](migrate-an-apsaradb-rds-for-sql-server-instance-across-zones.md)。
仅扩容存储空间，需要迁移数据到新实例吗？
您只需要进行扩容操作即可，不需要手动迁移数据。扩容存储空间时，系统会检查实例所在主机上是否有足够存储空间用于扩容。如果有则直接扩容，不需要迁移数据；如果没有，系统会自动迁移数据到拥有足够存储空间的主机上。
变更配置大概需要多久？
变更配置涉及到数据迁移等，一般90%的变配可以在30分钟内完成。
CPU、内存、磁盘同时升配，会闪断多久？
无论是单独升配CPU、内存、磁盘中的一个，还是三个同时升配，闪断的时间都是一样的，一般是分钟级的。切换过程中，可能会出现业务闪断或实例重启，而且与数据库、账号、网络等相关的大部分操作都无法执行，请选择在可维护时间段内执行变配操作。各变更项的详情，请参见[变更项](change-the-specifications-of-an-apsaradb-rds-for-sql-server-instance.md)。
变更配置时变配实例页面无可选实例规格，如何处理？
可能是浏览器缓存问题导致，建议您清理页面缓存或更换浏览器后重新操作。
## 相关API
[通过](api-rds-2014-08-15-modifydbinstancespec-sqlserver.md)[ModifyDBInstanceSpec](api-rds-2014-08-15-modifydbinstancespec-sqlserver.md)[接口变更](api-rds-2014-08-15-modifydbinstancespec-sqlserver.md)[RDS](api-rds-2014-08-15-modifydbinstancespec-sqlserver.md)[实例的规格和存储空间等](api-rds-2014-08-15-modifydbinstancespec-sqlserver.md)
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
