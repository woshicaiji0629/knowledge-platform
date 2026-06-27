# 时间插件配置参数格式与示例-日志服务-阿里云-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/time-processing-class-plug-in

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

# 时间处理类插件

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

时间处理类插件用于解析、提取、标准化日志时间。

## 插件效果示例

表格展示该原始日志在分别使用时间解析插件（原生）与不使用插件的情况下，保存到日志服务后的数据结构。

| 原始日志 | 不使用插件 | 使用时间解析插件（原生） |
| --- | --- | --- |
| 秒级时间： { "level":"INFO", "timestamp":"2025-09-29T09:56:01+0800", "cluster":"yilu-cluster-0728", "message":"User logged in successfully", "userId":"user-123" } | Content：" {"level":"INFO","timestamp":"2025-09-29T09:56:01+0800","cluster":"yilu-cluster-0728","message":"User logged in successfully","userId":"user-123"} " |  |
| 毫秒时间： { "time": "2026-01-05T11:58:40,647Z", "filename": "out_data.py", "levelname": "INFO", "threadName": "MainThread" } | Content：" {"time":"2026-01-05T11:58:40,647Z", "filename":"out_data.py","levelname": "INFO", "threadName":"MainThread"} " |  |
| 纳秒时间： { "time": "2026-01-05T11:40:22,298837465Z07:00", "filename": "out_data.py", "levelname": "INFO", "threadName": "MainThread" } | Content：" {"time": "2026-01-05T11:40:22,298837465Z07:00","filename":"out_data.py","levelname":"INFO","threadName": "MainThread"} " |  |


## 时间处理类插件概览

日志服务提供以下多种类型的时间处理类插件，请按需要进行选择。

| 插件名称 | 类型 | 功能说明 |
| --- | --- | --- |
| 时间解析 | 原生 | 解析并标准化日志中的时间字段。 |
| 提取日志时间 | 拓展 | 解析原始时间字段并可设为日志时间戳。 |


### 功能入口

当您需要使用Logtail插件处理日志时，您可以在创建或修改Logtail配置时，添加插件。具体操作，请参见[处理插件概述](products/sls/documents/overview-22.md)。

## 原生插件与拓展插件的区别

原生插件：C++实现，性能更强。

拓展插件：Go实现，生态丰富且灵活，当业务日志过于复杂，无法使用原生插件处理时，可以考虑使用拓展插件。

- 

拓展插件性能限制

- 

使用拓展插件进行日志处理时，LoongCollector会消耗更多的资源（以CPU为主），如有需求可以调整LoongCollector参数配置进行[配置管理](products/sls/documents/loongcollector-management-linux.md)。

- 

当原始数据量的生成速度超过5 MB/s时，不建议使用过于复杂的插件组合来处理日志，可以使用拓展插件进行简单处理，再通过[数据加工概述](products/sls/documents/data-transformation-overview.md)完成进一步处理。

- 

日志采集限制

- 

拓展插件对文本日志的处理采用行模式，即文件级别的元数据（例如__tag__:__path__、__topic__等）会被存放到每一条日志中。

- 

添加拓展插件后会影响和Tag相关的功能：

- 

上下文查询和LiveTail功能不可用。如果要使用这些功能，需要额外添加aggregators配置。

- 

__topic__字段会被重命名为__log_topic__。如果添加了aggregators配置，日志中将同时存在__topic__字段和__log_topic__字段。如果您不需要__log_topic__字段，可使用[丢弃字段插件](products/sls/documents/field-processing-class-plug-in.md)删除该字段。

- 

__tag__:__path__等字段不再具备原生字段索引，需要[创建索引](products/sls/documents/create-indexes.md)。

## 时间解析插件（原生）

时间解析插件用于解析日志的时间字段，并将解析结果设置为日志的__time__字段。

### 配置说明

