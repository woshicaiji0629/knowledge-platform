# 将RDS实例迁移至同一地域内的其他可用区-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-postgresql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-postgresql/getting-started.md)

- [DuckDB分析加速](products/rds/documents/apsaradb-rds-for-postgresql/duckdb-analytics-acceleration.md)

- [RDS for AI](products/rds/documents/apsaradb-rds-for-postgresql/rds-for-ai.md)

- [自研内核 AliPG](products/rds/documents/apsaradb-rds-for-postgresql/proprietary-alipg.md)

- [插件](products/rds/documents/apsaradb-rds-for-postgresql/plug-ins-1.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-postgresql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-postgresql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-postgresql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-postgresql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-postgresql/support.md)

[首页](https://help.aliyun.com/zh)

# 迁移可用区

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以将RDS实例迁移至同一地域内的其他可用区。迁移可用区后，实例的所有属性、配置和连接地址都不会改变。迁移所需时间跟实例的数据量有关，通常为几个小时。

## 前提条件

- 

实例所在的地域有多个可用区时，才支持迁移可用区功能。详情请参见[地域和可用区](https://help.aliyun.com/zh/document_detail/40654.html)。

- 

实例为主实例，且未创建只读实例。

- 

实例状态需为运行中。

说明

暂不支持集群系列实例。

## 使用限制

- 

高性能本地盘实例只支持迁移主可用区。

- 

暂不支持[Serverless](https://help.aliyun.com/zh/document_detail/607742.html#main-2272489)实例迁移可用区。

- 

当实例存储类型为高性能云盘并且开启了[Buffer Pool Extension（BPE）](products/rds/documents/apsaradb-rds-for-postgresql/buffer-pool-extension-bpe.md)时，无法迁移至不支持IO加速的可用区。IO加速支持的地域及可用区请参见[支持范围](products/rds/documents/apsaradb-rds-for-postgresql/buffer-pool-extension-bpe.md)。

您可以关闭IO加速后，再进行可用区迁移。

## 费用

- 

迁移可用区功能免费。即使将实例从单可用区迁移至多个可用区，也不收取费用。

- 

如果您的实例存储类型为SSD云盘，迁移时会自动从SSD云盘升级为ESSD PL1云盘。升级后，存储费用不变。

## 影响

- 

切换时实例可用性会受到短暂影响，请确保应用具有自动重连机制。

- 

迁移可用区会造成虚拟IP（VIP）的变更，请尽量在您的应用程序中使用连接地址进行连接，不要使用IP地址。

- 

迁移可用区期间如果发生主节点切换，会造成虚拟IP（VIP）的变更，请使用连接地址而非IP地址，并请及时清理客户端DNS缓存。对于JVM的应用，建议将TTL设置为不超过60秒，以确保VIP变更时能及时更新。

说明

JVM中设置TTL的方法请参见JDK官方文档：[Class InetAddress](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/net/InetAddress.html)。

- 

可用区迁移后，需重启正在执行的[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts#concept-26592-zh)任务。

- 

如果迁移的目标可用区资源不足，则可能导致迁移可用区失败。

- 

RDS PostgreSQL已不再支持新购SSD云盘，如果您的实例存储类型为SSD云盘，则在迁移可用区时，会自动从SSD云盘升级为ESSD PL1云盘。更多信息，请参见[【通知】部分](products/rds/documents/apsaradb-rds-for-postgresql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[RDS](products/rds/documents/apsaradb-rds-for-postgresql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[实例不再提供](products/rds/documents/apsaradb-rds-for-postgresql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[SSD](products/rds/documents/apsaradb-rds-for-postgresql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[云盘售卖](products/rds/documents/apsaradb-rds-for-postgresql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)。

## 迁移类型

| 迁移类型 | 场景 |
| --- | --- |
| 从一个可用区迁移至另一个可用区 | 实例所在可用区出现满负载或者其他影响实例性能的情况。 |
| 从一个可用区迁移至多个可用区 | 迁移后的主备实例分别位于不同的可用区，实现跨机房容灾。多可用区实例可以承受更高级别的灾难，例如机房级别的故障。 说明 对于包含主备节点的实例，建议迁移至多个可用区，实现实例的跨可用区容灾。 |
| 从多个可用区迁移至一个可用区 | 为了满足特定功能的要求。 |


## 操作步骤

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在基本信息区域，单击迁移可用区。

- 

在弹出的对话框中，选择迁移的主备可用区及交换机，单击确定。

主要参数及配置规则

- 

- 

- 

- 

- 

- 

- 

| 参数 | 配置规则 |
| --- | --- |
| 迁移至主可用区 | 选择新的主可用区和备可用区。 对于高性能本地盘实例，只支持迁移主可用区，不支持迁移备可用区。 对于云盘实例，支持同时迁移主可用区和备可用区，也支持单独迁移主可用区或备可用区。例如： 支持将 新加坡 可用区 A（主） + 可用区 B（备） 迁移至 新加坡 可用区 C（主） + 可用区 D（备） 。 支持将 新加坡 可用区 A（主） + 可用区 B（备） 迁移至 新加坡 可用区 A（主） + 可用区 C（备） 。 说明 单独迁移时，只需配置需要迁移的可用区。 |
| 迁移至备可用区 |  |
| 主可用区交换机 | 选择主、备可用区对应的虚拟交换机。如果当前可用区无虚拟交换机，请参见 [创建交换机](products/vpc/documents/user-guide/create-and-manage-vswitch.md) 。 |
| 备可用区交换机 |  |
| 切换时间 | 立即切换 ：配置后立即切换。 在可维护时间段内切换 ：使用提前设置好的可维护时间段切换，更多信息，请参见 [设置可维护时间段](products/rds/documents/apsaradb-rds-for-postgresql/set-the-maintenance-window-of-an-apsaradb-rds-for-postgresql-instance.md) 。 用户指定时间段生效 ：您可以直接指定切换时间。 |


单击确定后，底层开始拷贝数据到目标可用区，不影响实例运行。拷贝完成后，将按您指定的切换时（立即切换、在可维护时间段内切换或用户指定时间段生效），把流量切换到新链路。

警告

切换时会发生连接闪断。请确保应用具有自动重连机制，否则需手动重连。

由于客户端DNS缓存可能没有及时刷新，部分流量可能在10分钟后才进行切换，导致第二次闪断。客户端采用JVM的应用，建议将JVM配置中的TTL设置为不超过60秒，可确保在连接地址的VIP地址发生变更时，应用程序可以通过重新查询DNS来接收和使用资源的新VIP地址。设置方法请参见本文的[影响](products/rds/documents/apsaradb-rds-for-postgresql/migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region.md)章节。

## 相关API

| API | 描述 |
| --- | --- |
| [MigrateToOtherZone](products/rds/documents/apsaradb-rds-for-postgresql/api-rds-2014-08-15-migratetootherzone-postgresql.md) | 迁移 RDS 实例可用区。 |


[上一篇：主备切换原因](products/rds/documents/apsaradb-rds-for-postgresql/causes-for-primary-secondary-switchovers.md)[下一篇：变更网络类型或交换机](products/rds/documents/apsaradb-rds-for-postgresql/change-the-network-type-and-vswitch.md)

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
