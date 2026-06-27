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
* | SELECT json_array_length((json_extract(request, '$
