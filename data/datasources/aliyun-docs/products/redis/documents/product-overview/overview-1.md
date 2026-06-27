# 云上托管分布式内存数据库-Tair（企业版）-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/overview-1

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

# Tair（企业版）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Tair（企业版）是基于阿里集团内部使用的Tair产品研发的云上托管企业级内存数据库，从2009年开始正式承载阿里集团业务，历经天猫双十一、优酷春晚、菜鸟、高德等业务场景的磨练，是一款真正的企业级内存数据库产品。

## 实例存储介质

随着互联网的高速发展，业务场景变得越来越丰富和复杂，Tair（企业版）作为一个高可用、高性能的分布式NoSQL数据库，从访问延时、持久化需求、整体成本这三个核心维度考量，基于DRAM、NVM和ESSD云盘存储介质，推出了多种不同形态的产品，为您提供更强的性能、更多的数据结构和更灵活的存储方式，满足不同场景下的业务需求。

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

| 存储介质 | 特性 |
| --- | --- |
| 内存（DRAM）型 | 超高性能：采用多线程模型，读写性能达到同规格 Redis 开源版 实例的 3 倍，更多信息请参见 [Redis](products/redis/documents/support/performance-whitepaper-of-community-edition-instances.md) [开源版、Redis](products/redis/documents/support/performance-whitepaper-of-community-edition-instances.md) [倚天版、Tair](products/redis/documents/support/performance-whitepaper-of-community-edition-instances.md) [内存型性能白皮书](products/redis/documents/support/performance-whitepaper-of-community-edition-instances.md) 。 提供丰富的自研增强型数据结构： 包括 [exString](products/redis/documents/developer-reference/tairsting-command.md) （包含 [Redis String](products/redis/documents/developer-reference/cas-cad-command.md) [命令增强](products/redis/documents/developer-reference/cas-cad-command.md) ）、 [exHash](products/redis/documents/developer-reference/the-tairhash-command.md) 、 [exZset](products/redis/documents/developer-reference/tairzset-command.md) 、 [GIS](products/redis/documents/developer-reference/tairgis-command.md) 、 [Bloom](products/redis/documents/developer-reference/tairbloom-command.md) 、 [Doc](products/redis/documents/developer-reference/tairdoc-command.md) 、 [TS](products/redis/documents/developer-reference/the-tickets-command.md) 、 [Cpc](products/redis/documents/developer-reference/taircpc-command.md) 、 [Roaring](products/redis/documents/developer-reference/tairroaring-command.md) 、 [Search](products/redis/documents/developer-reference/tairsearch.md) 和 [Vector](products/redis/documents/developer-reference/tairvector.md) ，帮助您精简代码并提高业务整体性能，使您专注于业务创新。 支持诸多企业级特性： [通过数据闪回按时间点恢复数据](products/redis/documents/user-guide/use-data-flashback-to-restore-data-by-point-in-time.md) 、 [全球多活](products/redis/documents/user-guide/overview-of-global-distributed-cache-for-tair.md) 、代理查询缓存等。 支持高级企业级产品加密： [TLS](products/redis/documents/user-guide/enable-tls-encryption.md) [加密连接](products/redis/documents/user-guide/enable-tls-encryption.md) 、 [透明数据加密](products/redis/documents/user-guide/enable-tde.md) [TDE](products/redis/documents/user-guide/enable-tde.md) 等。 |
| 持久内存（NVM）型 | 超高性价比：对比相同容量下的 Redis 开源版 ，价格降低 30%左右，性能可达 Redis 开源版 的 90%，更多信息请参见 [持久内存型性能白皮书](products/redis/documents/support/performance-white-paper-of-persistent-memory-optimized-instances.md) 。 支持增强型数据结构模块（modules）： [exString](products/redis/documents/developer-reference/tairsting-command.md) （包含 [Redis String](products/redis/documents/developer-reference/cas-cad-command.md) [命令增强](products/redis/documents/developer-reference/cas-cad-command.md) ）、 [exHash](products/redis/documents/developer-reference/the-tairhash-command.md) 和 [Cpc](products/redis/documents/developer-reference/taircpc-command.md) 。 掉电数据不丢失：强大的命令级持久化保障，每个写操作持久化成功后返回，可将其作为内存数据库（非缓存）使用。 |
| 磁盘型 | 低成本：最低为 Redis 开源版 的 15%。 性能：约为 Redis 开源版 的 60%，更多信息请参见 [磁盘（ESSD）型性能白皮书](products/redis/documents/support/performance-white-paper-of-essd-based-instances.md) 、 [磁盘（SSD）型性能白皮书](products/redis/documents/support/disk-ssd-performance-white-paper.md) 。 磁盘存储：数据分布在 ESSD 或 SSD 中，容量可达百 TB 级别，拥有高数据可靠性。 数据分布：采用阿里云 TairDB 存储引擎，数据通过磁盘持久化，内存用于请求加速。 高兼容性：兼容 Redis 6.0 大部分的数据结构和命令。 |


