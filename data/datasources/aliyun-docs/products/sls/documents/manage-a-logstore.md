# 管理LogStore-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/manage-a-logstore

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

# 管理LogStore

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

LogStore是日志服务中的存储单元，用于收集、存储和查询日志数据。

## 核心概念

### 什么是LogStore

日志库（LogStore）是日志服务的数据容器。一个[Project（项目）](products/sls/documents/manage-a-project.md)下可以创建多个LogStore，用于隔离和管理不同业务或来源的日志。

此外，部分云产品或SLS自身功能也会自动创建专用的LogStore，这些LogStore有特定用途，不支持写入其他数据。例如：

- 

internal-operation_log：用于存储日志服务自身的[详细操作日志](products/sls/documents/manage-service-logs.md)。

- 

oss-log-store：在配置[OSS](products/sls/documents/usage-notes-of-oss-access-log.md)[访问日志](products/sls/documents/usage-notes-of-oss-access-log.md)转存时，自动创建的专属LogStore。

### LogStore规格对比

日志服务提供标准型（Standard）与查询型（Query）两种规格，它们在[功能](products/sls/documents/manage-a-logstore.md)与使用成本上有差异。

| 类型 | 成本（索引流量费用对比） | 适用场景 |
| --- | --- | --- |
| 标准型（Standard 规格） | 0.350 元 /GB | 适用于需要数据分析、实时监控和可视化能力，进行交互式分析、实时监控或构建可观测性系统的场景。 |
| 查询型（Query 规格） | 0.1 元 /GB | 不支持分析，适用于日志归档、审计日志存储、故障排查等快速检索日志内容而无需分析的归档类场景。典型应用包括大规模日志长期保存（如数月或数年），且访问频率较低的情况。 |


### 适用范围与权限

权限须知（可展开）

- 

使用阿里云主账号登录，默认拥有所有操作权限，可直接对LogStore进行相关操作。

- 

使用RAM用户登录，请根据需要向主账号使用者申请如下两种日志服务的系统策略。

- 

AliyunLogFullAccess：管理日志服务的权限。

- 

AliyunLogReadOnlyAccess：只读访问日志服务的权限。

当系统策略无法满足您的需求，您可以参考下表通过[创建自定义权限策略](products/ram/documents/create-a-custom-policy.md)实现精细化权限管理。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 操作 | 所需权限 |
| --- | --- |
| 管理 LogStore | log:ListProject log:GetAcceleration log:ListDomains log:GetLogging log:ListTagResources log:GetProject log:ListLogStores log:*LogStore log:*Index log:ListShards log:GetLogStoreHistogram log:GetLogStoreContextLogs |
| 查询 LogStore | log:ListProject log:GetAcceleration log:ListDomains log:GetLogging log:ListTagResources log:GetProject log:ListLogStores log:GetLogStore log:GetLogStoreHistogram log:GetIndex log:CreateIndex log:UpdateIndex log:ListShards log:GetLogStoreContextLogs |


## 创建基础LogStore

### 控制台

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签，单击+图标。

- 

在创建Logstore页面中，进行配置后，单击确定。

- 

LogStore类型：默认Standard。

- 

计费模式：

- 

[按使用功能计费（不支持更改）](products/sls/documents/pay-as-you-go.md)：按实际使用的每一项资源（如存储、索引、读写次数等）独立计费，并提供月度免费额度，便于小规模场景控制支出。

- 

[按写入数据量计费](products/sls/documents/billing-items-in-the-pay-per-data-write-mode.md)：只为原始写入数据付费，30天内存储及主流功能免费使用，成本结构更简单、更划算。

快速判断：存储天数越接近30天，索引字段数量越接近全文索引越适合按写入数据量计费。

- 

LogStore名称：在该Project内必须唯一，作为LogStore的唯一标识，创建后无法更改。

- 

数据保存时间：默认为30天。

- 

其余配置保持默认值即可。

