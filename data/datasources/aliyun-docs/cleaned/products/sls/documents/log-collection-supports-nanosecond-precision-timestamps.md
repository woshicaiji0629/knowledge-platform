# Logtail配置纳秒精度时间戳-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/log-collection-supports-nanosecond-precision-timestamps

# 日志采集支持纳秒精度时间戳
通过在 Logtail 采集配置中开启纳秒精度支持并配置时间解析插件，可以采集和存储毫秒、微秒、纳秒级的高精度时间戳。采集后的时间将拆分为秒级时间戳__time__和纳秒偏移量__time_ns_part__两个字段进行存储，以实现高精度的日志排序与分析。
## 业务场景说明
在分布式追踪、高频交易、性能剖析或对日志严格保序等场景中，秒级的时间精度无法满足业务需求。这些场景的业务日志中通常会记录毫秒、微秒甚至纳秒级的时间戳。本方案旨在指导如何配置 Logtail，以完整地采集、存储和分析这些高精度时间信息，确保日志分析的准确性和时序性。
## 方案架构
LoongCollector（Logtail）采集纳秒精度时间戳的核心机制是在标准秒级时间戳之外，额外存储一个纳秒级的偏移量。此设计旨在兼容现有以秒为单位的时间系统，同时提供高精度排序能力。
核心工作流程如下：
开启纳秒支持：在 Logtail 采集配置的高级参数中，通过{ "EnableTimestampNanosecond": true }激活高精度时间处理能力。此功能仅适用于 Logtail 1.8.0 及以上版本的 Linux 环境。
日志解析：使用分隔符、JSON 或正则表达式等插件从原始日志中提取包含高精度时间戳的字符串。
时间转换：时间解析插件将时间字符串转换为标准时间格式。
时间存储：日志服务将时间拆分为两个字段进行存储：
__time__：标准的 Unix 时间戳（长整型），单位为秒。
__time_ns_part__：纳秒部分（长整型），取值范围为 0 到 999,999,999。
查询与分析：在查询分析时，通过对__time__和__time_ns_part__两个字段组合排序，可以实现严格的日志时序分析。
## 实施步骤
本节将以一个包含纳秒级时间戳的JSON 日志为例，提供一个从日志采集、解析、索引配置到最终查询分析的完整端到端操作流程。
### 步骤一：创建Project和LogStore
采集日志前，需规划并创建用于管理与存储日志的Project和LogStore。
Project：日志服务的资源管理单元，用于隔离和管理不同项目或业务的日志。
LogStore：日志存储单元，用于存储日志。
如果已提前创建，可跳过本步骤，直接进入[配置机器组（安装](log-collection-supports-nanosecond-precision-timestamps.md)[LoongCollector）](log-collection-supports-nanosecond-precision-timestamps.md)。
登录[日志服务控制台](https://sls.console.aliyun.com)。
单击创建Project，并配置：
所属地域：根据日志来源选择，创建后不可修改。
Project名称：阿里云内全局唯一，创建后不可修改。
其他配置保持默认，单击创建。如需了解其他参数，请参见[管理](manage-a-project.md)[Project](manage-a-project.md)。
单击Project名称，进入目标Project。
在左侧导航栏，选择日志存储，单击+。
在创建LogStore页面，完成以下核心配置：
Logstore名称：设置一个在Project内唯一的名称，创建后不可修改。
Logstore类型：根据规格对比选择标准型或查询型。
计费模式：
按使用功能计费：按存储、索引、读写次数等各项资源独立计，适合小规模或功能使用不确定的场景。
按写入数据量计费：仅按原始写入数据量计费，并提供30天的免费存储周期及免费的数据加工、投递等功能。成本模型简单，适合存储周期接近30天或数据处理链路复杂的场景。
数据保存时间：设置日志的保留天数，取值范围为1~3650天（3650天表示永久保存）。默认为30天。
其他配置保持默认，单击确定。如需了解其他参数，请参考[管理](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
### 步骤二： 配置机器组（安装LoongCollector）
在成功[创建](log-collection-supports-nanosecond-precision-timestamps.md)[Project](log-collection-supports-nanosecond-precision-timestamps.md)[和](log-collection-supports-nanosecond-precision-timestamps.md)[LogStore](log-collection-supports-nanosecond-precision-timestamps.md)后，为服务器安装LoongCollector并将其加入机器组。本文以ECS实例安装LoongCollector（ECS与日志服务Project属于同一阿里云账号和地域）为例，若ECS实例与Project不属于同一账号或地域，或为自建服务器请参考[安装采集器](loongcollector-installation-linux.md)手动安装。
此功能仅支持 Linux 系统的LoongCollector（ Logtail），在 Windows 系统上配置不生效，Logtail版本为1.8.0及以上。
| 单击目标 Project，在日志库（LogStore） 页面： 单击目标 LogStore 名称前的 展开， 单击 数据接入 后的 ， 在弹框中选择文本日志接入模板，本文以 单行-文本日志 模板为例，单击 立即接入 。 所有文本日志接入模板仅在解析插件上有所差异，其余配置流程一致，后续均可修改。 |
| --- |
配置步骤：
在机器组配置页面，配置如下参数：
使用场景：主机场景
安装环境：ECS
配置机器组：根据目标服务器的LoongCollector安装情况与机器组配置状态，选择对应操作：
已安装LoongCollector且已加入某个机器组，可直接在源机器组列表中勾选，将其添加至应用机器组列表，无需重复创建。
未安装LoongCollector，单击创建机器组：
以下步骤将引导您完成LoongCollector的自动安装并创建新机器组。
系统会自动列出与 Project 同地域的 ECS 实例，勾选需要采集日志的一台或多台实例。
单击安装并创建为机器组，系统将自动在所选ECS实例上安装LoongCollector。
配置机器组名称并单击确定。
说明
如果安装失败或一直处于等待中，请检查ECS地域是否与Project相同。
如需将已安装LoongCollector的服务器加入已有机器组，请参考常见问题[如何将服务器加入到已有机器组？](host-text-log-collection-auto-install.md)
### 步骤三：创建采集配置
通过控制台配置
完成[LoongCollector](log-collection-supports-nanosecond-precision-timestamps.md)[安装和机器组配置](log-collection-supports-nanosecond-precision-timestamps.md)后，进入Logtail配置页面，开始定义日志采集和处理规则。
1. 开启纳秒精度支持
定义日志的采集源、采集规则，并开启纳秒精度支持。
全局配置：
配置名称：设置一个在Project内唯一的名称。创建成功后，无法修改。
其他全局配置：开启高级参数开关，并输入以下 JSON 内容以开启纳秒精度支持：
{ "EnableTimestampNanosecond": true }
输入配置：
类型：文本日志采集。
文件路径：日志采集的路径。
Linux：以“/”开头，如/data/mylogs/**/*.log，表示/data/mylogs目录下所有后缀名为.Log的文件。
Windows：以盘符开头，如C:\Program Files\Intel\**\*.Log。
最大目录监控深度：文件路径中通配符**匹配的最大目录深度。默认为0（仅监控本层目录）。
2. 配置处理插件
由于源日志为 JSON 格式，在处理配置区域，添加JSON解析插件，从原始日志中分离出包含纳秒时间戳的字符串，并将其存为一个独立的字段。
添加日志样例
假设日志文件中的日志格式如下，其中asctime字段包含了纳秒精度的时间戳。
{ "asctime": "2023-10-25 23:51:10,199999999", "filename": "generate_data.py", "levelname": "INFO", "lineno": 51, "module": "generate_data", "message": "{\"no\": 14, \"inner_loop\": 166, \"loop\": 27451, \"uuid\": \"9be98c29-22c7-40a1-b7ed-29ae6c8367af\"}", "threadName": "MainThread" }
添加JSON解析插件
单击添加处理插件，选择原生处理插件>JSON解析，单击确认。
添加时间解析插件
将上一步提取的时间字符串（asctime字段）转换为标准的纳秒时间戳，并将其作为该条日志的事件时间。
| 插件名称 | 核心功能 | 适用场景 |
| --- | --- | --- |
| 时间解析 | 基础时间解析 | 简单场景，格式固定。 |
| 提取日志时间 (strptime 时间格式) | 灵活，支持丰富的 strptime 格式 | 推荐使用 。功能全面，与业界标准兼容。 |
| 提取日志时间 (Go 语言时间格式) | 使用 Go 语言标准库格式 | 熟悉 Go 语言或日志格式与 Go 标准库匹配的场景。 |
## 时间解析
单击添加处理插件，选择原生处理插件>[时间解析](time-parsing.md)，进行如下配置：
原始字段：解析日志前，用于存放时间的原始字段，本示例为asctime。
时间格式：根据日志的时间字段内容设置对应的[时间格式](log-collection-supports-nanosecond-precision-timestamps.md)，本示例为%Y-%m-%d %H:%M:%S,%f。其中%f为秒的小数部分，精度最高支持为纳秒。
时间格式字符串必须与原始日志中的时间格式（包括秒和纳秒之间的分隔符，如,或.）完全一致，否则无法正确解析。
时区：选择日志时间字段所在的时区，默认使用机器时区。
## 提取日志时间（strptime时间格式）
单击添加处理插件，选择拓展处理插件>[提取日志时间（strptime](extract-log-time.md)[时间格式）](extract-log-time.md)，进行如下配置：
原始字段：解析日志前，用于存放时间的原始字段，本示例为asctime。
原始时间格式：根据日志的时间字段内容设置对应的[时间格式](log-collection-supports-nanosecond-precision-timestamps.md)，本示例为%Y-%m-%d %H:%M:%S,%f。其中%f为秒的小数部分，精度最高支持为纳秒。
时间格式字符串必须与原始日志中的时间格式（包括秒和纳秒之间的分隔符，如,或.）完全一致，否则无法正确解析。
## 提取日志时间（Go语言时间格式）
单击添加处理插件，选择拓展处理插件>[提取日志时间（Go](extract-log-time.md)[语言时间格式）](extract-log-time.md)，进行如下配置：
原始时间字段：解析日志前，用于存放时间的原始字段，本示例为asctime。
原始时间格式：根据原始日志的时间字段设置对应的时间格式，需要按照[Golang](log-collection-supports-nanosecond-precision-timestamps.md)[的时间格式规范](log-collection-supports-nanosecond-precision-timestamps.md)来编写。格式化时间模板为Go语言的诞生时间2006-01-02 15:04:05 -0700 MST。本示例对应的时间格式为2006-01-02 15:04:05,999999999。
时间格式字符串必须与原始日志中的时间格式（包括秒和纳秒之间的分隔符，如,或.）完全一致，否则无法正确解析。
结果时间字段：解析日志后，用于存放时间的目标字段，本示例为result_asctime。
结果时间格式：解析日志后的时间格式，按照[Golang](log-collection-supports-nanosecond-precision-timestamps.md)[的时间格式规范](log-collection-supports-nanosecond-precision-timestamps.md)编写。本示例为2006-01-02 15:04:05,999999999Z07:00。
3. 配置索引
完成Logtail配置后，单击下一步。进入查询分析配置页面：
系统默认开启[全文索引](create-indexes.md)，支持对日志原始内容进行关键词搜索。
如需按字段进行精确查询，请在页面加载出预览数据后，单击自动生成索引，日志服务将根据预览数据中的第一条内容生成[字段索引](create-indexes.md)。
配置完成后，单击下一步，完成整个采集流程的设置。
通过CRD配置（Kubernetes 场景）
在 ACK 或自建 Kubernetes 集群中，可以通过 AliyunLog CRD 来配置纳秒精度时间戳的采集。以下是三种不同插件的配置样例。
## 时间解析
apiVersion: telemetry.alibabacloud.com/v1alpha1 kind: ClusterAliyunPipelineConfig metadata: name: ${your-config-name} spec: config: aggregators: [] global: EnableTimestampNanosecond: true inputs: - Type: input_file FilePaths: - /test/sls/json_nano.log MaxDirSearchDepth: 0 FileEncoding: utf8 EnableContainerDiscovery: true processors: - Type: processor_parse_json_native SourceKey: content - Type: processor_parse_timestamp_native SourceKey: asctime SourceFormat: '%Y-%m-%d %H:%M:%S,%f' flushers: - Type: flusher_sls Logstore: ${your-logstore-name} sample: |- { "asctime": "2025-11-03 15:39:14,229939478", "filename": "log_generator.sh", "levelname": "INFO", "lineno": 204, "module": "log_generator", "message": "{"no": 45, "inner_loop": 15, "loop": 1697, "uuid": "80366fca-a57d-b65a-be07-2ac1173505d9"}", "threadName": "MainThread" } project: name: ${your-project-name} logstores: - name: ${your-logstore-name}
## 提取日志时间（strptime时间格式）
apiVersion: telemetry.alibabacloud.com/v1alpha1 kind: ClusterAliyunPipelineConfig metadata: name: ${your-config-name} spec: config: aggregators: [] global: EnableTimestampNanosecond: true inputs: - Type: input_file FilePaths: - /test/sls/json_nano.log MaxDirSearchDepth: 0 FileEncoding: utf8 EnableContainerDiscovery: true processors: - Type: processor_parse_json_native SourceKey: content - Type: processor_strptime SourceKey: asctime Format: '%Y-%m-%d %H:%M:%S,%f' KeepSource: true AlarmIfFail: true AdjustUTCOffset: false flushers: - Type: flusher_sls Logstore: ${your-logstore-name} sample: |- { "asctime": "2025-11-03 15:39:14,229939478", "filename": "log_generator.sh", "levelname": "INFO", "lineno": 204, "module": "log_generator", "message": "{"no": 45, "inner_loop": 15, "loop": 1697, "uuid": "80366fca-a57d-b65a-be07-2ac1173505d9"}", "threadName": "MainThread" } project: name: ${your-project-name} logstores: - name: ${your-logstore-name}
## 提取日志时间（Go语言时间格式）
apiVersion: telemetry.alibabacloud.com/v1alpha1 kind: ClusterAliyunPipelineConfig metadata: name: ${your-config-name} spec: config: aggregators: [] global: EnableTimestampNanosecond: true inputs: - Type: input_file FilePaths: - /test/sls/json_nano.log MaxDirSearchDepth: 0 FileEncoding: utf8 EnableContainerDiscovery: true processors: - Type: processor_parse_json_native SourceKey: content - Type: processor_gotime SourceKey: asctime SourceFormat: '2006-01-02 15:04:05,999999999' DestKey: result_asctime DestFormat: '2006-01-02 15:04:05,999999999Z07:00' SetTime: true KeepSource: true NoKeyError: true AlarmIfFail: true flushers: - Type: flusher_sls Logstore: ${your-logstore-name} sample: |- { "asctime": "2025-11-03 15:39:14,229939478", "filename": "log_generator.sh", "levelname": "INFO", "lineno": 204, "module": "log_generator", "message": "{"no": 45, "inner_loop": 15, "loop": 1697, "uuid": "80366fca-a57d-b65a-be07-2ac1173505d9"}", "threadName": "MainThread" } project: name: ${your-project-name} logstores: - name: ${your-logstore-name}
### 步骤四：结果验证
配置完成后，等待片刻，新的日志数据将被采集到LogStore中。
在日志服务的查询分析页面，查看采集日志，控制台会根据高精度的时间信息，自动进行显示优化，显示成毫秒、微秒、纳秒的形式。
日志查询结果中，时间戳显示为类似2025-11-03 17:34:40.747598929的格式。
## 常见问题
### 采集日志无法正常解析纳秒时间戳
配置采集后，发现高精度时间并未正常提取。
日志查看器中索引时间为10-26 00:30:39，而日志记录的 asctime 为2023-10-26 00:30:10,199999999，两者不一致，说明高精度时间未被正常提取。日志记录详情：
__file_offset__ xxx __tag__ xxx asctime: 2023-10-26 00:30:10,199999999 filename: xxx levelname: INFO lineno: 51 message: {"no": 14, "inner_loop": 166, "loop": 27451, "uuid": "9be98c29-22c7-40a1-b7ed-29ae6c8367af"} module: generate_data threadName: MainThread
错误原因
插件模式支持%f，但是时间格式需要与源时间内容保持一致。
解决方法
登录LoongCollector（Logtail）机器，查看日志，发现大量STRPTIME_PARSE_ALARM异常日志。
tail -f /usr/local/ilogtail/logtail_plugin.LOG 2023-10-26 00:30:39 [WRN] [strptime.go:164] [processLog] [##1.0##xxxx,xxx] AlarmType:STRPTIME_PARSE_ALARM strptime(2023-10-26 00:30:10,199999999, %Y-%m-%d %H:%M:%S %f) failed: 0001-01-01 00:00:00 +0000 UTC, <nil>
修改插件日志解析格式。
原始日志时间为2023-10-26 00:30:10,199999999，秒与高精度时间（这里是毫秒）之间分隔符为半角逗号（,），解析格式为%Y-%m-%d %H:%M:%S %f，秒与高精度时间之间分隔符为空格 。修改采集配置中时间转换格式为%Y-%m-%d %H:%M:%S,%f即可。
## 成本与限制说明
成本影响：__time_ns_part__字段会作为日志内容的一部分被存储，略微增加原始日志的存储量。
环境限制：此功能仅支持 Linux 系统的 Logtail 1.8.0 及以上版本，在 Windows 系统上配置不生效。
## 相关文档
[下载日志](download-logs.md)
[查询语法与功能](query-syntax.md)
[查询与分析概述](log-analysis-overview.md)
[SDK](high-precision-timestamp-and-global-sorting.md)[操作高精度时间戳](high-precision-timestamp-and-global-sorting.md)
## 附录一：常见日志时间格式
Linux服务器中，Logtail支持strftime函数提供的所有时间格式。即能被strftime函数格式化的日志时间字符串都能被Logtail解析并使用。
| 时间格式 | 说明 | 示例 |
| --- | --- | --- |
| %a | 星期的缩写。 | Fri |
| %A | 星期的全称。 | Friday |
| %b | 月份的缩写。 | Jan |
| %B | 月份的全称。 | January |
| %d | 每月第几天，十进制，范围为 01~31。 | 07, 31 |
| %f | 秒的小数部分（毫秒、微秒或纳秒） | 123 |
| %h | 月份的缩写，等同于 %b 。 | Jan |
| %H | 小时，24 小时制。 | 22 |
| %I | 小时，12 小时制。 | 11 |
| %m | 月份，十进制，范围为 01~12。 | 08 |
| %M | 分钟，十进制，范围为 00~59。 | 59 |
| %n | 换行符。 | 换行符 |
| %p | AM 或 PM。 | AM、PM |
| %r | 12 小时制的时间组合，等同于 %I:%M:%S %p 。 | 11:59:59 AM |
| %R | 小时和分钟组合，等同于 %H:%M 。 | 23:59 |
| %S | 秒数，十进制，范围为 00~59。 | 59 |
| %t | Tab 符号，制表符。 | 无 |
| %y | 年份，十进制，不带世纪，范围为 00~99。 | 04、98 |
| %Y | 年份，十进制。 | 2004、1998 |
| %C | 世纪，十进制，范围为 00~99。 | 16 |
| %e | 每月第几天，十进制，范围为 1~31。 如果是个位数字，前面需要加空格。 | 7、31 |
| %j | 一年中的天数，十进制，范围为 001~366。 | 365 |
| %u | 星期几，十进制，范围为 1~7，1 表示周一。 | 2 |
| %U | 每年的第几周，星期天是一周的开始，范围为 00~53。 | 23 |
| %V | 每年的第几周，星期一是一周的开始，范围为 01~53。 如果一月份刚开始的一周>=4 天，则认为是第 1 周，否则认为下一个星期是第 1 周。 | 24 |
| %w | 星期几，十进制，范围为 0~6，0 代表周日。 | 5 |
| %W | 每年的第几周，星期一是一周的开始，范围为 00~53。 | 23 |
| %c | 标准的日期和时间。 | Tue Nov 20 14:12:58 2020 |
| %x | 标准的日期，不带时间。 | Tue Nov 20 2020 |
| %X | 标准的时间，不带日期。 | 11:59:59 |
| %s | Unix 时间戳。 | 1476187251 |
时间格式示例
常见的时间标准、示例及对应的时间表达式如下所示。
| 示例 | 时间表达式 | 时间标准 |
| --- | --- | --- |
| 2017-12-11 15:05:07 | %Y-%m-%d %H:%M:%S | 自定义 |
| [2017-12-11 15:05:07.012] | [%Y-%m-%d %H:%M:%S | 自定义 |
| 2017-12-11 15:05:07.123 | %Y-%m-%d %H:%M:%S.%f | 自定义 |
| 02 Jan 06 15:04 MST | %d %b %y %H:%M | RFC822 |
| 02 Jan 06 15:04 -0700 | %d %b %y %H:%M | RFC822Z |
| Monday, 02-Jan-06 15:04:05 MST | %A, %d-%b-%y %H:%M:%S | RFC850 |
| Mon, 02 Jan 2006 15:04:05 MST | %A, %d %b %Y %H:%M:%S | RFC1123 |
| 2006-01-02T15:04:05Z07:00 | %Y-%m-%dT%H:%M:%S | RFC3339 |
| 2006-01-02T15:04:05.999999999Z07:00 | %Y-%m-%dT%H:%M:%S | RFC3339Nano |
| 1637843406 | %s | 自定义 |
| 1637843406123 | %s | 自定义（ 日志服务 以秒级精度处理） |
## 附录二：Golang时间格式
以下为Golang官方的时间格式示例：
const ( Layout = "01/02 03:04:05PM '06 -0700" // The reference time, in numerical order. ANSIC = "Mon Jan _2 15:04:05 2006" UnixDate = "Mon Jan _2 15:04:05 MST 2006" RubyDate = "Mon Jan 02 15:04:05 -0700 2006" RFC822 = "02 Jan 06 15:04 MST" RFC822Z = "02 Jan 06 15:04 -0700" // RFC822 with numeric zone RFC850 = "Monday, 02-Jan-06 15:04:05 MST" RFC1123 = "Mon, 02 Jan 2006 15:04:05 MST" RFC1123Z = "Mon, 02 Jan 2006 15:04:05 -0700" // RFC1123 with numeric zone RFC3339 = "2006-01-02T15:04:05Z07:00" RFC3339Nano = "2006-01-02T15:04:05.999999999Z07:00" Kitchen = "3:04PM"// Handy time stamps. Stamp = "Jan _2 15:04:05" StampMilli = "Jan _2 15:04:05.000" StampMicro = "Jan _2 15:04:05.000000" StampNano = "Jan _2 15:04:05.000000000" )
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
