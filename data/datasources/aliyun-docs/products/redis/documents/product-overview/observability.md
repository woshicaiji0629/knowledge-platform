# 产品可观测性各项能力详解-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/observability

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

# 可观测性能力介绍

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

相比Redis，云数据库 Tair（兼容 Redis）提供了维度更广、种类更多及功能更强大的可观测性能力（Observability）。

## 背景信息

可观测性是以系统的指标、日志、链路追踪三大数据支柱为基础，衍生出如数据监控、问题分析、系统诊断等一系列的能力。

- 

指标（Metrics）：记录一段时间内各个维度的量化信息，用来观察系统的某些状态和趋势。

- 

日志（Logs）：记录程序运行过程中产生的一些离散事件。

- 

链路追踪（Traces）：记录一次请求从接收到处理完成整个生命周期内的调用链路。

同时，云数据库 Tair（兼容 Redis）还基于三大数据支柱进行信息聚合，提供数据分析能力，下表为云数据库 Tair（兼容 Redis）与Redis的可观测性能力对比。为便于浏览和内容表达，表格约定使用下述注释：

- 

✔️表示支持。

- 

❌表示不支持。

- 

➖表示不涉及。

| 可观测性能力 | Redis | 阿里云 Redis 开源版 | Tair（企业版） |  |
| --- | --- | --- | --- | --- |
| 指标 | [性能指标](products/redis/documents/user-guide/view-monitoring-data.md) | ✔️ | ✔️（更细化） | ✔️（更细化） |
| 日志 | [运行日志](products/redis/documents/user-guide/view-active-logs.md) | ✔️ | ✔️ | ✔️ |
| [慢日志](products/redis/documents/user-guide/view-slow-logs.md) | ✔️ | ✔️ | ✔️ |  |
| [审计日志](products/redis/documents/user-guide/view-audit-logs.md) | ❌ | ✔️ | ✔️ |  |
| [时延洞察](products/redis/documents/user-guide/latency-insights.md) | ❌ | ✔️ | ✔️ |  |
| 链路追踪 | ➖ | ➖ | ➖ | ➖ |
| 分析能力 | [实时热](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) [Key](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) [分析](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) | ❌ | ✔️ | ✔️ |
| [实时大](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) [Key](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) [分析](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) | ❌ | ✔️ | ✔️ |  |
| [离线全量](products/redis/documents/user-guide/offline-key-analysis.md) [Key](products/redis/documents/user-guide/offline-key-analysis.md) [分析](products/redis/documents/user-guide/offline-key-analysis.md) | ❌ | ✔️ | ✔️ |  |
| [实例诊断](products/redis/documents/user-guide/create-a-diagnostic-report.md) | ❌ | ✔️ | ✔️ |  |


说明

链路追踪通常需要对客户端进行改造或由中间件提供。

## 指标

Redis提供了丰富的统计指标，包含Memory（内存分配、内存使用、内存碎片率情况等）， Stats（连接数、命令、网络、同步状态等）、CPU使用情况、Keyspace信息等。云数据库 Tair（兼容 Redis）结合用户的使用体验，在Redis的基础上增加了更细化的指标，例如读QPS、写QPS等，更多信息请参见[查看性能指标](products/redis/documents/user-guide/view-monitoring-data.md)。

与此同时，云数据库 Tair（兼容 Redis）的指标可观测性能力还具备如下优势：

- 

[实时性能](products/redis/documents/user-guide/view-performance-metrics-in-real-time.md)：实时展示指标信息。

- 

[实例会话](products/redis/documents/user-guide/instance-sessions.md)：实时展示Redis实例与客户端间的会话信息。

- 

[性能趋势](products/redis/documents/user-guide/performance-trends.md)：支持绘制任意时间跨度的曲线。

## 日志

云数据库 Tair（兼容 Redis）提供了查询运行日志、慢日志、审计日志、时延洞察等功能。

- 

运行日志（Redis log）

按行输出Redis运行过程中的日志信息，记录运行过程中持久化、同步复制、报错信息以及代码中定义的调试记录等。

在控制台目标实例详情页的日志管理>运行日志页签中，查看该实例的运行日志信息，更多信息请参见[查询运行日志](products/redis/documents/user-guide/view-active-logs.md)。

- 

慢日志（Slowlog）

