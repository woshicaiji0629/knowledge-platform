# 兼容Redis的内存型扩展数据结构数据库-Tair内存型-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/dram-based-instances

# 内存型
Tair内存型（简称内存型）适合并发量大、读写热点多，对性能要求超过Redis开源版实例的场景。相比Redis开源版，内存型重点增强了多线程性能并集成多个自研扩展数据结构。
## 功能概述
| 类别 | 说明 |
| --- | --- |
| 兼容性 | 100%兼容原生 Redis，无需修改业务代码，提供 兼容 Redis 7.0 、 兼容 Redis 6.0 与 兼容 Redis 5.0 版本。 |
| 性能 | 采用多线程模型，性能约为同规格 Redis 开源版 的 3 倍，能够突破热点数据高频读写受到的性能限制。 相比原生 Redis，高 QPS 场景下响应时间更低，性能表现更佳。 在大并发场景下运行稳定，可以极大地缓解突发大量请求导致的连接问题，从容应对业务高峰。 全量同步和增量同步在 IO 线程中进行，提高同步速度。 |
| 同步模式 | 额外支持 [半同步模式](../user-guide/modify-the-synchronization-mode-of-a-persistent-memory-optimized-instance.md) ，即客户端发起的更新在主节点执行完成后，主节点会将日志复制到备节点，待备节点确认接收后才返回信息给客户端，保证高可用切换后数据不丢失。 |
| 部署架构 | 支持标准、集群和读写分离部署架构。 |
| 数据结构模块集成 | 集成多个自研的 Tair 模块， 包括 [exString](../developer-reference/tairsting-command.md) （包含 [Redis String](../developer-reference/cas-cad-command.md) [命令增强](../developer-reference/cas-cad-command.md) ）、 [exHash](../developer-reference/the-tairhash-command.md) 、 [exZset](../developer-reference/tairzset-command.md) 、 [GIS](../developer-reference/tairgis-command.md) 、 [Bloom](../developer-reference/tairbloom-command.md) 、 [Doc](../developer-reference/tairdoc-command.md) 、 [TS](../developer-reference/the-tickets-command.md) 、 [Cpc](../developer-reference/taircpc-command.md) 、 [Roaring](../developer-reference/tairroaring-command.md) 、 [Search](../developer-reference/tairsearch.md) 和 [Vector](../developer-reference/tairvector.md) ，扩展了 Tair 的适用性，同时降低了复杂场景下业务的开发难度，让您专注于业务创新。 说明 [内存型](dram-based-instances.md) （兼容 Redis 7.0、6.0）兼容所有数据结构。 [内存型](dram-based-instances.md) （兼容 Redis 5.0）兼容除 TairVector 以外的所有数据结构。 |
| 企业级特性 | [通过数据闪回按时间点恢复数据](../user-guide/use-data-flashback-to-restore-data-by-point-in-time.md) ：最长支持将实例恢复至过去 7 天内的任意时间点。 代理查询缓存：代理节点缓存热点 Key 对应的请求和查询结果，提高热点查询效率。 [全球多活](../user-guide/overview-of-global-distributed-cache-for-tair.md) ：可轻松实现异地多个站点同时对外提供服务的业务场景。支持异地多个实例的数据同步服务，适用于异地多活、数据容灾等场景。 [Tair](../user-guide/configure-two-way-synchronization-between-apsaradb-for-redis-enhanced-edition-instances.md) [双向同步](../user-guide/configure-two-way-synchronization-between-apsaradb-for-redis-enhanced-edition-instances.md) ：支持双向同步，适用于异地多活、数据容灾等场景。 |
| 数据安全 | 支持 [开启](../user-guide/configure-ssl-encryption.md) [SSL](../user-guide/configure-ssl-encryption.md) [加密](../user-guide/configure-ssl-encryption.md) ，提升通信数据的安全性。 支持 [开启透明数据加密](../user-guide/enable-tde.md) [TDE](../user-guide/enable-tde.md) ，对 RDB 数据文件执行加密和解密，提升数据安全性。 |
应用场景
适用于视频直播、电商秒杀和在线教育等场景，下面列举了内存型在4个典型场景中的应用。
场景1：使用Redis开源版实例在秒杀场景中构建缓存，部分热点Key的QPS要求高达20万以上，无法满足业务高峰期的需求。
采用内存型（标准架构）实例后，热门商品秒杀过程流畅，未发生性能问题。
场景2：在业务中使用Redis开源版集群实例，但在使用事务和Lua脚本功能时有一定的限制。
采用内存型实例后，在满足性能需求的同时消除了集群版的命令使用限制。
场景3：自建有一主多备的Redis服务，随着业务中访问量的不断提高，备节点数量也要随之增加，管理维护成本越来越高。
采用具备一个数据节点五个只读副本的内存型（读写分离架构）实例后，可以轻松应对百万级QPS的业务挑战。
场景4：自建有Redis集群来承担线上千万级QPS的业务压力。随着业务的发展，Redis分片数不断增加，管理维护成本居高不下。
采用内存型（集群架构）实例后，集群规模缩到原来的三分之一，管理维护成本大幅降低。
## 线程模型对比
### Redis单线程模型
Redis开源版和原生Redis采用单线程模型，数据处理流程为：读取请求，解析请求，处理数据，发送响应。其中网络IO和请求解析占用了大部分的资源。
### Tair内存型多线程模型
Tair内存型将服务各阶段的任务进行分离，通过多个线程并行处理各阶段任务，从而提高性能。
主线程：负责建立连接、启动其他线程、分发任务等。
IO线程：负责读取请求、解析命令、处理命令、发送响应等。Tair内存型最多支持4个IO线程并发运行。
辅助（BIO）线程：负责高可用探测、数据持久化、内存惰性回收、保活等。
说明
Tair内存型对于通用的数据类型，例如String、List、Set、Hash、Zset、 Hyperloglog、Geo以及Tair扩展结构都有很好的加速效果。
区别于Redis 6.0的多线程（性能至多提升2倍，且CPU资源消耗高），内存型的Real Multi-IO能够彻底加速IO和命令执行，具备更高的抗连接冲击性，且可以线性地提升吞吐能力。
## 常见问题
Q：客户端不支持Tair扩展模块的命令怎么办？
A：您可以先在应用代码中定义需要使用的新模块命令，然后再使用这些命令，或者通过Tair客户端直接调用Tair扩展数据结构，更多信息，请参见[Clients](../developer-reference/redis-clients.md)[说明](../developer-reference/redis-clients.md)。
## 相关文档
[创建实例](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md)
[内存型性能测试](../performance-whitepaper-of-dram-based-instances-that-are-compatible-with-redis-5.md)
[实例规格](overview-4.md)
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