LogStore全量参数列表（可展开）

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 描述 |
| --- | --- |
| LogStore 类型 | SLS LogStore 支持 Standard 和 Query 两种规格，可以根据使用场景进行选择，帮助您节省成本。 Standard 规格包含 SLS 完整一站式数据分析功能，适合用于实时监控，交互式分析以及构建完整可观测性系统等场景使用。 Query 规格的索引流量单价是 Standard 规格的 29%，在整体支出相同时，Query 规格可开启更多字段的索引，有效降低费用。Query 规格仅支持关键词搜索，不支持统计分析。 |
| 计费模式 | 按使用功能计费模式：是日志服务 SLS 原计费模式，根据客户实际使用到的资源（如存储、索引等）及功能（如数据加工、数据投递等）进行计费，按需使用按量付费。 按写入数据量计费模式：是日志服务 SLS 推出的极简计费模式，主要对数据写入量（原始大小）进行收费，数据写入后提供 30 天的免费存储周期，同时可以免费使用数据加工、数据投递等功能。计费简单可估可控，有助于深度使用日志服务 SLS 挖掘更大数据价值。 |
| LogStore 名称 | LogStore 名称在 Project 内全局唯一，创建后不可修改。 |
| WebTracking | WebTracking 功能支持快速采集各种浏览器以及 iOS/Android/APP 访问信息，默认关闭。 |
| 数据保存时间 | 数据的保存时间，单位为天。取值范围为 1~3650。如果配置为 3650，表示永久保存。当日志保存时间达到您所设置的保存时间后，日志将被删除。 |
| 智能存储分层 | 通过生命周期管理功能实现数据自动分层。 热存储： 热存储是一种可扩展、高可用的数据存储方案，用于存储经常被访问的数据。 支持数据实时访问，提供高性能的日志查询和分析功能，适用于数据高频查询分析等业务场景。 低频存储 低频存储（原冷存储）是一种能降低您长周期存储的成本的存储类型，同时保证日志的查询、分析、可视化、告警、投递和加工等能力不受影响。 适用于较低查询分析频率，问题回溯等业务场景。 归档存储 归档存储在现有热存储、低频存储的基础上，为您提供更低成本且可查询、分析的长期数据存储方案。 适用于数据审计长期保存的业务场景。 |
| Shard 数目 | 每个 Shard 支持 5 MB/s 的数据写入和 10 MB/s 的数据读取，当数据流量超过 Shard 服务能力时，建议您分裂 Shard，当数据流量达不到 Shard 的最大读写能力时，建议您合并 Shard 以节省费用。 |
| 自动分裂 Shard | 当写入数据量超过已有分区（Shard） [数据读写](products/sls/documents/data-read-and-write.md) 且持续 5 分钟以上时，开启自动分裂功能可自动根据数据量增加分区数量。 |
| 最大分裂数 | 开启自动分裂分区（Shard）后，最大可支持自动分裂至 256 个分区。 |
| 记录外网 IP | 接收日志后，自动添加客户端外网 IP 和日志到达时间。 |


### API

[创建](products/sls/documents/developer-reference/api-sls-2020-12-30-createlogstore.md)[LogStore](products/sls/documents/developer-reference/api-sls-2020-12-30-createlogstore.md)

## 修改LogStore配置

以下参数可在创建时配置，此处以修改LogStore为例进行介绍。

- 

单击日志存储，在日志库中，将鼠标悬浮在目标LogStore上，选择修改。

- 

在LogStore属性中根据下列场景修改相关配置项。

### 删除指定日志/设置日志保存时间

### 控制台

在基础信息中，单击修改，修改数据保存时间，然后单击保存。

日志服务不支持删除指定内容的日志，仅支持通过修改日志保存时间来按时间删除，或者通过[停止计费/删除](products/sls/documents/manage-a-logstore.md)[LogStore](products/sls/documents/manage-a-logstore.md)来删除全部日志。

- 

限定天数：取值范围：1~3650，其中3650表示永久保存。当保存期限到达时，日志将会被删除。

