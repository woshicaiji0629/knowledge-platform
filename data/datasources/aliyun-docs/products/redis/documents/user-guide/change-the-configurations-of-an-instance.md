# 变更内存容量和实例架构-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/change-the-configurations-of-an-instance

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

# 变更实例配置

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库 Tair（兼容 Redis）支持灵活变更实例的配置，包括变更实例架构、扩缩容内存、分片数、备节点数等，以满足不同业务对性能和容量的需求。

## 支持的变配项及影响

变配不会影响什么？

所有变配操作：

- 

连接地址、账号密码、白名单等不变：变更完成后应用代码无需修改。

- 

通常不丢失数据：但在切换的瞬间，若发生原主节点宕机等并发的极端情况，存在丢失少量未同步数据的理论风险。

| 变配类型 | 变配影响 |
| --- | --- |
| 单节点变配到高可用（主从双副本） | 1~2 次 30 秒内连接闪断，1 分钟左右只读。 |
| [标准（主备）转集群](products/redis/documents/user-guide/change-the-architecture-of-an-instance.md) | 1~2 次 30 秒内连接闪断，1 分钟左右只读。 |
| [集群转标准（主备）](products/redis/documents/user-guide/change-the-architecture-of-an-instance.md) | 1~2 次 30 秒内连接闪断，1 分钟左右只读。 |
| [升降实例规格](products/redis/documents/user-guide/change-the-instance-specification.md) | 可能出现 1~2 次 30 秒内连接闪断，1 分钟左右只读。 |
| [调整集群分片数](products/redis/documents/user-guide/adjust-the-number-of-cluster-shards.md) | 可能出现 1~2 次 30 秒内连接闪断，1 分钟左右只读。 |
| [开关读写分离](products/redis/documents/user-guide/enable-read-write-splitting.md) | 秒级闪断。 |
| [增删备节点](products/redis/documents/user-guide/node-management.md) | 无。 |
| [转为云原生部署模式](products/redis/documents/user-guide/change-to-the-cloud-native-deployment-mode.md) | 1 次 30 秒内连接闪断，1 分钟左右只读。 |


## 自动扩容实例配置

云数据库 Tair（兼容 Redis）集成了[DAS](https://help.aliyun.com/zh/das/product-overview/what-is-das#concept-2419191)的自动扩容功能，当内存平均使用率达到阈值后会自动升级实例的规格，帮助您快速弹性适配业务高峰，避免内存溢出的风险，有效保障线上业务稳定性。具体操作，请参见[开启自动扩容](products/redis/documents/user-guide/enable-automatic-scale-up.md)。

## 常见问题

### 如何查询实例是否扩容过？

您可以在[任务中心](products/redis/documents/user-guide/job-center.md)选中状态统计为执行成功的任务，查看是否存在规格变更或迁移的任务，或通过[DescribeHistoryTasks](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-describehistorytasks-redis.md)API接口进行查询。

### 什么原因会导致变配失败？

- 

若实例中存在大Key，可能会导致变配失败。

建议在变配前，排查并删除大Key，再执行变配操作。关于排查大Key的方法请参见[离线全量](products/redis/documents/user-guide/offline-key-analysis.md)[Key](products/redis/documents/user-guide/offline-key-analysis.md)[分析](products/redis/documents/user-guide/offline-key-analysis.md)。

- 

为避免数据丢失，降配时存在如下限制：新实例内存规格的80%需大于原实例已使用内存（即新规格内存 * 0.8 > 原实例已使用内存 ），否则将变配失败。例如当前实例为8 GB标准架构内存型，已使用2 GB内存，可降配至4 GB标准架构内存型。

### Tair（企业版）不同存储介质如何变配？

Tair（企业版）不同存储介质（内存型、持久内存型、磁盘ESSD型）间不支持相互变配。

### 能否单独提高实例的CPU性能？

Tair（以及Redis开源版）不支持单独升级CPU。您可以通过以下方式提升实例整体的CPU性能：

- 

标准架构实例变更为集群架构或读写分离架构。

- 

读写分离架构实例增加只读节点数。

- 

集群架构实例增加分片数。

具体操作，请参见[如何升级实例的](products/redis/documents/support/how-to-upgrade-redis-cpu-specifications.md)[CPU](products/redis/documents/support/how-to-upgrade-redis-cpu-specifications.md)[规格](products/redis/documents/support/how-to-upgrade-redis-cpu-specifications.md)。

实例规格信息，请参见[实例规格](products/redis/documents/product-overview/overview-4.md)。

### 高可用（双副本）实例如何变更为单副本实例？

由于单副本无数据可靠性保证，因此不支持将高可用实例变配为单副本实例。

如有需要，请单独购买高可用实例，再通过DTS将高可用实例的数据迁移到单副本实例，更多信息请参见[云数据库](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-for-redis-instances#task-2119264)[Tair（兼容](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-for-redis-instances#task-2119264)[Redis）间的迁移](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-apsaradb-for-redis-instances#task-2119264)。

### 变配时，需要业务暂停读写吗？

不需要。但由于可能出现1分钟左右的只读状态和1～2次30秒内连接闪断，建议您在业务低峰期变更配置和执行切换。具体变配对业务的影响，请参见[支持的变配项及影响](products/redis/documents/user-guide/change-the-configurations-of-an-instance.md)。

### 标准版变配为集群版或集群版增减分片数时，数据会自动迁移到各个分片？

是的。标准版变配为集群版或集群版增减分片数时，后台将自动迁移数据，使数据均衡分布在各个分片。

### 变配需要多长时间？

变更配置与网络、业务请求量、数据量大小等多种因素有关，因此变配时长无法预估。

您可以在实例信息页面右上角，单击查看任务进度。

### 变配会丢失备份集吗？

变配不会造成备份集丢失。但经典版集群架构实例在减少分片或变配为标准架构时，会导致历史备份集与实例节点的映射关系产生变化。

在该场景下，如何查找历史备份集：您可以通过历史备份时间点、历史备份集ID检索相关的备份集。

如何完成恢复操作：您可以通过下载历史备份集（RDB文件）、解析、导入至新实例中完成备份恢复。

### 变配后，配置为什么没有更新？

可能是元数据缓存刷新延迟，请稍等几分钟后刷新页面。

### 为什么选择运维时间执行变配，但是任务依然立刻执行了？

对于云原生标准版高可用实例，在当本地资源充足时，升降配规格为无影响操作，系统将忽略用户指定的时间，默认立即执行；本地资源不足时，系统将按照用户指定的时间执行，在切换时会出现1～2次30秒内闪断。

## 相关API

| API 接口 | 说明 |
| --- | --- |
| [ModifyInstanceSpec](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-modifyinstancespec-redis.md) | 变配实例的规格。 |


[上一篇：实例回收站](products/redis/documents/user-guide/manage-instances-in-the-recycle-bin.md)[下一篇：变更实例架构](products/redis/documents/user-guide/change-the-architecture-of-an-instance.md)

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
