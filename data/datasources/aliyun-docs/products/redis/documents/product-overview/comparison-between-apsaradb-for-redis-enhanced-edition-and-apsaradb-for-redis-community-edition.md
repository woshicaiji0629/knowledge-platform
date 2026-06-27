# Tair与Redis开源版的选型参考与特性对比-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/product-overview/comparison-between-apsaradb-for-redis-enhanced-edition-and-apsaradb-for-redis-community-edition

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

# Tair（企业版）与Redis开源版特性对比

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文列出Tair（企业版）各形态产品与Redis开源版产品的相关特性对比，为您的产品选型提供相关参考。

## 选型参考

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 类别 | 系列 | 特点 | 适用场景 |
| --- | --- | --- | --- |
| Tair（企业版） | [内存型](products/redis/documents/product-overview/dram-based-instances.md) | 超高性能：采用多线程模型，读写性能达到同规格 Redis 开源版 实例的 3 倍，更多信息请参见 [Tair](products/redis/documents/support/performance-whitepaper-of-community-edition-instances.md) [内存型、Tair 持久内存型、Redis](products/redis/documents/support/performance-whitepaper-of-community-edition-instances.md) [开源版性能白皮书](products/redis/documents/support/performance-whitepaper-of-community-edition-instances.md) 。 提供丰富的自研增强型数据结构： 包括 [exString](products/redis/documents/developer-reference/tairsting-command.md) （包含 [Redis String](products/redis/documents/developer-reference/cas-cad-command.md) [命令增强](products/redis/documents/developer-reference/cas-cad-command.md) ）、 [exHash](products/redis/documents/developer-reference/the-tairhash-command.md) 、 [exZset](products/redis/documents/developer-reference/tairzset-command.md) 、 [GIS](products/redis/documents/developer-reference/tairgis-command.md) 、 [Bloom](products/redis/documents/developer-reference/tairbloom-command.md) 、 [Doc](products/redis/documents/developer-reference/tairdoc-command.md) 、 [TS](products/redis/documents/developer-reference/the-tickets-command.md) 、 [Cpc](products/redis/documents/developer-reference/taircpc-command.md) 、 [Roaring](products/redis/documents/developer-reference/tairroaring-command.md) 、 [Search](products/redis/documents/developer-reference/tairsearch.md) 和 [Vector](products/redis/documents/developer-reference/tairvector.md) ，帮助您精简代码并提高业务整体性能，使您专注于业务创新。 支持诸多企业级特性： [按时间点恢复数据](products/redis/documents/user-guide/use-data-flashback-to-restore-data-by-point-in-time.md) 、 [全球多活](products/redis/documents/user-guide/overview-of-global-distributed-cache-for-tair.md) 、代理查询缓存等。 支持高级企业级产品加密： [TLS](products/redis/documents/user-guide/enable-tls-encryption.md) [加密连接](products/redis/documents/user-guide/enable-tls-encryption.md) 、 [透明数据加密](products/redis/documents/user-guide/enable-tde.md) [TDE](products/redis/documents/user-guide/enable-tde.md) 等。 支持 [半同步模式](products/redis/documents/user-guide/modify-the-synchronization-mode-of-a-persistent-memory-optimized-instance.md) ：在异步复制的基础上提供半同步模式，提高数据一致性保障。 支持 [实时追踪](products/redis/documents/user-guide/real-time-tracking-log.md) ：实时追踪实例的读写请求，帮助您快速定位和排查问题。 支持 [高消耗](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) [Key](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) [统计及自定义阈值](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) ：实时统计高消耗 Key，支持自定义阈值告警。 支持 [服务端](products/redis/documents/user-guide/instance-sessions.md) [RBAL](products/redis/documents/user-guide/instance-sessions.md) [限流](products/redis/documents/user-guide/instance-sessions.md) ：提供服务端级别的请求速率限制能力，保障实例稳定运行。 | 以性能为中心的关键业务场景。 |
| [持久内存型](products/redis/documents/product-overview/persistent-memory-optimized-instances-1.md) | 超高性价比：对比相同容量下的 Redis 开源版 ，价格降低 30%左右，性能可达 Redis 开源版 的 90%，更多信息请参见 [持久内存型性能白皮书](products/redis/documents/support/performance-white-paper-of-persistent-memory-optimized-instances.md) 。 支持增强型数据结构模块（modules）： [exString](products/redis/documents/developer-reference/tairsting-command.md) （包含 [Redis String](products/redis/documents/developer-reference/cas-cad-command.md) [命令增强](products/redis/documents/developer-reference/cas-cad-command.md) ）、 [exHash](products/redis/documents/developer-reference/the-tairhash-command.md) 和 [Cpc](products/redis/documents/developer-reference/taircpc-command.md) 。 掉电数据不丢失：强大的命令级持久化保障，每个写操作持久化成功后返回，可将其作为内存数据库（非缓存）使用。 | 需要高性能且高数据持久化要求，且成本作为次要考虑因素的数据缓存与存储场景。 |  |
| [磁盘型](products/redis/documents/product-overview/essd-based-instances-1.md) | 低成本：最低为 Redis 开源版 的 15%。 性能：约为 Redis 开源版 的 60%，更多信息请参见 [磁盘（ESSD）型性能白皮书](products/redis/documents/support/performance-white-paper-of-essd-based-instances.md) 、 [磁盘（SSD）型性能白皮书](products/redis/documents/support/disk-ssd-performance-white-paper.md) 。 磁盘存储：数据分布在 ESSD 或 SSD 中，容量可达百 TB 级别，拥有高数据可靠性。 数据分布：采用阿里云 TairDB 存储引擎，数据通过磁盘持久化，内存用于请求加速。 高兼容性：兼容 Redis 6.0 大部分的数据结构和命令。 | 大存储、低访问密度、低访问延迟要求，且成本作为首要考虑因素的数据存储场景。 |  |
| Redis 开源版 | 无 | 兼容开源 Redis，高性能。 | 适用于标准化 Redis 使用和迁移场景。 |


