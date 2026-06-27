# Tair Proxy特性与路由转发规则-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/product-overview/features-of-proxy-nodes

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

# Tair Proxy特性说明

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在云数据库 Tair（兼容 Redis）集群架构和读写分离架构中，代理服务器（Proxy）承担着路由转发、负载均衡和故障转移等职责，可以帮助您简化客户端的逻辑，同时支持多数据库（DB）、缓存热点数据等高级功能。通过了解Proxy的路由转发规则和特定命令的处理方式，有助于您设计更高效的业务系统。

## Proxy介绍

代理服务器（Proxy）是Tair实例中的一个组件（单节点架构），不会占用数据分片的资源，通过多个Proxy节点实现负载均衡及故障转移。

- 

- 

| Proxy 能力 | 说明 |
| --- | --- |
| 集群版使用模式转换 | Proxy 能够实现架构转换，帮助您如同在使用标准架构一样地使用集群架构。Proxy 支持对 DEL 、 EXISTS 、 MGET 、 MSET 、 SDIFF 与 UNLINK 等命令进行跨 Slot 的多 Key 操作，更多信息请参见 [代理模式（Proxy）支持的命令列表](products/redis/documents/developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md) 。 当标准架构无法支撑业务发展时，您无需修改代码即可将标准架构的数据迁移至带有 Proxy 的集群架构，大幅度降低业务改造成本。 |
| 负载均衡和路由转发 | Proxy 与后端的数据分片建立长连接，负责请求负载均衡和路由转发操作，关于转发规则的介绍，请参见 [Proxy](products/redis/documents/product-overview/features-of-proxy-nodes.md) [的路由转发规则](products/redis/documents/product-overview/features-of-proxy-nodes.md) 。 |
| 管理只读节点流量 | Proxy 会实时探测只读节点的状态，当出现下述情况时，Proxy 会执行流量管控动作： 只读节点处于异常状态：Proxy 会降低该节点的服务权重，如果多次无法连接该节点，Proxy 会停止该节点的服务（即不再将流量转发至该节点），待该异常被修复后重新启用该节点。 只读节点处于全量同步状态：Proxy 会暂时停止该节点的服务，直到该节点完成全量同步。 |
| [代理查询缓存](products/redis/documents/product-overview/features-of-proxy-nodes.md) | 开启代理查询缓存功能（Proxy Query Cache）后，Proxy 会缓存热点 Key 对应的请求和返回信息，当在有效时间内收到同样的请求时直接返回结果至客户端，无需和后端的数据分片交互，可更好地改善对热点 Key 的发起大量读请求导致的访问倾斜。 说明 您可以设置 query_cache_enabled [参数](products/redis/documents/user-guide/parameter-support.md) 开启该功能，仅 Tair 内存型、持久内存型实例支持该功能。 |
| 支持多数据库（DB） | 集群模式下，原生 Redis 和 Cluster client 均不支持多数据库（DB）功能，只使用默认的 0 号数据库，也不支持 SELECT 命令。但您可以通过 Proxy 访问集群实例，支持多数据库（DB）功能，支持使用 SELECT 命令，集群版实例默认为 256 个 DB。 说明 若您使用 StackExchange.Redis 客户端，请使用 StackExchange.Redis 2.7.20 及以上版本，否则会产生报错，更多信息请参见 [StackExchange.Redis](products/redis/documents/product-overview/notice-suggestions-for-upgrading-stackexchange-redis-clients.md) [升级公告](products/redis/documents/product-overview/notice-suggestions-for-upgrading-stackexchange-redis-clients.md) 。 |


说明

由于Proxy的演进，Proxy的个数并不完全代表Proxy处理能力，阿里云会保证集群规格中Proxy的配比符合规格说明的要求。

## Proxy的路由转发规则

说明

