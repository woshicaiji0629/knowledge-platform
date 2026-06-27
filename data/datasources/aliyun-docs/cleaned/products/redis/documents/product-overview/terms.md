# 核心组件架构与技术属性-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/terms

# 基本概念
您可以在使用前了解云数据库 Tair（兼容 Redis）的基本概念，从而更好地理解与使用Tair数据库。
| 概念 | 说明 |
| --- | --- |
| 实例 ID | 每个实例对应一个用户空间，实例是使用 云数据库 Tair（兼容 Redis） 的基本单位。 Tair 对单个实例根据不同的容量规格有不同的连接数、带宽、CPU 处理能力等限制。用户可在控制台中看到自己购买的实例 ID 列表。 |
| 数据分片 | 将 Tair （或 Redis）数据进行分隔，分别存储在不同数据分片中，以提高实例的性能和扩展性。 [标准架构](standard-master-replica-instances.md) 为 1 分片，即主备架构，表示所有数据都在 1 个分片（主节点）中。支持最多 9 个备节点。 [集群架构](cluster-master-replica-instances.md) 支持 2~256 分片，通常情况下，集群的数据将均匀地分布在各个数据分片。 说明 集群架构的整个数据库空间会被分为 16384 个槽（Slot），每个数据分片存储与处理指定 Slot 的数据。以 3 个数据分片为例，3 个分片分别负责的 Slot 为：[0,5460]、[5461,10922]、[10923,16383]。 每个数据分片最多支持 1 个主节点、4 个备节点，分片中所有的节点规格均相同。 |
| 实例类型及节点 | 高可用 ：采用主备（Master-replica）架构搭建，通常有两个或以上的节点提供服务高可靠。 主节点 ：提供日常服务访问，负责处理读、写请求。 备节点 ：不对外提供服务，仅提供 HA 高可用。当主节点发生故障，系统会自动在 30 秒内切换至数据最完整的备节点，保证业务平稳运行。 只读节点 ：负责处理读请求，也具备容灾功能，仅在读写分离架构中。 单节点 ：仅使用单个数据库节点部署，无实时同步数据的备节点，适用于数据可靠性要求不高的纯缓存业务场景使用。单节点具有明显的价格优势，性价比较高。 |
| 主（备）可用区节点 | 该概念存在于多可用区部署的实例中。通常会将主节点部署在主可用区，即为 主可用区节点 ，将备节点部署在备可用区，即为 备可用区节点 。更多信息请参见 [地域和可用区](https://help.aliyun.com/zh/document_detail/40654.html) 。 若实例配置为 1 个主节点、2 个备节点，通常会在主可用区部署 1 个主节点、1 个备节点，在备可用区部署另 1 个备节点。 若实例配置为 1 个主节点、3 个或以上的备节点，您至少需要在主可用区部署 1 个主节点、1 个备节点，然后您可以自定义将剩余的备节点部署在主可用区或备可用区。 |
| 部署模式 | 云原生 ：基于新一代管控架构，扩容、弹性能力强，规格配置更加灵活。 经典 ：基于传统管控架构。 更多信息请参见 [云原生实例和经典实例对比](comparison-between-tair-instances-that-cloud-native-and-classic.md) 。 |
| 系列 | 标准版 ：CPU 为 X86 架构，支持单节点、主备、集群、读写分离四种架构，扩展性强。 倚天版 ：CPU 为 ARM（倚天）架构，仅支持主备架构，具有价格优势，更多信息请参见 [倚天版实例](cost-efficient-instances.md) 。 |
| 存储介质 | Tair 实例支持 3 种存储介质，其特点和应用场景如下： Redis 开源版 ：以内存为存储介质，提供高性能、低时延的服务。 应用场景：开源 Redis 使用场景。 [内存](dram-based-instances.md) ：以内存为存储介质，额外采用多线程模型，性能约为同规格 Redis 开源版 实例的 3 倍。支持半同步、数据按时间点恢复（PITR）、全球多活等功能，同时提供多种增强型数据结构模块简化开发。 应用场景：超高性能场景、全球多活等。 [持久内存](persistent-memory-optimized-instances-1.md) ：数据在持久内存中存取，提供命令级强持久化能力。 应用场景：适用于对性能要求较高，同时对数据一致性有要求的场景。 [磁盘](essd-based-instances-1.md) ：数据存储在 ESSD、SSD 磁盘中，大容量、提供命令级强持久化能力，性能约为 Redis 开源版 的 60%，但价格最低为 Redis 开源版 的 15%。 应用场景：对性能要求不高，但是对成本有控制要求的场景。 |
| 版本兼容性 | 兼容 Redis 的版本，支持 Redis 7.0、Redis 6.0、Redis 5.0、Redis 4.0。 |
| 逐出策略 | 与 Redis 的逐出策略保持一致，详情请参见 [Key eviction](https://valkey.io/topics/lru-cache/) 。 |
| DB | Database， Tair 支持 256 个 DB（0 ~ 255），默认写入到第 0 个 DB 中，无法修改总 DB 数。 |
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