记录Redis中执行时间（不含命令排队与网络传输时间）超过指定阈值的请求，慢日志信息包含执行时间戳、执行时长、命令参数、客户端信息等。您可以通过该功能第一时间查询耗时过长的命令列表，并进行相应优化，避免线上服务发生阻塞。

在控制台目标实例详情页的日志管理>慢日志页签中，查看该实例的慢日志信息，更多信息请参见[查询慢日志](products/redis/documents/user-guide/view-slow-logs.md)。

- 

审计日志（Audit log）

云数据库 Tair（兼容 Redis）基于[日志服务](products/sls/documents/what-is-log-service.md)[SLS（Log Service）](products/sls/documents/what-is-log-service.md)，提供审计日志功能，每条审计日志包含日志类型、执行时长、DB序号、客户端IP、账户名、命令详细信息以及扩展信息等。基于该功能，为您提供在线查询、分析操作日志（包含敏感操作FLUSHALL、FLUSHDB、DEL等）、慢日志及运行日志等，并且支持导出。

在控制台目标实例详情页的日志管理>审计日志页签中，查看该实例的审计日志信息，更多信息请参见[审计日志](products/redis/documents/user-guide/enable-the-new-audit-log-feature.md)。

- 

时延洞察（Latency metric）

时延洞察是云数据库 Tair（兼容 Redis）提供的升级版时延统计功能，支持记录多达27个事件及所有Redis命令的执行耗时，并支持保存最近3天内所有的时延统计数据。

在控制台目标实例详情页的CloudDBA>时延洞察页签中，查看该实例的时延信息，更多信息请参见[时延洞察](products/redis/documents/user-guide/latency-insights.md)。

## 分析能力

分析能力是基于指标、日志、链路追踪三大基础数据进行的信息聚合，是云数据库 Tair（兼容 Redis）重要的服务能力。

- 

热Key与大Key分析

当某个Key接收的访问次数显著高于其它Key时，可以将其称为热Key（Hotkeys），若未能及时处理热Key可能会导致访问倾斜甚至缓存击穿等问题；当某个Key含有较多数据成员或者占用较大内存时，可以将其称为大Key（Big keys），若未能及时处理大Key会导致执行命令的耗时增加，严重时甚至引发内存溢出（Out Of Memory）。

您可以通过云数据库 Tair（兼容 Redis）的实时Top Key统计功能，帮助定位热Key与大Key，实时Top Key统计功能支持实时展示实例中的热Key和大Key信息，同时支持查看4天内大Key和热Key的历史信息。实时Top Key统计功能准确性高，且对性能几乎无影响，帮助您掌握Key在内存中的占用、Key的访问频次等信息，溯源分析问题，为您的优化操作提供数据支持。

在控制台目标实例详情页的CloudDBA>实时Top Key统计页签中，进行热Key与大Key分析，更多信息请参见[实时](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md)[Top Key](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md)[统计](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md)。

- 

离线全量Key分析

离线全量Key分析功能支持全数据结构、全实例架构及Redis各个版本的离线RDB备份文件解析，对线上服务无影响。相比开源工具redis-rdb-tool的解析速度，离线全量Key分析在大小Key混合（占比1：9）的场景下实现4倍速度提升，在中大Key场景下实现20倍速度提升，同时保证进程内存占用固定维持在1 GB以内，避免大Key解析可能带来内存溢出的问题。离线全量Key分析还提供了最长子元素查询，方便进一步业务排查。

在控制台目标实例详情页的CloudDBA>离线全量Key分析页签中进行分析，更多信息请参见[离线全量](products/redis/documents/user-guide/offline-key-analysis.md)[Key](products/redis/documents/user-guide/offline-key-analysis.md)[分析](products/redis/documents/user-guide/offline-key-analysis.md)。

- 

实例诊断

云数据库 Tair（兼容 Redis）综合了性能指标、慢日志、key分析等能力，提供了一站式全链路的实例诊断功能，从性能水位、访问倾斜情况、慢日志等多方面评估实例的健康状况，并给出改善建议，极大程度地提高了Redis实例的自动化运维能力，降低使用成本。

在控制台目标实例详情页的CloudDBA>诊断报告页签中，进行实例诊断，更多信息请参见[实例诊断](products/redis/documents/user-guide/create-a-diagnostic-report.md)。

[上一篇：灾备方案介绍](products/redis/documents/product-overview/disaster-recovery.md)[下一篇：集群无感扩缩容介绍](products/redis/documents/product-overview/imperceptible-scaling.md)

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