关于各类命令的介绍，请参见[命令概览](products/redis/documents/developer-reference/overview-3.md)。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 架构 | 转发规则 | 说明 |
| --- | --- | --- |
| 集群架构 | 基础转发规则 | 对于操作单个 Key 的命令，Proxy 会根据 Key 所属的 Slot（槽）将请求发送给所属的数据分片。 对于操作多个 Key 的命令，如果这些 Key 是储存在不同的数据分片，Proxy 会将命令拆分成多个命令分别发送给对应的分片。 说明 自 Redis 开源版 5.0 版本的 5.0.1 小版本起，以及在 6.0、7.0 及更高版本中，Proxy 对命令进行 Slot 级别拆分，与 Redis 社区保持一致。 但 Redis 开源版 5.0 版本在 5.0.1 之前的小版本，以及在 4.0、2.8 版本中，Proxy 对命令进行分片级别拆分。当这部分实例升级至 Redis 开源版 5.0 及以上版本时，由于命令拆分规则的变化，可能会导致 QPS 增加以及流量略有上升。然而，由于 Proxy 是以 Pipeline 方式投递命令，因此对性能的影响相对较小。 |
| 特定命令转发规则 | 发布订阅类命令 对于 PUBLISH 、 SUBSCRIBE 等发布订阅命令，Proxy 会根据 channel name 进行 Hash 计算，并路由至对应数据分片。Pub/Sub 类命令虽然不会往数据库中写入数据，但仍会占用一定的内存和资源，资源消耗主要体现在客户端连接、订阅状态管理和消息缓冲区上。 例如某 channel 属于数据分片 1 ，那么订阅该频道的客户端会占用数据分片 1 的内存、CPU、网络带宽等资源。 说明 您可以在控制台的 [性能监控](products/redis/documents/user-guide/view-monitoring-data.md) 页面选择 数据节点 ，然后将自定义监控项设置为 Pub/Sub 监控组 ，即可查看各数据分片（默认展示第一个数据分片）中发布与订阅（Pub/Sub）相关命令的监控信息。 阿里云自研的命令 使用阿里云自研的命令（例如 IINFO 、 ISCAN 等）时，如果通过 idx 参数指定了数据分片 ID，Proxy 会将这些命令发送到指定的数据分片。更多信息，请参见 [阿里云自研的](products/redis/documents/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode.md) [Proxy](products/redis/documents/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode.md) [命令](products/redis/documents/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode.md) 。 |  |
| 读写分离架构 | 基础转发规则 | 写请求：Proxy 将其直接转发到主节点（Master）。 读请求：Proxy 将读请求平均分配到主节点和只读节点，暂不支持自定义控制。例如拥有 3 个只读节点的实例，主节点和 3 个只读节点的读权重均为 25%。 说明 SLOWLOG 和 DBSIZE 也属于读命令。 |
| 特定命令转发规则 | SCAN 类命令 当您执行 HSCAN 、 SSCAN 、 ZSCAN 命令时，Proxy 会先计算 Key 所属的 Slot，然后通过取模计算确定目标节点，从而将请求均匀分配至主节点和只读节点。 阿里云自研的命令 使用阿里云自研的命令（例如 RIINFO 、 RIMONITOR 等）时，可通过 ro_slave_idx 参数指定该命令要转发到的只读节点，通过 idx 参数指定该命令要转发到的数据分片。更多信息，请参见 [阿里云自研的](products/redis/documents/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode.md) [Proxy](products/redis/documents/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode.md) [命令](products/redis/documents/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode.md) 。 其他命令 Proxy 会将事务命令（ MULTI 或 EXEC ）、Lua 脚本命令 （ EVAL 或 EVALSHA ）、 SCAN 、 INFO 、发布订阅命令（ PUBLISH 、 SUBSCRIBE 等）转发至主节点。 |  |


## 代理查询缓存

代理节点支持缓存：包含热点Key的请求和对应查询结果。当Proxy在缓存有效期内收到同样请求时，将直接返回结果至客户端，无需和后端的数据分片交互。本功能可缓解或预防热点Key读请求引发的访问性能倾斜问题。

- 

此热点Key与[Top Key](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md)[统计](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md)功能中的热Key（QPS）一致，由数据库内核根据排序和统计算法进行识别。默认为Key的QPS超过5000，也可以通过bigkey-threshold参数自定义阈值。

- 

若热点Key在缓存有效期内被修改，其修改结果不会同步至缓存中。即后续请求可能会读到缓存中的脏数据，直至缓存失效。对此，您可以根据实际情况缩短缓存有效期。

说明

- 

Proxy节点并不缓存整个热点Key，而是缓存包含热点Key的请求和对应查询结果。

- 

本功能仅支持Tair内存型、持久内存型实例，且实例为集群架构代理模式或读写分离架构。

应用场景

适用于热搜榜单、大V用户信息、游戏公告等场景，应用程序能够容忍稍旧的数据。

功能架构使用方法

本功能默认关闭，您可以设置query_cache_enabled[参数](products/redis/documents/user-guide/parameter-support.md)开启该功能。

查看使用方法详细说明

- 

- 

