。但是当您需要对JSON结构本身进行分析时，需要使用json_extract函数。例如您要统计一次请求中的订单数，即统计request.param.orders字段中JSON数组的长度，可使用如下查询分析语句。
* | SELECT json_array_length((json_extract(request, '$.param.orders')))
查询和分析结果如下所示。
重要
json_extract_scalar函数的返回值是varchar类型。例如您上述示例中的数值2，其数据类型也是varchar类型，如果您要对该值进行求和等计算，需要先使用cast函数，将其转换为bigint类型。更多信息，请参见[类型转换函数](data-type-conversion-functions.md)。
