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
