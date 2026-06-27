# 创建、修改、删除时序库MetricStore-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/manage-a-metricstore

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

# 管理MetricStore

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

删除MetricStore必须提前删除所有Logtail配置，通过减少数据保存时间，实现日志的自动删除。本文介绍如何在日志服务控制台上创建、修改、删除MetricStore与时序数据等操作。

## 基本概念

时序库（MetricStore）是日志服务中时序数据的采集、存储和查询单元。每个MetricStore隶属于一个Project，每个Project中可创建多个MetricStore。更多信息，请参见[时序库（MetricStore）](products/sls/documents/metricstore.md)。

## 前提条件

已创建Project。具体操作，请参见[管理](products/sls/documents/manage-a-project.md)[Project](products/sls/documents/manage-a-project.md)。

## 创建MetricStore

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在时序存储>日志库页签中，单击+图标。

- 

在创建MetricStore面板，配置如下参数，单击确定。

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| MetricStore 名称 | MetricStore 名称在其所属 Project 内必须唯一，创建后不能修改。 |
| 数据保存时间 | 日志服务采集的时序数据在 MetricStore 中的保存时间。 选择数据保存模式为 限定天数 保存，并按需设置数据保存时间。单位为天，取值范围：1~3000。 警告 当日志保存时间达到您所设置的保存时间后，日志将被删除。 缩短数据保存时间后，日志服务将在 1 小时内删除所有已超过保存时间的数据。但日志服务控制台首页的 用量明细 将于次日更新。例如您原本的数据保存时间为 5 天，现修改为 1 天，则日志服务将在 1 小时内删除前 4 天的日志。 选择数据保存模式为 永久保存 时，日志服务将永久保存采集到的时序数据。 说明 通过 SDK 方式获取数据保存时间时，如果对应值为 3650 则表示永久保存。 |
| Shard 数目 | 日志服务使用 Shard 读写数据。一个 Shard 提供的写入能力为 5 MB/s、500 次/s，读取能力为 10 MB/s、100 次/s。每个 MetricStore 中最多创建 10 个 Shard，每个 Project 中最多创建 200 个 Shard。更多信息，请参见 [分区（Shard）](products/sls/documents/shard.md) 。 |
| 自动分裂 Shard | 打开 自动分裂 Shard 开关后，如果您写入的数据量超过已有 Shard 服务能力，日志服务会自动根据数据量增加 Shard 数量。更多信息，请参见 [管理](products/sls/documents/manage-shards.md) [Shard](products/sls/documents/manage-shards.md) 。 |
| 最大分裂数 | 打开 自动分裂 Shard 开关后，最多支持自动分裂至 256 个 readwrite 状态的 Shard。 |


## 修改MetricStore配置

- 

在时序存储>日志库页签中，将鼠标悬浮在目标MetricStore上，选择修改。

- 

在MetricStore属性页面中，单击修改。

- 

基础信息

- 

数据保存时间：参数说明请参见[创建](products/sls/documents/manage-a-metricstore.md)[MetricStore](products/sls/documents/manage-a-metricstore.md)。

- 

自动分裂Shard：开启后支持自动分裂更多Shard以提供更大的写入能力，参见[管理](products/sls/documents/manage-shards.md)[Shard](products/sls/documents/manage-shards.md)。

- 

最大分裂数：限制单Store最大可分裂的Shard个数，最多支持自动分裂至256个readwrite状态的Shard。

- 

记录外网IP：打开记录外网IP开关后，日志服务自动把以下信息添加到日志的Tag字段中。

- 

__client_ip__：日志来源设备的公网IP地址。

- 

__receive_time__：日志到达服务端的时间，格式为Unix时间戳，表示从1970-1-1 00:00:00 UTC计算起的秒数。

- 

Shard管理：

创建MetricStore时，默认为MetricStore创建2个Shard。在后续使用中，您可以根据业务需求分裂或合并Shard。具体操作，请参见[管理](products/sls/documents/manage-shards.md)[Shard](products/sls/documents/manage-shards.md)。

- 

查询加速配置

Prometheus Query计算引擎默认不对执行结果进行缓存，每次查询都需全量读取所有数据并重新执行计算；并且标准计算引擎仅支持单节点上执行单协程化计算，在时间线多、查询时间段长、计算逻辑复杂等场景下性能较差。为提供更高效的PromQL计算，SLS时序计算引擎引入了全局缓存、并发计算两项计算增强能力。详细设计原理与配置方式参见[查询加速](products/sls/documents/speed-up-promql.md)。

- 

写入配置

由于MetricStore对指标数据按时间顺序组织存储的特性，若时序库中乱序写入过多脏数据（例如，实时MetricStore中持续乱序写入数月前的数据、或因机器时钟问题致使生成非法数据等场景）会严重影响时序库的查询性能。

MetricStore支持过滤掉异常时间点的监控数据，在写入配置页面中配置左/右时间段窗口即可。“左/右区间”配置项的单位是秒，以数据到达SLS 服务时间为基准，合法数据写入时间为【数据到达时间-左区间，数据到达时间+右区间】，如超出范围，进行数据抛弃操作，当区间为【0,0】时，不进行数据写入时间范围规则判断。

说明

此特性仅对按Prometheus Remote Write协议写入的数据有效，采集接入方式参见[通过](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[Remote Write](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[协议接入](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[Prometheus](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[监控数据](products/sls/documents/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)。

- 

写入处理器

数据写入前进行处理。支持字段修改、字段解析、数据过滤、数据脱敏等多种使用场景。详情参见[数据写入时处理（写入处理器）](products/sls/documents/sls-write-processor.md)。

- 

标签

支持对MetricStore添加标签信息,当您需要对MetricStore进行分组管理时，可以使用标签来区分MetricStore。

- 

单击保存。

## 删除MetricStore

重要

- 

删除MetricStore前必须删除其对应的Logtail配置。具体操作，请参见[删除](products/sls/documents/manage-logtail-configurations-for-log-collection.md)[Logtail](products/sls/documents/manage-logtail-configurations-for-log-collection.md)[采集配置](products/sls/documents/manage-logtail-configurations-for-log-collection.md)。

- 

如果该MetricStore上还启用了数据投递，建议删除前停止向该MetricStore写入新数据，并确认MetricStore中已有的数据已经全部投递成功。

- 

删除全部MetricStore的当天仍会产生存储等费用，次日不再产生任何费用。即您在删除全部MetricStore的第三天不会再收到日志服务的账单。

- 

删除MetricStore后，以当前MetricStore为数据源的导出任务、数据加工任务、定时SQL任务和以当前MetricStore为目标的导入任务都将被删除。

删除MetricStore前，建议在任务管理>全部任务查看当前Project的全部任务，并删除与当前MetricStore关联的任务。

- 

在时序存储>日志库页签中，将鼠标悬浮在目标MetricStore上，选择删除。

警告

MetricStore一旦删除，其存储的时序数据将会被永久删除，不可恢复，请谨慎操作。

- 

在确认对话框中，单击确认。

## 删除时序数据

当时序数据保存时间达到您所设置的保存时间后，时序数据将被删除。因此您可以通过修改数据保存时间，从而删除时序数据。

重要

缩短数据保存时间后，日志服务将在1小时内删除所有已超过保存时间的数据。但日志服务控制台首页的用量明细将于次日更新。例如您原本的数据保存时间为5天，现修改为1天，则日志服务将在1小时内删除前4天的数据。

[上一篇：管理LogStore](products/sls/documents/manage-a-logstore.md)[下一篇：管理EventStore](products/sls/documents/manage-an-eventstore.md)

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