- 

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| query_cache_enabled | 代理节点查询缓存功能。启用后，代理节点会缓存热点 Key 对应的请求和查询结果，当在有效时间内收到同样的请求时直接返回结果至客户端，无需和后端的数据分片交互。 重要 由于代理节点中缓存的热点 Key 的键值对信息在有效时间内不会更新，在启用该功能前，您需要确认业务上是否允许数据在缓存有效时间内的 最终一致性 。 query_cache_enabled ：是否启用该功能。取值为 0 （不启用、默认）、 1 （启用）。 query_cache_expire ：缓存数据的有效时间，单位为毫秒，取值范围为[100-60000]，默认为 1000。 若缓存数据在有效期内被修改，修改后的数据不会同步至缓存中，即相同的读请求会获取到缓存中的脏数据，直至缓存失效。 您需要根据具体的业务场景和对脏数据的容忍度谨慎评估该参数的值，该值设置过小会降低缓存的命中率，设置过大会导致客户端在较长的时间内读取到的是脏数据。 query_cache_mode ：代理节点查询缓存功能的工作模式，取值如下。 0 （默认）：只缓存数据分片推送的热点 Key。 1 ：缓存所有 Key 并进行根据最近最少使用算法 LRU（Least Recently Used）进行淘汰。 由于代理节点的缓存空间有限（代理节点每个线程 100 MB），若设置该参数的值为 1 ，代理节点将按照 LRU 算法淘汰 Key，可能降低缓存的命中率，从而引起整体性能的下降。 |
| query_cache_expire |  |
| query_cache_mode |  |


您可以通过Tair自研的QUERYCACHE KEYS、QUERYCACHE INFO、QUERYCACHE LISTALL命令，查看代理查询缓存的使用情况。

查看使用情况

QUERYCACHE KEYS

命令格式：QUERYCACHE KEYS

命令描述：查询代理节点中已缓存的所有热点Key，将返回每个热点Key的数据库名和Key名称信息。

命令示例：

QUERYCACHE KEYS

返回示例：

1) 1) (integer) 0 2) "key:000000000003" 2) 1) (integer) 0 2) "key:000000000001" 3) 1) (integer) 0 2) "key:000000000002" 4) 1) (integer) 0 2) "key:000000000000"

QUERYCACHE INFO

命令格式：QUERYCACHE INFO

命令描述：获取代理查询缓存的运行情况。

命令示例：

QUERYCACHE INFO

返回示例：

1) "put_qps:4.00" 2) "get_qps:16570.00" 3) "hit_rate:99.98" 4) "memory_size:180" 5) "query_count:4" 6) "bandwidth_limit_query_cnt:0" 7) "qps_limit_query_cnt:0"

返回示例说明：

- 

put_qps：数据节点每秒往Querycache写入的次数。

- 

get_qps：客户端每秒从Querycache中读取的次数。

- 

hit_rate：缓存的命中率。

- 

memory_size：缓存数据占用的内存容量，单位为字节。

- 

query_count：已缓存的请求的数量。

- 

bandwidth_limit_query_cnt：因带宽限制访问Querycache被限流的次数，默认未开启限制。

- 

qps_limit_query_cnt：因QPS限制访问Querycache被限流的次数，默认未开启限制。

QUERYCACHE LISTALL

命令格式：QUERYCACHE LISTALL

命令描述：获取已缓存的所有请求命令。

命令示例：

QUERYCACHE LISTALL

返回示例：

1) 1) (integer) 0 2) "*2\r\n$3\r\nGET\r\n$16\r\nkey:000000000000\r\n" 3) (integer) 668 2) 1) (integer) 0 2) "*2\r\n$3\r\nGET\r\n$16\r\nkey:000000000001\r\n" 3) (integer) 668 3) 1) (integer) 0 2) "*2\r\n$3\r\nGET\r\n$16\r\nkey:000000000003\r\n" 3) (integer) 668 4) 1) (integer) 0 2) "*2\r\n$3\r\nGET\r\n$16\r\nkey:000000000002\r\n" 3) (integer) 667

