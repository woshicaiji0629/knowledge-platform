# 实例规格类型与性能参数-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/overview-4

# 实例规格
云数据库 Tair（兼容 Redis）具备多种类型、系列和架构，您可以通过本文的导航信息快速找到相关类型实例的规格文档。
## Redis倚天版
云数据库 Tair（兼容 Redis）推出倚天版实例，满足您低成本使用Redis的需求，更多信息请参见[倚天版实例](cost-efficient-instances.md)。
## Redis开源版
| 实例规格文档 | 简介 |
| --- | --- |
| [Redis](instance-types-of-cloud-native-community-edition-instances.md) [开源版云原生版](instance-types-of-cloud-native-community-edition-instances.md) | 标准架构：内存容量上限可达 64 GB，支持约 100,000 QPS。 读写分离架构：内存容量上限可达 64 GB，支持约 600,000 QPS。 集群架构：内存容量上限可达 16,384 GB（64 GB*256 分片数），实例整体的性能= 分片数 * 各分片的规格对应的性能。 |
| [Redis](instance-types-of-classic-community-edition-instances.md) [开源版经典版](instance-types-of-classic-community-edition-instances.md) | 标准架构（多副本）：主备（master-replica）架构的 Redis 实例。内存容量上限可达 64 GB，支持约 80,000 QPS（参考值）。 标准架构（单副本）：单节点的 Redis 实例。内存容量上限可达 32 GB，支持约 80,000 QPS（参考值）。 集群架构（双副本）：每个数据分片都是主备（master-replica）架构。内存容量上限可达 4,096 GB（16 GB*256 分片数），支持约 25,600,000 QPS（参考值）。 集群架构（单副本）：每个数据分片都是单节点架构。内存容量上限可达 2,048 GB（16 GB*128 分片数），支持约 12,800,000 QPS（参考值）。 读写分离架构：由一个主备架构的主节点、一个或多个只读副本组成的 Redis 实例。内存容量上限可达 64 GB，支持约 600,000 QPS。 |
| 早期已停售规格 | 云数据库 Tair（兼容 Redis） 的部分规格已停止新购，但这些规格的已购实例仍可正常使用。您可以在 [早期已停售规格](retired-instance-types.md) 中查看这些规格的连接数限制、带宽、QPS 参考值等信息。 |
## Tair（企业版）
| 实例规格文档 | 简介 |
| --- | --- |
| [内存型实例规格](enhanced-performance.md) | 采用多线程模型，性能约为同规格 Redis 开源版 的 3 倍。 标准架构：内存容量上限可达 64 GB，支持约 300,000 QPS。 读写分离架构：内存容量上限可达 64 GB，支持约 1,800,000 QPS。 集群架构：内存容量上限可达 16,384 GB（64 GB*256 分片数），实例整体的性能= 分片数 * 各分片的规格对应的性能。 同时，内存型也支持 经典 版实例： 内存型（标准架构）：采用多线程模型的主备双副本实例，性能约为同规格 Redis 开源版 的 3 倍。内存容量上限可达 64 GB，支持约 240,000 QPS。 内存型（读写分离架构）：采用多线程模型的读写分离实例，由一个主数据节点、一个或多个只读副本组成的 Redis 实例，性能约为同规 Redis 开源版 的 3 倍。 内存容量上限可达 64 GB，支持约 1,440,000 QPS。 内存型（集群架构）：采用多线程模型的集群实例，每个数据分片均为主备双副本架构，性能约为同规格 Redis 开源版 的 3 倍。内存容量上限可达 4,096 GB（16 GB*256 分片数），支持约 61,440,000 QPS（参考值）。 |
| [持久内存型实例规格](persistent-memory-type.md) | 数据持久化不依赖传统磁盘，每个操作均保证持久化，同时可提供近乎 Redis 开源版 的吞吐和延时。标准版的持久内存型实例，单实例成本对比 Redis 开源版 最高可降低 30%。 标准架构：内存容量上限可达 64 GB，支持约 100,000 QPS。 读写分离架构：内存容量上限可达 64 GB，支持约 600,000 QPS。 集群架构：内存容量上限可达 16,384 GB（64 GB*256 分片数），实例整体的性能= 分片数 * 各分片的规格对应的性能。 |
| [磁盘型实例规格](capacity-storage-type.md) | 所有数据均存储在磁盘中，内存用于加速缓存，成本最低为 Redis 开源版 的 15%，性能约为 Redis 开源版 的 60%。适用于兼容 Redis、需要大容量且较高访问性能的温冷数据存储场景。内存容量上限可达 32,768 GB（128 GB*256 分片）、常规存储容量可达 327,680 GB（1280 GB*256 分片）。 |
## 常见问题
选择规格时，是否需要预留快照内存资源？
答：不需要。目前Redis开源版与Tair（企业版）均为实例售卖模式，您无需在选型时预留快照所需的内存资源。规格对应的内存容量即为用户最大可用的容量，包含用户数据占用的内存、数据库运行静态内存消耗以及网络链路占用的内存。
实例规格都有QPS参考值，如果超过了这个值会有什么影响？
答：QPS参考值仅用于参考，并无限制。建议您关注实例的CPU使用率、带宽流量等监控指标，在上述任一指标达到上限后，可能会影响实例的正常访问。
说明
实例规格表中的QPS参考值基于GET/SET简单命令（16字节数据）测得。而在实际使用中，实例QPS受命令的时间复杂度、请求大小和访问模型的影响，具体请参考[性能白皮书](../support/performance-whitepaper-of-community-edition-instances.md)以及业务场景压测的结果。
为什么找不到某个规格？
答：您寻找的规格可能已下线。更多信息，请参见[早期已停售规格](retired-instance-types.md)。
怎么通过规格代码（InstanceClass）查找规格？
答：您可以在阿里云任意文档页面右上方的搜索栏中输入规格代码进行查询。
怎么测试这些Tair实例的性能？
答：您可以根据性能白皮书中介绍的方法测试Tair实例的性能。更多信息，请参见[性能白皮书](../support/performance-whitepaper-of-community-edition-instances.md)。
## 相关文档
[Tair（企业版）与](comparison-between-apsaradb-for-redis-enhanced-edition-and-apsaradb-for-redis-community-edition.md)[Redis](comparison-between-apsaradb-for-redis-enhanced-edition-and-apsaradb-for-redis-community-edition.md)[开源版特性对比](comparison-between-apsaradb-for-redis-enhanced-edition-and-apsaradb-for-redis-community-edition.md)
[云原生实例和经典实例对比](comparison-between-tair-instances-that-cloud-native-and-classic.md)
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