| 参数名称 | 说明 |
| --- | --- |
| 原始字段 | 解析日志前，用于存放日志内容的原始字段，默认值为 content。 说明 在使用正则解析插件时，原始字段仅支持设置为 time，请确保您的正则解析配置中包含 time 作为提取字段。 |
| 时间格式 | 根据日志中的时间内容设置对应的时间格式。例如日志中的时间为 10/Sep/2023:12:36:49 ，对应的时间转换格式为 %d/%b/%Y:%H:%M:%S 。 |
| 时区 | 选择日志时间字段所在的时区。如果不选择，则默认使用机器时区，即使用 Logtail 进程所在环境的时区。 |


默认情况下，日志服务中的日志时间戳精确到秒，所以时间格式只需配置到秒，无需配置毫秒、微秒等信息。如果原始日志中的时间字段包含毫秒、微秒或纳秒级精度，且需在日志服务中保留该精度，请参考如下示例开启纳秒精度，详细信息请参见[日志采集支持纳秒精度时间戳](products/sls/documents/log-collection-supports-nanosecond-precision-timestamps.md)。

| 原始日志 | 时间解析插件配置 | 时间格式 |
| --- | --- | --- |
| { "time": "2026-01-05T11:40:22,298837465Z07:00", "filename": "out_data.py", "levelname": "INFO", "threadName": "MainThread" } |  | %Y-%m-%dT%H:%M:%S,%f |


开启纳秒精度支持：

进入Logtail配置页面，在全局配置>其他全局配置，开启高级参数开关，并输入以下 JSON 内容以开启纳秒精度支持：

{ "EnableTimestampNanosecond": true }

在使用以下拓展插件解析纳秒或毫秒场景，也需要开启该高级参数 EnableTimestampNanosecond。

## 提取日志时间插件（拓展）

使用processor_gotime插件或processor_strptime插件解析原始日志中的时间字段。此处介绍两种插件的参数说明和配置示例。

说明

如果原始日志中的时间字段包含毫秒、微秒或纳秒级精度，且需在日志服务中保留该精度，请参见[日志采集支持纳秒精度时间戳](products/sls/documents/log-collection-supports-nanosecond-precision-timestamps.md)。

### Go语言时间格式（processor_gotime）

processor_gotime插件使用Go语言时间格式解析原始日志中的时间字段，并支持将解析结果设置为日志服务中的日志时间。

重要

- 

Logtail 0.16.28及以上版本支持processor_gotime插件。

- 

表单配置方式：采集文本日志和容器标准输出时可用。

- 

JSON配置方式：采集文本日志时不可用。

### 表单配置方式

- 

参数说明

配置处理插件类型为提取日志时间（Go语言时间格式）。

相关参数说明如下表所示。

| 参数 | 说明 |
| --- | --- |
| 原始时间字段 | 原始字段名。 |
| 原始时间格式 | 原始时间的格式。 |
| 原始时间时区 | 原始时间的时区。选择 机器时区 时，表示 Logtail 所在主机或容器的时区。 |
| 结果时间字段 | 解析后的目标字段，该字段不支持设置为 __time__ 。 |
| 结果时间格式 | 解析后的时间格式。 |
| 自定义结果时间时区 | 解析后的时区。选择 机器时区 时，表示本机的时区。 |
| 高级参数> 设为日志时间 | 选中该选项后，系统会将解析后的时间设置为日志时间。 |
| 高级参数> 保留原始字段 | 选中该选项后，解析后的日志中将保留原始字段。 |
| 高级参数> 原始字段缺失报错 | 选中该选项后，如果原始日志中无您所指定的原始字段，系统将报错。 |
| 高级参数> 提取失败报错 | 选中该选项后，如果提取日志时间失败，系统将报错。 |


- 

示例

原始时间（s_key字段）的格式为2006-01-02 15:04:05（东八区），现将原始时间解析为2006/01/02 15:04:05（东九区）格式，添加到d_key字段中，并设置解析结果为日志服务中的日志时间。

