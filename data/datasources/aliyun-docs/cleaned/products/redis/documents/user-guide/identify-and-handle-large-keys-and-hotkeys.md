# 大Key和热Key的找出优化与预防方法-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/identify-and-handle-large-keys-and-hotkeys/

# 大Key和热Key
Big keys（大Key）与Hot keys（热Key）可能导致服务性能下降、请求超时，甚至引发系统故障。本文介绍如何快速找出和优化大Key与热Key，分析其产生原因及影响，并提供预防措施以降低对业务的影响。
## 步骤一：快速找出大Key和热Key
### 阿里云控制台工具
Tair和Redis在控制台提供了Top Key统计和离线全量Key分析功能帮助您快速找出大Key与热Key。
| 方法 | 使用限制 | 说明 | 操作步骤 |
| --- | --- | --- | --- |
| [Top Key](use-the-real-time-key-statistics-feature.md) [统计](use-the-real-time-key-statistics-feature.md) （推荐） | 仅 Redis 开源版 5.0 及以上版本和 Tair（企业版） 内存型、持久内存型支持该功能。 | 实时显示每个分片中各数据类型前三的大 Key 和热 Key 信息。 支持查看 4 天内大 Key 和热 Key 的历史信息。 | 访问 [实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou) ，在上方选择地域，然后单击目标实例 ID。 在左侧导航栏，单击 CloudDBA > 实时 Top Key 统计 或 离线全量 Key 分析 。 |
| [离线全量](offline-key-analysis.md) [Key](offline-key-analysis.md) [分析](offline-key-analysis.md) | 单副本实例或 磁盘型实例不支持该功能。 | 对 RDB 备份文件进行定制化的分析，得出 Key 在内存中的占用和分布、Key 过期时间等信息。 时效性差，RDB 文件较大时耗时较长。 无法分析热 Key 信息。 |  |
如果您的实例不能使用上述功能，请参考以下方法。
### 其他方法找出大Key和热Key
| 方法 | 优缺点 | 说明 |
| --- | --- | --- |
| 通过 redis-cli 的 bigkeys 、 memkeys 和 hotkeys 参数 | 优点：方便、快速、安全。 缺点：分析结果不可定制化，准确性与时效性差；需要遍历实例当前所有 Key，可能影响实例性能。 | redis-cli 的 bigkeys 、 memkeys 与 hotkeys 参数能获取 Key 的整体统计信息与每个数据类型中 Top1 的大 Key 或热 Key。 区别如下： bigkeys ：统计大 Key 信息，集合或列表类型返回元素个数。 memkeys ：统计大 Key 信息，返回所有数据类型所占内存大小。 hotkeys ：统计热 Key 信息。 支持的数据类型：STRING、LIST、HASH、SET、ZSET、STREAM。 以 bigkeys 为例，命令示例为 redis-cli -h r-***************.redis.rds.aliyuncs.com -a <password> --bigkeys 。 |
| 通过内置命令对目标 Key 进行分析 | 优点：对线上服务影响小。 缺点：返回的 Key 序列化长度并不等同于它在内存空间中的真实长度，因此不够准确，仅可作为参考。 | 对不同数据类型的目标 Key，分别通过如下风险较低的命令进行分析，来判断目标 Key 是否符合大 Key 判定标准。 STRING 类型： STRLEN 命令，返回对应 Key 的 value 的字节数。 LIST 类型： LLEN 命令，返回对应 Key 的列表长度。 HASH 类型： HLEN 命令，返回对应 Key 的成员数量。 SET 类型： SCARD 命令，返回对应 Key 的成员数量。 ZSET 类型： ZCARD 命令，返回对应 Key 的成员数量。 STREAM 类型： XLEN 命令，返回对应 Key 的成员数量。 说明 DEBUG OBJECT 与 MEMORY USAGE 命令在执行时需占用较多资源，且时间复杂度为 O(N)，有阻塞实例的风险，不建议使用。 |
| 通过业务层定位热 Key | 优点：可准确并及时地定位热 Key。 缺点：业务代码复杂度的增加，同时可能会降低一些性能。 | 通过在业务层增加相应的代码对实例的访问进行记录并异步汇总分析。 |
| 通过 redis-rdb-tools 工具以定制化方式找出大 Key | 优点：支持定制化分析，对线上服务无影响。 缺点：时效性差，RDB 文件较大时耗时较长。 | [Redis-rdb-tools](https://github.com/sripathikrishnan/redis-rdb-tools) 是通过 Python 编写的开源工具，支持定制化分析 RDB 快照文件。 [下载](download-a-backup-file.md) [RDB](download-a-backup-file.md) [文件](download-a-backup-file.md) 后，您可以根据业务需求分析实例中所有 Key 的内存占用情况，并支持灵活地查询。 |
| 通过 MONITOR 命令找出热 Key | 优点：方便、安全。 缺点：会占用 CPU、内存、网络资源，时效性与准确性较差。 | MONITOR 命令能够忠实地打印实例中的所有请求，包括时间信息、Client 信息、命令以及 Key 信息。 在发生紧急情况时，可以通过短暂执行 MONITOR 命令并将返回信息输入至文件，在关闭 MONITOR 命令后，对文件中请求进行归类分析，找出这段时间中的热 Key。 说明 由于 MONITOR 命令对实例性能消耗较大，非特殊情况不推荐使用 MONITOR 命令。 |
## 步骤二：优化大Key与热Key
### 大Key
| 方案 | 适用场景 | 操作建议 |
| --- | --- | --- |
| 清理过期数据 | 大量过期数据堆积，如 HASH 中未清理的增量数据。 | 通过 HSCAN 命令配合 HDEL 命令对失效数据进行清理，避免清理大量数据造成实例阻塞。 |
| 压缩大 Key | JSON、XML 文本数据等可压缩数据，如日志、配置。 | 序列化时启动压缩，如 GZIP、Snappy。 使用二进制序列化协议，如 Protocol Buffers。 说明 压缩和解压缩操作需要消耗额外的 CPU 资源，可能影响处理性能。 |
| 拆分大 Key | 高频访问的 HASH、ZSET 等，如排行榜。 | 按照业务逻辑拆分，如用户 ID、时间范围。 使用分片键设计，如：user:1001:shard1、user:1001:shard2。 拆分大 Key 能有效避免数据倾斜。 |
| 转存大 Key | String 类型大文件或 BLOB。 | 将不适用数据存至其它存储（如 OSS），并在实例中删除此类数据。 Redis 开源版 4.0 及之后版本：您可以通过 UNLINK 命令安全地删除大 Key 甚至特大 Key，该命令通过异步方式清理 Key，避免阻塞主线程。 Redis 开源版 4.0 之前的版本：建议先通过 SCAN 命令读取部分数据，然后进行删除，避免一次性删除大量 key 导致主线程阻塞。 |
### 热Key
| 方案 | 适用场景 | 操作建议 |
| --- | --- | --- |
| 在集群架构中对热 Key 进行复制 | 热 Key 作为整体存储在单一分片，无法通过迁移部分数据分散请求。 | 将热 Key 复制并迁移至其他数据分片，例如将热 Key foo 复制出 3 个内容完全一样的 Key 并命名为 foo2、foo3、foo4，将这三个 Key 迁移到其他数据分片来解决单个数据分片的热 Key 压力。 说明 该方案的缺点是需修改代码维护多个副本，且多副本间的数据一致性难以保障（例如更新操作需同步所有副本）。建议将该方案作为临时解决方案，用于缓解紧急问题。 |
| [开启读写分离](enable-read-write-splitting.md) | 读多写少 | 如果开启后读请求负载依旧很高，可通过增加只读节点数量进一步缓解读请求负载。 说明 在请求量极大的场景下，主备同步会产生不可避免的延迟，此时会出现读取到脏数据的问题。因此，在读、写压力都较大且对数据一致性要求很高的场景下，不推荐开启读写分离。 |
## 步骤三：预防大Key和热Key影响业务
### 大Key和热Key产生的原因
Tair和Redis的最小数据分布粒度为Key。单个Key将存储在特定的数据分片中，且不会被拆分。业务规划不足、无效数据的堆积以及访问量的突增等因素，均会使实例产生大Key与热Key，如：
| 类别 | 原因 |
| --- | --- |
| 大 Key | 在不适用的场景下使用 Tair 和 Redis ，易造成 Key 的 value 过大，如使用 String 类型的 Key 存放大体积二进制文件型数据； 业务上线前规划设计不足，没有对 Key 中的成员进行合理的拆分，造成个别 Key 中的成员数量过多； 未定期清理无效数据，造成如 HASH 类型 Key 中的成员持续不断地增加； 使用 LIST 类型 Key 的业务消费侧发生代码故障，造成对应 Key 的成员只增不减。 |
| 热 Key | 预期外的访问量陡增，如突然出现的爆款商品、访问量暴涨的热点新闻、直播间某主播搞活动带来的大量刷屏点赞、游戏中某区域发生多个工会之间的战斗涉及大量玩家等。 |
### 大Key和热Key带来的影响
| 类别 | 影响 |
| --- | --- |
| 大 Key | 客户端执行命令的时长变慢。 实例内存达到 maxmemory 上限时，可能导致操作阻塞、重要 Key 被逐出，甚至内存溢出（OOM）。 集群架构下，某个数据分片的内存使用率远超其他数据分片，无法使数据分片的内存资源达到均衡。 对大 Key 执行读请求，会使实例的带宽使用率被占满，导致自身服务变慢，同时易波及相关的服务。 对大 Key 执行删除操作，易造成主库较长时间的阻塞，进而可能引发同步中断或主备切换。 |
| 热 Key | 占用大量的 CPU 资源，同时可能增加网络带宽的使用，进而影响其他请求并导致整体性能降低。 集群架构下，产生访问倾斜，即某个数据分片被大量访问，而其他数据分片处于空闲状态，可能引起该数据分片的连接数被耗尽，新的连接建立请求被拒绝等问题。 在抢购或秒杀场景下，可能因商品对应库存 Key 的请求量过大，超出实例处理能力造成超卖。 热 Key 的请求压力数量超出实例的承受能力，容易造成缓存击穿，即大量请求将被直接指向后端的存储层，导致存储访问量激增甚至宕机，从而影响其他业务。 |
### 预防策略
| 策略 | 说明 |
| --- | --- |
| [监控报警设置](alert-settings.md) | 设置合理的 CPU、内存、连接数使用率等报警阈值进行报警，例如内存使用率超过 70%、内存在 1 小时内增长率超过 20%等。出现报警时，按照本文步骤一和步骤二的指引定位并优化大 Key 和热 Key，在其发展到影响业务之前解决。 |
| 使用 Tair（企业版） 避开失效数据的清理工作 | 针对 hash 类型的大 key 场景， Tair（企业版） 提供了增强型数据结构 [TairHash](../developer-reference/the-tairhash-command.md) 。它支持为每个 field 设置过期时间和版本。通过合理使用 TairHash，可以显著减少运维负担、简化业务代码复杂度，并有效应对大 Key 和热 Key 带来的问题。 |
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
