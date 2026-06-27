### 基于分词符的查询示例
日志服务会根据分词符，将日志内容拆分成多个词。日志服务默认配置的分词符为, '";=()[]{}?@&<>/:\n\t\r。如果设置分词符为空，则字段值将被当成一个整体，您只能通过完整字符串或模糊查询查找对应的日志。如何设置分词符，请参见[创建索引](create-indexes.md)。
例如http_user_agent字段值为Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/192.0.2.0 Safari/537.2。
设置分词符为空时，该字段值将被当成一个整体，则使用http_user_agent:Chrome查询语句进行查询时，无法查询到日志。
设置分词符为, '";=()[]{}?@&<>/:\n\t\r后，该字段值拆分为Mozilla、5.0、Windows、NT、6.1、AppleWebKit、537.2、KHTML、like、Gecko、Chrome、192.0.2.0、Safari、537.2。可以使用http_user_agent:Chrome等查询语句进行查询。
重要
当查询关键字中包含分词符时，您可以使用短语查询或者Like语法。例如：
短语查询：#"redo_index/1"。更多信息，请参见[短语查询](phrase-search.md)。
Like语法：* | select * from log where key like 'redo_index/1'。
