# 日志采集失败的 6 大经典雷区-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/6-log-collection-failures

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 日志采集失败的 6 大经典雷区

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文探讨了日志采集过程中常见的六大错误及原因，并介绍了标准化实践（如 LoongCollector）的解决方案，帮助提升日志采集的稳定性与可靠性。

## 背景信息

科学的日志管理策略有助于保留历史记录、降低性能开销并提升采集效率。然而，许多运维实践中的反模式使主流日志采集工具（如 LoongCollector 等）难以高效工作。从源头优化日志管理，采用标准实践方案，可实现高效稳定的日志采集。

## 使用 copy truncate 模式轮转日志，因两个动作非原子并创建新文件，可能导致日志丢失或重复采集

使用 logrotate 的 copy truncate 模式轮转日志的原理是先复制原日志文件，然后截断原文件。这种方式存在以下问题：

- 

copy 动作产生的新文件可能被当作新的内容重复采集。因为文件系统的 inode 变化，采集器可能无法正确识别这是轮转后的旧文件。

- 

copy 和 truncate 之间产生的日志可能丢失。在这两个操作之间有一个时间窗口，此时写入的内容既不在复制的文件中，又会被截断操作清除。

- 

truncate 操作可能导致文件大小变小和头部内容变化，缩小文件或改变文件头部签名会导致采集器误判为新文件，造成重复采集。

因此，copy truncate 模式可能导致日志重复采集、内容丢失或不一致的问题。

优化方案：

推荐使用 create 模式进行日志轮转，即创建新文件并重命名旧文件，这样可以保证文件的完整性和连续性。如果无法避免，请在配置采集配置时使用精确的路径名。

## 使用 NAS、OSS 作为日志存储，因元信息不一致和 ls 性能低，可能导致日志采集截断或停止

网络附加存储（NAS）通常采用基于最终一致性的一致性模型，这在分布式系统中是常见的设计。在实时采集场景下，这可能导致以下问题：

- 

文件元信息与实际内容不一致。由于最终一致性，文件大小等元数据可能先于实际内容更新。

- 

读取到文件空洞。当元信息显示文件已增大，但实际内容尚未同步时，读取操作可能返回\0字符（文件空洞）。

- 

数据延迟。写入操作的结果可能不会立即对读取操作可见，导致采集延迟。

- 

数据丢失。由于 NAS 不支持 inotify 并且 list 性能低下，因此文件可能无法被发现，导致数据丢失。

这些问题可能导致采集到的数据与最终内容不一致。

优化方案：

建议使用 EBS，自建机器使用本地磁盘，以保证日志读写的效率和一致性。如无法避免，请在消费端做好异常日志的兼容逻辑。

## 多进程写日志，因数据互相覆盖，可能导致采集到的数据不完整

多进程并发写入同一日志文件是一种常见但不推荐的做法，它可能导致以下问题：

- 

文件内容交叉。多个进程的写入可能相互交叉，导致日志条目混乱。

- 

采集不完整。当文件发生写入事件时，采集器开始采集数据。但如果采集过程中其他进程继续写入，这些新写入的内容可能被跳过。

- 

文件锁争用。多进程写入可能导致文件锁争用，影响写入性能和可靠性。

这种模式可能导致采集到的数据不完整且与文件的最终内容不一致。

优化方案：

推荐多进程写入各自不同文件，这样可以保证日志的完整性和顺序性。如无法避免，请在消费端做好异常日志的兼容逻辑。

## 创建文件空洞释放日志文件空间，因改变文件签名和内容，可能导致日志重复采集或数据丢失

通过在文件头部创建空洞来释放日志文件空间是一种存在风险的做法，原因如下：

- 

文件签名改变。LoongCollector（原 iLogtail）为避免 inode 复用漏采数据，额外使用文件头部的内容作为文件唯一性的判断依据。创建空洞可能改变这个签名，导致采集器误判为新文件。

- 

数据完整性问题。创建空洞实际上是用\0字符替换了原有内容，可能导致重要的历史日志丢失。

- 

文件系统碎片化。频繁创建空洞可能导致文件系统碎片化，影响读写性能。

文件系统碎片化。频繁创建空洞可能导致文件系统碎片化，影响读写性能。

优化方案：

推荐使用标准的日志轮转机制来管理日志文件大小，如使用 logrotate 工具定期轮转日志文件，这样可以保证日志的完整性和可追溯性。如无法避免，建议使用fallocate而非truncate 或 dd，并在消费端做好异常日志的兼容逻辑。

## 频繁覆盖写文件，因文件内容频繁变化，可能导致采集数据不完整或不一致

频繁覆盖写整个日志文件是一种不安全的日志管理方式，可能导致以下问题：

- 

文件元信息与内容不一致。在覆盖过程中，文件大小等元信息可能先于实际内容更新，导致采集器读取到不完整或不一致的内容。

- 

数据丢失风险。如果在日志采集过程中发生覆盖写入，可能导致采集读取到的数据内容错乱或丢失。

- 

历史数据难以保留。频繁覆盖会导致无法保留历史日志，不利于问题追溯和分析。

这种做法可能导致采集到的内容与文件最终内容不一致，或完全丢失文件内容。

优化方案：

建议采用追加写入（append）的方式记录日志，并配合日志轮转机制管理文件大小。如无法避免，请在消费端做好异常日志的兼容逻辑。

## 使用 vim 编辑文件保存，因创建新文件替换原文件，可能导致日志重复采集

使用 vim 编辑并保存文件时，vim 的保存机制可能导致以下问题：

- 

inode 变化。vim 创建新文件替换原文件时，新文件的 inode 与原文件不同，可能导致采集器误判为新文件。

- 

文件签名改变。新文件的头部内容可能与原文件不同，改变了文件签名，导致采集器无法正确识别。

- 

文件内容丢失。当 vim 替换文件时，写入程序可能没有切换到新保存日志文件，可能导致日志内容丢失。

这种编辑方式可能导致日志重复采集或数据丢失。

优化方案：

如仅需查看日志，建议使用 less、grep 等只读工具。如无法避免，请在消费端做好去重和异常处理的逻辑

## 总结

日志是系统运行的“黑匣子”，其管理质量直接影响故障排查效率与系统可靠性。通过规避本文提到的反模式，遵循使用日志库轮转、本地盘写入、单线程追加等方案，可显著降低日志采集风险，提升可观测性能。

[上一篇：投递CDN实时日志到SLS来分析用户访问数据](products/sls/documents/ship-and-analyze-alibaba-cloud-cdn-real-time-logs-in-log-service.md)[下一篇：使用OOS批量安装或升级Logtail](products/sls/documents/best-practice-use-oos-to-batch-install-or-upgrade-logtail.md)

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
