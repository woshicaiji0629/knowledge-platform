# 查询语法介绍和相关示例-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/query-syntax

# 查询语法与功能
日志服务支持使用查询语句对日志进行筛选。筛选结果可独立使用，也可以用于分析语句，进行更复杂的分析处理。
## 前提条件
对日志进行查询，必须先[创建索引](create-indexes.md)。
## 基础语法
说明
[SLS Query Skill 智能查询分析日志](sls-query-skill-intelligent-log-query-and-analysis.md)：日志服务提供了Agent Skill，支持在本地 AI Agent 中通过自然语言查询和分析 SLS 日志数据。
[通过](copilot-automatic-generation-of-ai-assisted-sql-statements.md)[AI](copilot-automatic-generation-of-ai-assisted-sql-statements.md)[智能生成查询与分析语句（Copilot）](copilot-automatic-generation-of-ai-assisted-sql-statements.md)：日志服务也提供了AI智能辅助SQL语句的使用，支持自然语言生成SQL、解释复杂SQL、优化SQL语句。
查询语句与分析语句以|分割，格式为查询语句|分析语句，示例如下：
* | SELECT status, count(*) AS PV GROUP BY status
| 语句类型 | 说明 |
| --- | --- |
| 查询语句 | 查询条件，可以为关键词、数值、数值范围、空格、星号（*）等。 如果为空格或星号（*），表示无过滤条件。 重要 查询语句中建议不超过 30 个条件。 |
| 分析语句 | 重要 必须与查询语句一起使用，分析语句中无需填写 FROM 子句和 WHERE 子句，默认分析当前 LogStore 中的数据。分析语句不支持 offset，不区分大小写，末尾无需加分号。 对查询结果或全量数据进行计算和统计。日志服务支持的分析函数和语法： [SQL](sql-function.md) [函数](sql-function.md) [SQL](sql-syntax.md) [子句](sql-syntax.md) [机器学习函数](machine-learning-functions.md) |
## 查询语句编写思路
查询语句的编写流程可分为以下三步：
### 步骤一：确定查询方式
重要
不同的索引配置，会产生不同的查询和分析结果，如果同时创建了全文索引和字段索引，以字段索引的配置为准。
根据索引类型的不同，日志服务LogStore查询可分为全文查询和字段查询。全文查询和字段查询区别如下：
如果只创建全文索引，则只能使用全文查询。
如果已创建字段索引，则按以下规则查询：
double、long类型：只能根据字段查询语法进行查询。
text类型：若知晓关键词属于某个已创建索引的text类型字段，建议使用字段查询语法。如果不确定关键词的具体字段，请使用全文查询语法。
如果没有创建全文索引，全文查询语法仅在字段索引是text类型的字段中查询。
如果已创建全文索引，全文查询语法会从所有text类型索引中查询。
## 全文查询
不针对具体的字段进行查询，支持通配符（*、?）和逻辑运算符（如and、or等）。
查询语法keywords1 [ and | or | not ] keywords2 ...
示例
示例1
查询关键词为GET相关的日志。则查询语法：GET。
示例2
查询关键词为GET或POST相关的日志。则查询语法：GET or POST。
示例3
查询以Jo开头相关的日志，例如Joe、Jon等。则查询语法为：Jo？。
## 字段查询
针对具体字段名，支持类型化运算（如数值比较、正则表达式），需字段已建立索引。
重要
indexname1是需要查询的字段名，当字段名、表名等专有名词中存在特殊字符（空格、中文等）、语法关键词（and、or等）等内容时，则需要使用""（双引号）包裹。在查询中使用引号，请参见[如何在查询和分析语句中使用引号](how-do-i-use-quotation-marks-in-query-statements.md)。
字段索引涉及long、double类型，可以使用比较运算符>、>=、<、<=、=、in。
查询语法indexname1 [ : | > | >= | < | <= | = | in ] keyword1 [ [ and | or | not ] indexname2 ... ]
示例
示例1
查询request_method为GET相关的日志，则查询语法为：request_method: GET。
示例2
查询request_time_msec大于50相关的日志，则查询语法为request_time_msec>50（该字段索引类型为double）。
示例3
查询request_method为GET且request_time_msec大于50相关的日志。则查询语法为：request_method: GET and request_time_msec>50。
### 步骤二：确定字段类型
编写查询语句时需要考虑字段类型的特点，合理使用运算符，快速、精准地锁定目标日志。
字段类型
| 字段类型 | 说明 | 可用运算符 |
| --- | --- | --- |
| [text](data-types.md) [类型](data-types.md) | 字符串类型的字段。开启全文索引后，日志服务默认将整条日志（除 __time__ 以外所有字段）设置为 text 类型。 | and 、 or 、 not 、 () 、 : 、 "" 、 \ 、 * 、 ? 。 |
| [long](data-types.md) [和](data-types.md) [double](data-types.md) [类型](data-types.md) | 只有设置字段的数据类型为 long 或 double 后，才能通过数值范围查询该字段的值。 如果字段的数据类型不被设置为 double 、 long 或者查询时数值范围的语法错误，那么日志服务会按照全文查询方式进行查询，这样查询到的结果可能与期望的结果不同。 例如字段 owner_id 不是 double 、 long 类型，则执行查询语句 owner_id>100 时，会返回同时包含 owner_id 、 > （非分词符）、 100 这三个词的日志。 如果将字段的类型从 text 类型改成 double 、 long 类型，则只支持等号 = 查询。如果需要使用范围查询、大于号（>）、小于号（<）等运算符，必须 [重建索引](reindex-logs-for-a-logstore.md) 。 | and 、 or 、 not 、 () 、 > 、 >= 、 < 、 <= 、 = 、 in 。 |
| [JSON](data-types.md) [类型](data-types.md) | 针对 JSON 对象中的字段，可根据其值，将数据类型设置为 long 、 double 或 text ，并开启统计功能。 | 根据 JSON 对象中的字段的类型使用不同的运算符。 |
运算符
重要
in运算符只能小写，其他运算符不区分大小写。
日志服务保留以下运算符的使用权，如果您需要使用以下运算符作为查询关键字，请使用""（双引号）包裹：sort、asc、desc、group by、avg、sum、min、max和limit。
运算符的优先级由高到低排序如下所示：
冒号（:）
双引号（""）
圆括号（）
and、not
or
| 运算符 | 说明 |
| --- | --- |
| : | 用于字段查询（Key:Value），例如 request_method:GET 。 如果字段名称或者字段值内有空格、冒号（:）、连字符（-）等特殊字符，请使用双引号（""）包裹字段名称或者字段值，例如 "file info":apsara 。 |
| and | and 运算符。例如 request_method:GET and status:200 。 如果多个关键词之间没有语法关键词，默认为 and 关系，例如 GET 200 cn-shanghai 等同于 GET and 200 and cn-shanghai 。 |
| or | or 运算符。例如 request_method:GET or status:200 。 |
| not | not 运算符。例如 request_method:GET not status:200 、 not status:200 。 |
| ( ) | 用于提高括号内查询条件的优先级。例如 (request_method:GET or request_method:POST) and status:200 。 |
| "" | 使用 "" （双引号）包裹一个语法关键词，可以将该语法关键词转换成普通字符。在字段查询中 "" 内的所有词被当成一个整体。 当字段名或字段值中存在特殊字符（空格、中文、 : 、 - 等）、语法关键词（ and 、 or 等）等内容时，需要使用 "" 包裹。例如 "and" 表示查询包含 and 的日志，此处的 and 不代表运算符。 日志服务保留以下运算符的使用权，如果需要使用以下运算符作为查询关键字，请使用 "" 包裹： sort 、 asc 、 desc 、 group by 、 avg 、 sum 、 min 、 max 和 limit 。 通过数据加工或者 Logtail 插件处理的日志，其 tag 中的 key 会被转换成普通 key，即查询时需使用 "" 包裹字段名，例如 "__tag__:__client_ip__":192.0.2.1 ，此处的 __tag__:__client_ip__ 为日志服务保留字段，表示日志所在主机的 IP 地址。更多信息，请参见 [保留字段](reserved-fields.md) 。 |
| \ | 转义符号，用于转义 "" （双引号），转义后的双引号表示符号本身。例如日志内容为 instance_id:nginx"01" ，您可以使用 instance_id:nginx\"01\" 进行查询。 |
| * | 通配符查询，匹配零个、单个、多个字符。例如 host:www*com 。 说明 日志服务会在所有日志中为您查询到符合条件的 100 个词，返回包含这 100 个词并满足查询条件的所有日志。 |
| ? | 通配符查询，匹配单个字符。例如 host:aliyund?c 。 |
| > | 查询某字段值大于某数值的日志。例如 request_time>100 。 |
| >= | 查询某字段值大于或等于某数值的日志。例如 request_time>=100 。 |
| < | 查询某字段值小于某数值的日志。例如 request_time<100 。 |
| <= | 查询某字段值小于或等于某数值的日志。例如 request_time<=100 。 |
| = | 查询某字段值等于某数值的日志。针对 double、long 类型的字段， = 和 : 作用相同。例如 request_time=100 等同于 request_time:100 。 |
| in | 查询某字段值处于某数值范围内的日志，中括号表示闭区间，小括号表示开区间，两个数字之间使用空格分隔。例如 request_time in [100 200] 或 request_time in (100 200] 。 重要 in 只能为小写字母。 |
| __source__ | 查询某个日志源的日志，支持通配符。例如 __source__:192.0.2.* 。 重要 日志服务中的 __source__ 为保留字段，可缩写为 source 。如果您自定义的字段中存在 source 字段，则会与日志服务保留字段 source 冲突，此时您需要使用 Source 、 SOURCE 等词查询自定义的字段。 |
| __tag__ | 通过元数据信息查询日志。例如 __tag__:__receive_time__:1609837139 。 |
| __topic__ | 查询某日志主题下的日志。例如 __topic__:nginx_access_log 。 |
### 步骤三：确定匹配模式
根据掌握的关键词信息及实际业务场景的需要灵活控制使用精准查询还是模糊查询。
| 查询方式 | 说明 | 示例 |
| --- | --- | --- |
| 精确查询 | 使用完整的词进行查询。 日志服务查询采用的是分词法，精确查询时并不能完全匹配关键词。例如查询语句为 abc def ，查询结果将包含所有 abc 和 def 的日志，无法完全匹配目标短语。如果您要完全匹配短语 abc def ，可以使用短语查询或者 Like 语法。更多信息，请参见 [短语查询](phrase-search.md) 、 [如何精准查询日志](how-do-i-query-logs-by-using-exact-match.md) 。 | host:example.com 表示查询 host 字段值包含 example.com 的日志。 PUT and cn-shanghai 表示查询同时包含关键字 PUT 和 cn-shanghai 的日志。 * | Select * where http_user_agent like '%like Gecko%' 表示查询 http_user_agent 字段值中包含短语 like Gecko 的日志。 #"redo_index/1" 表示查询包含短语 redo_index/1 的日志。 |
| 模糊查询 | 在查询语句中指定一个 64 个字符以内的词，在词的中间或者末尾加上模糊查询关键字，即星号（*）或问号（?），日志服务会在所有日志中为您查询到符合条件的 100 个词，返回包含这 100 个词并满足查询条件的所有日志。指定的词越精确，查询结果越精确。 重要 星号（*）或问号（?）不能用在词的开头。 long 数据类型和 double 数据类型不支持使用星号（*）或问号（?）进行模糊查询。可以使用数值范围进行模糊查询，例如 status in [200 299]。 模糊查询是一种采样查询，查询机制如下所示： 开启字段索引，且指定某个字段进行查询时，日志服务从该字段的索引数据中随机采样，返回部分结果并不是全量扫描底层数据。 开启全文索引，且没有指定某个字段进行查询时，日志服务从全文索引数据中随机采样，返回部分结果并不是全量扫描底层数据。 | request_time>60 and request_method:Ge* 表示查询 request_time 字段值大于 60 且 request_method 字段值以 Ge 开头的日志。 addr* 表示在所有日志中查找以 addr 开头的 100 个词，并返回包含这些词的日志。 host:www.yl* 表示在所有日志中查找 host 字段值以 www.yl 开头的 100 个词，并返回包含这些词的日志。 更多信息，请参见 [如何模糊查询日志？](how-do-i-query-logs-by-using-fuzzy-match.md) 。 |
## 查询语句示例
同一条查询语句，针对不同的日志内容和索引配置时，会有不同的查询结果。本文基于如下日志样例和索引介绍查询语句示例。
## text、double、long类型
### 日志样例
本文以Nginx访问日志为例，介绍常见的查询语句。
### 索引配置
在查询日志前，请确保已[创建索引](create-indexes.md)。检查索引配置的步骤，如下所示：
在LogStore的查询/分析页面，选择查询分析属性>属性。
在打开的查询分析页面，查看是否已配置字段索引。
### 普通查询示例
| 查询需求 | 查询语句 | 调试 |
| --- | --- | --- |
| 查询 GET 请求成功（状态码为 200~299）的日志。 | request_method:GET and status in [200 299] | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/waf-demo-log/logsearch/waf-log?encode%3Dbase64%26queryString%3DcmVxdWVzdF9tZXRob2Q6R0VUIGFuZCBzdGF0dXMgaW4gWzIwMCAyOTld) |
| 查询来自非杭州地域的 GET 请求的日志。 | request_method:GET not region:cn-hangzhou | 无 |
| 查询 GET 请求或 POST 请求的日志。 | request_method:GET or request_method:POST | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DcmVxdWVzdF9tZXRob2Q6R0VUIG9yIHJlcXVlc3RfbWV0aG9kOlBPU1Q%3D) |
| 查询非 GET 请求的日志。 | not request_method:GET | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3Dbm90IHJlcXVlc3RfbWV0aG9kOkdFVA%3D%3D) |
| 查询 GET 请求或 POST 请求成功的日志。 | (request_method:GET or request_method:POST) and status in [200 299] | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DKHJlcXVlc3RfbWV0aG9kOkdFVCBvciByZXF1ZXN0X21ldGhvZDpQT1NUKSBub3Qgc3RhdHVzIGluIFsyMDAgMjk5XQ%3D%3D) |
| 查询 GET 请求或 POST 请求失败的日志。 | (request_method:GET or request_method:POST) not status in [200 299] | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DKHJlcXVlc3RfbWV0aG9kOkdFVCBvciByZXF1ZXN0X21ldGhvZDpQT1NUKSBub3Qgc3RhdHVzIGluIFsyMDAgMjk5XQ%3D%3D) |
| 查询 GET 请求成功（状态码为 200~299）且请求时间小于 60 秒的日志。 | request_method:GET and status in [200 299] not request_time>=60 | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DcmVxdWVzdF9tZXRob2Q6R0VUIGFuZCBzdGF0dXMgaW4gWzIwMCAyOTldIG5vdCByZXF1ZXN0X3RpbWU%2BPTYw) |
| 查询请求时间为 60 秒的日志。 | request_time:60 | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log%3FqueryString=request_time:60) |
| request_time=60 | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log%3FqueryString=request_time=60) |  |
| 查询请求时间大于等于 60 秒，并且小于 200 秒的日志。 | request_time>=60 and request_time<200 | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DcmVxdWVzdF90aW1lPj02MCBhbmQgcmVxdWVzdF90aW1lPDIwMA%3D%3D) |
| request_time in [60 200) | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DcmVxdWVzdF90aW1lIGluIFs2MCAyMDAp) |  |
| 查询 request_time 字段是否存在。 | request_time:* | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DcmVxdWVzdF90aW1lOiogbm90IHJlcXVlc3RfdGltZSA%2BIC0xMDAwMDAwMDAwMA%3D%3D%26queryTimeType%3D99) |
| 查询 request_time 字段值为空或非法数字的日志。 | (request_time:"") or (not request_time > -10000000000) | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DcmVxdWVzdF90aW1lOiogbm90IHJlcXVlc3RfdGltZSA%2BIC0xMDAwMDAwMDAwMA%3D%3D%26queryTimeType%3D99) |
| 查询包含 request_time 字段且字段值为数字的日志。 | request_time > -1000000000 | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DcmVxdWVzdF90aW1lID4gLTEwMDAwMDAwMDA%3D) |
| 查询包含 and 的日志。 | "and" 说明 此处的 and 为普通字符串，不代表运算符。 | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DImFuZCI%3D) |
| 查询 request method 字段值是 PUT 的日志。 | "request method":PUT 重要 字段名 request method 中存在空格，在查询时需使用双引号（""）包裹。 | 无 |
| 查询日志主题为 HTTPS 或 HTTP 的日志。 | __topic__:HTTPS or __topic__:HTTP | 无 |
| 查询采集于 192.0.2.1 主机的日志。 | __tag__:__client_ip__:192.0.2.1 此处的 __tag__:__client_ip__ 为日志服务保留字段，表示日志所在主机的 IP 地址。更多信息，请参见 [保留字段](reserved-fields.md) 。 重要 通过数据加工或者 Logtail 插件处理的日志，其 tag 中的 key 会被转换成普通 key，即查询时需使用双引号（""）包裹字段名，例如 "__tag__:__client_ip__":192.0.2.1 。 | 无 |
| 查询包含 192.168.XX.XX 的日志。 | * | select * from log where key like '192.168.%.%' 更多信息，请参见 [通过](how-do-i-query-logs-by-using-fuzzy-match.md) [SQL](how-do-i-query-logs-by-using-fuzzy-match.md) [的](how-do-i-query-logs-by-using-fuzzy-match.md) [like](how-do-i-query-logs-by-using-fuzzy-match.md) [语法进行精确的模糊查询](how-do-i-query-logs-by-using-fuzzy-match.md) 。 | 无 |
| 查询 remote_user 字段值不为空的日志。 | not remote_user:"" | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3Dbm90IHJlbW90ZV91c2VyOiIi) |
| 查询 remote_user 字段值为空的日志。 | remote_user:"" | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DcmVtb3RlX3VzZXI6IiI%3D) |
| 查询 remote_user 字段值不为 null 的日志。 | not remote_user:"null" | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3Dbm90IHJlbW90ZV91c2VyOiJudWxsIg%3D%3D) |
| 查询不存在 remote_user 字段的日志。 | not remote_user:* | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3Dbm90IHJlbW90ZV91c2VyOio%3D) |
| 查询存在 remote_user 字段的日志。 | remote_user:* | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DcmVtb3RlX3VzZXI6Kg%3D%3D) |
| 查询 城市 字段值不为 上海 的日志。 | not 城市:上海 说明 当查询中文字符串时，需要在配置索引时，打开 包含中文 开关。更多信息，请参见 [创建索引](create-indexes.md) 。 | 无 |
### 模糊查询示例
| 查询需求 | 查询语句 | 调试 |
| --- | --- | --- |
| 查询包含以 cn 开头的词的日志。 | cn* | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DY24q) |
| 查询 region 字段值是以 cn 开头的日志。 | region:cn* | 无 |
| 查询 region 字段值包含 cn* 的日志。 | region:"cn*" 说明 此处的 cn* 为一个独立词。例如： 如果日志内容为 region:cn*,en ，分词符为半角逗号（,），则该日志内容被拆分为 region 、 cn* 和 en ，您可以通过上述语句查询到该日志。 如果日志内容为 region:cn*hangzhou ，则 cn*hangzhou 为一个整体，您执行上述语句无法查询到该日志。 | 无 |
| 查询包含以 mozi 开头，以 la 结尾，中间还有一个字符的词的日志。 | mozi?la | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DbW96aT9sYQ%3D%3D) |
| 查询包含以 mo 开头，以 la 结尾，中间包含零个、单个或多个字符的词的日志。 | mo*la | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DbW8qbGE%3D%26queryTimeType%3D99) |
| 查询包含以 moz 开头的词和以 sa 开头的词的日志。 | moz* and sa* | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DbW96KiBhbmQgc2Eq) |
| 查询 region 字段值以 hai 结尾的所有日志。 | 目前使用查询语句无法查询到对应的日志，您可以使用 SQL 分析中的 Like 语法进行查询。更多信息，请参见 [通过](how-do-i-query-logs-by-using-fuzzy-match.md) [SQL](how-do-i-query-logs-by-using-fuzzy-match.md) [的](how-do-i-query-logs-by-using-fuzzy-match.md) [like](how-do-i-query-logs-by-using-fuzzy-match.md) [语法进行精确的模糊查询](how-do-i-query-logs-by-using-fuzzy-match.md) 。 *| select * from log where region like '%hai' | 无 |
| 查询 message 字段值以 "get_time: 0. 开头的所有日志。 | 使用 SQL 分析中的 [like](how-do-i-query-logs-by-using-fuzzy-match.md) 语法进行查询。 *| select message where message like '"get_time: 0.%' 或者使用 [SPL](spl-instructions-and-functions.md) [中的](spl-instructions-and-functions.md) [where](spl-instructions-and-functions.md) [指令](spl-instructions-and-functions.md) 进行过滤查询。 *| where message like '"get_time: 0.%' | 无 |
### 基于分词符的查询示例
日志服务会根据分词符，将日志内容拆分成多个词。日志服务默认配置的分词符为, '";=()[]{}?@&<>/:\n\t\r。如果设置分词符为空，则字段值将被当成一个整体，您只能通过完整字符串或模糊查询查找对应的日志。如何设置分词符，请参见[创建索引](create-indexes.md)。
例如http_user_agent字段值为Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/192.0.2.0 Safari/537.2。
设置分词符为空时，该字段值将被当成一个整体，则使用http_user_agent:Chrome查询语句进行查询时，无法查询到日志。
设置分词符为, '";=()[]{}?@&<>/:\n\t\r后，该字段值拆分为Mozilla、5.0、Windows、NT、6.1、AppleWebKit、537.2、KHTML、like、Gecko、Chrome、192.0.2.0、Safari、537.2。可以使用http_user_agent:Chrome等查询语句进行查询。
重要
当查询关键字中包含分词符时，您可以使用短语查询或者Like语法。例如：
短语查询：#"redo_index/1"。更多信息，请参见[短语查询](phrase-search.md)。
Like语法：* | select * from log where key like 'redo_index/1'。
| 查询需求 | 查询语句 | 调试 |
| --- | --- | --- |
| 查询 http_user_agent 字段值中包含 Chrome 的日志。 | http_user_agent:Chrome | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DaHR0cF91c2VyX2FnZW50OkNocm9tZQ%3D%3D) |
| 查询 http_user_agent 字段值中包含 Linux 和 Chrome 的日志。 | http_user_agent:Linux and http_user_agent:Chrome | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DaHR0cF91c2VyX2FnZW50OkxpbnV4IGFuZCBodHRwX3VzZXJfYWdlbnQ6Q2hyb21l) |
| http_user_agent:"Linux Chrome" | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DaHR0cF91c2VyX2FnZW50OiJMaW51eCBDaHJvbWUi) |  |
| 查询 http_user_agent 字段值中包含 Firefox 或 Chrome 的日志。 | http_user_agent:Firefox or http_user_agent:Chrome | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DaHR0cF91c2VyX2FnZW50OkZpcmVmb3ggb3IgaHR0cF91c2VyX2FnZW50OkNocm9tZQ%3D%3D) |
| 查询 request_uri 字段值包含 /request/path-2 的日志。 | request_uri:/request/path-2 | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DcmVxdWVzdF91cmk6L3JlcXVlc3QvcGF0aC0y) |
| 查询 request_uri 字段值以 /request 开头，但不包含 /file-0 的日志。 | request_uri:/request* not request_uri:/file-0 | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DcmVxdWVzdF91cmk6L3JlcXVlc3QqIG5vdCByZXF1ZXN0X3VyaTovZmlsZS0w) |
| 完全匹配包含短语 redo_index/1 的日志。 | #"redo_index/1" * | select * from log where key like 'redo_index/1' 说明 通过短语查询或者 Like 语法，可完全匹配目标短语。使用普通的精确查询，将匹配 redo_index 、 1 等词。 | 无 |
### 关键词转义示例
- 在查询语句中
使用""（双引号）包裹一个语法关键词，可以将该语法关键词转换成普通字符。在字段查询中""内的所有词被当成一个整体。
当字段名或字段值中存在特殊字符（空格、中文、:、-等）、语法关键词（and、or等）等内容时，需要使用""包裹。例如"and"表示查询包含and的日志，此处的and不代表运算符。
日志服务保留以下运算符的使用权，如果需要使用以下运算符作为查询关键字，请使用""包裹：sort、asc、desc、group by、avg、sum、min、max和limit。
通过数据加工或者Logtail插件处理的日志，其tag中的key会被转换成普通key，即查询时需使用""包裹字段名，例如"__tag__:__client_ip__":192.0.2.1，此处的__tag__:__client_ip__为日志服务保留字段，表示日志所在主机的IP地址。更多信息，请参见[保留字段](reserved-fields.md)。
| 查询需求 | 查询语句 |
| --- | --- |
| 查询 request method 字段值为 PUT 的日志。字段名 request method 中存在空格，需使用双引号（""）包裹。 | "request method":PUT |
| 查询 system error description 字段值中包含 DB 的日志。字段名 system error description 中存在空格。 | "system error description":DB* |
| 查询 region 字段值包含 cn* 的日志。这里的 cn* 为一个字符串。如果日志内容为 region:cn*,en ，分词符为半角逗号（,），则该日志内容被拆分为 region 、 cn* 和 en ，可通过右侧语句查询到该日志。 | region:"cn*" |
| 查询 remote_user 字段值为空的日志。 | remote_user:"" |
| 查询 Authorization 字段值为 Bearer 12345 的日志。字段值 Bearer 12345 中存在空格。 | "Authorization": "Bearer 12345" |
| 分析 errorContent 字段值包含 The body is not valid json string 的日志。字段值中存在空格。 | * | select * where errorContent like '%The body is not valid json string%' |
| 查询采集于 192.0.2.1 主机的日志。 | "__tag__:__client_ip__":192.0.2.1 |
- 在分析语句中
当字段名、表名等专有名词中存在特殊字符（空格、中文、:、-等）、语法关键词（and、or等）等内容时，需要使用""包裹。
表示字符串的字符必须使用''（单引号）包裹。无符号包裹或被""（双引号）包裹的字符表示字段名或列名。例如：'status'表示字符串status，status或"status"表示日志字段status。
| 查询需求 | 查询语句 |
| --- | --- |
| 查询包含 192.168.XX.XX 的日志。 | * | select * from log where key like '192.168.%.%' |
| 计算请求时长的前 10 名。 | 列名 top 10 中存在空格，需使用双引号（""）包裹。 * | SELECT max(request_time,10) AS "top 10" |
| 统计不同请求状态对应的日志数量。 | 此处 content 字段的索引为 JSON 类型。更多信息，请参见 [如何查询和分析有索引的](faq-about-the-query-and-analysis-of-json-logs.md) [JSON](faq-about-the-query-and-analysis-of-json-logs.md) [字段](faq-about-the-query-and-analysis-of-json-logs.md) 。 * | SELECT "content.status", COUNT(*) AS PV GROUP BY "content.status" |
## json类型
### 日志样例
{ "timestamp": "2025-03-21T14:35:18Z", "level": "ERROR", "service": { "name": "payment-processor", "version": "v2.8.1", "environment": "production" }, "error": { "code": 5031, "message": "Failed to connect to third-party API", "details": { "endpoint": "https://api.paymentgateway.com/v3/verify", "attempts": 3, "last_response": { "status_code": 504, "headers": { "Content-Type": "application/json", "X-RateLimit-Limit": "100" } } } }, "user": { "id": "usr-9a2b3c4d", "session": { "id": "sess-zxy987", "device": { "type": "mobile", "os": "Android 14", "network": "4G" } } }, "trace": { "correlation_id": "corr-6f5e4d3c", "span_id": "span-00a1b2" } }
### 索引配置
在查询日志前，请确保已[创建索引](create-indexes.md)。检查索引配置的步骤，如下所示：
在LogStore的查询/分析页面，选择查询分析属性>属性。
在打开的查询分析页面，查看是否已配置字段索引。
### 示例
| 查询需求 | 查询语句 |
| --- | --- |
| 查询请求错误的日志。 | level:error |
| 查询用户 ID 为 usr-9a2b3c4d 的所有请求。 | user.id:usr-9a2b3c4d |
| 查询用户 ID 为 usr-9a2b3c4d ，并且查看错误状态。 | user.id:usr-9a2b3c4d and error.details.last_response.status_code :504 |
## 常见问题
### 无法找到想要的日志
[查询不到日志的排查思路](user-guide/what-do-i-do-if-no-results-are-returned-when-i-query-a-log.md)。
### JSON日志问题
[查询和分析](faq-about-the-query-and-analysis-of-json-logs.md)[JSON](faq-about-the-query-and-analysis-of-json-logs.md)[日志的常见问题](faq-about-the-query-and-analysis-of-json-logs.md)
### 查询错误排查
[日志查询常见问题](user-guide/faq-about-log-query.md)
[查询与分析日志的常见报错](resolve-common-errors-that-may-occur-when-i-query-and-analyze-logs.md)
## 相关文档
分析函数和语法，请参见[分析函数和语法](log-analysis-overview.md)。
[优化查询的方法](optimize-queries.md)
日志查询示例
[如何精确的按照时间排序查询日志](how-to-precisely-sort-query-logs-by-time.md)
[查询和分析网站日志](query-and-analyze-website-logs.md)
[分析负载均衡](analyze-layer-7-access-logs-of-slb.md)[7](analyze-layer-7-access-logs-of-slb.md)[层访问日志](analyze-layer-7-access-logs-of-slb.md)
查询JSON日志（字段值为JSON对象、JSON数组）的查询和分析的示例，请参见[查询和分析](query-and-analyze-json-logs.md)[JSON](query-and-analyze-json-logs.md)[日志](query-and-analyze-json-logs.md)。
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
