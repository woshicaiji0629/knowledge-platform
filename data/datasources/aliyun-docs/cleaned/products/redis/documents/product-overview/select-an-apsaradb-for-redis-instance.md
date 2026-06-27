# 如何选择阿里云Tair，Redis产品-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/product-overview/select-an-apsaradb-for-redis-instance

# 云数据库 Tair（兼容 Redis）产品选型参考
创建云数据库 Tair（兼容 Redis）实例前，您需要结合产品性能、价格、业务场景（例如用作高速缓存或内存数据库）、工作负载等因素，作出性价比与稳定性最优的决策。本文围绕以上因素，介绍产品类型、容灾方案、架构类型和实例规格，为您的选型提供相关参考。
## 免费试用
阿里云免费试用面向符合条件的新用户，提供一定时间段的免费试用阿里云产品的权益，更多信息请参见[免费试用](https://free.aliyun.com/?searchKey=redis)。
## 快速推荐
单击下表的推荐规格列中链接，您仅需配置地域、网络等选项即可创建出对应规格实例。
| 关注项 | 推荐规格 | 推荐原因 |
| --- | --- | --- |
| 性能优先 | [Tair（企业版）内存型（兼容](https://common-buy.aliyun.com/?commodityCode=kvstore&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22enginetype%22:%22Tair%22,%22paymode%22:%22Prepaid%22,%22cloudarchitecture%22:%22CloudNative%22,%22kvstore_series_type%22:%22tair_rdb%22,%22region%22:%22cn-hangzhou%22,%22kvstore_zonetype%22:%22singlezone%22,%22kvstore_iz%22:%22cn-hangzhou-g%22,%22kvstore_web_type%22:%221%22,%22instance_type%22:%22standard_type%22,%22kvstore_engineversion_type%22:%22rdb6.0%22,%22kvstore_architecture_type%22:%22cluster%22,%22connection_mode%22:%22proxy_on%22,%22shard_type%22:%22share%22,%22shard_class%22:%22tair.rdb.with.proxy.2g%22,%22shard_quantity%22:4,%22rwsplit_switch%22:%22false%22,%22replica_quantity%22:%222%22,%22ro_quantity%22:%220%22,%22kvstore_password%22:%22later%22%7D&regionId=cn-hangzhou) [Redis 6.0）、高可用、启用集群](https://common-buy.aliyun.com/?commodityCode=kvstore&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22enginetype%22:%22Tair%22,%22paymode%22:%22Prepaid%22,%22cloudarchitecture%22:%22CloudNative%22,%22kvstore_series_type%22:%22tair_rdb%22,%22region%22:%22cn-hangzhou%22,%22kvstore_zonetype%22:%22singlezone%22,%22kvstore_iz%22:%22cn-hangzhou-g%22,%22kvstore_web_type%22:%221%22,%22instance_type%22:%22standard_type%22,%22kvstore_engineversion_type%22:%22rdb6.0%22,%22kvstore_architecture_type%22:%22cluster%22,%22connection_mode%22:%22proxy_on%22,%22shard_type%22:%22share%22,%22shard_class%22:%22tair.rdb.with.proxy.2g%22,%22shard_quantity%22:4,%22rwsplit_switch%22:%22false%22,%22replica_quantity%22:%222%22,%22ro_quantity%22:%220%22,%22kvstore_password%22:%22later%22%7D&regionId=cn-hangzhou) | 在 Redis 开源版 能力的基础上提供： 更强的性能 ，采用多线程模型在流量突增场景中能够更好的保证响应时延与性能稳定性。 更高的数据可靠性 ，支持 [半同步](../user-guide/modify-the-synchronization-mode-of-a-persistent-memory-optimized-instance.md) 、 [按时间点恢复数据](../user-guide/use-data-flashback-to-restore-data-by-point-in-time.md) 。 更丰富的数据结构 ， [Tair](../developer-reference/extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md) [扩展数据结构](../developer-reference/extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md) 可简化业务代码逻辑。 |
| 性能和成本均衡 | [Redis](https://common-buy.aliyun.com/?&commodityCode=kvstore_prepaid_public_cn&request={%22instance_scene%22:%22professional%22,%22region%22:%22cn-beijing%22,%22kvstore_iz%22:%22cn-beijing-l%22,%22kvstore_engineversion_type%22:%226.0%22,%22kvstore_architecture_type%22:%22cluster%22,%22shard_class%22:%22redis.shard.mid.ce%22,%22shard_quantity%22:%224%22,%22shard_class%22:%22redis.shard.with.proxy.mid.ce%22}) [开源版](https://common-buy.aliyun.com/?&commodityCode=kvstore_prepaid_public_cn&request={%22instance_scene%22:%22professional%22,%22region%22:%22cn-beijing%22,%22kvstore_iz%22:%22cn-beijing-l%22,%22kvstore_engineversion_type%22:%226.0%22,%22kvstore_architecture_type%22:%22cluster%22,%22shard_class%22:%22redis.shard.mid.ce%22,%22shard_quantity%22:%224%22,%22shard_class%22:%22redis.shard.with.proxy.mid.ce%22}) [6.0、高可用、启用集群](https://common-buy.aliyun.com/?&commodityCode=kvstore_prepaid_public_cn&request={%22instance_scene%22:%22professional%22,%22region%22:%22cn-beijing%22,%22kvstore_iz%22:%22cn-beijing-l%22,%22kvstore_engineversion_type%22:%226.0%22,%22kvstore_architecture_type%22:%22cluster%22,%22shard_class%22:%22redis.shard.mid.ce%22,%22shard_quantity%22:%224%22,%22shard_class%22:%22redis.shard.with.proxy.mid.ce%22}) | 高可用性 ：通过主备复制和故障自动转移机制，确保数据的高可用性。 高扩展性 ：可通过增加分片数或增加分片中节点数提升容量和性能。 |
| 成本优先 | [Redis](https://common-buy.aliyun.com/?&commodityCode=kvstore_prepaid_public_cn&request={%22instance_scene%22:%22professional%22,%22region%22:%22cn-beijing%22,%22kvstore_iz%22:%22cn-beijing-l%22,%22kvstore_engineversion_type%22:%226.0%22,%22shard_class%22:%22redis.shard.large.ce%22}) [开源版](https://common-buy.aliyun.com/?&commodityCode=kvstore_prepaid_public_cn&request={%22instance_scene%22:%22professional%22,%22region%22:%22cn-beijing%22,%22kvstore_iz%22:%22cn-beijing-l%22,%22kvstore_engineversion_type%22:%226.0%22,%22shard_class%22:%22redis.shard.large.ce%22}) [6.0、高可用、不启用集群](https://common-buy.aliyun.com/?&commodityCode=kvstore_prepaid_public_cn&request={%22instance_scene%22:%22professional%22,%22region%22:%22cn-beijing%22,%22kvstore_iz%22:%22cn-beijing-l%22,%22kvstore_engineversion_type%22:%226.0%22,%22shard_class%22:%22redis.shard.large.ce%22}) | 高可用性 ：通过主备复制和故障自动转移机制，确保数据的高可用性。 低成本 ：支持最小容量 256 MB，适合用于业务起步阶段。 |
## 选型参考
### 选择产品类型
云数据库 Tair（兼容 Redis）在提供Redis开源版的同时，还基于阿里巴巴的业务实践研发并推出企业级内存数据库产品--Tair（企业版）。Tair（企业版）从访问延时、持久化需求、整体成本这三个核心维度考量，推出了内存型（DRAM），持久内存型（NVM），磁盘型（ESSD/SSD）产品，为您提供更强的性能、更多的数据结构和更灵活的存储方式，满足不同场景下的业务需求。
重要
各系列支持的命令与参数，请参见[Redis](../developer-reference/overview-3.md)[命令支持概览](../developer-reference/overview-3.md)和[设置参数](../user-guide/modify-the-values-of-parameters-for-an-instance.md)。
产品类型简介如下表：
| 对比项 | Redis 开源版 | Tair（企业版） |  |  |
| --- | --- | --- | --- | --- |
| [部署模式](comparison-between-tair-instances-that-cloud-native-and-classic.md) | 云原生（推荐） 经典 | 云原生 |  |  |
| 存储介质 | 内存 | [内存型](dram-based-instances.md) | [持久内存型](persistent-memory-optimized-instances-1.md) | [磁盘型](essd-based-instances-1.md) |
| 兼容 Redis 版本 | 5.0、6.0、7.0 | 5.0、6.0、7.0 | 6.0 | 6.0 |
| 性能 | 100%（基准） | 300% | 90% | 最高 60% |
| 特点 | 云上开源 Redis 服务。 | 提供丰富的自研 [扩展数据结构](../developer-reference/extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md) ，帮助您精简代码并提高业务整体性能。 支持企业级特性： [按时间点恢复数据](../user-guide/use-data-flashback-to-restore-data-by-point-in-time.md) 、代理查询缓存、 [全球多活](../user-guide/overview-of-global-distributed-cache-for-tair.md) 等。 支持高级加密： [TLS](../user-guide/enable-tls-encryption.md) [加密连接](../user-guide/enable-tls-encryption.md) 、 [透明数据加密](../user-guide/enable-tde.md) [TDE](../user-guide/enable-tde.md) 等。 | 高性价比：成本对比 Redis 开源版最高可降低 30%。 更高可靠性：同步持久化，每个写操作在主节点持久化成功之后返回。 | 数据通过磁盘持久化存储，内存用于请求加速。 |
| 适用场景参考 | 开源 Redis 场景。 | 对请求的响应时间要求极高场景，如视频直播、在线教育，在线游戏，RTA 等。 千万级 QPS 使用缓存场景，如在线购物、社交网络等。 | 海量数据下追求性价比和数据可靠性的场景，如物联网。 | 需要大存储空间且访问性能较高的温冷数据存储，且以成本作为首要考虑因素的场景，如文件存储的索引、历史消息的长期存储等。 |
说明
Redis开源版和Tair（企业版）的功能和性能的差异详情，请参见[特性数据与对比](comparison-between-apsaradb-for-redis-enhanced-edition-and-apsaradb-for-redis-community-edition.md)。
### 选择容灾方案
云数据库 Tair（兼容 Redis）提供了单可用区、同城、跨地域三种容灾方式，可根据您的业务要求进行选择。
| 灾备方案 | 说明 | 操作指引 |
| --- | --- | --- |
| [单可用区高可用方案](disaster-recovery.md) | 主备节点部署在同一可用区中的不同机器上，提供机器级别故障恢复能力。 | 在售卖页 可用区类型 选择 单可用区 。 |
| [同城容灾（多可用区）方案](disaster-recovery.md) | 主备节点部署在同一地域下的不同可用区（机房）中，提供机房级别故障恢复能力。 | 在售卖页 可用区类型 选择 双可用区 。 |
| [跨地域容灾方案](disaster-recovery.md) | 由多个子实例部署在不同地域构成全球分布式实例，提供地域级别（自然灾害）故障恢复能力。更多介绍，请参见 [全球多活](../user-guide/overview-of-global-distributed-cache-for-tair.md) 。 | 具体操作，请参见 [创建分布式实例](../user-guide/create-a-distributed-instance.md) 。 |
### 选择架构类型
云数据库 Tair（兼容 Redis）支持标准（不启用集群）、集群两种架构类型，以及可选的读写分离功能，可满足不同的业务场景对业务读写能力、数据量和性能要求。
说明
下表默认介绍分片为高可用（双副本）类型的实例架构。标准架构和集群架构还支持单节点（单副本）类型，但单节点类型无数据热备功能，仅适用于测试及纯缓存场景。
| 实例架构 | 架构模型 | 数据分布 | 适用场景 | 读写分离 |
| --- | --- | --- | --- | --- |
| [标准架构](standard-master-replica-instances.md) | 1 分片，分片采用主备（master-replica）模型。 | 数据全量存储在一个分片中。 | 单个节点能承担业务数据和流量。 命令相对简单，排序和计算之类的命令较少。 | 可选是否开启，支持自定义只读节点数量，最多 1 主 9 只读节点。 |
| [集群架构](cluster-master-replica-instances.md) | 由代理节点和多个分片构成，每个分片采用主备模型。 | 数据分布在各分片中。 | 单分片无法承载全量业务数据和流量。 涉及命令复杂，执行耗时较高。 | 可选是否开启，支持自定义只读节点数量，每个分片最多 1 主 4 只读节点。 |
### 选择实例规格
您需要综合业务预估量（容量、带宽、连接数、QPS等）选择合适的实例规格购买量（分片规格和分片数）。建议安全规格：（预估量÷购买量）< 80%。
在预估容量时，无需考虑持久化Fork写时复制占用的内存开销以及增强功能（如安全白名单、审计、大Key、热Key等）的内存开销，这些开销由阿里云承担，不会占用购买的实例规格容量。
重要
[大](../user-guide/identify-and-handle-large-keys-and-hotkeys.md)[Key](../user-guide/identify-and-handle-large-keys-and-hotkeys.md)是Redis使用中的常见问题。如果集群总容量较大而单分片容量较小，当业务产生大Key时，更容易造成大Key所在分片容量用尽。
集群架构的分片规格选择建议：
| 实例总容量 | 建议分片规格 |
| --- | --- |
| 16 GB～64 GB | 2 GB 及以上 |
| 64 GB～256 GB | 4 GB 及以上 |
| 大于 256 GB | 8 GB 及以上 |
说明
在购买后，如果您的业务变动导致当前所选规格不满足业务需求，可随时[变更实例配置](../user-guide/change-the-configurations-of-an-instance.md)。
## 后续操作指引
[购买](https://common-buy.aliyun.com/?enginetype=Redis&commodityCode=kvstore_prepaid_public_cn)[Redis](https://common-buy.aliyun.com/?enginetype=Redis&commodityCode=kvstore_prepaid_public_cn)[开源版](https://common-buy.aliyun.com/?enginetype=Redis&commodityCode=kvstore_prepaid_public_cn)或[购买](https://common-buy.aliyun.com/?enginetype=Tair&commodityCode=kvstore_pretair_public_cn&regionId=cn-hangzhou)[Tair（企业版）](https://common-buy.aliyun.com/?enginetype=Tair&commodityCode=kvstore_pretair_public_cn&regionId=cn-hangzhou)
[Redis](../user-guide/overview-5.md)[数据迁移方案](../user-guide/overview-5.md)
[通过](../user-guide/use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[redis-cli](../user-guide/use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[连接实例](../user-guide/use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)
[客户端程序连接教程](../user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance.md)
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