- 

原始日志

"s_key":"2022-07-05 19:28:01"

- 

Logtail插件处理配置

- 

处理结果

"s_key":"2022-07-05 19:28:01" "d_key":"2022/07/05 20:28:01"

### JSON配置方式

- 

参数说明

配置type为processor_gotime，detail说明如下表所示。

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| SourceKey | String | 是 | 原始字段名。 |
| SourceFormat | String | 是 | 原始时间的格式。 |
| SourceLocation | Int | 是 | 原始时间的时区。参数值为空时，表示 Logtail 所在主机或容器的时区。 |
| DestKey | String | 是 | 解析后的目标字段，该字段不支持设置为 __time__ 。 |
| DestFormat | String | 是 | 解析后的时间格式。 |
| DestLocation | Int | 否 | 解析后的时区。参数值为空时，表示本机时区。 |
| SetTime | Boolean | 否 | 是否将解析后的时间设置为日志时间。 true（默认值）：是 false：否 |
| KeepSource | Boolean | 否 | 被解析后的日志中是否保留原始字段。 true（默认值）：保留 false：不保留 |
| NoKeyError | Boolean | 否 | 原始日志中无您所指定的原始字段时，系统是否报错。 true（默认值）：报错 false：不报错 |
| AlarmIfFail | Boolean | 否 | 提取日志时间失败，系统是否报错。 true（默认值）：报错 false：不报错 |


- 

示例

原始时间（s_key字段）的格式为2006-01-02 15:04:05（东八区），现将原始时间解析为2006/01/02 15:04:05（东九区）格式，添加到d_key字段中，并设置解析结果为日志服务中的日志时间。

- 

原始日志

"s_key":"2019-07-05 19:28:01"

- 

Logtail插件处理配置

{ "processors":[ { "type":"processor_gotime", "detail": { "SourceKey": "s_key", "SourceFormat":"2006-01-02 15:04:05", "SourceLocation":8, "DestKey":"d_key", "DestFormat":"2006/01/02 15:04:05", "DestLocation":9, "SetTime": true, "KeepSource": true, "NoKeyError": true, "AlarmIfFail": true } } ] }

- 

处理结果

"s_key":"2019-07-05 19:28:01" "d_key":"2019/07/05 20:28:01"（）

### strptime时间格式（processor_strptime）

