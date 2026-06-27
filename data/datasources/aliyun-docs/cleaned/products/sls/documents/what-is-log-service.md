# 一站式可观测数据采集处理存储分析-日志服务-阿里云-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/what-is-log-service

# 什么是日志服务
日志服务SLS作为云原生数据应用平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。借助一站式数据采集、处理加工、存储、查询与分析、监控、输出与集成等功能，提升开发、运维、运营、安全等场景数字化能力。
## 典型应用场景
| 日志管理 提供客户端、服务端、云产品等完整渠道的数据采集能力。 支持冷热分层存储，适应不同生命周期数据的需求。 每天支持 PB 级查询和分析处理，快速响应业务需求。 | 统一的数据管道/数据湖 支持数十种采集方式，实现海量数据统一实时采集。 用于加工清洗、实时消费与分发，适配业务分析、大数据分析等。 每天支持 PB 级查询和分析处理，快速响应业务需求。 | 日志安全与合规审计 构建多账号、多地域统一采集的日志安全审计方案。 自动采集新实例日志，中心化存储以支持审计所需功能。 内置审计规则并可对接第三方 SIEM 系统。 | 全链路可观测运维 支持 Log/Metric/Trace 等可观测数据的统一存储与联合分析。 集成智能巡检、智能预测及根因分析等 AIOps 工具，实现异常检测和自动告警，提升系统稳定性和用户体验。 | 业务分析监控 打通系统数据与业务数据，提供实时洞察。 支持预防系统风险、调整业务策略，相比 BI 系统的 T+1 展示，实现实时或分钟级延迟的数据分析。 |
| --- | --- | --- | --- | --- |
## 为什么选择日志服务
SLS 不仅是一个日志系统，更是企业级统一数据中台与智能运维平台的核心组件。相比自建方案（如 ELK），SLS 具备以下核心优势：
统一接入：支持Log、Metric、Trace多类型数据，覆盖客户端、服务端、IoT、移动端、云产品、开源系统、多云及本地服务器。
高效处理：提供采集时、写入时、写入后多阶段实时数据加工能力，内置丰富函数与流式处理引擎。
统一存储：打破数据孤岛，支持热/冷分层存储，生命周期自动管理。
智能分析：秒级查询百亿级数据，内置近百种分析函数，支持本地Agent[Skill 智能查询分析日志](sls-query-skill-intelligent-log-query-and-analysis.md)，支持AI 助手自动生成查询语句（Copilot）。
全链路可观测：统一存储与联合分析 Log/Metric/Trace，集成 AIOps 智能异常检测、根因分析。
成本可控：按量付费，TCO 降低 50% 以上，每天支持PB级弹性伸缩应对流量洪峰。
开箱即用：内置CloudLens（可观测性）、FinOps（成本分析）等企业级应用，支持开放生态，兼容多种开源引擎。
## 核心功能
### [数据采集](data-collection-overview.md)
多源接入：支持客户端日志（Web、App、IoT），服务器与应用日志，阿里云产品日志（RDS、SLB、OSS等），标准协议（Syslog、SNMP、HTTP等），开源系统日志（Nginx、MySQL、Kafka等）。打通跨账号、跨云、云上云下等场景数据。
多种采集方式：支持自研采集器LoongCollector（Logtail 升级版）、WebTracking前端采集、SDK&API 等。
高可靠性保障：断点续传、弹性伸缩、多路径传输（公网、内网、全球加速），自动发现新实例并采集日志。
### [数据处理](comparison-of-processing-plug-ins-write-processors-data-processing-and-consumer-processors.md)
SLS 提供全链路数据处理加工能力，支持在采集时、写入时、写入后进行实时处理。可进行数据规整、清洗过滤、格式化、脱敏、加密、流转、富化。内置文本处理、JSON解析、正则提取、字段映射、数据转换等多种函数，具备流式大吞吐能力，延迟低。支持SPL加工语句。
### [数据存储](data-tiered-storage-overview.md)
日志服务提供智能的数据存储方案，保障功能正常使用的前提下优化存储成本，通过冗余保障数据持久性和可用性。
统一存储平台：打破数据孤岛，支持Log/Metric/Trace 统一存储。
智能生命周期管理：对于热数据：支持高频访问，毫秒级响应；对于冷数据：提供低频访问，自动转为低频/归档存储，降低存储成本。
高可用与持久性：多副本冗余存储，保障数据不丢失。存储类型可选：标准型、查询型。
### [查询与分析](quick-guide-to-query-and-analysis.md)
高性能查询引擎：支持[索引模式](query-and-analyze-logs-in-index-mode.md)（秒级响应百亿数据）、[扫描模式](query-and-analyze-logs-in-scan-mode.md)（轻量级分析）。内置近百种[查询](query-syntax.md)与[分析](sql-syntax-and-functions.md)函数（统计、聚合、字符串、时间等），支持跨日志库联合查询（StoreView），SQL 独享版（高精度分析）。
智能生成：支持[通过](copilot-automatic-generation-of-ai-assisted-sql-statements.md)[AI](copilot-automatic-generation-of-ai-assisted-sql-statements.md)[智能生成查询与分析语句（Copilot）](copilot-automatic-generation-of-ai-assisted-sql-statements.md)。
智能运维能力：集成 AIOps，提供异常检测、根因分析、智能巡检能力。支持[定时](scheduled-sql.md)[SQL](scheduled-sql.md)[查询](scheduled-sql.md)，用于报表生成。
兼容多种产品：支持关联外部数据源查询，将MySQL、PostgreSQL、OSS、CSV等数据作为外部存储，并进行查询分析。支持第三方工具查询与分析，可对接Elasticsearch、Azure等第三方工具。
### 数据监控（[可视化](overview-of-visualization.md)与[告警](sls-alerting.md)）
可视化：提供[仪表盘](dashboard.md)功能，内置10+[图表类型](statistical-charts.md)（表格、线图、柱状图、地图等）。且支持自定义仪表盘、控制台嵌入、下钻分析，可对接Grafana，QuickBI等第三方系统。
智能告警：提供一站式告警能力，包括告警监控，告警管理，通知（行动）管理等。支持多源、多账号、多条件统一告警。自动智能降噪，消除“告警风暴”。支持电话、短信、钉钉、微信、飞书、webhook等多渠道通知。
### [数据输出与集成](sls-log-output-and-integration.md)
日志服务支持将[日志下载到本地](download-logs.md)，或将日志投递到其他云产品。也可以借助日志服务平台对日志进行实时消费。
[数据消费](data-consumption-and-subscription.md)：支持Spark Streaming、Flume、Flink等实时消费。
[数据投递](data-shipping-overview.md)：实时投递至OSS、MaxCompute、TSDB等云产品。
## 开始使用
为了帮助您快速、高效地使用日志服务，建议遵循以下三个核心阶段。每个阶段都包含基础步骤（建议所有用户完成）和可选/进阶操作（供需要更深入使用的用户参考）。
|  | 使用前准备 | 数据接入 | 数据应用 |
| --- | --- | --- | --- |
| 核心目标 | 了解核心概念，完成基础设置，为数据接入做好准备。 | 将日志、指标、链路等各类数据安全、高效地传输到日志服务中。 | 发掘数据价值，通过查询分析、监控告警和数据洞察来驱动业务。 |
| 基础步骤 | 开通 [日志服务](https://sls.console.aliyun.com/) 。 了解核心资源： [Project（项目）](manage-a-project.md) 与 [Store（存储库）](manage-sls-store.md) 。 创建一个 Project。 | 熟悉 [数据采集方式](data-collection-overview.md) ，了解可采集范围。 创建 Store（根据数据模型选择）： [LogStore](manage-a-logstore.md) ， [MetricStore（指标）](manage-a-metricstore.md) ， [EventStore（事件）](manage-an-eventstore.md) 。 选择采集方式接入数据： [日志采集(Log)](sls-log-collection.md) ， [指标采集(Metric)](data-collection.md) ， [链路采集(Trace)](trace-app.md) ， [事件采集(Event)](acquisition-events-sls.md) 。 | 查询分析 [索引模式](query-and-analyze-logs-in-index-mode.md) ：毫秒级快速查询与分析。 [扫描模式](query-and-analyze-logs-in-scan-mode.md) ：对原始数据进行全面扫描分析。 [AI](copilot-automatic-generation-of-ai-assisted-sql-statements.md) [辅助](copilot-automatic-generation-of-ai-assisted-sql-statements.md) ：使用 Copilot 智能生成查询与分析语句。 监控与可视化 [仪表盘](dashboard.md) ：使用仪表盘将数据可视化。 [告警](alarm-settings-quick-start.md) ：设置数据告警规则与策略。 |
| 可选/进阶步骤 | 通过 [快速入门：采集](getting-started.md) [ECS](getting-started.md) [文本日志](getting-started.md) 体验日志服务。 资源规划：预先规划 [资源层级与生命周期](resource-management-overview.md) ，了解 [基础资源限制](basic-resources.md) 以及 [资源流控策略](expansion-of-resources.md) 。 权限管理：通过配置 [RAM](log-service-ram-access-control-permissions-configuration.md) [权限](log-service-ram-access-control-permissions-configuration.md) 进行访问控制或通过 [限制访问](use-project-policies-to-manage-access-permissions-on-log-service-resources.md) [IP](use-project-policies-to-manage-access-permissions-on-log-service-resources.md) [控制访问权限](use-project-policies-to-manage-access-permissions-on-log-service-resources.md) 。 | 了解数据存储方式，通过 [智能存储分层](data-tiered-storage-overview.md) 配置存储策略。 日志服务在 采集时、写入时、写入后 等多阶段提供了不同的数据处理器，可根据 [不同数据处理器的差异说明](comparison-of-processing-plug-ins-write-processors-data-processing-and-consumer-processors.md) 进行选择，配置数据处理加工规则（脱敏、过滤、富化）。 | 查询分析 [Storeview](cross-domain-query-and-analysis-dataset-storeview.md) ：支持跨 Project，跨存储库数据关联查询。 [定时](scheduled-sql.md) [SQL](scheduled-sql.md) [查询](scheduled-sql.md) ：设置定时 SQL 执行，帮助报表生成。 [SQL](dedicated-sql.md) [独享版](dedicated-sql.md) ：大数据量时进行高精度分析。 [关联外部数据源](associate-external-data-sources.md) ：连接外部数据作为外部存储，进行查询分析。 监控与可视化 [添加过滤器](add-a-filter-of-the-filter-type.md) ：通过增加过滤条件修改仪表盘展示数据。 [告警中心大盘](alert-center-dashboards.md) ：告警信息会记录到默认名为 internal-alert-center-log 的 LogStore 中，可进行 [自定义分析告警日志](use-custom-query-statements-to-analyze-alert-logs.md) 。 [对接函数计算实现告警自动处理](synchronize-log-service-alert-events-to-function-compute.md) ：支持通过对接函数计算接收告警通知并自动处理告警事件。 输出与集成 [下载日志](download-logs.md) 或 [向外部进行数据投递](data-shipping-limits.md) 。 [数据实时消费](data-consumption-and-subscription.md) 。 |
## 如何计费
计费方式
[按量付费](pay-by-volume.md)：适用于业务用量经常变化的场景。
[资源包](resource-plan.md)：适用于业务用量相对稳定的场景。
计费模式与计费项
[按使用功能计费模式计费项](billable-items.md)：精细化计费。使用的每一项功能独立收费，适合功能使用明确、可精细化控制成本的场景。
[按写入数据量计费模式计费项](billing-items-in-the-pay-per-data-write-mode.md)：简化计费。核心费用是按写入的原始数据量计费，适合查询分析频繁、希望成本模型简单的场景。
## 常见问题
### 阿里云会使用我在日志服务上存储的数据吗？
就用户业务数据，阿里云除执行您的服务要求或者法律法规要求外，不进行任何未获授权的使用及披露。更多信息，请参见[服务条款](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud202003060931_27750.html?spm=a2c4g.11186623.2.2.7c3b4ac4VDjqN8)。
### 阿里云内部是否会使用日志服务存储数据？
是的。日志服务是阿里巴巴内部自用的日志及监控平台，经历多次双十一的考验。阿里云内部的开发人员也在很多项目中使用日志服务。
### 如果数据量突然激增，日志服务如何保证服务不受影响？
日志服务提供弹性伸缩、灵活适配的数据基础框架，具备每天PB级别的弹性伸缩能力。无论是流量高峰还是业务增长都能轻松应对。
### 如何合理规划日志服务的使用成本
日志服务的使用成本主要可以分为读写，存储两部分。可以针对这两部分进行使用成本的规划。
读写：从Shard分区数量，单次读写流量大小，索引使用等方面进行规划。
存储：从存储周期与存储类型等方面进行规划。
具体请参考[费用优化](cost-optimization.md)。
### 如何关闭日志服务/停止计费
若需终止日志服务的计费，需从数据采集和资源存储两方面操作：
关闭日志采集：停止采集后，采集器将不再传输新日志。
清理存储资源：删除日志服务中对应的Project 和 LogStore，确保删除所有关联资源，避免因存储空间占用产生费用。
具体请参考[停止计费](stop-billing.md)。
### 日志服务中的数据可以保存多久？
您可以设置数据永久保存或者仅保存到规定的时间，超过规定保存时间的数据将会自动删除。您也可以开启[智能存储分层](data-tiered-storage-overview.md)，将超过特定时间的数据转存为低频或归档数据，以降低数据存储费用。
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
