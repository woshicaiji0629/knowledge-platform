# JSON函数-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/json-functions

# JSON函数
本文介绍JSON函数的基本语法及示例。
日志服务支持如下JSON函数。
重要
在日志服务分析语句中，表示字符串的字符必须使用单引号（''）包裹，无符号包裹或被双引号（""）包裹的字符表示字段名或列名。例如：'status'表示字符串status，status或"status"表示日志字段status。
如果日志字段的值为JSON类型且需要展开为多行，请使用unnest语法。更多信息，请参见[UNNEST](unnest-clause.md)[子句](unnest-clause.md)。
如果字符串被解析成JSON类型失败，则返回null。
如果在采集过程中，JSON日志被截断，则在使用JSON函数进行查询与分析时，系统将报错且中止查询与分析。针对该错误，您可以使用TRY表达式捕获异常信息，使得系统继续执行查询和分析操作。例如* | select message, try(json_parse(message))。更多信息，请参见[TRY](conditional-expressions.md)[表达式](conditional-expressions.md)。
| 函数名称 | 语法 | 说明 | 支持 SQL | 支持 SPL |
| --- | --- | --- | --- | --- |
| [json_array_contains](json-functions.md) [函数](json-functions.md) | json_array_contains( x , value ) | 判断 JSON 数组中是否包含某个值。 | √ | √ |
| [json_array_get](json-functions.md) [函数](json-functions.md) | json_array_get( x , index ) | 获取 JSON 数组中某个下标对应的元素。 | √ | × |
| [json_array_length](json-functions.md) [函数](json-functions.md) | json_array_length( x ) | 计算 JSON 数组中元素的数量。 | √ | √ |
| [json_extract](json-functions.md) [函数](json-functions.md) | json_extract( x , json_path) | 从 JSON 对象或 JSON 数组中提取一组 JSON 值（数组或对象）。 | √ | √ |
| [json_extract_scalar](json-functions.md) [函数](json-functions.md) | json_extract_scalar( x , json_path ) | 从 JSON 对象或 JSON 数组中提取一组标量值（字符串、整数或布尔值）。类似于 json_extract 函数。 | √ | √ |
| [json_extract_bool](json-functions.md) [函数](json-functions.md) | json_extract_bool(x, json_path) | 从 JSON 对象或 JSON 数组中提取 boolean 值。 | √ | × |
| [json_extract_long](json-functions.md) [函数](json-functions.md) | json_extract_long(x, json_path) | 从 JSON 对象或 JSON 数组中提取 bigint 值。 | √ | × |
| [json_extract_double](json-functions.md) [函数](json-functions.md) | json_extract_double(x, json_path) | 从 JSON 对象或 JSON 数组中提取 double 值。 | √ | × |
| [json_format](json-functions.md) [函数](json-functions.md) | json_format( x ) | 把 JSON 类型转换为字符串类型。 | √ | √ |
| [json_parse](json-functions.md) [函数](json-functions.md) | json_parse( x ) | 把字符串类型转换为 JSON 类型。 | √ | √ |
| [json_size](json-functions.md) [函数](json-functions.md) | json_size( x , json_path ) | 计算 JSON 对象或数组中元素的数量。 | √ | √ |
| [json_object_flatten](json-functions.md) [函数](json-functions.md) | json_object_flatten(x) | 将 JSON 对象压缩为单层键值结构。 | √ | × |
## json_array_contains函数
json_array_contains函数用于判断JSON数组中是否包含某个值。
### 语法
json_array_contains(x, value)
### 参数说明
| 参数 | 说明 |
| --- | --- |
| x | 参数值为 JSON 数组。 |
| value | 数值。 |
### 返回值类型
boolean类型。
### 示例
判断JSON数组[1, 2, 3]中是否包含2。
查询和分析语句（[调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DKiB8IFNFTEVDVCBqc29uX2FycmF5X2NvbnRhaW5zKCdbMSwgMiwgM10nLCAyKQ%3D%3D)）
* | SELECT json_array_contains('[1, 2, 3]', 2)
查询和分析结果为true，表示JSON数组[1, 2, 3]中包含2。
## json_array_get函数
json_array_get函数用于获取JSON数组下标对应的元素。
### 语法
json_array_get(x, index)
### 参数说明
| 参数 | 说明 |
| --- | --- |
| x | 参数值为 JSON 数组。 |
| index | JSON 下标，从 0 开始。 |
### 返回值类型
varchar类型。
### 示例
返回JSON数组["a", [3, 9], "c"]下标为1的元素。
查询和分析语句（[调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DKiB8IFNFTEVDVCBqc29uX2FycmF5X2dldCgnWyJhIiwgWzMsIDldLCAiYyJdJywgMSk%3D)）
* | SELECT json_array_get('["a", [3, 9], "c"]', 1)
查询和分析结果为[3,9]。
## json_array_length函数
json_array_length函数用于计算JSON数组中元素的数量。
### 语法
json_array_length(x)
### 参数说明
| 参数 | 说明 |
| --- | --- |
| x | 参数值为 JSON 数组。 |
### 返回值类型
bigint类型。
### 示例
示例1：计算Results字段值中JSON元素的数量。
字段样例
Results:[{"EndTime":1626314920},{"FireResult":2}]
查询和分析语句
* | SELECT json_array_length(Results)
查询和分析结果为2。
示例2：计算time字段值中JSON元素的数量。
字段样例
time:["time_local","request_time","upstream_response_time"]
查询和分析语句
* | SELECT json_array_length(time)
查询和分析结果为3。
## json_extract函数
json_extract函数用于从JSON对象或JSON数组中提取一组JSON值（数组或对象）。
重要
针对非法的JSON类型，json_extract函数会报错，建议您使用json_extract_scalar函数。
### 语法
json_extract(x, json_path)
### 参数说明
| 参数 | 说明 |
| --- | --- |
| x | 参数值为 JSON 对象或 JSON 数组。 |
| json_path | JSON 路径，格式为$.store.book[0].title。更多信息，请参见 [如何设置](faq-about-the-query-and-analysis-of-json-logs.md) [json_path](faq-about-the-query-and-analysis-of-json-logs.md) 。 |
### 返回值类型
JSON格式的string类型。
### 示例
SQL
获取Results字段中EndTime字段的值。
字段样例
Results:[{"EndTime":1626314920},{"FireResult":2}]
查询和分析语句
* | SELECT json_extract(Results, '$.0.EndTime')
查询和分析结果为1626314920。
SPL
获取Results字段中EndTime字段的值。
字段样例
Results:[{"EndTime":1626314920},{"FireResult":2}]
SPL语句
* | extend a = json_extract(Results, '$.0.EndTime')
SPL结果
返回结果中，字段a的值为1626314920。
## json_extract_scalar函数
json_extract_scalar函数用于从JSON对象或JSON数组中提取一组标量值（字符串、整数或布尔值）。
### 语法
json_extract_scalar(x, json_path)
### 参数说明
| 参数 | 说明 |
| --- | --- |
| x | 参数值为 JSON 对象或 JSON 数组。 |
| json_path | JSON 路径，格式为$.store.book[0].title。更多信息，请参见 [如何设置](faq-about-the-query-and-analysis-of-json-logs.md) [json_path](faq-about-the-query-and-analysis-of-json-logs.md) 。 |
### 返回值类型
varchar类型。
### 示例
SQL
从Results字段中获取RawResultCount字段的值，并将该值转换为bigint类型进行求和。
字段样例
Results:[{"EndTime":1626314920},{"RawResultCount":1}]
查询和分析语句
* | SELECT sum(cast(json_extract_scalar(Results,'$.1.RawResultCount') AS bigint) )
查询和分析结果为288。
SPL
从Results字段中获取RawResultCount字段的值。
字段样例
Results:[{"EndTime":1626314920},{"RawResultCount":1}]
SPL语句
* | extend a = json_extract_scalar(Results, '$.1.RawResultCount')
SPL结果中，字段a的值为1。
## json_extract_bool函数
json_extract_bool函数用于从JSON对象或JSON数组中提取boolean值，提取失败返回null。
### 语法
json_extract_bool(x, json_path)
### 参数说明
| 参数 | 说明 |
| --- | --- |
| x | 参数值为 JSON 类型。 |
| json_path | JSON 路径，格式为$.store.book[0].title。更多信息，请参见 [如何设置](faq-about-the-query-and-analysis-of-json-logs.md) [json_path](faq-about-the-query-and-analysis-of-json-logs.md) 。 |
### 返回值类型
boolean类型。
### 示例
从JSON数组Results中提取boolean值。
字段样例
Results:[{"ret":true},{"status":FALSE}]
查询和分析语句
* | SELECT json_extract_bool(Results, '$.0.ret')
查询和分析结果
返回结果为true。
## json_extract_long函数
json_extract_long函数用于从JSON对象或JSON数组中提取bigint值，提取失败返回null。
### 语法
json_extract_long(x, json_path)
### 参数说明
| 参数 | 说明 |
| --- | --- |
| x | 参数值为 JSON 类型。 |
| json_path | JSON 路径，格式为$.store.book[0].title。更多信息，请参见 [如何设置](faq-about-the-query-and-analysis-of-json-logs.md) [json_path](faq-about-the-query-and-analysis-of-json-logs.md) 。 |
### 返回值类型
bigint类型。
### 示例
从JSON数组Results中提取bigint值。
字段样例
Results:[{"EndTime":1626314920},{"FireResult":2}]
查询和分析语句
* | SELECT json_extract_long(Results, '$.0.EndTime')
查询和分析结果
返回结果为1626314920。
## json_extract_double函数
json_extract_double函数用于从JSON对象或JSON数组中提取double值，提取失败返回null。
### 语法
json_extract_double(x, json_path)
### 参数说明
| 参数 | 说明 |
| --- | --- |
| x | 参数值为 JSON 类型。 |
| json_path | JSON 路径，格式为$.store.book[0].title。更多信息，请参见 [如何设置](faq-about-the-query-and-analysis-of-json-logs.md) [json_path](faq-about-the-query-and-analysis-of-json-logs.md) 。 |
### 返回值类型
double类型。
### 示例
从JSON数组Results中提取double值。
字段样例
Results:[{"EndTime":1626314920},{"FireResult":2}]
查询和分析语句
* | SELECT json_extract_double(Results, '$.0.EndTime')
查询和分析结果
返回结果为1626314920.0。
## json_format函数
json_format函数用于将JSON类型转化成字符串类型。
### 语法
json_format(x)
### 参数说明
| 参数 | 说明 |
| --- | --- |
| x | 参数值为 JSON 类型。 |
### 返回值类型
varchar类型。
### 示例
将JSON数组[1,2,3]转换为字符串[1, 2, 3]。
查询和分析语句（[调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DKiB8IFNFTEVDVCBqc29uX2Zvcm1hdChqc29uX3BhcnNlKCdbMSwgMiwgM10nKSk%3D)）
* | SELECT json_format(json_parse('[1, 2, 3]'))
查询和分析结果为[1,2,3]。
## json_parse函数
json_parse函数只用于将字符串类型转化成JSON类型，判断是否符合JSON格式。一般情况下，json_parse函数使用意义不大，如果您需要从JSON中提取值，建议使用json_extract_scalar函数。
### 语法
json_parse(x)
### 参数说明
| 参数 | 说明 |
| --- | --- |
| x | 参数值为字符串。 |
### 返回值类型
JSON类型。
### 示例
SQL
示例1
将字符串[1,2,3]转换为JSON数组[1, 2, 3]。
查询和分析语句（[调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DICogfCBTRUxFQ1QganNvbl9wYXJzZSgnWzEsIDIsIDNdJyk%3D)）
* | SELECT json_parse('[1, 2, 3]')
查询和分析结果为[1,2,3]。
示例2
提取logging字段中的各个子字段。
字段样例如下，logging字段为JSON对象，包含message、processName、thread、threadName、module、funcName、levelName、process等键值对。
查询和分析语句（[调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/internal-etl-log?encode%3Dbase64%26queryString%3DKnwgU0VMRUNUIG1hcF9rZXlzKHRyeV9jYXN0KGpzb25fcGFyc2UobG9nZ2luZykgQVMgbWFwKHZhcmNoYXIsIGpzb24pKSk%3D)）
*| SELECT map_keys(try_cast(json_parse(logging) AS map(varchar, json)))
查询和分析结果为["funcName","levelname","message","module","process","processName","thread","threadName"]。
SPL
将字符串[1,2,3]转换为JSON数组[1, 2, 3]。
SPL语句
* | extend a = json_parse('[1, 2, 3]')
SPL结果
返回结果中，字段a的值为[1, 2, 3]。
## json_size函数
json_size函数用于计算JSON对象或JSON数组中元素的数量。
### 语法
json_size(x, json_path)
### 参数说明
| 参数 | 说明 |
| --- | --- |
| x | 参数值为 JSON 对象或 JSON 数组。 |
| json_path | JSON 路径，格式为$.store.book[0].title。更多信息，请参见 [如何设置](faq-about-the-query-and-analysis-of-json-logs.md) [json_path](faq-about-the-query-and-analysis-of-json-logs.md) 。 |
### 返回值类型
bigint类型。
### 示例
返回status字段中元素的数量。
字段样例
Results:[{"EndTime":1626314920,"FireResult":2,"RawResults":[{"_col0":"1094"}]}]
查询和分析语句
* | SELECT json_size(Results, '$.0.RawResults')
查询和分析结果为1。
## json_object_flatten函数
json_object_flatten函数用于将JSON 对象压缩为单层键值结构。
### 语法
json_object_flatten(x)
### 参数说明
| 参数 | 说明 |
| --- | --- |
| x | 参数值为 JSON 类型。如果 JSON 对象非 Object，则返回 null。 |
### 返回值类型
map(varchar, varchar)类型。
### 示例
将content字段JSON内容压缩为1层键值对。
字段样例
content: '{"Time":1626314920,"Info":[{"count":"1"}],"Body":"this is test"}'
查询和分析语句
select json_object_flatten(content) as data from (values '{"Time":1626314920,"Info":[{"count":"1"}],"Body":"this is test"}') t (content) limit 1;
输出数据
如下，data字段的值为{"Time":"1626314920","Info":"[{\"count\":\"1\"}]","Body":"this is test"}，即原始JSON对象已被压缩为单层键值结构。
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
