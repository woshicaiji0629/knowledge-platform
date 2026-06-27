request: { request_length:"73" request_method:"GE
重要
日志服务支持JSON对象中的叶子节点建立索引，但不支持包含叶子节点的子节点建立索引。
日志服务不支持值为JSON数组的字段建立索引，也不支持JSON数组中的字段建立索引。
如果字段的值为Boolean类型，则您可以在建立索引时，将字段的数据类型设置为text。
查询和分析语句格式为查询语句|分析语句。在分析语句中，您必须使用双引号（""）包裹字段名称，使用单引号（''）包裹字符串。
更多参考信息
关于查询和分析JSON日志的更多操作场景和常见问题，包括设置索引、查询和分析具有索引的JSON字段、使用JSON函数、分析JSON数组等，请参见[查询和分析](faq-about-the-query-and-analysis-of-json-logs.md)[JSON](faq-about-the-query-and-analysis-of-json-logs.md)[日志的常见问题](faq-about-the-query-and-analysis-of-json-logs.md)。
查询和分析JSON日志相关的基础配置和基本用法，请参见[查询和分析](query-and-analyze-json-logs.md)[JSON](query-and-analyze-json-logs.md)[日志](query-and-analyze-json-logs.md)。
在查询和分析JSON日志时，如果数据量比较小，您可以不对JSON叶子节点建立字段索引，而是使用JSON函数进行查询和分析。另外，针对一些特殊情况，只能使用JSON函数进行查询与分析。相关案例，请参见[何时使用](faq-about-the-query-and-analysis-of-json-logs.md)[JSON](faq-about-the-query-and-analysis-of-json-logs.md)[函数](faq-about-the-query-and-analysis-of-json-logs.md)。关于JSON函数的完整介绍和案例，请参见[JSON](json-functions.md)[函数](json-functions.md)。
