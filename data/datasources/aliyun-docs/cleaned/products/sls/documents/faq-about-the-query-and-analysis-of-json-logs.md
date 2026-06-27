# JSON日志索引查询与分析FAQ-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/faq-about-the-query-and-analysis-of-json-logs

# 查询和分析JSON日志的常见问题
本文介绍查询和分析JSON日志的常见问题。
## 日志样例
本文中介绍的各个案例是基于如下JSON格式的订单处理系统日志。
request字段为订单请求信息，JSON格式。一个请求中包含一个用户的多个订单，订单中包含购买的商品和支付总价。
response字段为订单处理结果。
请求成功时，response字段值为SUCCESS。
请求失败时，response字段值为JSON格式，包含errcode和msg信息。
您可以通过Logtail将该日志采集到日志服务中，进行查询与分析。具体操作，请参见[使用](collect-logs-in-json-mode.md)[JSON](collect-logs-in-json-mode.md)[模式采集日志](collect-logs-in-json-mode.md)。
## 如何设置索引？
索引是一种存储结构，用于对日志中的一列或多列进行排序。您只有设置索引后，才能进行查询和分析操作。在为JSON日志设置索引时，可能涉及如下方面的问题。
### 如何选择索引类型？
日志服务索引分为全文索引和字段索引，您可以参考如下说明，选择索引类型。更多信息，请参见[创建索引](create-indexes.md)。
如果您需要查询日志中的所有字段，建议创建全文索引；如果您明确仅查询部分字段，可针对目标字段建立字段索引，减少索引费用。
如果对字段有SQL分析需求，则必须对目标字段建立索引，并开启统计功能。
说明
如果您同时配置了全文索引和字段索引，则配置了字段索引的字段，以字段索引的配置为准。
例如您要统计分析request字段和response字段，则需要创建这两个字段的字段索引，并开启统计功能。
### 在索引配置中，如何选择字段的数据类型？
在设置索引时，字段的数据类型分为text、long、double和JSON。更多信息，请参见[数据类型](data-types.md)。
当您设置JSON字段的数据类型时，可参考如下思路。
如果字段值不是标准JSON格式，可能只是包含了JSON格式的内容，则设置为text类型；如果字段值是标准JSON格式，则设置为JSON类型。
说明
针对非完全合法的JSON日志，日志服务支持解析合法部分。
将某个字段设置为JSON类型后，如果对JSON对象中的某个叶子节点有进一步的分析需求，可以为叶子节点建立索引，这样可以加快叶子节点的查询和分析速度，但同时也会产生额外的索引费用。
日志服务支持JSON对象中的叶子节点建立索引，但不支持包含叶子节点的子节点建立索引。
日志服务不支持值为JSON数组的字段建立索引，也不支持为JSON数组中的字段建立索引。
例如基于本文的日志样例，您可以创建如下索引。
request字段
request字段为JSON格式，设置为JSON类型，并开启统计功能。
request.clientIp字段需要经常分析，建议单独建立索引，设置为text类型，并开启统计功能。
request.http.path字段很少需要分析，可不用单独建立索引。在需要分析时，直接通过JSON函数进行解析。
request.param字段为包含叶子节点的子节点，不支持建立索引。
request.param.userId字段需要经常分析，建议单独建立索引，设置为text类型，并开启统计功能。
request.param.orders字段值为JSON数组，不支持建立索引。
response字段
response字段不一定是JSON格式，因此设置为text类型，并开启统计功能。
创建索引后，新采集的日志将显示为如下格式。
### 如何设置别名？
JSON叶子节点的路径较长，您可以为其设置别名。更多信息，请参见[列的别名](column-aliases.md)。
说明
在设置索引时，不同字段的字段名或别名不能重复。
对于JSON类型的字段，JSON叶子节点的名称是按照全路径进行重名判定的。例如为response字段设置别名为clientIp，系统不会判定该别名与request.clientIp字段名重复。
## 如何查询和分析有索引的JSON字段？
查询和分析语句格式为查询语句|分析语句。在分析语句中，您必须使用双引号（""）包裹字段名称，使用单引号（''）包裹字符串。您还需为目标字段加上所有的父路径，格式为Key1.Key2.Key3。例如request.clientIp、request.param.userId。更多信息，请参见[查询和分析](query-and-analyze-json-logs.md)[JSON](query-and-analyze-json-logs.md)[日志](query-and-analyze-json-logs.md)。
例如统计186499用户的客户端IP地址，可执行如下语句。
* and request.param.userId: 186499 | SELECT distinct("request.clientIp")
查询和分析结果如下所示。
## 何时使用JSON函数？
首先，在查询和分析JSON日志时，如果数据量很大或结构复杂但相对固定，并且您对查询分析性能有要求时，建议对JSON叶子节点建立字段索引，然后再进行查询分析。如果数据量比较小，出于成本考虑，您可以不对JSON叶子节点建立字段索引，而是使用JSON函数进行查询和分析。使用JSON函数，可以灵活地对JSON日志进行动态处理和分析。另外，针对一些特殊情况，只能使用JSON函数进行查询与分析。
字段值不一定是JSON格式或者需要先进行一些预处理。
例如response字段，只有在请求失败时是JSON格式，并且包含errcode字段。那么您要分析errcode的分布情况，则需先使用查询语句过滤出请求失败的日志，然后在分析语句中使用JSON函数动态提取errcode字段值。
* not response :SUCCESS | SELECT json_extract_scalar(response, '$.errcode') AS errcode
查询和分析结果如下所示。
不支持建立索引的JSON节点，只能使用JSON函数实时分析。例如request.param字段和request.param.orders字段。
## 如何选择json_extract函数和json_extract_scalar函数？
json_extract函数和json_extract_scalar函数都是用于从JSON对象或JSON数组中提取内容，用法类似，主要区别如下：
json_extract函数的返回值是JSON类型，json_extract_scalar函数的返回值是varchar类型。
说明
此类型是指SQL语法中的数据类型，例如varchar、bigint、boolean、JSON、array、date等，与日志服务索引中的数据类型不同。您可以通过typeof函数查看SQL分析对象的数据类型。更多信息，请参见[typeof](data-type-conversion-functions.md)[函数](data-type-conversion-functions.md)。
json_extract函数可以解析JSON对象中任意一块子结构，json_extract_scalar函数只解析标量类型（字符串、布尔值或者整型值）的叶子节点，返回对应的字符串。
例如提取request字段中的clientIp字段，两个函数都支持。
使用json_extract函数进行提取。
* | SELECT json_extract(request, '$.clientIp')
查询和分析结果如下所示。
使用json_extract_scalar函数进行提取。
* | SELECT json_extract_scalar(request, '$.clientIp')
查询和分析结果如下所示。
在上述基础上，如果要提取clientIp字段值中的第一部分，您需要先使用json_extract_scalar函数提取clientIp的值，然后使用split_part函数提取IP地址中的第一个数字。此处不支持使用json_extract函数，因为split_part函数的入参需为varchar类型。
* | SELECT split_part( json_extract_scalar(request, '$.clientIp'), '.', 1 ) AS segment
查询和分析结果如下所示。
一般情况下，如果您需要从JSON对象中提取字段进行分析，直接使用json_extract_scalar函数即可。因为json_extract_scalar函数的返回值为varchar类型，便于与其他函数结合使用。但是当您需要对JSON结构本身进行分析时，需要使用json_extract函数。例如您要统计一次请求中的订单数，即统计request.param.orders字段中JSON数组的长度，可使用如下查询分析语句。
* | SELECT json_array_length((json_extract(request, '$.param.orders')))
查询和分析结果如下所示。
重要
json_extract_scalar函数的返回值是varchar类型。例如您上述示例中的数值2，其数据类型也是varchar类型，如果您要对该值进行求和等计算，需要先使用cast函数，将其转换为bigint类型。更多信息，请参见[类型转换函数](data-type-conversion-functions.md)。
## 如何设置json_path？
使用json_extract等函数从JSON日志中提取字段时，您需指定json_path，用于标明需要提取JSON对象中的哪一部分。json_path格式为$.a.b，美元符号（$）代表当前JSON对象的根节点，然后通过半角句号（.）引用到待提取的节点。
如果JSON对象的字段中存在特殊字符（例如http.path字段、http path字段、http-path字段等），则需要使用中括号[]代替半角句号（.），然后使用双引号（""）包裹字段名，例如* |SELECT json_extract_scalar(request, '$["http.path"]')。
说明
如果是通过SDK进行查询和分析，则需要对双引号（""）进行转义，例如* | select json_extract_scalar(request, '$[\"http.path\"]')。
提取JSON数组中的某个元素时，可以用中括号[]。在中括号中，通过数字来表示下标，下标从0开始。例如：
查看用户第一个订单的金额。
* | SELECT json_extract_scalar(request, '$.param.orders[0].payment')
查询和分析结果如下所示。
查看用户第一个订单中购买的第二件商品。
* | SELECT json_extract_scalar(request, '$.param.orders[0].commodity[1]')
查询和分析结果如下所示。
## 如何分析JSON数组？
当日志中有JSON数组时，您可以结合cast函数和UNNEST子句，展开JSON数组，再进行聚合统计。
### 示例1
例如您要统计所有请求成功的订单的金额，可参见如下思路。
使用查询语句过滤出请求成功的日志，然后在分析语句中使用json_extract函数提取出orders字段的值。
* and response: SUCCESS | SELECT json_extract(request, '$.param.orders')
查询和分析结果如下所示。
将上述提取的JSON数组（JSON类型）转换为array类型。
* and response: SUCCESS | SELECT cast( json_extract(request, '$.param.orders') AS array(json) )
查询和分析结果如下所示。
使用UNNEST子句将数组展开。
* and response: SUCCESS | SELECT orderinfo FROM log, unnest( cast( json_extract(request, '$.param.orders') AS array(json) ) ) AS t(orderinfo)
查询和分析结果如下所示。
使用json_extract_scalar提取payment字段值，再使用cast函数将其转换为bigint类型，最后进行求和计算。
* and response: SUCCESS | SELECT sum( cast( json_extract_scalar(orderinfo, '$.payment') AS bigint ) ) FROM log, unnest( cast( json_extract(request, '$.param.orders') AS array(json) ) ) AS t(orderinfo)
查询和分析结果如下所示。
### 示例2
统计所有成功的请求中，每一种商品被购买的数量。您可以先提取order字段，将其转换为array(json)类型，再使用UNNEST语句将其展开，展开结果中的每一行代表一个订单。然后使用json_extract函数提取commodity字段，将其转换为array(json)类型，再使用UNNEST语句将其展开，展开结果中的每一行代表一个商品。最后再进行分组求和。具体思路请参见示例1。
* and response: SUCCESS | SELECT item, count(1) AS cnt FROM ( SELECT orderinfo FROM log, unnest( cast( json_extract(request, '$.param.orders') AS array(json) ) ) AS t(orderinfo) ), unnest( cast( json_extract(orderinfo, '$.commodity') AS array(json) ) ) AS t(item) GROUP BY item ORDER BY cnt DESC
查询和分析结果如下所示。
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