- 

永久保存：将永久保存该LogStore中的日志。

说明

修改后立即生效，但删除过期数据需要一定的时间。

### API

[更新](products/sls/documents/developer-reference/api-sls-2020-12-30-updatelogstore.md)[LogStore](products/sls/documents/developer-reference/api-sls-2020-12-30-updatelogstore.md)中ttl的值，来调整日志存储时间。

### 使用分层优化存储成本

### 控制台

- 

在基础信息中，单击修改，打开智能存储分层开关。

- 

进行存储策略配置：三种存储天数总和需要等于数据保存时间中的天数。

- 

热存储：至少7天。

- 

低频存储：至少30天。

- 

归档存储：至少60天。

将数据保存时间设置为限定天数，开启智能存储分层开关，并在存储策略中配置各层转换操作：热存储到期后自动转换为低频存储，低频存储到期后自动转换为归档存储，归档存储到期后自动删除。

- 

单击保存。详细了解参考[智能存储分层](products/sls/documents/data-tiered-storage-overview.md)。

### API

[更新](products/sls/documents/developer-reference/api-sls-2020-12-30-updatelogstore.md)[LogStore](products/sls/documents/developer-reference/api-sls-2020-12-30-updatelogstore.md)中ttl、hot_ttl和infrequentAccessTTL的值，来动态调整存储分层的保留策略。

### 收集前端日志

日志服务提供webTracking功能，用以收集小程序/客户端（iOS/Android/APP）/浏览器上的日志数据。

该功能有两种使用方式：

- 

通过[使用](products/sls/documents/use-the-web-tracking-feature-to-collect-logs.md)[STS](products/sls/documents/use-the-web-tracking-feature-to-collect-logs.md)[鉴权方式](products/sls/documents/use-the-web-tracking-feature-to-collect-logs.md)进行传输，适用于生产场景。该方式无需修改LogStore配置。

- 

通过OpenAPI等进行[匿名传输](products/sls/documents/use-the-web-tracking-feature-to-collect-logs.md)数据，仅适用于测试场景。需要在LogStore中打开开关，参考下文进行配置。

### 控制台

在基础属性中，单击修改，打开WebTracking开关，然后单击保存。

### API

[更新](products/sls/documents/developer-reference/api-sls-2020-12-30-updatelogstore.md)[LogStore](products/sls/documents/developer-reference/api-sls-2020-12-30-updatelogstore.md)中enable_tracking参数为true来开启WebTracking功能。

### 为日志自动添加公网IP与到达日志服务时间

开启此功能后，后续采集会自动在日志中添加：

- 

__tag__:__client_ip__：日志来源设备的公网IP。

- 

__tag__:__receive_time__：日志到达日志服务服务端的时间，格式为Unix时间戳，表示从1970-1-1 00:00:00 UTC计算起的秒数。

### 控制台

在基础属性中，单击修改，打开记录外网IP开关，然后单击保存。

### API

[更新](products/sls/documents/developer-reference/api-sls-2020-12-30-updatelogstore.md)[LogStore](products/sls/documents/developer-reference/api-sls-2020-12-30-updatelogstore.md)中appendMeta参数来开启记录外网IP功能。

### 通过Shard调整采集性能

每个Shard支持5MB/s或500次/s的数据写入、10MB/s或100次/s的数据读取。此限制非硬性限制，超出限制时，系统会尽可能提供服务，但是不保证服务质量。当数据读写流量超出Shard读写能力时，需要及时分裂Shard以增加Shard个数，从而提供更高的读写能力。

### 控制台

在基础属性中，单击修改，打开自动分裂Shard，并设置分裂上限，然后单击保存。

日志服务支持针对某个Shard进行[分裂与合并](products/sls/documents/manage-shards.md)。

### API

[分裂](products/sls/documents/developer-reference/api-sls-2020-12-30-splitshard.md)[Shard](products/sls/documents/developer-reference/api-sls-2020-12-30-splitshard.md)。

