# 与自建Redis对比的核心优势-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/comparison-between-apsaradb-for-redis-and-self-managed-redis

# 云数据库 Tair（兼容 Redis）与自建Redis的对比
相比自购服务器搭建Redis数据库，云数据库 Tair（兼容 Redis）在数据安全、运维投入、内核优化等方面都有一定的优势。
| 对比项 | 云数据库 Tair（兼容 Redis） | 自建 Redis |
| --- | --- | --- |
| 安全防护 | 事前防护： VPC 网络隔离。 [白名单控制访问](../getting-started/step-2-configure-whitelists.md) 。 [自定义账号与权限](../user-guide/create-and-manage-database-accounts.md) 。 | 事前防护： 需自行构建网络安全体系，成本高，难度大。 Redis 的默认访问配置存在安全漏洞，可能导致 Redis 数据泄露。 无账号鉴权体系。 |
| 事中保护： [TLS](../user-guide/enable-tls-encryption.md) [加密](../user-guide/enable-tls-encryption.md) 。 | 事中保护：需要自行通过第三方工具实现 SSL 加密访问。 |  |
| 事后审计： [审计日志](../user-guide/view-audit-logs.md) 。 | 事后审计：无审计功能。 |  |
| 备份恢复 | Tair（企业版） [内存型](dram-based-instances.md) 支持数据闪回功能，可以恢复指定时间点的数据。更多信息，请参见 [通过数据闪回按时间点恢复数据](../user-guide/use-data-flashback-to-restore-data-by-point-in-time.md) 。 | 仅支持一次性全量恢复。 |
| 运维管理 | 支持十余组监控指标，最小监控粒度为 5 秒。更多信息，请参见 [监控指标说明](../user-guide/metrics.md) 。 支持 [报警设置](../user-guide/alert-settings.md) 。 可根据需求创建多种架构的实例，支持变配到其它架构和规格。 提供基于快照的大 key 分析功能，精度高，无性能损耗。更多信息，请参见 [离线全量](../user-guide/offline-key-analysis.md) [Key](../user-guide/offline-key-analysis.md) [分析](../user-guide/offline-key-analysis.md) 。 | 需使用管理方式复杂的第三方监控工具实现服务监控。 改变规格或架构的操作复杂，且需要停止服务。 支持基于采样的大 key 分析，统计粗糙，精度较低。 |
| 部署和扩容 | 即时开通，弹性扩容。 | 需要自行完成采购硬件、机房托管、部署机器等工作，周期较长，且需要自行维护节点关系。 |
| 高可用 | [单可用区高可用方案](disaster-recovery.md) 。 [同城容灾（多可用区）方案](disaster-recovery.md) 。 高可用性由独立的中心化模块保障，决策效率高且稳定，不会出现脑裂（split brain）现象。 | 需要自行部署基于哨兵模式的机房内高可用架构。 可基于哨兵模式搭建同城容灾架构。 高可用性由哨兵机制保障，搭建成本高，且在业务高峰期决策效率低，可能发生脑裂导致业务受损。 |
| 内核优化 | Tair（企业版） 提供多线程的 [增强性能实例](dram-based-instances.md) ，性能为同规格标准版实例的 3 倍。 Tair（企业版） 提供 [磁盘型](essd-based-instances-1.md) 和 [持久内存型](persistent-memory-optimized-instances-1.md) 实例，支持大容量存储和命令级别持久化。 | 6.0 以上版本支持多 IO 线程以增强性能，性能至多提升 2 倍，且 CPU 资源消耗高。 可采用 SSDB、Pika 等持久化存储方案，但对 Redis 协议的兼容度低，仅支持 key 级别冷热数据管理，大 key 交换成本高，管理困难。 |
| 内存 | 已购内存 100%可用，容灾、运维管理、扩容、实例持久化（Fork 写时复制）等占用的内存开销均由阿里云承担，不占用实例内存容量。 例如：采购 64 GB 的实例，用户可用内存为 64 GB。 | 需预留 25% ~ 40%的内存资源用于容灾、运维管理、扩容等用途。 例如：采购 2 台内存为 64 GB 的 ECS 搭建 Redis 主备实例，用户可用内存通常低于 45 GB。 |
说明
云数据库 Tair（兼容 Redis）与Redis完全兼容（请参见[云数据库 Tair（兼容 Redis）兼容](../support/which-version-of-redis-is-apsaradb-for-redis-compatible-with.md)[Redis](../support/which-version-of-redis-is-apsaradb-for-redis-compatible-with.md)[哪个版本？](../support/which-version-of-redis-is-apsaradb-for-redis-compatible-with.md)），连接数据库的方式也基本相同，您可以根据自身应用特点选用任何兼容Redis协议的客户端程序，详情请参见[客户端程序连接教程](../user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance.md)。
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
