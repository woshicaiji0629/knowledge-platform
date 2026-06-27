# Tair,Redis集群架构的连接模式.组件介绍-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/product-overview/cluster-master-replica-instances

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

# 集群架构

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库 Tair（兼容 Redis）支持多副本集群架构实例，同时也支持集群架构开启读写分离功能。可轻松突破Redis自身单线程瓶颈，满足大容量、高性能的业务需求。集群架构支持代理和直连两种连接模式，您可以根据本章节的说明，选择适合业务需求的连接模式。

## 代理模式（推荐）

代理（Proxy）模式能够大大简化集群架构实例的使用方式，其连接方式与标准架构（主备）相同。代理服务器会自动实现路由转发，将客户端的请求转发到各数据分片，同时代理节点还提供了缓存热点Key、故障转移等高级特性，更多信息请参见[Tair Proxy](products/redis/documents/product-overview/features-of-proxy-nodes.md)[特性说明](products/redis/documents/product-overview/features-of-proxy-nodes.md)。

代理模式的服务架构图和组件说明如下。

### 多副本

多副本集群架构代理模式服务

集群架构代理模式组件说明

| 组件 | 说明 |
| --- | --- |
| 代理服务器（Proxy Server） | 负责将客户端的请求转发到各数据分片。集群架构中存在多个 Proxy 节点提供服务，并互相提供灾备支持。 |
| 数据分片（Data Shards） | 每个数据分片均为一主多备（分别部署在不同机器上）的高可用架构。备节点的数量范围为 1 ~ 4，可以选择部署在备可用区。多个备节点可以提高容灾能力，减少数据丢失的可能性。 |
| 高可用服务（HA） | 主节点（Master）发生故障后，系统会自动在 30 秒内切换至备节点（Replica），以保证服务高可用和数据高可靠。如果实例为双可用区部署，当主可用区存在备节点时，主备切换会优先选择主可用区的备节点进行切换，避免业务跨可用区访问。 |


### 单节点

单节点的集群架构是指的集群分片服务器由单节点组成，当某服务节点出现故障时，系统会重新拉起一个新的Redis进程（没有数据）。当节点故障业务自动切换完成后，对应故障的节点将损失全部数据，业务数据需要重新进行预热，且流量有可能会冲击到后端数据库，业务上需要做好应用程序的预热保护机制。因此，不建议对数据可靠性要求高的敏感性业务使用该架构。

警告

- 

单节点架构不能保障数据可用性和服务连续性，选用前请务必确认风险，不建议您在生产环境中使用该架构的实例。

- 

单节点架构不支持以下功能：[自动或手动备份](products/redis/documents/user-guide/automatic-or-manual-backup.md)、[离线全量](products/redis/documents/user-guide/offline-key-analysis.md)[Key](products/redis/documents/user-guide/offline-key-analysis.md)[分析](products/redis/documents/user-guide/offline-key-analysis.md)和[实例回收站](products/redis/documents/user-guide/manage-instances-in-the-recycle-bin.md)。若您对数据有可靠性要求，推荐使用多副本类型。

单节点集群架构代理模式服务架构

集群架构代理模式组件说明

| 组件 | 说明 |
| --- | --- |
| 代理服务器（proxy servers） | 单节点配置，集群架构中会有多个 Proxy 组成，系统会自动对其实现负载均衡及故障转移。 |
| 数据分片（data shards） | 每个数据分片均为单节点架构，不支持高可用。数据节点故障之后，系统会在 30 秒内重新拉起一个 Redis 进程保证服务高可用，但是该节点的数据将会丢失。 |


### 开启读写分离

云原生版集群架构（代理模式）还支持开启读写分离功能，当读请求流量非常大，超过主节点性能上限时，您可以开启集群架构的读写分离功能。更多信息请参见[集群架构开启读写分离](products/redis/documents/product-overview/read-or-write-splitting-instances-1.md)。

## 直连模式

直连模式为类似连接原生Redis Cluster的方式连接集群。客户端首次连接时会通过DNS将直连地址解析为一个随机数据分片的虚拟IP（VIP）地址，之后即可通过Redis Cluster协议访问各数据分片。集群架构直连模式同样支持多副本与单节点，但不支持开启读写分离，直连模式的服务架构和说明如下。

集群架构直连模式服务架构（以多副本为例）

说明

直连模式与代理模式的连接方式区别较大，相关注意事项和连接示例请参见[使用直连模式连接实例](products/redis/documents/user-guide/use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)。

## 使用场景

- 

数据量较大

相比标准架构，集群架构可以有效地扩展存储量，最大可达16 TB（64 GB * 256分片），能有效地满足业务扩展的需求。

- 

请求负载较大

