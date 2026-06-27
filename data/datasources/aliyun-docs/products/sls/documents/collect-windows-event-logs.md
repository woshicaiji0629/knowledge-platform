# 如何通过控制台创建Logtail采集Windows事件日志-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/collect-windows-event-logs

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

# 采集Windows事件日志

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以通过Logtail插件采集Windows事件日志。本文介绍如何通过日志服务控制台创建Logtail配置采集Windows事件日志。

## 前提条件

- 

已在服务器上安装Windows Logtail 1.0.0.0及以上版本。具体操作，请参见[安装](products/sls/documents/install-logtail-on-a-windows-server.md)[Logtail（Windows](products/sls/documents/install-logtail-on-a-windows-server.md)[系统）](products/sls/documents/install-logtail-on-a-windows-server.md)。

- 

目标服务器持续产生日志。

重要

Logtail只采集增量日志。如果下发Logtail配置后，日志文件无更新，则Logtail不会采集该文件中的日志。更多信息，请参见[读取日志](products/sls/documents/log-collection-process-of-logtail.md)。

## 原理

对于事件日志，Windows提供了[Windows Event Log](https://docs.microsoft.com/en-us/windows/desktop/wes/windows-event-log)和[Event Logging](https://docs.microsoft.com/en-us/windows/desktop/EventLog/event-logging)两套API，前者是后者的升级，仅在Windows Vista及以上的版本中提供。Logtail插件会根据所运行的系统，自动选择API（优先选择Windows Event Log）来获取Windows事件日志。

Windows事件日志采用发布订阅的模式，应用程序或者内核将事件日志发布到指定的通道（例如Application、Security、System），Logtail通过对应的Logtail插件调用Windows API，实现对这些通道的订阅，从而不断地获取相关的事件日志并发送到日志服务。

Logtail支持同时采集多个通道事件，例如同时采集应用程序和系统日志。

## 查看通道信息

您可以在Windows服务器的事件查看器中查看通道信息。

- 

单击开始。

- 

搜索并打开事件查看器。

- 

在左侧导航栏中展开Windows 日志或应用程序和服务日志。

- 

查看通道的全名与通道相关信息。

Windows日志

- 

在Windows日志下，选择目标通道，右键单击属性，查看通道全名，包括：

- 

应用程序：Application

- 

安全：Security

- 

Setup：Setup

- 

系统：System

- 

在Windows日志下，单击目标通道，在页面中间区域查看事件的级别、日期和时间、来源和事件ID等信息。

在Logtail配置中，您可根据这些信息进行日志过滤。

应用程序和服务日志

- 

在应用程序和服务日志下，选择目标通道，右键单击属性，查看通道全名，例如：

- 

获取TerminalServices-LocalSessionManager/Operational的通道名。

- 

获取PowerShell/Operational的通道名。

## 采集步骤

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在接入数据区域，单击Windows 事件日志。

- 

选择目标Project和LogStore，单击下一步。

- 

在机器组配置页面，配置机器组。

- 

根据实际需求，选择使用场景和安装环境。

重要

无论是否已有机器组，都必须根据实际需求正确选择使用场景和安装环境，这将影响后续的页面配置。

- 

确认目标机器组已在应用机器组区域，单击下一步。

### 已有机器组

从源机器组列表选择目标机器组。

### 没有可用机器组

单击创建机器组，在创建机器组面板设置相关参数。机器组标识分为IP地址和用户自定义标识，更多信息请参见[创建用户自定义标识机器组（推荐）](products/sls/documents/create-a-user-defined-identity-machine-group.md)或[创建](products/sls/documents/create-an-ip-address-based-machine-group.md)[IP](products/sls/documents/create-an-ip-address-based-machine-group.md)[地址机器组](products/sls/documents/create-an-ip-address-based-machine-group.md)。

重要

创建机器组后立刻应用，可能因为连接未生效，导致心跳为FAIL，您可单击自动重试。如果还未解决，请参见[Logtail](products/sls/documents/troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组无心跳](products/sls/documents/troubleshoot-the-errors-related-to-logtail-machine-groups.md)进行排查。

- 

在数据源设置页签中，设置配置名称和插件配置，然后单击下一步。

- 

inputs为数据源配置，必选项。

重要

一个inputs中只允许配置一个类型的数据源。

- 

processors为处理配置，用于解析数据。可选项，您可以配置一种或多种处理方式。

如果当前的inputs配置无法满足日志解析需求，您可以在插件配置中添加processors配置，即添加Logtail插件处理数据。例如提取字段、提取日志时间、脱敏数据、过滤日志等。更多信息，请参见[使用](products/sls/documents/overview-22.md)[Logtail](products/sls/documents/overview-22.md)[插件处理数据](products/sls/documents/overview-22.md)。

例如您要采集应用程序、系统、TerminalServices-LocalSessionManager/Operational等通道对应的日志，则可以在inputs中添加如下示例。

{ "inputs": [ { "type": "service_wineventlog", "detail": { "Name": "Application", "IgnoreOlder": 259200 } }, { "type": "service_wineventlog", "detail": { "Name": "System", "IgnoreOlder": 259200 } }, { "type": "service_wineventlog", "detail": { "Name": "Microsoft-Windows-TerminalServices-LocalSessionManager/Operational", "IgnoreOlder": 259200 } } ] }

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| type | String | 是 | 数据源类型，固定为 service_wineventlog 。 |
| Name | String | 是 | 待采集事件日志所属的通道名称。不配置时，默认为 Application，表示采集 应用程序 通道中的事件日志。您可以在 Windows 系统中查看通道全名。更多信息，请参见 [步骤](products/sls/documents/collect-windows-event-logs.md) [4](products/sls/documents/collect-windows-event-logs.md) 。 |
| IgnoreOlder | UINT | 否 | 根据事件时间过滤日志，此配置是相对于采集开始时间的偏移量，单位为秒，早于此设置的日志会被忽略。 例如： 设置为 3600，表示相对于采集开始时间一小时前的日志都会被忽略。 设置为 14400，表示相对于采集开始时间四小时前的日志都会被忽略。 默认为空，表示不根据事件时间进行过滤，采集服务器上所有的历史事件日志。 说明 该选项仅在首次配置采集时生效，Logtail 会记录事件采集的 Checkpoint，保证不会重复采集事件日志。 |
| Level | String | 否 | 根据事件等级过滤日志，默认值为 information, warning, error, critical ，表示采集除了 verbose 等级外的其他所有日志。 可选值包括：information、warning、error、critical、verbose。您可以使用半角逗号（,）指定多个等级。 说明 该参数仅支持 Windows Event Log API，即只能在 Windows Vista 及以上的操作系统上使用。 |
| EventID | String | 否 | 根据事件 ID 过滤日志，可以指定正向过滤（单个或范围）或者反向过滤（不支持范围设置）。默认为空，表示采集所有事件。例如： 1-200 表示只采集事件 ID 在 1-200 范围内的事件日志。 20 表示只采集事件 ID 为 20 的事件日志。 -100 表示采集除了事件 ID 为 100 以外的所有事件日志。 1-200,-100 表示采集 1-200 范围内除了 100 以外的事件日志。 您可以使用半角逗号（,）指定多个值。 说明 该参数仅支持 Windows Event Log API，即只能在 Windows Vista 及以上的操作系统上使用。 |
| Provider | String 数组 | 否 | 根据事件来源过滤日志。例如设置为 ["App1", "App2"] 表示只采集来源名字为 App1 和 App2 的事件日志，其他事件日志都会被忽略。 默认为空，表示采集所有来源的事件。 说明 该参数仅支持 Windows Event Log API，即只能在 Windows Vista 及以上的操作系统上使用。 |
| IgnoreZeroValue | Boolean | 否 | 并非每条事件日志都拥有所有的字段，您可以使用此参数过滤空字段，空字段的定义根据类型而定，例如整数类型使用 0 表示空字段。 默认为 false ，表示不过滤空字段。 |


- 

创建索引和预览数据，然后单击下一步。日志服务默认开启全文索引。您也可以根据采集到的日志，手动创建字段索引，或者单击自动生成索引，日志服务将自动生成字段索引。更多信息，请参见[创建索引](products/sls/documents/create-indexes.md)。

重要

如果需要查询日志中的所有字段，建议使用全文索引。如果只需查询部分字段、建议使用字段索引，减少索引流量。如果需要对字段进行分析（SELECT语句），必须创建字段索引。

- 

单击查询日志，系统将跳转至LogStore查询分析页面。

您需要等待1分钟左右，待索引生效后，才能在原始日志页签中，查看已采集到的日志。更多信息，请参见[查询与分析快速指引](products/sls/documents/quick-guide-to-query-and-analysis.md)。

## 问题排查

使用Logtail采集日志后，如果预览页面或查询页面无数据，您可以参见[Logtail](products/sls/documents/what-do-i-do-if-errors-occur-when-i-use-logtail-to-collect-logs.md)[采集日志失败的排查思路](products/sls/documents/what-do-i-do-if-errors-occur-when-i-use-logtail-to-collect-logs.md)进行排查。

## 后续步骤

采集Windows事件至日志服务后，您可以在日志服务控制台上查看日志。

_source_: xxx __tag__:__client_ip__: xxx __tag__:__hostname__: xxx __tag__:__receive_time__: 1545292473 __topic__: activity_id: {085C7022-038B-40E4-BF0B-EB97C4337940} computer_name: xxx event_data: {"DCName":"\\\\HZ-FT-xxx","ProcessingMode":"0","ProcessingTimeInMilliseconds":"5812","SupportInfo1":"1","SupportInfo2":"4220"} event_id: 1501 kernel_time: 0 keywords: [] level: 信息 log_name: System message: 成功处理了此用户的组策略设置。自上一次成功处理了组策略后，没有检测到更改。 message_error: opcode: 开始 process_id: 248024 processor_id: 0 processor_time: 0 provider_guid: {AEA1B4FA-97D1-45F2-A64C-4D69FFFD92C9} record_number: 6908 related_activity_id: session_id: 0 source_name: Microsoft-Windows-GroupPolicy

| 字段名 | 说明 |
| --- | --- |
| activity_id | 当前事件所属活动的全局事务 ID，同一个活动的事件具有相同的全局事务 ID。 |
| computer_name | 产生当前事件的节点名。 |
| event_data | 和当前事件相关的数据。 |
| event_id | 当前事件的 ID。 |
| kernel_time | 当前事件消耗的内核时间，一般为 0 。 |
| keywords | 当前事件关联的关键字，用于事件分类。 |
| level | 当前事件的等级。 |
| log_name | 当前事件的通道名，即 Logtail 采集配置中 Name 参数。 |
| message | 当前事件关联的消息。 |
| message_error | 在解析当前事件关联消息时发生的错误信息。 |
| opcode | 当前事件关联的操作码。 |
| process_id | 当前事件的进程 ID。 |
| processor_id | 当前事件对应的处理器 ID，一般为 0 。 |
| processor_time | 当前事件消耗的处理器时间，一般为 0 。 |
| provider_guid | 当前事件来源的全局事务 ID。 |
| record_number | 当前事件关联的记录编号。事件的记录编号会随着每条事件的写入递增，当超过 2 32 （Event Logging）或 2 64 （Windows Event Log）后会重新从 0 开始。 |
| related_activity_id | 当前事件所属活动关联的其他活动的全局事务 ID。 |
| session_id | 当前事件的会话 ID，一般为 0 。 |
| source_name | 当前事件的来源，即 Logtail 采集配置中 Provider 参数。 |
| task | 当前事件关联的任务。 |
| thread_id | 当前事件的线程 ID。 |
| type | 获取当前事件使用的 API。 |
| user_data | 当前事件关联的用户数据。 |
| user_domain | 当前事件关联的用户域。 |
| user_identifier | 当前事件关联的用户 Windows 安全标识。 |
| user_name | 当前事件关联的用户名。 |
| user_time | 当前事件消耗的用户态时间，一般为 0 。 |
| user_type | 当前事件关联的用户的类型。 |
| version | 当前事件的版本号。 |
| xml | 当前事件最原始的信息，XML 格式。 |


[上一篇：采集Kubernetes事件](products/sls/documents/collect-kubernetes-events.md)[下一篇：采集Docker事件](products/sls/documents/collect-docker-events.md)

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