## 购买指引

[创建实例](products/redis/documents/getting-started/step-1-create-an-apsaradb-for-redis-instance.md)

## 阿里云Tair的诞生与发展

2004年，淘宝开始应用缓存技术。最先投入应用的是基于前端页面的缓存技术，采用ESI来标识可以加速和不能加速的网页内容片段，有效减少了从服务端抓取整个页面的次数。

随着淘宝网的流量快速增长，数据库的压力与日俱增，基于后端系统的缓存技术应运而生。从服务淘宝详情和验证码等业务的持久化系统TBStore，到初始服务于淘宝用户中心的TDBM等等，后端系统缓存技术经历了多个系统和阶段的演变与积累，到2009年，这些系统、技术经验经过进一步的研发，融合成了阿里巴巴大规模高性能内存数据库Tair。

如今，Tair（企业版）已经是阿里巴巴集团调用量最大的系统之一，在多年的阿里巴巴双十一全球狂欢节上提供了核心的在线访问加速能力，承受住了每秒数亿次的调用。

- 

- 

- 

| 时间 | 事件 |
| --- | --- |
| 2024 年 07 月 | 发布内存型（兼容 Redis 7.0），性能与内存型（兼容 Redis 6.0）相当。 |
| 2022 年 10 月 | 发布内存型（兼容 Redis 6.0），相比较同规格的内存型（兼容 Redis 5.0）实例，约提升 20%性能。 |
| 2020 年 09 月 | 发布新产品系列： 持久内存型： 基于持久内存技术，为您提供大容量、兼容 Redis 的内存数据库产品。单实例成本对比 Redis 开源版 最高可降低 30%，且数据持久化不依赖传统磁盘，保证每个操作持久化的同时提供近乎 Redis 开源版 的吞吐和延时，极大提升业务数据可靠性。 磁盘型：基于 ESSD/SSD 研发，兼容 Redis 核心数据结构与接口，可提供大容量、低成本、强持久化的数据库服务。 Tair 将重点建设 云原生 版，如软硬件技术结合、数据智能分布、数据存储和计算处理一体化等核心能力。 |
| 2019 年 11 月 | 发布 Tair 3.0，即 Tair（企业版） ： 内存型（兼容 Redis 5.0）：采用多线程模型，集成多个自研 Tair 数据结构，提供高性能、高兼容性及带有诸多企业级特性的数据库服务。 |
| 2019 年 04 月 | Tair 团队在 Redis 开源社区贡献排名前三，并在 RedisConf 2019 上发表了公开演讲。 |
| 2018 年 08 月 | Tair 在中国率先推出混合存储实例，冷热数据分离，有效降低大客户使用成本。 |
| 2017 年 11 月 | Tair 热点散列经过双十一考验，解决了业内的缓存热点难题。 |
| 2017 年 04 月 | Tair 2.0 上线，开始支持高德、优酷新 BU。 云上 OCS 升级为 KVStore。 |
| 2016 年 08 月 | Tair 智能运维平台上线，助力 2016 双十一迈入千亿时代。 |
| 2015 年 03 月 | Tair 推出阿里云 KVStore，即云数据库 Redis 版，真正进入了云时代。 |
| 2014 年 05 月 | Tair 推出阿里云上缓存产品 OCS，成为阿里云初始的基础产品之一，服务云上 Memcache 用户。 |
| 2013 年 04 月 | Fastdump 系统落地，大幅度降低导入时间和访问延时。 Tair 在阿里妈妈获得规模化应用。 |
| 2012 年 10 月 | 推出 RDB 缓存引擎，引入类 Redis 接口，支持更灵活、复杂的数据结构。 |
| 2011 年 06 月 | 上线 LDB 持久化引擎，满足互联网 KV 存储需求。 |
| 2009 年 11 月 | Tair 的第一个双十一，正式开始支撑超大流量场景。 |
| 2009 年 04 月 | Tair 1.0 正式诞生，并被应用于淘宝核心系统、MDB 缓存、用户中心等业务。 |


## 相关文档

- 

[Redis](products/redis/documents/support/performance-whitepaper-of-community-edition-instances.md)[开源版、Redis](products/redis/documents/support/performance-whitepaper-of-community-edition-instances.md)[倚天版、Tair](products/redis/documents/support/performance-whitepaper-of-community-edition-instances.md)[内存型性能白皮书](products/redis/documents/support/performance-whitepaper-of-community-edition-instances.md)

- 

[持久内存型性能测试](products/redis/documents/support/performance-white-paper-of-persistent-memory-optimized-instances.md)

- 

[磁盘（ESSD）型性能测试](products/redis/documents/support/performance-white-paper-of-essd-based-instances.md)

- 

[磁盘（SSD）型性能白皮书](products/redis/documents/support/disk-ssd-performance-white-paper.md)

[上一篇：集群无感扩缩容介绍](products/redis/documents/product-overview/imperceptible-scaling.md)[下一篇：内存型](products/redis/documents/product-overview/dram-based-instances.md)

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