标准架构无法支撑较大的请求负载，需要采用多分片的部署方式来突破单分片的性能瓶颈。

当读请求流量非常大，超过主节点性能上限时，您可以开启集群架构的读写分类功能。

说明

由于仅云原生版集群架构（代理模式）实例支持开启读写分离，您可以通过新建实例、使用DTS同步数据的方式将其他版本的实例迁移至集群版（开启读写分离）实例。

- 

吞吐密集型应用

相比标准架构，集群架构的吞吐量可通过增加分片数量线性扩展，可以更好地支持热点数据读取、大吞吐类业务。

- 

多KEY操作较少的应用

由于集群为分布式架构，在一次操作多个KEY时需要确保所有KEY均在同一slot中，因此会对多KEY操作带来一些限制。详情请参见[集群架构与读写分离实例的命令限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。

- 

延迟敏感应用

双可用区实例可以在主可用区增加备节点，例如主可用区1个主节点、1个备节点，备可用区1个备节点。既提高了容灾的可靠性，同时也能避免由主备切换后应用跨可用区访问带来延迟升高的问题。

## 注意事项

- 

云原生版集群架构不支持同时使用代理模式和直连模式，建议选择代理模式。

- 

经典版集群架构仅支持单副本、双副本，不支持开启读写分离。

## 集群变配操作指南

- 

添加副本节点数：在实例详情页的节点管理页面中，单击修改，可以增减节点数。

- 

添加只读节点：在实例详情页的节点管理页面中，需要先开启读写分离开关，再单击修改，可以增加只读节点数。

- 

添加分片数：在实例详情页的右上角，选择分片调整>增加分片数量。

- 

变更分片规格：在实例详情页的右上角，选择规格调整>规格升降配。

## 常见问题

Tair集群架构与开源Redis Cluster有什么区别？

相比开源Redis Cluster，云数据库 Tair（兼容 Redis）集群架构在安全性、内核性能、负载均衡和扩缩容等方面具有如下优势：

- 

内核性能提升：Tair集群架构实例在内核性能方面进行大量优化，包含但不限如下。

- 

容灾速度更快，不会产生Gossip广播风暴问题。

- 

在集群实例扩缩容时，支持自动重新平衡分片数据，且在数据重新平衡时对业务请求几乎无影响。

- 

轻松支持大量短连接场景。

- 

便捷运维管理：相比自购服务器搭建Redis数据库，Tair集群架构实例支持多维度访问控制，支持灵活弹性扩缩容，提供丰富的监控指标以及多种高可用容灾方案等，更多信息请参见[与自建](products/redis/documents/product-overview/comparison-between-apsaradb-for-redis-and-self-managed-redis.md)[Redis](products/redis/documents/product-overview/comparison-between-apsaradb-for-redis-and-self-managed-redis.md)[的对比](products/redis/documents/product-overview/comparison-between-apsaradb-for-redis-and-self-managed-redis.md)。

- 

支持代理模式：Tair集群架构实例可选择代理模式，该模式提供代理服务器（Proxy），通过Proxy能实现架构转换，帮助您如同在使用标准架构一样地使用集群架构。同时，Proxy还支持负载均衡和路由转发、管理只读节点流量、缓存热点Key信息与支持集群架构使用多数据库（DB）等，更多信息请参见[Tair Proxy](products/redis/documents/product-overview/features-of-proxy-nodes.md)[特性说明](products/redis/documents/product-overview/features-of-proxy-nodes.md)。

标准架构升级至集群架构后需要修改代码吗？

- 

若实例升级至集群架构代理模式，无需修改代码。您仍可以像使用标准架构一样地使用集群架构，因为[Proxy](products/redis/documents/product-overview/features-of-proxy-nodes.md)[节点](products/redis/documents/product-overview/features-of-proxy-nodes.md)能够实现架构转换。这将显著降低业务改造成本。

- 

若实例升级至集群架构直连模式，需修改连接池代码，以更换为支持Cluster的客户端。

说明

除此之外，您还需了解并遵守集群架构执行多Key（跨Slot）命令、事务以及Lua脚本等相应的规范，更多信息请参见[集群架构命令限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。

集群架构实例变配后，数据是否会自动均衡？

在标准架构升级至集群架构，或在集群架构中增减分片时，实例将自动分析数据的分布情况，并执行数据重平衡。您无需执行额外操作。

此外，Proxy模式额外支持[无感扩缩容](products/redis/documents/product-overview/imperceptible-scaling.md)。而直连模式在客户端正确处理MOVED重定向的情况下，也能实现无感扩缩容。

[上一篇：产品架构](products/redis/documents/product-overview/product-architecture.md)[下一篇：标准架构](products/redis/documents/product-overview/standard-master-replica-instances.md)

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
