# 配置索引实现日志的查询和分析-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/create-indexes

# 创建索引
如需对采集到LogStore中的日志进行查询和分析，则必须创建索引。本文为您介绍日志服务索引概念、索引类型、创建索引、关闭索引、配置示例和计费说明等。
## 为什么需要创建索引
通常我们使用关键词从原始日志中检索想要的内容，例如包含curl的日志：curl/7.74.0。如果不进行切分，该日志文本会作为一个整体，不能和关键词curl完全对应，因此不会被日志服务检索到。
为了便于检索，需要将日志切分成独立、可搜索的词。日志切分由分词符实现，这些符号决定了日志文本内容被切分的位置。以该日志为例，使用分词符\n\t\r,;[]{}()&^*#@~=<>/\?:'"进行分割，得到的词是curl、7.74.0。日志服务基于切分出的关键词建立索引。创建索引后，您才能对日志进行查询和分析。
日志服务Project支持创建全文索引和字段索引。如果您同时创建了全文索引和字段索引，以字段索引的配置为准。
## 索引类型
### 全文索引
全文索引根据分词符直接将整个日志切分成多个text类型的词语。创建全文索引后，可以通过关键词进行查询，例如查询语句：Chrome or Safari，查询包括Chrome或Safari的日志。
重要
分词符不支持中文，开启包含中文选项，日志服务会自动按照中文分词。
如果只配置全文索引，则只能使用全文查询功能。更多信息，请参见[查询语法与功能](query-syntax.md)。
### 字段索引
字段索引将日志根据字段名称（KEY）进行区分，然后在字段内使用分词符进行分割。字段索引支持text、long、double和JSON四种类型的数据。更多信息，请参见[数据类型](data-types.md)。创建字段索引后，可以指定字段名称和字段值（Key:Value）进行查询，也可以使用SELECT语句。更多信息，请参见[查询语法与功能](query-syntax.md)。
重要
如需对字段进行查询或分析（SELECT语句），必须创建字段索引。字段索引的优先级高于全文索引，如果同时创建了全文索引和字段索引，以字段索引的配置为准。
text类型的字段，可以使用全文查询语句、字段查询语句和分析语句（SELECT）。
如果未开启全文索引，全文查询语句是从所有text类型的字段中查询结果。
如果已开启全文索引，全文查询语句是从所有日志中查询结果。
long和double类型的字段，可以使用字段查询语句和分析语句（SELECT）进行查询和分析。
## 创建索引
重要
不同的索引配置，会产生不同的查询和分析结果，请根据您的需求，合理创建索引。创建索引后需要大约一分钟生效。
创建索引只对增量日志有效。如需查询历史日志，请使用[重建索引](reindex-logs-for-a-logstore.md)功能。
日志服务已为部分保留字段创建索引。更多信息，请参见[保留字段](reserved-fields.md)。
其中__topic__和__source__的索引分词符为空，查询这两个字段时，关键字必须完全匹配。
__tag__为前缀的字段不支持全文索引。只支持创建text类型的字段索引。您需要创建字段索引后，才能执行查询和分析操作，例如*| select "__tag__:__receive_time__"。
日志中存在同名字段（例如都为request_time）时，日志服务会将其中一个字段名显示为request_time_0，底层存储的字段名仍为request_time。因此在创建索引、查询、分析、投递、加工时，只能使用原始字段名request_time。
### 控制台方式
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
在LogStore的查询和分析页面，单击开启索引。
说明
开启后等待1min左右即可查询最新数据。
（可选）关闭自动更新索引
当LogStore为云产品专属LogStore或内部LogStore时，默认打开索引自动更新开关，后续如有版本更新时可以升级到内置索引最新版本。如果需要创建索引，请在查询分析面板中，关闭自动更新开关。
警告
删除云产品专属LogStore的索引会影响相关报表、告警等功能的使用。
创建索引
创建全文索引
单击开启索引后，全文索引开关默认打开。您可根据需要选择是否打开日志聚类、大小写敏感、包含中文功能，也可选择指定分词符或自定义分词符。
页面配置如下所示：
配置项说明如下所示：
| 参数 | 说明 |
| --- | --- |
| 日志聚类 | 打开 日志聚类 开关后，日志服务在采集文本日志时会自动聚合相似度高的日志，提取共同的日志模式，帮助您快速掌握日志整体情况。更多信息，请参见 [日志聚类](logreduce.md) 。 |
| 大小写敏感 | 查询时是否区分英文字母的大小写。 打开 大小写敏感 开关，则查询时区分大小写。例如某条日志含有 internalError ，那么您只能使用 internalError 才能查询到该日志。 关闭 大小写敏感 开关，则查询时不区分大小写。例如某条日志含有 internalError ，那么您使用关键字 INTERNALERROR 和 internalerror 都能查到该日志。 |
| 包含中文 | 查询时是否区分中英文。 打开 包含中文 开关后，如果日志中包含中文，则按照中文语法拆分中文内容，按照分词符的设置拆分英文内容。 重要 中文分词对写入速度会有一定影响，请根据需求谨慎设置。 关闭 包含中文 开关后，按照分词符的设置拆分所有内容。 例如日志内容为 user:SLS 日志服务用户张先生 。 关闭 包含中文 开关后，按照分词符半角冒号（:）进行拆分，日志会被拆分为 user 、 SLS 日志服务用户张先生 ，您可以通过 user 或 SLS 日志服务用户张先生 查找该日志。 打开 包含中文 开关后，日志服务后台分词器将日志拆分为 user 、 SLS 、 日志服务 、 用户 和 张先生 ，您通过 日志服务 或 张先生 等词都可以查找到该日志。 |
| 分词符 | 根据指定分词符，将日志内容拆分成多个词。日志服务的默认分词符为 , '";=()[]{}?@&<>/:\n\t\r 。当默认设置不能满足您的需求时，您可以自定义设置分词符。所有的 ASCII 码都可被定义为分词符。 如果设置 分词符 为空，则字段值将被当成一个整体，您只能通过完整字符串或模糊查询查找对应的日志。 例如日志内容为 /url/pic/abc.gif 。 如果不设置任何分词符，整条日志被作为一个词 /url/pic/abc.gif ，您只能通过完整字符串 /url/pic/abc.gif 或模糊查询 /url/pic/* 查找该日志。 如果设置分词符为正斜线（/），则原始日志被拆分为 url 、 pic 和 abc.gif 三个词，您通过任意一个词或词的模糊查询都可以找到该日志，例如 url 、 abc.gif 、 pi* 、 /url/pic/abc.gif 。 如果设置分词符为正斜线（/）和半角句号（.），则原始日志被拆分为 url 、 pic 、 abc 和 gif 四个词，您通过任意一个词或词的模糊查询都可以找到该日志。 |
创建字段索引
单击开启索引后。您可在查询分析页面单击自动生成索引。日志服务会根据采集时预览数据中的第一条内容，自动生成字段索引。如需自定义字段索引，可单击页面下方的+创建，具体字段说明请参见[配置项说明](create-indexes.md)。
首次打开时页面如下所示：
字段索引配置项如下所示：
配置项说明如下所示：
| 参数 | 说明 |
| --- | --- |
| 字段名称 | 日志字段名称（KEY），例如 client_ip 。 字段名称只能包括字母、数字或下划线（_），且只能以字母或下划线（_）开头。 重要 设置公网 IP 地址、Unix 时间戳等 __tag__ 字段的索引时，需设置 字段名称 为 __tag__:KEY 形式，例如 __tag__:__receive_time__ 。更多信息，请参见 [保留字段](reserved-fields.md) 。 __tag__ 字段不支持数值类型索引，请将所有 __tag__ 字段的索引的 类型 设置为 text 。 |
| 类型 | 日志字段值（Value）的数据类型，可选值为 text 、 long 、 double 和 json 。更多信息，请参见 [数据类型](data-types.md) 。 long 和 double 类型不支持设置 大小写敏感 、 包含中文 和 分词符 。 |
| 别名 | 字段的别名，例如设置 client_ip 字段的别名为 ip 。 字段别名只能包括字母、数字或下划线（_），且只能以字母或下划线（_）开头。 重要 别名仅用于分析语句（SELECT 语句），查询语句中仍需使用原始字段名称。更多信息，请参见 [列的别名](column-aliases.md) 。 |
| 大小写敏感 | 查询时是否区分英文字母的大小写。 打开 大小写敏感 开关，则查询时区分大小写。例如某条日志含有 internalError ，那么您只能使用 internalError 才能查询到该日志。 关闭 大小写敏感 开关，则查询时不区分大小写。例如某条日志含有 internalError ，那么您使用关键字 INTERNALERROR 和 internalerror 都能查到该日志。 |
| 分词符 | 根据指定分词符，将日志内容拆分成多个词。日志服务的默认分词符为 , '";=()[]{}?@&<>/:\n\t\r 。当默认设置不能满足您的需求时，您可以自定义设置分词符。所有的 ASCII 码都可被定义为分词符。 如果设置 分词符 为空，则字段值将被当成一个整体，您只能通过完整字符串或模糊查询查找对应的日志。 例如日志内容为 /url/pic/abc.gif 。 如果不设置任何分词符，整条日志被作为一个词 /url/pic/abc.gif ，您只能通过完整字符串 /url/pic/abc.gif 或模糊查询 /url/pic/* 查找该日志。 如果设置分词符为正斜线（/），则原始日志被拆分为 url 、 pic 和 abc.gif 三个词，您通过任意一个词或词的模糊查询都可以找到该日志，例如 url 、 abc.gif 、 pi* 、 /url/pic/abc.gif 。 如果设置分词符为正斜线（/）和半角句号（.），则原始日志被拆分为 url 、 pic 、 abc 和 gif 四个词，您通过任意一个词或词的模糊查询都可以找到该日志。 |
| 包含中文 | 查询时是否区分中英文。 打开 包含中文 开关后，如果日志中包含中文，则按照中文语法拆分中文内容，按照分词符的设置拆分英文内容。 重要 中文分词对写入速度会有一定影响，请根据需求谨慎设置。 关闭 包含中文 开关后，按照分词符的设置拆分所有内容。 例如日志内容为 user:SLS 日志服务用户张先生 。 关闭 包含中文 开关后，按照分词符半角冒号（:）进行拆分，日志会被拆分为 user 、 SLS 日志服务用户张先生 ，您可以通过 user 或 SLS 日志服务用户张先生 查找该日志。 打开 包含中文 开关后，日志服务后台分词器将日志拆分为 user 、 SLS 、 日志服务 、 用户 和 张先生 ，您通过 日志服务 或 张先生 等词都可以查找到该日志。 |
| 开启统计 | 打开 开启统计 功能后，您才能对该字段进行统计分析。 |
（可选）设置字段的最大长度
SQL分析过程中，默认为截取一定长度，日志服务的默认配置为2048字节，即2KB。如果您需要修改字段值的最大长度，可在查询分析页面底部设置统计字段（text）最大长度，取值范围为64~16384字节。
重要
更新索引配置只对增量数据有效。
如果单个字段值长度超过最大长度，超出部分将被截断，不参与分析。
### API方式
日志服务支持通过API方式管理索引。具体操作，请参见：
[创建索引](developer-reference/api-sls-2020-12-30-createindex.md)
[获取索引](developer-reference/api-sls-2020-12-30-getindex.md)
[更新索引](developer-reference/api-sls-2020-12-30-updateindex.md)
[删除索引](developer-reference/api-sls-2020-12-30-deleteindex.md)
### SDK方式
日志服务支持通过多语言SDK进行索引管理，以下列举一些常用的SDK。更多信息，请参见[SDK](developer-reference/overview-of-log-service-sdk.md)[参考概述](developer-reference/overview-of-log-service-sdk.md)。
## Java
使用日志服务Java SDK方式管理索引的具体操作，请参见[使用](developer-reference/use-log-service-sdk-for-java-to-manage-indexes.md)[Java SDK](developer-reference/use-log-service-sdk-for-java-to-manage-indexes.md)[管理索引](developer-reference/use-log-service-sdk-for-java-to-manage-indexes.md)。
## Python
使用日志服务Python SDK方式管理索引的具体操作，请参见[使用](developer-reference/use-log-service-sdk-for-python-to-manage-indexes.md)[Python SDK](developer-reference/use-log-service-sdk-for-python-to-manage-indexes.md)[管理索引](developer-reference/use-log-service-sdk-for-python-to-manage-indexes.md)。
日志服务除自研的SDK外，还支持公共的阿里云SDK，关于阿里云SDK的使用方式，请参见[日志服务_SDK](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)[中心-阿里云](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)[OpenAPI](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)[开发者门户](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)。
### CLI方式
日志服务提供命令行工具CLI（Command Line Interface）管理索引。具体操作，请参见：
[create_index](developer-reference/create-index.md)
[delete_index](developer-reference/delete-index.md)
[get_index_config](developer-reference/get-index-config.md)
[update_index](developer-reference/update-index.md)
## 更新索引
### 操作步骤
在目标LogStore的查询和分析页面，选择查询分析属性>属性。不同的索引配置，会产生不同的查询和分析结果，请根据您的需求，合理更新索引。更新索引后需要大约一分钟生效。
## 关闭索引
重要
关闭索引后，历史索引的存储空间将在当前LogStore的数据保存时间到期后，自动被清除。
### 操作步骤
在目标LogStore的查询和分析页面，选择查询分析属性>关闭索引。
## 索引配置示例
### 示例1
日志内容中有request_time字段，执行字段查询语句request_time>100。
只建立全文索引，返回同时包含request_time、>（非分词符）、100这三个词的日志。
只建立double、long类型的字段索引，返回结果是request_time大于100的日志。
建立全文索引和double、long类型的字段索引，request_time的全文索引失效，返回结果是request_time大于100的日志。
### 示例2
日志内容中有request_time字段，执行全文查询语句request_time。
只建立double、long类型的字段索引，无法查询到相关日志。
只建立全文索引，从所有日志文本中查询包括request_time的日志。
只建立text类型的字段索引，从字段索引是text类型的字段中查询包括request_time的日志。
### 示例3
日志内容中有status字段，执行分析语句* | SELECT status, count(*) AS PV GROUP BY status。
只建立全文索引，无法查询到相关日志。
为status建立字段索引，返回结果是不同的状态码及对应的PV总数。
## 索引流量说明
### 全文索引
所有字段名和字段值都将作为text类型存储，即字段名和字段值都被计入索引流量。
### 字段索引
不同数据类型的字段的索引流量计算方式不同。
text类型：字段名和字段值都被计入索引流量中。
long类型和double类型：字段名不计入索引流量中，每个字段值所占的索引流量统一为8字节。
例如对status字段设置了索引（long类型），字段值为200，则字符串status不会被计入在索引流量中，200的索引流量统一为8字节。
JSON类型：字段名和字段值都被计入到索引流量中，包括未被创建索引的子节点。更多信息，请参见[如何计算](why-is-index-traffic-generated-for-json-subfields-that-are-not-indexed.md)[JSON](why-is-index-traffic-generated-for-json-subfields-that-are-not-indexed.md)[类型字段的索引流量](why-is-index-traffic-generated-for-json-subfields-that-are-not-indexed.md)。
如果未对子节点设置索引，则其索引流量按照text类型进行计算。
如果对子节点设置了索引，则其索引流量按照其子节点数据类型（text、long或double）进行计算。
## 计费说明
### 按写入数据量计费的LogStore
创建的索引会占用存储空间，存储类型请参见[管理智能存储分层](data-tiered-storage-overview.md)。
重建索引不产生费用。
索引流量计费请参见[按写入数据量计费模式计费项](billing-items-in-the-pay-per-data-write-mode.md)。
### 按使用功能计费的LogStore
创建的索引会占用存储空间，存储类型请参见[管理智能存储分层](data-tiered-storage-overview.md)。
创建索引会产生流量，索引流量计费请参见[按使用功能计费模式计费项](billable-items.md)中的索引流量-日志索引和索引流量-日志索引-查询型。降低索引流量的建议，请参见[如何降低索引流量费用？](how-do-i-reduce-index-traffic-fees.md)。
重建索引会产生费用。计费项、计费价格和创建索引相同。
## 后续步骤
查询和分析的示例，请参见：
[通过](copilot-automatic-generation-of-ai-assisted-sql-statements.md)[AI](copilot-automatic-generation-of-ai-assisted-sql-statements.md)[智能生成查询与分析语句（Copilot）](copilot-automatic-generation-of-ai-assisted-sql-statements.md)
[SLS Query Skill 智能查询分析日志](sls-query-skill-intelligent-log-query-and-analysis.md)
[查询与分析快速指引](quick-guide-to-query-and-analysis.md)
[查询和分析网站日志](query-and-analyze-website-logs.md)
[查询和分析](query-and-analyze-json-logs.md)[JSON](query-and-analyze-json-logs.md)[日志](query-and-analyze-json-logs.md)
[采集和查询分析](collect-and-analyze-nginx-monitoring-logs.md)[Nginx](collect-and-analyze-nginx-monitoring-logs.md)[监控日志](collect-and-analyze-nginx-monitoring-logs.md)
[分析负载均衡](analyze-layer-7-access-logs-of-slb.md)[7](analyze-layer-7-access-logs-of-slb.md)[层访问日志](analyze-layer-7-access-logs-of-slb.md)。
[查询轻量消息队列（原](query-mns-logs.md)[MNS）日志](query-mns-logs.md)
优化查询的方法，请参见[提高查询分析日志速度的方法](optimize-queries.md)。
查询和分析JSON类型的网站日志，请参见[查询和分析](query-and-analyze-json-logs.md)[JSON](query-and-analyze-json-logs.md)[日志](query-and-analyze-json-logs.md)。
## 常见问题
为什么导入日志后查询不到日志？
检查已设置的分词符是否符合要求。
索引配置只对新增日志生效，如果您要查询和分析历史数据，请使用重建索引功能。具体操作，请参见[重建索引](reindex-logs-for-a-logstore.md)。
如何完成双重条件查询？
需要使用两个条件查询日志时，只需同时输入两个语句即可。需要在LogStore中查询数据状态不是OK或者Unknown的日志。 直接搜索not OK not Unknown即可得到符合条件的日志。
如何查询包括包含多个关键字的日志？
以查询http_user_agent字段值中包含like Gecko的日志为例。
短语查询。http_user_agent:#"like Gecko"。[短语查询](phrase-search.md)
like语法。* | Select * where http_user_agent like '%like Gecko%'
如何在日志中搜索包含空格的关键字？
例如，当您搜索POS version时，会得到包含POS或者version的所有日志。如果使用双引号包裹，例如“POS version”，则会得到包含关键字POS version的所有日志。
[日志查询常见问题](user-guide/faq-about-log-query.md)
[查询与分析日志的常见报错](resolve-common-errors-that-may-occur-when-i-query-and-analyze-logs.md)
[如何模糊查询日志？](how-do-i-query-logs-by-using-fuzzy-match.md)
[查询和分析](faq-about-the-query-and-analysis-of-json-logs.md)[JSON](faq-about-the-query-and-analysis-of-json-logs.md)[日志的常见问题](faq-about-the-query-and-analysis-of-json-logs.md)
[如何将日志下载到本地](how-do-i-download-logs-to-a-local-device.md)
[为什么查询和分析时，字段值会被截断？](index-and-query-faq.md)
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
