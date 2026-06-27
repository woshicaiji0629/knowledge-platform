# 将RDS实例迁移至同地域其他可用区-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/migrate-an-apsaradb-rds-for-mysql-instance-across-zones-in-the-same-region

# 迁移可用区
您可以将RDS实例迁移至同一地域内的其他可用区。迁移所需时间跟实例的数据量有关，通常为小时级。
## 前提条件
RDS实例需满足以下条件：
实例系列：高可用系列、基础系列（不支持Serverless实例）
实例规格：不能是[历史规格](primary-apsaradb-rds-for-mysql-instance-types.md)。如需变更实例规格，请参见[变更配置](change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)。
实例运行状态：运行中
说明
如果当前实例创建了只读实例，则只读实例的状态也需要为运行中，否则主节点迁移可用区时将报错OperationDenied.MasterDBInstancestate。
如果为云盘实例，内核小版本不可低于20201031。如何升级内核小版本，请参见[升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-mysql-instance.md)。
实例所在的地域需要有多个可用区，才支持迁移可用区功能。关于地域和可用区的详情，请参见[地域和可用区](https://help.aliyun.com/zh/document_detail/40654.html#concept-2459516)。
实例未开通共享代理。
说明
确认共享代理的方法：您可以在实例控制台的数据库代理页面查看，如果有读写分离（共享）页签表示当前使用的是共享代理。
共享代理功能已于2021年04月01日停止更新维护，若您仍在使用共享代理，建议您[升级共享代理为独享型代理](upgrade-the-database-proxy-of-an-apsaradb-rds-for-mysql-instance-from-a-shared-proxy-to-a-dedicated-proxy.md)。
使用独享型代理或者通用型代理，不会影响可用区迁移。
其他引擎迁移可用区请参见：
[PostgreSQL](../apsaradb-rds-for-postgresql/migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region.md)[迁移可用区](../apsaradb-rds-for-postgresql/migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region.md)
[SQL Server](../apsaradb-rds-for-sql-server/migrate-an-apsaradb-rds-for-sql-server-instance-across-zones.md)[迁移可用区](../apsaradb-rds-for-sql-server/migrate-an-apsaradb-rds-for-sql-server-instance-across-zones.md)
## 费用
迁移可用区功能免费。即使将实例从单可用区迁移至多个可用区，也不收取费用。
## 注意事项
仅支持在同地域下的可用区之间进行迁移。如需跨地域迁移可用区，可以在目标地域和可用区[购买新实例](create-an-apsaradb-rds-for-mysql-instance-1.md)，使用DTS[将原实例数据迁移至新实例](migrate-data-between-apsaradb-rds-for-mysql-instances.md)，检查无误后[释放原实例](release-or-unsubscribe-from-an-instance.md)。
主节点切换：迁移可用区期间可能会导致主节点切换，造成主节点连接地址、代理连接地址短时间不可用，请确保应用具有自动重连机制。若无自动重连机制，请手动进行应用与数据库的重连。具体影响请参见[实例切换的影响](untitled-document-1701914031929.md)。主节点切换的场景如下：
当主节点目标可用区与主节点当前可用区不一致时，会发生主节点切换。
当主节点目标可用区与当前主实例网络资源所在可用区不一致时，会发生主节点切换。
虚拟IP（VIP）变更：迁移可用区期间如果发生主节点切换，会造成虚拟IP（VIP）的变更，连接地址不会发生变化，请尽量在您的应用程序中使用连接地址进行连接，请勿使用IP地址。
如果您的RDS MySQL实例挂载在PolarDB-X实例之下，VIP的变更会影响到RDS实例与PolarDB-X实例之间的连通性，请及时手动修复。更多信息，请参见[修复分库连接](https://help.aliyun.com/zh/polardb/polardb-for-xscale/user-guide/fix-database-shard-connections#multiTask294)。
请及时清理客户端DNS缓存。客户端采用JVM的应用，建议将JVM配置中的TTL设置为不超过60秒，可确保在连接地址的VIP地址发生变更时，应用程序可以通过重新查询DNS来接收和使用资源的新VIP地址。
说明
JVM中设置TTL的方法请参见JDK官方文档：[Class InetAddress](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/net/InetAddress.html)。
DTS任务中断：如果有正在执行的[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts#concept-26592-zh)任务，可用区迁移后，需要重启相应的DTS任务。
重新创建表文件：迁移可用区会重新创建表文件，从而导致表文件的创建时间发生变化，进而引起INFORMATION_SCHEMA中表的CREATE_TIME字段发生变化。
如果迁移的目标可用区资源不足，则可能迁移可用区失败。
迁移可用区时，不支持只更改交换机。若您需要修改实例的交换机，请参见[切换专有网络](change-the-vpc-and-vswitch-for-an-apsaradb-rds-for-mysql-instance.md)[VPC](change-the-vpc-and-vswitch-for-an-apsaradb-rds-for-mysql-instance.md)[和虚拟交换机](change-the-vpc-and-vswitch-for-an-apsaradb-rds-for-mysql-instance.md)。
当实例存储类型为高性能云盘并且开启了[Buffer Pool Extension（BPE）功能](buffer-pool-extension-bpe.md)时，无法迁移至不支持Buffer Pool Extension（BPE）的可用区。Buffer Pool Extension（BPE）支持的地域及可用区请参见[适用范围](buffer-pool-extension-bpe.md)。
您可以关闭Buffer Pool Extension（BPE）后，再进行可用区迁移。
## 操作步骤
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在实例基本信息页面，单击右上角迁移可用区。
说明
如果控制台没有迁移可用区按钮，请确认您的实例是否符合前提条件。
在将实例迁移至其他可用区对话框中，选择目标可用区、目标可用区交换机和切换时间，单击确定。
重要
在迁移至目标可用区时，必须确保该可用区内已配置专有网络（VPC）和至少一个交换机（VSwitch）。若目标可用区内不存在交换机，则无法进行选择和迁移，请先[创建交换机](../../../vpc/documents/user-guide/create-and-manage-vswitch.md)。
| 迁移场景 | 说明 |
| --- | --- |
| 从一个可用区迁移至另一个可用区 | 主节点目标可用区 和 备节点目标可用区 选择相同的可用区。 例如将 新加坡 可用区 C（主）+ 可用区 C（备） 迁移至 新加坡 可用区 A（主）+ 可用区 A（备） 。 |
| 从一个可用区迁移至多个可用区 | 主节点目标可用区 和 备节点目标可用区 选择不同的可用区。 例如将 新加坡 可用区 C（主）+ 可用区 C（备） 迁移至 新加坡 可用区 B（主）+ 可用区 A（备） 。 说明 迁移后的主备节点分别位于不同的可用区，能够实现跨可用区容灾。 相对于单可用区实例，多可用区实例可以承受更高级别的灾难。例如，单可用区实例可以承受服务器和机架级别的故障，而多可用区实例可以承受机房级别的故障。 对于包含主备节点的实例，建议迁移至多个可用区，实现实例的跨可用区容灾。 |
| 从多个可用区迁移至一个可用区 | 主节点目标可用区 和 备节点目标可用区 选择相同的可用区。 例如将 新加坡 可用区 B（主）+ 可用区 A（备） 迁移至 新加坡 可用区 C（主）+ 可用区 C（备） 。 说明 实例单可用区部署不具备跨可用区容灾能力，建议迁移至多可用区。 |
| 从多个可用区迁移至多个可用区 | 主节点目标可用区 和 备节点目标可用区 选择不同的可用区。 例如将 新加坡 可用区 B（主）+ 可用区 C（备） 迁移至 新加坡 可用区 A（主）+ 可用区 B（备） 。 |
重要
您也可以选中我需要变更配置，在迁移可用区的同时变更实例规格和存储空间。变更配置会产生费用，请根据需要进行。
系统会按您指定的切换时间（立即切换或在可维护时间段内进行切换）进行可用区迁移（同时若您选择的交换机发生了变更，实例将切换到新链路），请确保应用具有自动重连机制。若应用没有自动重连机制，需手动重连。
由于客户端DNS缓存可能没有及时刷新，部分流量可能在10分钟后才进行切换，在切换过程中实例将发生第二次切换，请确保应用具有自动重连机制。若应用没有自动重连机制，需手动重连。
实例切换的影响请参见[实例切换的影响](untitled-document-1701914031929.md)。
在迁移可用区弹窗中，确认迁移前后的可用区信息，并单击确定。
## 相关API
| API | 描述 |
| --- | --- |
| [迁移可用区](../api-migrate-an-instance-across-zones.md) | 迁移 RDS 实例可用区。 |
## 常见问题
Q：迁移过程中发生数据写入，切换后对原有数据是否有影响？对于迁移过程中新写入的数据，切换后新数据是否还会保留？
A：原有数据不会有影响；对于迁移过程中新写入的数据会保留。
重要
迁移过程中会出现实例切换，请确保应用具有自动重连机制。若应用没有自动重连机制，需手动重连。实例切换的影响请参见[实例切换的影响](untitled-document-1701914031929.md)。
Q：实例可用区迁移时间与什么有关？
A：对于高性能本地盘实例，迁移时间与数据量成正比，数据量越大迁移时间越长，通常为几个小时。对于云盘实例，通常在一个小时内完成。
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