[合并](products/sls/documents/developer-reference/api-sls-2020-12-30-mergeshard.md)[shard](products/sls/documents/developer-reference/api-sls-2020-12-30-mergeshard.md)。

## 停止计费/删除LogStore

警告

LogStore一旦删除，其存储的日志数据将会被永久删除，不可恢复，请谨慎操作。

### 控制台

- 

删除前清理。

- 

删除LogStore前需先删除其对应的所有Logtail配置。

- 

若该LogStore启用了日志投递，删除前请停止向该LogStore写入新数据，并确认LogStore中已有的数据已全部投递成功。

- 

删除LogStore前，在任务管理中查看当前Project的全部任务，并删除与当前LogStore关联的任务。

- 

删除步骤。

- 

在日志存储>日志库页签中，将鼠标悬浮在目标LogStore上，选择删除。

- 

在警告对话框中，单击确认删除。

- 

删除后事项。

- 

删除LogStore的当天仍会产生存储等费用，次日不再产生费用。即在删除LogStore的第三天不会再收到日志服务的账单。

- 

删除LogStore后，以当前LogStore为数据源的导出任务、数据加工任务、定时SQL任务和以当前LogStore为目标的导入任务都将被删除。

### API

[删除](products/sls/documents/developer-reference/api-sls-2020-12-30-deletelogstore.md)[LogStore](products/sls/documents/developer-reference/api-sls-2020-12-30-deletelogstore.md)

## 实际场景使用配置示例

### 大数据量业务实时监控分析场景

线上应用实时产生大量业务日志，出现故障，需要快速定位错误日志，并对应用性能指标（如QPS、响应延迟）进行实时监控和告警。

选型推荐：标准型LogStore+按写入量计费+Shard自动分裂。

原因：标准型LogStore支持分析，实时监控与可视化 ，大量日志写入且分析可能需要较多索引推荐按写入量计费，Shard自动分裂可以保障数据写入与分析的性能。

### 合规/审计/等保场景

根据行业法规，需要将用户操作日志、安全日志等保存储6个月以上用于审计，但日常查询和分析频率很低。

选型推荐：查询型LogStore+智能存储分层。

原因：查询型LogStore仅支持查询但索引流量费用低于标准型LogStore，智能存储分层对日志数据根据存储时长进行分类，降低长期存储成本。

## 相关参考

### 功能计费模式下LogStore对比

查询型仅支持功能计费，因此按使用功能计费模式下，标准型和查询型两种类型的LogStore对比如下：

| 对比项 | 标准型（Standard 规格 ） | 查询型（Query 规格 ） |  |
| --- | --- | --- | --- |
| 费用 | [索引流量](products/sls/documents/billable-items.md) | 0.350 元 /GB | 0.1 元 /GB |
| 功能 | [数据采集](products/sls/documents/data-collection-overview.md) （仅业务系统日志场景） | 支持 | 不支持采集云产品日志。 |
| [开启智能存储分层](products/sls/documents/enable-hot-and-cold-tiered-storage-for-a-logstore.md) | 支持 | 支持 |  |
| [查询](products/sls/documents/log-search-overview.md) | 支持 | 支持 |  |
| [分析](products/sls/documents/log-analysis-overview.md) （SQL 语句） | 支持 | 不支持 |  |
| [上下文查询](products/sls/documents/contextual-query.md) | 支持 | 支持 |  |
| [LiveTail](products/sls/documents/livetail.md) | 支持 | 支持 |  |
| [日志聚类](products/sls/documents/logreduce.md) | 支持 | 不支持 |  |
| [重建索引](products/sls/documents/reindex-logs-for-a-logstore.md) | 支持 | 支持 |  |
| [仪表盘](products/sls/documents/dashboard.md) | 支持 | 不支持 |  |
| [告警](products/sls/documents/user-guide/the-alerting-feature-of-log-service.md) | 支持 | 仅支持基于查询语句的告警 |  |
| [定时](products/sls/documents/how-scheduled-sql-works.md) [SQL](products/sls/documents/how-scheduled-sql-works.md) | 支持 | 不支持 |  |
| [数据加工](products/sls/documents/data-transformation-overview.md) | 支持 | 支持 |  |
| [数据投递](products/sls/documents/data-shipping-overview.md) | 支持 | 支持 |  |
| [普通消费](products/sls/documents/overview-of-real-time-consumption.md) | 支持 | 支持 |  |