说明

关于产品选型的详细介绍，请参见[产品选型参考](products/redis/documents/product-overview/select-an-apsaradb-for-redis-instance.md)。

## 特性对比

下述表格中，✔️表示支持该功能，❌表示不支持该功能。

| 类别 | 对比项 | Tair（企业版） | Redis 开源版 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [内存型](products/redis/documents/product-overview/dram-based-instances.md) | [持久内存型](products/redis/documents/product-overview/persistent-memory-optimized-instances-1.md) | [磁盘型](products/redis/documents/product-overview/essd-based-instances-1.md) （ESSD） | [磁盘型](products/redis/documents/product-overview/essd-based-instances-1.md) （SSD） | 2.8、4.0 及 5.0 版本 | 6.0、7.0 版本 | Redis 倚天版 |  |  |
| 基本性能 | 性能基准（以 Redis 开源版 为基准） | 300% | 90% | 读：40% | 读：60% | 一致 | 120% | 120% |
| 写：30% | 写：40% |  |  |  |  |  |  |  |
| 单个数据节点的最大连接数 | 30,000 | 10,000 | 10,000 | 40,000 | 10,000 | 10,000 | 10,000 |  |
| 单 Key 服务能力（QPS 参考值）① | 450,000 | 130,000 | 30,000~60,000 | 50,000~60,000 | 140,000 | 160,000 | 160,000 |  |
| 最大带宽（MB/s） | 96~2,048 | 96~2,048 | 187.5~1,000 | 187.5~2,048 | 10~2048 | 48~2,048 | 96~2,048 |  |
| 规格特性 | IO 与 Worker 模型 | 多 IO（Real Multi-IO）③ | 单线程 | 多 IO+多 Worker（Real Multi-IO） | 多 IO+多 Worker（Real Multi-IO） | 单线程 | 单线程 | 单线程 |
| 数据结构 | 基础数据结构及命令支持 | 不同形态支持的命令有所不同，详情请参见 [Tair（企业版）命令支持与限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md) 。 | 部分命令不支持，详情请参见 [Redis](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md) [开源版命令支持](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md) 。 |  |  |  |  |  |
| [Tair](products/redis/documents/developer-reference/extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md) [扩展数据结构概览](products/redis/documents/developer-reference/extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md) | ✔️ | ✔️️️（部分） | ❌ | ❌ | ❌ | ❌ | ❌ |  |
| 落盘模式 | 主备复制一致性 | 最终一致 | 最终一致 | 最终一致 | 最终一致 | 最终一致 | 最终一致 | 最终一致 |
| 落盘一致性 ④ | Write Back | Write Through | Write Through | Write Through | Write Back | Write Back | Write Back |  |
| 持久化级别 | 秒级 | 命令级 | 命令级 | 命令级 | 秒级 | 秒级 | 秒级 |  |
| 安全性 | [开启](products/redis/documents/user-guide/enable-tls-encryption.md) [TLS](products/redis/documents/user-guide/enable-tls-encryption.md) [加密](products/redis/documents/user-guide/enable-tls-encryption.md) | ✔️ | ✔️ | ❌ | ❌ | ✔️ | ✔️ | ✔️ |
| [透明数据加密](products/redis/documents/user-guide/enable-tde.md) [TDE](products/redis/documents/user-guide/enable-tde.md) | ✔️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |  |
| [IP](products/redis/documents/getting-started/step-2-configure-whitelists.md) [白名单](products/redis/documents/getting-started/step-2-configure-whitelists.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| 性能分析 | [Top Key](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) [统计](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) | ✔️ | ✔️ | ❌ | ❌ | ✔️ | ✔️ | ✔️ |
| [查询历史热点](products/redis/documents/user-guide/query-historical-hotkeys.md) [Key](products/redis/documents/user-guide/query-historical-hotkeys.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [离线分析大](products/redis/documents/user-guide/offline-key-analysis.md) [Key](products/redis/documents/user-guide/offline-key-analysis.md) | ✔️ | ✔️ | ❌ | ❌ | ✔️ | ✔️ | ✔️ |  |
| [审计日志](products/redis/documents/user-guide/enable-the-new-audit-log-feature.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| 高级功能 | [按时间点恢复数据](products/redis/documents/user-guide/use-data-flashback-to-restore-data-by-point-in-time.md) | ✔️ | ✔️ | ❌ | ✔️ | ❌ | ❌ | ❌ |
| [半同步模式](products/redis/documents/user-guide/modify-the-synchronization-mode-of-a-persistent-memory-optimized-instance.md) | ✔️ | ❌ | ✔️ | ✔️ | ❌ | ❌ | ❌ |  |
| 代理查询缓存 | ✔️ | ✔️ | ❌ | ❌ | ❌ | ❌ | ❌ |  |
| [全球多活](products/redis/documents/user-guide/overview-of-global-distributed-cache-for-tair.md) | ✔️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |  |
| [DTS](products/redis/documents/user-guide/configure-one-way-data-synchronization-between-apsaradb-for-redis-instances.md) [单向同步](products/redis/documents/user-guide/configure-one-way-data-synchronization-between-apsaradb-for-redis-instances.md) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |  |
| [DTS](products/redis/documents/user-guide/configure-two-way-synchronization-between-apsaradb-for-redis-enhanced-edition-instances.md) [双向同步](products/redis/documents/user-guide/configure-two-way-synchronization-between-apsaradb-for-redis-enhanced-edition-instances.md) | ✔️ | ✔️ | ✔️ | ❌ | ❌ | ❌ | ❌ |  |


表格中数字标记的解释如下：

- 

①：该QPS（每秒访问次数）参考值以时间复杂度为O(1)的命令衡量，时间复杂度越高，QPS参考值会相应降低。

- 

②：该性能与数据访问的冷热分布相关，命中内存的比例越高性能越接近Redis开源版基准性能。

- 

③：区别于Redis6.0的IO多线程，内存型的Real Multi-IO能够彻底加速IO和命令执行，具备更高的抗连接冲击性，且可以线性地提升吞吐能力。

- 

④：数据落盘方式主要有下述两种：

- 

Write Through：数据写入成功，数据同步落盘后返回。

- 

Write Back：数据写入成功即返回成功，数据异步刷盘。

## 相关文档

- 

[Tair（企业版）](products/redis/documents/product-overview/overview-1.md)

- 

[实例规格](products/redis/documents/product-overview/overview-4.md)

- 

[产品架构](products/redis/documents/product-overview/product-architecture.md)

[上一篇：与自建Redis的对比](products/redis/documents/product-overview/comparison-between-apsaradb-for-redis-and-self-managed-redis.md)[下一篇：云原生实例和经典实例对比](products/redis/documents/product-overview/comparison-between-tair-instances-that-cloud-native-and-classic.md)

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
