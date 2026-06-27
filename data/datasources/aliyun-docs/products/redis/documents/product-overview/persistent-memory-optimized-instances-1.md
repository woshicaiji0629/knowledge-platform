# 兼容Redis的大容量持久化内存数据库-持久内存型-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/persistent-memory-optimized-instances-1

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

# 持久内存型

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Tair持久内存型（简称持久内存型）基于持久内存技术，为您提供大容量、兼容Redis的内存数据库产品。单实例成本对比Redis开源版最高可降低30%，且数据持久化不依赖传统磁盘，保证每个操作持久化的同时提供近乎Redis社区版的吞吐和延时，极大提升业务数据可靠性。

## 购买方式

[创建实例](products/redis/documents/getting-started/step-1-create-an-apsaradb-for-redis-instance.md)

## 背景信息

由于内存的价格相对昂贵且容量具备较大的局限性，限制了在某些场景中的规模化使用。阿里云于2018年正式开始投入持久化内存的研究和落地，成功应用于当年双11的电商商品核心集群中，大幅降低了成本，是中国首先在生产环境正式部署应用持久化内存硬件的产品。

随着云上环境的成熟和持久内存相关技术的完善，阿里云基于持久内存全新研发了数据持久落地的自研引擎，结合[神龙裸金属服务器](products/ecs/documents/user-guide/elastic-bare-metal-server-overview.md)推出了Tair持久内存型产品，将传统Redis内存易失性演进到了持久内存原生持久化能力，大幅降低数据丢失的风险。

持久内存型产品既拥有内存级的访问延时和吞吐，也拥有数据持久化的能力。除了降低成本之外，持久内存型还能带来应用架构的简化，可将目前流行的应用+缓存+持久存储的架构模型，演进为更加简洁的应用+具备持久能力的内存数据库的架构模型，如下图所示。

## 产品优势

持久内存型基于持久内存技术，提供大容量、兼容Redis的内存数据库产品，数据持久化不依赖传统磁盘，保证每个操作持久化的同时提供近乎Redis开源版的吞吐和延时，极大提升业务数据可靠性。适用于兼容Redis、大容量、服务抖动稳定可控，数据持久化要求高的热温数据存储场景。

- 

- 

- 

- 

- 

| 优势项 | 说明 |
| --- | --- |
| 超高性价比 | 相同容量下对比阿里云 Redis 开源版 ，价格降低 30%左右。 性能可达到 Redis 的 90%。 |
| 数据结构模块集成 | 支持 [exString](products/redis/documents/developer-reference/tairsting-command.md) （包含 [Redis String](products/redis/documents/developer-reference/cas-cad-command.md) [命令增强](products/redis/documents/developer-reference/cas-cad-command.md) ）、 [exHash](products/redis/documents/developer-reference/the-tairhash-command.md) 和 [Cpc](products/redis/documents/developer-reference/taircpc-command.md) 。 |
| 大规格优化 | 解决大规格下执行 AOF 重写调用 fork 引起的延时抖动、服务数据加载慢等问题，无需在性能与持久化中取舍。 |
| 更高可靠性 | 提供命令级持久化保障，每个写操作请求将在主节点持久化成功之后返回。 |
| 高兼容性 | 完全适配现有阿里云 Redis 数据库体系，具备高可用、弹性扩容缩容、日志、智能诊断与灵活的备份还原服务能力。 兼容 Redis 6.0 版本及以下版本接口和数据结构。 |


## 适用场景

- 

海量数据下对性能与成本要求高的场景

计算中间数据对性能的要求很高，采用Redis开源版成本较高，如果采用HBase之类的数据库存储数据则可能无法满足性能需求。采用持久存储型实例保障数据持久化的同时提供近乎Redis开源版的吞吐和延时，可很好地平衡性能与成本。

- 

最终数据存储持久化要求高的场景

游戏场景直接采用持久存储型实例作为最终的数据存储，相较于使用Redis+MySQL的架构场景，可获得更简洁的架构，更高的性能和性价比，且数据更加可靠。

## 实例规格

[持久内存型实例规格](products/redis/documents/product-overview/persistent-memory-type.md)

## 相关文档

- 

[持久内存型性能测试](products/redis/documents/support/performance-white-paper-of-persistent-memory-optimized-instances.md)

[上一篇：内存型](products/redis/documents/product-overview/dram-based-instances.md)[下一篇：磁盘型](products/redis/documents/product-overview/essd-based-instances-1.md)

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
