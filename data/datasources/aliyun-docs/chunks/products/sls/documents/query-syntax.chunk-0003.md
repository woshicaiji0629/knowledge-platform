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
