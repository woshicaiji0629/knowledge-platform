## 何时使用JSON函数？
首先，在查询和分析JSON日志时，如果数据量很大或结构复杂但相对固定，并且您对查询分析性能有要求时，建议对JSON叶子节点建立字段索引，然后再进行查询分析。如果数据量比较小，出于成本考虑，您可以不对JSON叶子节点建立字段索引，而是使用JSON函数进行查询和分析。使用JSON函数，可以灵活地对JSON日志进行动态处理和分析。另外，针对一些特殊情况，只能使用JSON函数进行查询与分析。
字段值不一定是JSON格式或者需要先进行一些预处理。
例如response字段，只有在请求失败时是JSON格式，并且包含errcode字段。那么您要分析errcode的分布情况，则需先使用查询语句过滤出请求失败的日志，然后在分析语句中使用JSON函数动态提取errcode字段值。
* not response :SUCCESS | SELECT json_extract_scalar(response, '$.errcode') AS errcode
查询和分析结果如下所示。
不支持建立索引的JSON节点，只能使用JSON函数实时分析。例如request.param字段和request.param.orders字段。
