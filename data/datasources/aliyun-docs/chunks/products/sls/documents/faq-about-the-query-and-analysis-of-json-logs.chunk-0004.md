## 如何查询和分析有索引的JSON字段？
查询和分析语句格式为查询语句|分析语句。在分析语句中，您必须使用双引号（""）包裹字段名称，使用单引号（''）包裹字符串。您还需为目标字段加上所有的父路径，格式为Key1.Key2.Key3。例如request.clientIp、request.param.userId。更多信息，请参见[查询和分析](query-and-analyze-json-logs.md)[JSON](query-and-analyze-json-logs.md)[日志](query-and-analyze-json-logs.md)。
例如统计186499用户的客户端IP地址，可执行如下语句。
* and request.param.userId: 186499 | SELECT distinct("request.clientIp")
查询和分析结果如下所示。
