| 运算符 | 说明 |
| --- | --- |
| : | 用于字段查询（Key:Value），例如 request_method:GET 。 如果字段名称或者字段值内有空格、冒号（:）、连字符（-）等特殊字符，请使用双引号（""）包裹字段名称或者字段值，例如 "file info":apsara 。 |
| and | and 运算符。例如 request_method:GET and status:200 。 如果多个关键词之间没有语法关键词，默认为 and 关系，例如 GET 200 cn-shanghai 等同于 GET and 200 and cn-shanghai 。 |
| or | or 运算符。例如 request_method:GET or status:200 。 |
| not | not 运算符。例如 request_method:GET not status:200 、 not status:200 。 |
| ( ) | 用于提高括号内查询条件的优先级。例如 (request_method:GET or request_method:POST) and status:200 。 |
| "" | 使用 "" （双引号）包裹一个语法关键词，可以将该语法关键词转换成普通字符。在字段查询中 "" 内的所有词被当成一个整体。 当字段名或字段值中存在特殊字符（空格、中文、 : 、 - 等）、语法关键词（ and 、 or 等）等内容时，需要使用 "" 包裹。例如 "and" 表示查询包含 and 的日志，此处的 and 不代表运算符。 日志服务保留以下运算符的使用权，如果需要使用以下运算符作为查询关键字，请使用 "" 包裹： sort 、 asc 、 desc 、 group by 、 avg 、 sum 、 min 、 max 和 limit 。 通过数据加工或者 Logtail 插件处理的日志，其 tag 中的 key 会被转换成普通 key，即查询时需使用 "" 包裹字段名，例如 "__tag__:__client_ip__":192.0.2.1 ，此处的 __tag__:__client_ip__ 为日志服务保留字段，表示日志所在主机的 IP 地址。更多信息，请参见 [保留字段](reserved-fields.md) 。 |
| \ | 转义符号，用于转义 "" （双引号），转义后的双引号表示符号本身。例如日志内容为 instance_id:nginx"01" ，您可以使用 instance_id:nginx\"01\" 进行查询。 |
| * | 通配符查询，匹配零个、单个、多个字符。例如 host:www*com 。 说明 日志服务会在所有日志中为您查询到符合条件的 100 个词，返回包含这 100 个词并满足查询条件