返回示例说明：每个请求命令的信息由三行信息组成，分别为数据库名、请求命令的完整内容（格式遵照[Redis](https://valkey.io/topics/protocol/)[协议规范](https://valkey.io/topics/protocol/)）、剩余生存时间（单位为毫秒）。

## 连接数使用说明

通常情况下，Proxy通过与数据分片建立长连接来处理请求。当请求中包含以下命令时，Proxy会根据命令的处理需求在相应的数据分片上创建额外的连接，此时连接无法聚合，实例的最大连接数会受到数据节点单个分片的限制（单个分片的限制请参见具体的实例规格）。您需要合理使用下述命令，避免连接数超限。

说明

代理模式下，Redis社区版实例每个数据分片的连接数上限为10,000，Tair（企业版）实例每个数据分片的连接数上限为30,000。

- 

阻塞类命令：BRPOP、BRPOPLPUSH、BLPOP、BZPOPMAX、BZPOPMIN、BLMOVE、BLMPOP、BZMPOP。

- 

事务类命令：MULTI、EXEC、WATCH。

- 

MONITOR类命令：MONITOR、IMONITOR、RIMONITOR。

- 

订阅命令：SUBSCRIBE、UNSUBSCRIBE、PSUBSCRIBE、PUNSUBSCRIBE、SSUBSCRIBE、SUNSUBSCRIBE。

## 常见问题

- 

Q：是否支持将只进行读操作的Lua脚本转发至只读节点吗？

A：支持，但需要满足以下条件。

- 

使用只读账号，更多信息请参见[创建与管理账号](products/redis/documents/user-guide/create-and-manage-database-accounts.md)。

- 

将实例的readonly_lua_route_ronode_enable参数的值设置为1，即仅包含读操作的Lua脚本会被转发到只读副本处理。具体操作，请参见[设置参数](products/redis/documents/user-guide/modify-the-values-of-parameters-for-an-instance.md)。

- 

Q：代理（Proxy）模式和直连模式有什么区别，推荐使用什么模式？

A：推荐使用代理模式，介绍与区别如下：

- 

代理模式：客户端的请求由代理节点转发至数据分片，可享受代理节点带来的负载均衡、读写分离、故障转移、[代理查询缓存](products/redis/documents/user-guide/use-read-write-splitting-to-mitigate-issues-caused-by-hotkeys.md)、长连接等特性能力。

- 

直连模式：可通过直连地址绕过代理，直接访问后端的数据分片（类似连接原生Redis集群）。相比代理模式，直连模式节约了通过代理处理请求的时间，可以在一定程度上提高Redis服务的响应速度。

- 

Q：为什么控制台上只有一个数据分片的Pub/Sub监控组有数值显示，而其他分片没有？

A：Proxy会根据channel name进行Hash计算，并路由至对应数据分片，所以在channel数量较少或仅有1个的情况下，仅会路由到一个数据分片上。

如果Pub/Sub的路由仅集中在一个数据分片上，当channel的数据量和流量较大时，会造成该数据分片的CPU使用率和出入流量明显高于其他分片，从而造成资源使用不均衡。

建议多发布几个不同名称的channel，以便Proxy根据Hash计算将channel平均地分布于各个数据分片中。

- 

Q：如果后端的某个数据分片出现异常，对数据读写有什么影响？

A：如果您的实例为[集群版-单副本](https://help.aliyun.com/zh/document_detail/59201.html#concept-ydy-g24-tdb)，由于仅具有主节点，无法保障数据可用性和服务连续性。推荐选择[集群架构](products/redis/documents/product-overview/cluster-master-replica-instances.md)，数据分片均采用主备高可用架构，当主节点发生故障后，系统会自动进行主备切换保证服务高可用。在某些极端场景下某个数据分片出现异常后，对数据的影响及优化方案如下。

- 

- 

- 

- 

- 

- 

- 

- 

| 场景 | 影响与优化方案 |
| --- | --- |
| 图 1. 多 Key 命令场景 | 影响： 客户端通过 4 个连接发送 4 个请求，当数据分片 2 处于异常状态时，仅有请求 1（ GET Key1 可正常读取到数据），其他请求会访问到数据分片 2 会返回超时。 优化方案： 降低多 Key 命令（例如 MGET ）的使用频率，或降低一次请求中包含的 Key 的数量，避免因单个数据分片异常导致该请求全部返回失败。 降低事务类命令的使用频率或降低事务大小，避免因某个子事务失败导致整个事务失败。 |
| 图 2. 单连接场景 | 影响： 客户端通过 1 个连接分别发送 2 个请求，当数据分片 2 处于异常状态时，请求 2（ GET Key2 ）将返回超时，同时由于请求 1（ GET Key1 ）和请求 2 共用同一连接，导致请求 1 也无法正常返回。 优化方案： 避免或降低对 pipeline 的使用。 避免使用单连接的客户端，推荐使用连接池的客户端，例如 [客户端程序连接教程](products/redis/documents/user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance.md) （需设置合理的超时时间和连接池大小）。 |


[上一篇：读写分离功能](products/redis/documents/product-overview/read-or-write-splitting-instances-1.md)[下一篇：实例规格](products/redis/documents/product-overview/overview-4.md)

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