### 使用限制

按写入数据量计费模式支持完整日志服务功能集合，增值功能如查询分析、数据加工、智能告警、消费投递等能力均不产生额外费用，但存在配额限制，具体说明如下。

| 配额限制 | 说明 |
| --- | --- |
| 数据加工量 | 单个 LogStore 每月支持的最大加工数据量为 100 TB。 |
| 定时 SQL 数据量 | 单个 LogStore 每月支持的定时 SQL 数据量为 20 TB。 |
| 投递数据量 | 单个 LogStore 每月支持的投递数据量为 100 TB。 |
| 消费数据量 | 单个 LogStore 每月支持的消费数据量为 100 TB。 |
| 告警作业计算数据量 | 单个 LogStore 每月支持的告警作业计算数据量为 100 TB。 |


## 计费说明

LogStore的费用主要由所选的计费模式决定。

- 

按使用功能计费：根据实际使用的资源量（如存储容量、索引流量、读写次数、Shard数量等）独立计费。

- 

按写入数据量计费：仅对写入的原始数据量收费，并包含30天免费存储及多项免费功能。

关键计费项价格：

- 

标准型（Standard）索引流量：0.350元/GB。

- 

查询型（Query）索引流量：0.1元/GB。

成本优化建议：

- 

如果日志存储周期接近或超过30天，按写入数据量计费模式通常更具成本优势。

- 

对于仅需归档和检索的场景，使用查询型（Query）规格可降低索引费用。

- 

通过配置智能存储分层，将不常访问的数据转移到低成本存储层。

## 常见问题

### 无法创建LogStore

一个Project默认最多创建200个LogStore。请删除无用LogStore或参考下文进行配额申请。

- 

登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表区域，单击目标Project。

- 

在Project页面的项目概览-基础信息-资源配额中单击管理，即可在资源配额面板中，调整目标资源的LogStore上限配额，然后单击保存提交申请。修改申请需要等待1小时左右完成。

### 日志服务SLS的日志丢失？

- 

Project、LogStore丢失

如果主动删除LogStore、Project，日志无法恢复。您可以通过[操作审计](https://help.aliyun.com/zh/actiontrail/user-guide/query-events-in-the-actiontrail-console)功能查询最近90天的删除Project/LogStore事件。

- 

没有采集到日志，参考[LoongCollector](products/sls/documents/loongcollector-collection-exception-troubleshooting.md)[采集异常问题汇总排查](products/sls/documents/loongcollector-collection-exception-troubleshooting.md)。

- 

日志服务欠费：超过7天，将视为主动放弃服务，日志服务Project将被回收，数据会被清理且不可恢复。更多信息，请参见[欠费说明](products/sls/documents/overdue-payments.md)。

### 如何优化日志的存储成本？

- 

查询日志服务的费用，请参见[如何查看日志服务的存储容量和消费记录](products/sls/documents/how-to-view-the-storage-capacity-and-consumption-records-of-log-service.md)。

- 

将历史日志[下载到本地](products/sls/documents/download-logs.md)，或者[投递到](products/sls/documents/create-oss-shipping-tasks-new-version.md)[OSS](products/sls/documents/create-oss-shipping-tasks-new-version.md)[进行存储](products/sls/documents/create-oss-shipping-tasks-new-version.md)。

[上一篇：管理Store](products/sls/documents/manage-sls-store.md)[下一篇：管理MetricStore](products/sls/documents/manage-a-metricstore.md)

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
