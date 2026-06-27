# 数据库命令事件时延统计分析-时延洞察-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/latency-insights

# 时延洞察
CloudDBA的时延洞察功能可以对云数据库 Tair（兼容 Redis）数据库所有命令以及自定义特殊事件进行时延统计，并给出精确到微秒级别的延迟时间。您可以通过该功能排查云数据库 Tair（兼容 Redis）数据库的故障和性能降低的原因。
## 功能简介
Redis在2.8.13版引入时延监控（Latency Monitoring）特性，基于事件机制帮助您发现和排查可能的时延问题。该功能仅支持获取最近160秒的数据，且只存取每秒内时延最高的事件。
时延洞察是云数据库 Tair（兼容 Redis）提供的升级版时延统计功能，支持记录多达[27](latency-insights.md)[个事件](latency-insights.md)及所有Redis命令的执行耗时，并支持保存最近3天内所有的时延统计数据。时延洞察具有如下特点：
持久化：支持数据持久化，时延毛刺可追溯。
高精度：支持全量事件微秒级别监控信息。
高性能：异步实现，对性能几乎无影响。
实时性：支持实时数据查询和聚合操作。
多维度：提供全面的时延信息，可支持从事件、时间、时延三个维度对实例进行分析。
## 前提条件
云数据库 Tair（兼容 Redis）实例为如下版本，升级方法请参见[升级小版本与代理版本](update-the-minor-version.md)。
Tair（企业版）[内存型](../product-overview/dram-based-instances.md)，小版本为1.6.9及以上。若需统计Tair module命令，请升级小版本至1.7.28及以上。
Redis开源版5.0，小版本为5.1.4及以上。
Redis开源版6.0，小版本为6.0.1.15及以上。
Redis开源版7.0，小版本为7.0.0.6及以上。
### 费用
此功能不收费。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击CloudDBA>时延洞察。
在时延洞察页，选定待查看的时间段（默认为最近5分钟），单击查看。
对于集群和读写分离架构的实例，支持分别查看数据节点和代理节点的统计信息。
说明
仅支持查询最近3天内的历史数据，且开始时间和结束时间的间隔不超过1小时。
单击事件名称或列表中的统计数字，查看事件对应指标随时间的变化趋势。
在趋势图中，您也可以选择对应的指标，查看其随时间的变化趋势。
说明
仅会记录与展示耗时超过阈值的命令或事件。若您在使用该功能的过程中遇到实例时延问题，您可参考[常见](suggestions-for-handling-common-latency-events.md)[Latency（时延）事件的处理建议](suggestions-for-handling-common-latency-events.md)文档处理时延问题。
| 指标 | 说明 |
| --- | --- |
| 事件 | 事件名称，包含 ExpireCycle、EventLoop、Ping、Scan、Commands、Info 等事件，更多信息请参见 [常见特殊事件附录](latency-insights.md) 。 |
| 总数 | 事件的数量。 |
| 时延 avg(us) | 事件的平均延迟时间，单位 ：微秒（us）。 |
| 时延 max(us) | 事件的最大延迟时间，单位：微秒（us）。 |
| <1ms 聚合 | 延迟时间小于 1ms 事件的聚合统计数量，单击 查看<1us、<2us、<4us、<8us、<16us、<32us、<64us、<128us、<256us、<512us 和<1ms 等不同时间范围的统计数据。 说明 不同时间范围的统计规则：例如，<1us，统计延迟时间在 0~1us 之间的事件数量；<2us，统计延迟时间在 1us~2us 之间的事件数量。 |
| <2ms <4ms ... >33s | 延迟时间对应此范围内的事件数量。 说明 不同时间范围的统计规则：例如，<2ms，统计延迟时间在 1ms~2ms 之间的事件数量；>33s，统计延迟时间大于 33s 的事件数量。 |
## 常见特殊事件附录
| 类别 | 名称 | 阈值 | 说明 |
| --- | --- | --- | --- |
| 内存驱逐相关 | EvictionDel | 30ms | 在逐出周期中删除 Key 的耗时。 |
| EvictionLazyFree | 30ms | 在逐出周期中，等待后台线程释放内存的耗时。 |  |
| EvictionCycle | 30ms | 一次逐出周期的耗时，包含逐出数据的选择、删除操作，及后台线程等待的时间。 |  |
| 内存碎片整理 | ActiveDefragCycle | 100ms | 内存碎片整理过程的耗时。 |
| Rehash | Rehash | 100ms | 发生 Rehash 过程的耗时。 |
| 数据结构升级 | ZipListConvertHash | 30ms | Hash 编码类型转换耗时（Ziplist 转换为 Dict）。 |
| IntsetConvertSet | 30ms | Set 编码类型转换耗时（Intset 转换为 Set）。 |  |
| ZipListConvertZset | 30ms | Zset 编码类型转换耗时（Ziplist 转换为 Skiplist）。 |  |
| AOF 相关 | AofWriteAlone | 30ms | 一次正常写入 AOF 文件的耗时。 |
| AofWrite | 30ms | 写入 AOF（AppendOnly File）的耗时。每次成功写入 AOF 文件后，会记录 AofWrite 事件以及 AofWriteAlone、AofWriteActiveChild、AofWritePendingFsync 三者中的一种事件。 |  |
| AofFstat | 30ms | Fstat 的耗时。 |  |
| AofRename | 30ms | Rename 的耗时统计。 |  |
| AofReWriteDiffWrite | 30ms | 子进程重写完 AOF 后，主进程把 buffer 中的增量 AOF 写入的耗时。 |  |
| AofWriteActiveChild | 30ms | 写入 AOF 文件的耗时，写入过程中存在其他子进程也在向磁盘写数据等情况。 |  |
| AofWritePendingFsync | 30ms | 写入 AOF 文件的耗时，写入过程中存在后台进程正在执行 fsync。 |  |
| RDB 相关 | RdbUnlinkTempFile | 50ms | bgsave 子进程中断后删除临时 RDB 文件的耗时。 |
| 其他 | Commands | 30ms | 常规命令（未被标为@fast）的耗时。 |
| FastCommand | 30ms | 被标为@fast 的命令（命令的时间复杂度为 O(1)和 O(log N)）的耗时。 |  |
| EventLoop | 50ms | Main Loop 一次的耗时。 |  |
| Fork | 100ms | 调用 Fork 操作的耗时。 |  |
| Transaction | 50ms | 实际事务执行的耗时。 |  |
| PipeLine | 50ms | 多线程 Pipeline 耗时。 |  |
| ExpireCycle | 30ms | 一次清理过期 Key 周期的耗时。 |  |
| ExpireDel | 30ms | 在清理过期 Key 周期中，删除 Key 的耗时。 |  |
| SlotRdbsUnlinkTempFile | 30ms | Slot bgsave 子进程中断后删除临时 RDB 文件的耗时。 |  |
| LoadSlotRdb | 100ms | Slot 载入至（load）RDB 的耗时。 |  |
| SlotreplTargetcron | 50ms | Slot 子进程载入至（load）RDB 到一个临时的数据库（DB）后，再将其移动至目标数据库（DB）的耗时。 |  |
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