processor_strptime插件使用[Linux strptime](http://man7.org/linux/man-pages/man3/strptime.3.html)[时间格式](http://man7.org/linux/man-pages/man3/strptime.3.html)解析日志中的时间字段，并支持将解析结果设置为日志时间。

重要

Logtail 0.16.28及以上版本支持processor_strptime插件。

### 表单配置方式

- 

参数说明

配置处理器类型为提取日志时间（strptime时间格式），相关参数说明如下表所示。

| 参数 | 说明 |
| --- | --- |
| 原始字段 | 原始字段名。 |
| 原始时间格式 | 原始时间的格式。 |
| 保留原始字段 | 选中该选项后，被解析后的日志中将保留原始字段。 |
| 提取失败报错 | 选中该选项后，如果提取日志时间失败，系统将报错。 |
| 进行时间偏移 | 选中该选项后，您可以设置时间偏移秒数。 |
| 时间偏移秒数 | 时间偏移秒数。例如 28800 表示东八区，-3600 代表西一区。 |


- 

配置示例

将%Y/%m/%d %H:%M:%S格式的原始时间（log_time字段的值）解析为对应的日志时间，时区使用机器所在时区。假设时区为东八区。

- 

原始日志

"log_time":"2022/01/02 12:59:59"

- 

Logtail插件处理配置

- 

处理结果

"log_time":"2022/01/02 12:59:59" Log.Time = 1451710799

- 

常见的时间表达式

说明

processor_strptime插件支持%f格式解析，表示秒的小数部分，最高精度为纳秒。

| 示例 | 时间表达式 |
| --- | --- |
| 2016/01/02 12:59:59 | %Y/%m/%d %H:%M:%S |
| 2016/01/02 12:59:59.1 | %Y/%m/%d %H:%M:%S.%f |
| 2016/01/02 12:59:59.987654321 +0700 (UTC) | %Y/%m/%d %H:%M:%S.%f %z (%Z) |
| 2016/Jan/02 12:59:59,123456 | %Y/%b/%d %H:%M:%S,%f |
| 2019-07-15T04:16:47:123Z | %Y-%m-%dT%H:%M:%S:%f |


### JSON配置方式

- 

参数说明

配置type为processor_strptime，detail说明如下表所示。

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 说明 |
| --- | --- | --- | --- |
| SourceKey | String | 是 | 原始字段名。 |
| Format | String | 是 | 原始时间的格式。 |
| AdjustUTCOffset | Boolean | 否 | 是否调整时区。 true：是。 false（默认值）：否 |
| UTCOffset | Int | 否 | 用于调整的时区偏移秒数。例如 28800 表示东八区。 |
| AlarmIfFail | Boolean | 否 | 提取日志失败时，系统是否报错。 true（默认值）：报错。 false：不报错。 |
| KeepSource | Boolean | 否 | 被解析后的日志中，是否保留原始字段。 true（默认值）：保留。 false：不保留。 |


- 

示例

将%Y/%m/%d %H:%M:%S格式的原始时间（log_time字段的值）解析为对应的日志时间，时区使用机器所在时区。

- 

示例1：假设时区为东八区。

- 

原始日志

"log_time":"2016/01/02 12:59:59"

- 

Logtail插件处理配置

{ "processors":[ { "type":"processor_strptime", "detail": { "SourceKey": "log_time", "Format": "%Y/%m/%d %H:%M:%S" } } ] }

- 

处理结果

"log_time":"2016/01/02 12:59:59" Log.Time = 1451710799

- 

示例2：假设时区为东七区。

- 

原始日志

"log_time":"2016/01/02 12:59:59"

- 

Logtail插件处理配置

{ "processors":[ { "type":"processor_strptime", "detail": { "SourceKey": "log_time", "Format": "%Y/%m/%d %H:%M:%S", "AdjustUTCOffset": true, "UTCOffset": 25200 } } ] }

- 

处理结果

"log_time":"2016/01/02 12:59:59" Log.Time = 1451714399

- 

示例3：假设时区为东七区。

- 

原始日志

"log_time":"2016/01/02 12:59:59.123"

- 

Logtail插件处理配置

{ "processors":[ { "type":"processor_strptime", "detail": { "SourceKey": "log_time", "Format": "%Y/%m/%d %H:%M:%S.%f" } } ] }

- 

处理结果

"log_time":"2016/01/02 12:59:59.123" Log.Time = 1451714399

- 

常见的时间表达式

说明

processor_strptime插件支持%f格式解析，表示秒的小数部分，最高精度为纳秒。

| 示例 | 时间表达式 |
| --- | --- |
| 2016/01/02 12:59:59 | %Y/%m/%d %H:%M:%S |
| 2016/01/02 12:59:59.1 | %Y/%m/%d %H:%M:%S.%f |
| 2016/01/02 12:59:59.987654321 +0700 (UTC) | %Y/%m/%d %H:%M:%S.%f %z (%Z) |
| 2016/Jan/02 12:59:59,123456 | %Y/%b/%d %H:%M:%S,%f |
| 2019-07-15T04:16:47:123Z | %Y-%m-%dT%H:%M:%S:%f |


## 常见日志时间格式

processor_gotime扩展插件支持的常见日志时间格式请参见[https://pkg.go.dev/time#pkg-constants](https://pkg.go.dev/time#pkg-constants)。processor_parse_timestamp_native原生插件与 processor_strptime 扩展插件支持的常见日志时间格式如下表所示：

说明

- 

在Linux服务器中，Logtail支持strftime函数提供的所有时间格式。即能被strftime函数格式化的日志时间字符串都能被Logtail解析并使用。

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


### 示例

常见的时间标准、示例及对应的时间表达式如下所示。

| 示例 | 时间表达式 | 时间标准 |
| --- | --- | --- |
| 2017-12-11 15:05:07 | %Y-%m-%d %H:%M:%S | 自定义 |
| [2017-12-11 15:05:07.012] | [%Y-%m-%d %H:%M:%S.%f | 自定义 |
| 2017-12-11 15:05:07.123 | %Y-%m-%d %H:%M:%S.%f | 自定义 |
| 02 Jan 06 15:04 MST | %d %b %y %H:%M | RFC822 |
| 02 Jan 06 15:04 -0700 | %d %b %y %H:%M | RFC822Z |
| Monday, 02-Jan-06 15:04:05 MST | %A, %d-%b-%y %H:%M:%S | RFC850 |
| Mon, 02 Jan 2006 15:04:05 MST | %A, %d %b %Y %H:%M:%S | RFC1123 |
| 2006-01-02T15:04:05Z07:00 | %Y-%m-%dT%H:%M:%S | RFC3339 |
| 2006-01-02T15:04:05.999999999Z07:00 | %Y-%m-%dT%H:%M:%S.%f | RFC3339Nano |
| 1637843406 | %s | 自定义 |
| 1637843406123 | %s | 自定义（ 日志服务 以秒级精度处理） |


## 相关文档

- 

通过API接口配置Logtail流水线：

- 

[获取](products/sls/documents/developer-reference/api-sls-2020-12-30-getlogtailpipelineconfig.md)[Logtail](products/sls/documents/developer-reference/api-sls-2020-12-30-getlogtailpipelineconfig.md)[流水线配置](products/sls/documents/developer-reference/api-sls-2020-12-30-getlogtailpipelineconfig.md)

- 

[罗列](products/sls/documents/developer-reference/api-sls-2020-12-30-listlogtailpipelineconfig.md)[Logtail](products/sls/documents/developer-reference/api-sls-2020-12-30-listlogtailpipelineconfig.md)[流水线配置](products/sls/documents/developer-reference/api-sls-2020-12-30-listlogtailpipelineconfig.md)

- 

[创建](products/sls/documents/developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md)[Logtail](products/sls/documents/developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md)[流水线配置](products/sls/documents/developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md)

- 

[删除](products/sls/documents/developer-reference/api-sls-2020-12-30-deletelogtailpipelineconfig.md)[Logtail](products/sls/documents/developer-reference/api-sls-2020-12-30-deletelogtailpipelineconfig.md)[流水线配置](products/sls/documents/developer-reference/api-sls-2020-12-30-deletelogtailpipelineconfig.md)

- 

[更新](products/sls/documents/developer-reference/api-sls-2020-12-30-updatelogtailpipelineconfig.md)[Logtail](products/sls/documents/developer-reference/api-sls-2020-12-30-updatelogtailpipelineconfig.md)[流水线配置](products/sls/documents/developer-reference/api-sls-2020-12-30-updatelogtailpipelineconfig.md)

- 

通过控制台配置处理插件：

- 

[持续采集主机文本日志](products/sls/documents/host-text-log-collection-auto-install.md)

- 

[通过控制台采集集群容器日志（标准输出/文件）](products/sls/documents/collect-kubernetes-cluster-text-logs-daemonset.md)

- 

[通过](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)[Kubernetes CRD](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)[采集集群容器日志（标准输出/文件）](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)

[上一篇：字段处理类插件](products/sls/documents/field-processing-class-plug-in.md)[下一篇：使用Logtail SPL解析日志](products/sls/documents/use-logtail-spl-to-parse-logs.md)

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
