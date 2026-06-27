# Tair容灾架构介绍以及如何选择容灾方案-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/product-overview/disaster-recovery

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/redis/documents/product-overview.md)

- [快速入门](products/redis/documents/getting-started.md)

- [Tair AI能力](products/redis/documents/tair-ai-ability.md)

- [操作指南](products/redis/documents/user-guide.md)

- [实践教程](products/redis/documents/use-cases.md)

- [安全合规](products/redis/documents/security-compliance.md)

- [开发参考](products/redis/documents/developer-reference.md)

- [服务支持](products/redis/documents/support.md)

- [视频专区](products/redis/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 灾备方案介绍

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库 Tair（兼容 Redis）作为高性能的Key-Value数据库，在业务场景中往往承载着大量的重要数据，为保障数据安全性，云数据库 Tair（兼容 Redis）提供了多种灾备方案供您选择。

## 容灾架构演进

当实例因不可预料的原因（例如设备故障、机房断电等）发生故障，容灾机制可用于保障数据的一致性和业务可用性。

图 1.容灾架构演进

| 灾备方案 | 灾备级别 | 说明 |
| --- | --- | --- |
| [单可用区高可用方案](products/redis/documents/product-overview/disaster-recovery.md) | ★★★☆☆ | 主备节点部署在同一可用区中的不同机器上，当任一节点发生故障时，由高可用 HA（High Availability）系统自动执行故障切换，避免单点故障引起的服务中断。 |
| [同城容灾（多可用区）方案](products/redis/documents/product-overview/disaster-recovery.md) | ★★★★☆ | 主备节点分别部署在同一地域下两个不同的可用区，当任一可用区因电力、网络等不可抗因素失去通信时，高可用 HA 系统将执行故障切换，确保整个实例的持续可用。 |
| [跨地域容灾方案](products/redis/documents/product-overview/disaster-recovery.md) | ★★★★★ | 由多个子实例构成全球多活实例，所有子实例通过同步通道保持实时数据同步，由通道管理器负责子实例的健康状态监测、主备切换等等异常事件的处理，适用于异地灾备、异地多活、应用就近访问、分摊负载等场景。 |


## 单可用区高可用方案

实例全架构（不含单副本版）均支持单机房高可用架构。由高可用HA（High Availability）系统监控主备节点的健康状态并自动执行故障切换，避免单点故障引起的服务中断。

- 

- 

- 

- 

| 部署架构 | 说明 |
| --- | --- |
| [标准架构（双副本）](products/redis/documents/product-overview/standard-master-replica-instances.md) | 图 2. 标准版-双副本高可用架构 标准架构（双副本）实例采用双机主备（Master-Replica）架构，高可用 HA 模块侦测到主节点故障时，会自动进行主备切换，将 Replica 提升为 Master，而原来的 Master 恢复连接后会成为新的 Replica。 |
| [集群架构（多副本）](products/redis/documents/product-overview/cluster-master-replica-instances.md) | 图 3. 集群版-多副本高可用架构 集群架构（多副本）实例中的数据分片用于承载数据，每个数据分片均为多副本（分别部署在不同机器上）高可用架构，主节点发生故障后，系统会自动进行主备切换保证服务高可用。 |
| [读写分离架构](products/redis/documents/product-overview/read-or-write-splitting-instances-1.md) | 图 4. 读写分离版高可用架构 自动监控各节点的健康状态，异常时发起主备切换或重搭只读节点，并更新相应的路由及权重信息。 Proxy 会实时探测只读节点的状态，当出现下述情况时，Proxy 会执行流量管控动作： 只读节点处于异常状态：Proxy 会降低该节点的服务权重，如果多次无法连接该节点，Proxy 会停止该节点的服务（即不再将流量转发至该节点），待该异常被修复后重新启用该节点。 只读节点处于全量同步状态：Proxy 会暂时停止该节点的服务，直到该节点完成全量同步。 |


## 同城容灾（多可用区）方案

云数据库 Tair（兼容 Redis）提供多可用区的同城容灾架构。如果业务为单一地域部署，且对容灾要求较高，可在创建实例时，选择支持同城容灾的多可用区。操作方法，请参见[创建实例](products/redis/documents/getting-started/step-1-create-an-apsaradb-for-redis-instance.md)。

图 5.创建同城容灾实例

完成创建后，备机房将创建与主机房相同规格的Replica实例，主备机房的实例数据通过专门的复制通道同步。

当主机房出现电力或网络问题时，Replica实例将升级为Master实例，系统调用Config Server接口为Proxy更新路由信息。同时，云数据库 Tair（兼容 Redis）优化了Redis的同步机制，在同步位点上借鉴MySQL的GTID，实现了全局Opid，查找Opid的操作通过后台线程无锁进行，发送AOF binlog是异步同步的过程（可限流），保障了Redis服务的性能。

图 6.同城容灾实例的数据同步过程

## 跨地域容灾方案

随着业务的快速发展，在业务分布较广时，如果还采用跨地域远距离访问的架构，将导致访问的延迟大，影响用户体验。借助阿里云的Tair全球多活（分布式缓存）功能，可帮助您解决业务因跨地域访问导致延迟大的问题，全球多活功能具有如下优势：

- 

可直接创建或指定需要同步的子实例，无需通过业务自身的冗余设计来实现，极大降低业务设计的复杂度，让您专注于上层业务的开发。

- 

可提供跨域复制（Geo-replication）能力，快速实现数据异地灾备和多活。

该功能可应用于跨地域数据同步场景及多媒体、游戏、电商等行业的全球化业务部署等场景。更多介绍，请参见[全球多活](products/redis/documents/user-guide/overview-of-global-distributed-cache-for-tair.md)。

图 7.Tair全球多活架构

## 如何应对故障

故障（例如设备故障、机房断电、自然灾害等）通常可分为主节点故障或可用区级别故障，虽然发生概率较低，但故障可能会导致实例一段时间无法写入、闪断，甚至会造成实例停机或数据丢失（实例的可靠性还与架构息息相关，通常集群架构的可靠性更高）。为了尽可能地降低故障带来的影响，多副本、多可用区实例会在故障时自动执行切换，这会最大限度地缩短停机时间。下文向您介绍不同灾备方案的实例如何应对故障。

### 应对节点故障

当主节点发生故障时：

- 

若实例为单可用区多副本节点（例如具备主、备节点）：系统会在发生节点故障时自动执行故障切换，选取复制延迟最小的备节点成为新的主节点，并更新路由关系。

- 

若实例为单可用区单副本节点：系统会在发生节点故障时创建一个全新的节点，原实例数据会丢失。

- 

若实例为多可用区：系统会在发生节点故障时自动执行故障切换，选取另一可用区的备节点成为新的主节点，并更新路由关系。但此时可能产生实例与其他业务跨机房访问的情况。

说明

在多可用区集群架构中，当主、备可用区都存在备节点时，主备切换会优先选择主可用区的备节点进行切换，避免业务跨可用区访问。

### 应对可用区故障

当发生可用区故障（例如断电、火灾等，造成整个机房不可用）时：

- 

若实例为单可用区部署：实例整体不可用，需要等待该可用区恢复，此时，您可以通过历史的备份数据在其他可用区创建新实例。

- 

若实例为多可用区部署：会触发自动切换。

重要

- 

从安全性来说，选择多可用区、并在每个可用区创建多个副本可以尽可能地减少停机时间，但您需要在发生故障的概率、业务数据的重要性、成本之间作出选择。

- 

全球多活的子实例也适用上述原则，但单个子实例故障时不会影响其他子实例的可用性。推荐全球多活的子实例为多可用区部署，避免因单个子实例故障而导致数据写入失败。

## 相关文档

[通过自定义节点数规避跨可用区切换](products/redis/documents/use-cases/prevent-cross-zone-switchover-by-specifying-the-number-of-nodes.md)

[上一篇：应用场景](products/redis/documents/product-overview/common-scenarios.md)[下一篇：可观测性能力介绍](products/redis/documents/product-overview/observability.md)

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
