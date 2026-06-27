# 标准架构的分类详解与适用场景-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/standard-master-replica-instances

# 标准架构
云数据库 Tair（兼容 Redis）标准架构指未启用集群模式的架构，所有数据存储在一个分片中，具有简单易用、服务高可靠、高性价比等特点，可满足多种场景下的需求。相比集群架构，标准架构不支持调整分片数量，提供高可用（多副本）与单节点（单副本）实例类型。
## 高可用
标准架构高可用类型采用一主多备（Master-Replica）架构搭建。主节点负责日常服务访问，而备节点通常不对外提供服务，仅用于维护高可用性（HA）。当主节点发生故障时，系统会在30秒内自动切换至备节点，保证业务平稳运行。
云原生版标准架构
云原生版最多支持1个主节点、9个[备节点](../user-guide/node-management.md)。当多可用区触发HA时，优先会在同可用区进行切换，避免业务跨可用区访问。
经典版标准架构
经典版仅支持1个主节点、1个备节点。若实例为多可用区实例，则备节点部署在备可用区。
特点
可靠性
服务可靠：采用主备（master-replica）多机架构，主、备节点位于不同物理机。当主节点出现故障，自研的HA系统会自动进行主备切换，保证业务平稳运行。
数据可靠：默认开启数据持久化功能，数据全部落盘。支持数据备份功能，您可以针对备份集回滚实例或者克隆实例，有效地解决数据误操作等问题。同时，在支持容灾的可用区（例如杭州可用区H+I）创建的实例，还具备同城容灾的能力。
兼容性：兼容Redis协议，自建的Redis数据库可以平滑迁移Redis标准版。阿里云还提供数据传输工具[DTS](../user-guide/migrate-data-from-a-self-managed-redis-database-to-an-apsaradb-for-redis-instance.md)进行增量的Redis迁移，保证业务平稳过渡。
阿里云自研
故障探测切换系统（HA）：采用自研HA切换系统，实时探测主节点的异常情况，可以有效解决磁盘IO故障，CPU故障等问题导致的服务异常，及时进行主备切换，从而保证服务高可用。
主备复制机制：对主备全量同步中的Fork问题进行了优化，实现了无阻塞，在增量同步中采用增量日志格式进行复制传输。当主备复制中断后，对系统性能及稳定性影响极低，有效地避免了Redis原生主备复制的弊端。
Redis原生复制弊端
Redis复制中断后，备节点会立即发起psync，psync尝试部分同步，如果不成功，就会全量同步RDB并发送至备节点。
如果Redis需要进行全量同步，将导致主节点执行全量备份，并触发进程Fork，这可能会导致主节点出现毫秒级或秒级的卡顿现象。
Redis进程Fork导致Copy-On-Write，Copy-On-Write导致主节点进程内存消耗，极端情况下造成主节点内存溢出，程序异常退出。
Redis主节点生成备份文件导致服务器磁盘IO和CPU资源消耗。
发送GB级别大小的备份文件，会导致服务器网络出口爆增，磁盘顺序IO吞吐量高，期间会影响业务正常请求响应时间，并产生其他连锁影响。
应用场景
对Redis协议兼容性要求较高的业务
标准架构兼容Redis协议，业务可以平滑迁移。
Redis作为持久化数据存储使用的业务
标准架构提供持久化机制及备份恢复机制，极大地保证数据可靠性。
单个Redis性能压力可控的业务
由于Redis原生采用单线程机制，在10万QPS以下的业务建议使用。如果需要更高的性能要求，请开启读写分离功能或选用集群架构。
Redis命令相对简单，排序、计算类命令较少的业务
由于Redis的单线程机制，CPU会成为主要瓶颈。如排序、计算类较多的业务建议选用集群架构配置。
## 单节点
标准架构单节点类型采用单个数据库节点部署架构，没有可实时同步数据的备节点。由于该架构只有一个数据库节点，无热备节点用于HA。当数据库节点发生故障时，数据会丢失，系统会重新拉起一个新的Redis进程（没有数据）。当节点故障业务自动切换完成后，应用程序需要将数据重新预热。
警告
单节点架构不能保障数据可用性和服务连续性，选用前请务必确认风险，不建议您在生产环境中使用该架构的实例。
单节点架构不支持以下功能：[自动或手动备份](../user-guide/automatic-or-manual-backup.md)、[离线全量](../user-guide/offline-key-analysis.md)[Key](../user-guide/offline-key-analysis.md)[分析](../user-guide/offline-key-analysis.md)和[实例回收站](../user-guide/manage-instances-in-the-recycle-bin.md)。若您对数据有可靠性要求，推荐使用高可用架构。
特点及应用场景：
单节点架构具有明显的价格优势，性价比较高。适用于数据可靠性要求不高的纯缓存业务场景使用。
## 常见问题
Q：原有业务为Redis哨兵模式，迁移上云应该选什么架构？
A：推荐选择标准架构（高可用版）。创建实例后，您可以开启[Sentinel](../user-guide/use-the-sentinel-compatible-mode-to-connect-to-an-apsaradb-for-redis-instance.md)[兼容模式](../user-guide/use-the-sentinel-compatible-mode-to-connect-to-an-apsaradb-for-redis-instance.md)，然后可以像连接开源Redis Sentinel一样连接Tair（以及Redis开源版）实例。
Q：若当前实例为8 GB、标准架构，如何在不升级内存容量的情况下升级实例性能？
A：根据业务需求，分别推荐如下升级方案。
若现有实例的连接数或实例带宽不足，表示该实例可能无法满足超高的读流量。您可以考虑[开启读写分离](../user-guide/enable-read-write-splitting.md)（推荐），无需升级内存规格，即可快速提升实例读性能。
该方案无需修改业务代码（也无需修改连接地址），即开即用，也支持随时关闭。开启后，实例能够自动识别读、写请求并进行对应转发，满足高并发读写的业务场景。
若现有实例的CPU使用率总是过高，您可以考虑将实例升级为集群架构，通过增加数据分片解决单分片CPU使用率过高的问题。
但该方案将修改实例架构，集群架构与标准架构的大部分命令是兼容的，但仍然存在部分不兼容的命令（更多信息请参见[集群架构的命令限制](../developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)）。建议您评估后再进行升级。
以下为Redis开源版8 GB实例不同架构的性能对比：
| 架构 | 内存（GB） | CPU（核） | 带宽（MB/s） | 最大连接数 | QPS 参考值 |
| --- | --- | --- | --- | --- | --- |
| 标准架构（主备节点） | 8 | 2 | 96 | 20,000 | 100,000 |
| 标准架构（开启读写分离，1 个主节点、1 个只读节点） | 8 | 4（2 * 2） | 192（96 * 2） | 40,000（20,000 * 2） | 200,000 |
| 集群架构（2 分片） | 8（4 GB * 2 分片） | 4（2 * 2） | 192（96 * 2） | 40,000（20,000 * 2） | 200,000 |
## 相关文档
[节点管理](../user-guide/node-management.md)
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
