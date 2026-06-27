# 将PostgreSQL实例升级为集群系列-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/upgrade-the-rds-edition-from-rds-basic-edition-or-rds-high-availability-edition-to-rds-cluster-edition

# PostgreSQL基础系列或高可用系列升级集群系列
RDS PostgreSQL支持将基础系列升级至集群系列，增强容灾能力、灵活性和可靠性。同时，您也可以将高可用系列升级至集群系列，以降低成本，并进一步提升灵活性和可靠性。
## 背景信息
RDS PostgreSQL集群系列实例采用计算与存储分离、一主多备的架构，支持自动故障切换、任意备节点可切换为主节点、备节点可读、按需增删节点、多可用区容灾、节点粒度的监控、集群节点拓扑管理等功能，详情请参见[集群系列](rds-cluster-edition.md)。
## 前提条件
实例大版本为RDS PostgreSQL 14或以上版本。
实例系列为基础系列或高可用系列。
说明
您可以在实例的基本信息页面查看实例的系列。
实例存储类型为ESSD云盘或高性能云盘。
说明
实例存储类型为高性能云盘时，未开启IO加速或数据归档功能。
如果实例的存储类型为SSD云盘，请先升级为ESSD云盘。升级操作请参见[SSD](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)[云盘升级为](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)[ESSD](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)[云盘](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)。
实例为主实例，且没有只读实例。
实例未开通数据库代理服务。
实例未启用Babelfish，即小版本号后缀不带babelfish。
实例未开通连接池（PgBouncer）。
## 费用说明
变更实例系列的费用请参见[变更配置](specification-changes.md)。
## 影响
RDS变更配置可能涉及底层数据迁移，请您耐心等待。在迁移完成后会根据您设置的切换时间自动进行切换，切换时会出现30秒左右的闪断，请确保应用具备重连机制。
说明
升级后实例连接地址不会改变，应用侧无需做修改。
升级后无法回退到原基础系列或高可用系列。
## 操作步骤
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在基本信息页面的配置信息，单击变更配置。
（仅包年包月实例需要执行此步骤）在弹出的对话框中，选择立即升配，单击下一步。
设置如下参数。
| 参数名称 | 说明 |
| --- | --- |
| 产品系列 | 选择 集群系列 。 |
| 存储类型 | 选择实例的存储类型。详情请参见 [存储类型介绍](storage-types-of-apsaradb-rds-for-postgresql.md) 。 |
| 实例规格 | 选择实例规格。每种规格都有对应的 CPU 核数、内存、最大连接数和最大 IOPS。详情请参见 [主实例规格列表](../product-overview/primary-apsaradb-rds-instance-types.md) 。 |
| 存储空间 | 设置存储空间。存储空间只能增加，不能降低。 |
| 切换时间 | 选择升级的切换时间： 立即切换 ：立即开始迁移，迁移过程对实例无影响，迁移完成后进行实例切换。 可维护时间内进行切换 ：立即开始迁移，迁移过程对实例无影响，但是迁移完成后不切换，等到可维护时间才进行实例切换。 |
仔细阅读变配提醒，确认无误后勾选服务协议，单击去支付。
在弹出的对话框中确认变配前后实例对比信息，确认无误后单击继续支付，完成支付流程。
验证升级结果：在基本信息页面，当实例的类型及系列显示为常规实例（集群系列），表示升级成功。
## 相关API
| API | 描述 |
| --- | --- |
| [ModifyDBInstanceSpec - 变更](api-rds-2014-08-15-modifydbinstancespec-postgresql.md) [RDS](api-rds-2014-08-15-modifydbinstancespec-postgresql.md) [实例](api-rds-2014-08-15-modifydbinstancespec-postgresql.md) | 调用 [ModifyDBInstanceSpec](api-rds-2014-08-15-modifydbinstancespec-postgresql.md) 接口，将实例系列升级为集群系列。您需要将 DBInstanceClass 参数取值修改为需要升级的集群系列实例规格， Category 参数取值修改为 Cluster ，其他参数请按需配置。 |
| [DescribeDBInstanceAttribute - 查询实例详情](api-rds-2014-08-15-describedbinstanceattribute-postgresql.md) | 验证升级结果：调用 [DescribeDBInstanceAttribute](api-rds-2014-08-15-describedbinstanceattribute-postgresql.md) 接口，查看 Category 参数取值是否为 Cluster。 如果为 Cluster ，则升级成功。 |
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
