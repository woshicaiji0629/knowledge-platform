# 管理日志项目Store-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/manage-sls-store

# 管理Store
Store是日志服务中数据存储和查询的单元。针对不同的数据类型，日志服务分别提供了日志库（LogStore）、时序库（MetricStore）和事件库（EventStore）。
## 如何选择Store类型
日志服务提供日志库（LogStore），指标库（Metricstore），事件库（Eventstore）三种类型的Store，不同类型的Store主要区别在于对数据类型的兼容性上。请根据数据类型选择对应Store，如无特殊需要可默认使用LogStore。
| Store 类型 | 适用场景 |
| --- | --- |
| 日志库（LogStore） | [日志数据（Log）](manage-sls-store.md) ：系统运行过程中变化的一种抽象数据，其内容为指定对象的操作和其操作结果按时间的有序集合。广义上来说包含了几乎所有类型的数据，默认情况下可使用 LogStore。 [链路数据（Trace）](manage-sls-store.md) ：用于记录单次请求范围内的处理信息，其中包括服务调用和处理时长等数据。 |
| 时序库（MetricStore） | [时序数据（Metric）](manage-sls-store.md) ：由时序标识和数据点组成，相同时序标识的数据组成时间线。当数据需要时序存储时使用 MetricStore。 |
| 事件库（EventStore） | [事件数据（Event）](manage-sls-store.md) ：事件（Event）是指值得关注的、有价值的数据。例如监控告警数据、定期巡检作业的结果等。当数据需要事件存储时使用 EventStore。 |
### 日志库（LogStore）
LogStore是日志服务中日志数据存储和查询的单元。每个LogStore隶属于一个Project，每个Project中可创建多个LogStore。可以根据实际需求在目标Project中创建多个LogStore，一般是为同一个应用中不同类型的日志创建独立的LogStore。例如采集App A所涉及的操作日志（operation_log）、应用程序日志（application_log）以及访问日志（access_log），可以创建一个名为app-a的Project，并在该Project下创建名为operation_log、application_log和access_log的LogStore，用于分别存储操作日志、应用程序日志和访问日志。
在执行写入日志、查询和分析日志、加工日志、消费日志、投递日志等操作时，都需要指定LogStore。具体说明如下：
以LogStore为采集单元采集日志。
以LogStore为存储单元存储日志以及执行加工、消费、投递等操作。
在LogStore中建立索引用于查询和分析日志。
### 时序库（MetricStore）
[时序库（MetricStore）](manage-a-metricstore.md)是日志服务中时序数据存储和查询的单元。每个MetricStore隶属于一个Project，每个Project中可创建多个MetricStore。可以根据实际需求为某个项目创建多个MetricStore，一般是为不同类型的时序数据创建不同的MetricStore。例如需要采集基础主机监控数据、云服务监控数据、业务应用监控数据，可以创建一个名为demo-monitor的Project，然后在该Project下创建名为host-metrics、cloud-service-metrics和app-metrics的MetricStore，用于分类存储基础主机监控数据、云服务监控数据和业务应用监控数据。
在执行写入、查询和分析、消费时序数据时，都需要指定MetricStore。具体说明如下：
以MetricStore为采集单元采集时序数据。
以MetricStore为存储单元存储时序数据以及执行消费操作。
[查询和分析时序数据](time-metric-data-query-and-analysis-syntax.md)支持PromQL语法、SQL92语法和SQL+PromQL语法。
### 事件库（EventStore）
[事件库（EventStore）](manage-an-eventstore.md)是日志服务中事件数据存储和查询的单元。每个EventStore隶属于一个Project，每个Project中可创建多个EventStore。根据实际需求为某个项目创建多个EventStore，一般是为不同类型的事件数据创建不同的EventStore。例如可以根据基础设施异常事件、业务应用事件、自定义事件等进行分类，通过不同的EventStore来进行存储和分析。
在执行写入、查询和分析、消费事件数据时，都需要指定EventStore。具体说明如下：
以EventStore为采集单元采集事件数据。
以EventStore为存储单元存储事件数据以及执行消费操作。
## 相关参考
### 日志组（LogGroup）
日志组（LogGroup）是一组日志的集合，是写入与读取日志的基本单元。一个日志组中的数据包含相同Meta（IP地址、Source等信息）。写入日志到日志服务或从日志服务读取日志时，多条日志被打包为一个日志组，以日志组为单元进行写入与读取。该方式可减少读写次数，提高业务效率。每个日志组最大长度为5 MB。
日志服务的基本数据模型请参见[LogStore](use-a-consumer-group-to-consume-logs-in-high-reliability-mode.md)[数据模型](use-a-consumer-group-to-consume-logs-in-high-reliability-mode.md)。
### 日志数据（Log）
日志数据是系统运行过程中变化的一种抽象数据，其内容为指定对象的操作和其操作结果按时间的有序集合。文本日志（LogFile）、事件（Event）、数据库日志（BinLog）、时序数据（Metric）等数据都是日志的不同载体。日志服务采用半结构化的数据模式定义一条日志，包含日志主题、日志时间、日志内容、日志来源和日志标签五个数据域。日志服务对各个数据域的格式要求不同，详细说明如下表所示。
| 数据域 | 说明 | 格式 |
| --- | --- | --- |
| 日志主题（Topic） | 日志服务保留字段（ __topic__ ）用于标识日志主题，可区分不同服务、用户或实例产生的日志。例如，系统 A 包含前端 HTTP 请求处理、缓存、逻辑处理、存储等模块时，可分别为其日志设置 Topic（如 http_module、cache_module、logic_module、store_module）。日志采集至同一 LogStore 后，可通过 Topic 快速区分来源。日志主题（Topic）需在 [采集配置](manage-logtail-configurations-for-log-collection.md) 的 全局配置 中设置。 LogStore、Topic、 [Shard](manage-shards.md) 之间的关系如下： | 包括空字符串在内的任意字符串，大小为 0~128 字节。 若不需要区分 LogStore 中的日志，则在采集日志时设置为空字符串即可。空字符串是一个有效的 Topic，即 Topic 的值为空字符串。 |
| 日志时间 | 日志服务保留字段（ __time__ ）用于标识日志时间。更多信息，请参见 [保留字段](reserved-fields.md) 。 | Unix 时间戳。 |
| 日志内容 | 日志的具体内容，由一个或多个内容项组成，内容项为 Key:Value 格式。 您通过 Logtail 极简模式（单行或多行）采集日志时，Logtail 不会对日志内容进行解析。整条原始日志将被上传到 content 字段中。 | Key:Value 的详细说明如下： Key 为字段名称，需为 UTF-8 编码字符串（字母、下划线和数字但不以数字开头）。字符串大小为 1~128 字节。不可使用如下字段。 __time__ __source__ __topic__ __partition_time__ _extract_others_ __extract_others__ Value 为字段值，可以为任意字符串，大小不超过 1 MB。 |
| 日志来源 | 日志服务保留字段（ __source__ ）用于标识日志来源，例如产生日志的服务器 IP 地址。 | 任意字符串，大小为 0~128 字节。 |
| 日志标签 | 日志标签。包括： 自定义标签：通过 [PutLogs](putlogs.md) 接口，在写入日志时添加标签。 系统标签：日志服务为日志添加的标签，包括 __client_ip__ 和 __receive_time__ 。 | 字典格式，Key 和 Value 均为字符串类型。在日志中以 __tag__: 为前缀进行展示。 |
示例
以下以一条网站访问日志为例，说明原始日志与日志服务中数据模型的映射关系。
原始日志
127.0.0.1 - - [01/Mar/2021:12:36:49 0800] "GET /index.html HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36
通过极简模式采集到日志服务后的日志，整条原始日志被保存在content字段中。
通过正则模式采集到日志服务后的日志，日志内容被结构化，即根据设置的正则表达式将日志内容提取为多个键值对。
### 时序数据（Metric）
时序数据由时序标识和数据点组成，相同时序标识的数据组成时间线。日志服务的时序数据类型遵循Prometheus的[定义规范](https://prometheus.io/docs/concepts/data_model/)，在时序库中所有的数据都按照时序类型存储。
时序标识
每条时间线都有一个唯一的时序标识，由Metric name和Labels组成。
Metric name是一个字符串类型的标识符，用于标识指标类型。Metric name需遵循正则表达式[a-zA-Z_:][a-zA-Z0-9_:]*。例如http_request_total表示接收到的HTTP请求的总数。
Labels由一组组键值对组成，各组键值对之间使用竖线（|）分割，用于标识指标的相关属性。Key需遵循正则表达式[a-zA-Z_][a-zA-Z0-9_]*，Value则不能包含竖线（ | ）。例如method为POST，URL为/api/v1/get。
数据点
数据点代表时间线在具体某个时间点的值，每个数据点由时间戳和值组成。其中时间戳精度为纳秒，值的类型为double。
数据结构
时序数据的写入协议和日志写入协议一致，使用Protobuf的[数据编码方式](developer-reference/data-encoding.md)。时序标识和数据点都在content字段中，具体表示方式如下所示。
| 字段 | 说明 | 示例 |
| --- | --- | --- |
| __name__ | Metric 名称。 | nginx_ingress_controller_response_size |
| __labels__ | Label 信息，格式为 {key}#$#{value}|{key}#$#{value}|{key}#$#{value} 。 说明 Label 的 Key 需按照字母顺序进行排序。 建议不要写入 Value 为空字符串的 Label。例如 Label 信息为 app#$#|controller_class#$#nginx ，则不建议将 Key 为 app 的 Label 写入时序库，可能造成 PromQL 聚合计算报错。 | app#$#ingress-nginx|controller_class#$#nginx|controller_namespace#$#kube-system|controller_pod#$#nginx-ingress-controller-589877c6b7-hw9cj |
| __time_nano__ | 时间戳。支持以秒（s）、毫秒（ms）、微秒（us）、纳秒（ns）等多种精度的时间戳写入。SQL 查询时，所有时间戳统一化为微秒（us）精度输出，确保时间计算的一致性。 | 1585727297293000 |
| __value__ | 值。 | 36.0 |
说明
除上表提到的字段之外，其他自定义字段（例如 Topic、Source、LogTags 等）在通过 SDK 写入时将不被存储到时序库中，详情可参考[通过](use-an-sdk-to-collect-metrics.md)[SDK](use-an-sdk-to-collect-metrics.md)[写入时序数据](use-an-sdk-to-collect-metrics.md)的说明部分。
示例
查询process_resident_memory_bytes指标在指定时间区间内的所有原始时序数据。
* | select * from "sls-mall-k8s-metrics.prom" where __name__ = 'process_resident_memory_bytes' limit all
### 事件数据（Event）
事件（Event）是指值得关注的、有价值的数据。例如监控告警数据、定期巡检作业的结果等。日志服务的事件数据遵循[CloudEvents](https://cloudevents.io/)协议规范，具体说明如下表所示。
| 字段类型 | 字段名 | 是否必选 | 数据格式 | 说明 |
| --- | --- | --- | --- | --- |
| 协议字段 | specversion | 是 | String | 根据 CloudEvents 协议规范，默认使用 1.0 。 |
| id | 是 | String | 事件 ID，您可以根据 source+id 来区分事件的唯一性。 |  |
| source | 是 | String | 通常用来标识事件发生的上下文信息，例如事件来源、发布事件的实例等。 |  |
| type | 是 | String | 事件类型，例如 sls.alert 。 |  |
| subject | 否 | String | 事件主题，是对 source 字段的补充，例如用于描述实际触发事件的对象。 |  |
| datacontenttype | 否 | String | 事件类型，默认取值为 application/cloudevents+json 。 |  |
| dataschema | 否 | URI | data 字段需要遵循的 Schema，默认为空。 |  |
| data | 否 | JSON | 具体的事件内容。不同来源和类型的事件格式会有差异。 |  |
| time | 是 | Timestamp | 事件时间，具体格式，请参见 [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) 。例如 2022-10-17T11:20:45.984+0800 。 |  |
| 扩展字段 | title | 是 | String | 事件标题。 |
| message | 是 | String | 事件描述。 |  |
| status | 是 | String | 事件状态。取值： ok info warning error |  |
示例
例如一个告警事件，示例数据如下：
{ "specversion": "1.0", "id": "af****6c", "source": "acs:sls", "type": "sls.alert", "subject": "https://sls.console.aliyun.com/lognext/project/demo-alert-chengdu/logsearch/nginx-access-log?encode=base64&endTime=1684312259&queryString=c3RhdHVzID49IDQwMCB8IHNlbGVjdCByZXF1ZXN0X21ldGhvZCwgY291bnQoKikgYXMgY250IGdyb3VwIGJ5IHJlcXVlc3RfbWV0aG9kIA%3D%3D&queryTimeType=99&startTime=1684311959", "datacontenttype": "application/cloudevents+json", "data": { "aliuid": "16****50", "region": "cn-chengdu", "project": "demo-alert-chengdu", "alert_id": "alert-16****96-247190", "alert_name": "Nginx访问错误", "alert_instance_id": "77****e4-1aad9f7", "alert_type": "sls_alert", "next_eval_interval": 300, "fire_time": 1684299959, "alert_time": 1684312259, "resolve_time": 0, "status": "firing", "severity": 10, "labels": { "request_method": "GET" }, "annotations": { "__count__": "1", "cnt": "49", "desc": "Nginx最近五分钟内GET请求错误49次", "title": "Nginx访问错误告警触发" }, "results": [ { "region": "cn-chengdu", "project": "demo-alert-chengdu", "store": "nginx-access-log", "store_type": "log", "role_arn": "", "query": "status >= 400 | select request_method, count(*) as cnt group by request_method ", "start_time": 1684311959, "end_time": 1684312259, "fire_result": { "cnt": "49", "request_method": "GET" }, "raw_results": [ { "cnt": "49", "request_method": "GET" }, { "cnt": "3", "request_method": "DELETE" }, { "cnt": "7", "request_method": "POST" }, { "cnt": "6", "request_method": "PUT" } ], "raw_result_count": 4, "truncated": false, "dashboard_id": "", "chart_title": "", "is_complete": true, "power_sql_mode": "auto" } ], "fire_results": [ { "cnt": "49", "request_method": "GET" } ], "fire_results_count": 1, "condition": "Count:[1] > 0; Condition:[49] > 20", "raw_condition": "Count:__count__ > 0; Condition:cnt > 20" }, "time": "2023-05-17T08:30:59Z", "title": "Nginx访问错误告警触发", "message": "Nginx最近五分钟内GET请求错误49次", "status": "error" }
### 链路数据（Trace）
链路数据（Trace）用于记录单次请求范围内的处理信息，其中包括服务调用和处理时长等数据。一条链路数据对应一条调用链，格式参考[Trace](trace-data-formats.md)[数据格式](trace-data-formats.md)。在广义上，一个调用链代表一个事务或者流程在（分布式）系统中的执行过程。在OpenTracing标准中，调用链是多个Span组成的一个有向无环图（Directed Acyclic Graph，简称DAG），每一个Span代表调用链中被命名并计时的连续性执行片段。
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
