### 步骤三：确定匹配模式
根据掌握的关键词信息及实际业务场景的需要灵活控制使用精准查询还是模糊查询。

| 查询方式 | 说明 | 示例 |
| --- | --- | --- |
| 精确查询 | 使用完整的词进行查询。 日志服务查询采用的是分词法，精确查询时并不能完全匹配关键词。例如查询语句为 abc def ，查询结果将包含所有 abc 和 def 的日志，无法完全匹配目标短语。如果您要完全匹配短语 abc def ，可以使用短语查询或者 Like 语法。更多信息，请参见 [短语查询](phrase-search.md) 、 [如何精准查询日志](how-do-i-query-logs-by-using-exact-match.md) 。 | host:example.com 表示查询 host 字段值包含 example.com 的日志。 PUT and cn-shanghai 表示查询同时包含关键字 PUT 和 cn-shanghai 的日志。 * | Select * where http_user_agent like '%like Gecko%' 表示查询 http_user_agent 字段值中包含短语 like Gecko 的日志。 #"redo_index/1" 表示查询包含短语 redo_index/1 的日志。 |
| 模糊查询 | 在查询语句中指定一个 64 个字符以内的词，在词的中间或者末尾加上模糊查询关键字，即星号（*）或问号（?），日志服务会在所有日志中为您查询到符合条件的 100 个词，返回包含这 100 个词并满足查询条件的所有日志。指定的词越精确，查询结果越精确。 重要 星号（*）或问号（?）不能用在词的开头。 long 数据类型和 double 数据类型不支持使用星号（*）或问号（?）进行模糊查询。可以使用数值范围进行模糊查询，例如 status in [200 299]。 模糊查询是一种采样查询，查询机制如下所示： 开启字段索引，且指定某个字段进行查询时，日志服务从该字段的索引数据中随机采样，返回部分结果并不是全量扫描底层数据。 开启全文索引，且没有指定某个字段进行查询时，日志服务从全文索引数据中随机采样，返回部分结果并不是全量扫描底层数据。 | request_time>60 and request_method:Ge* 表示查询 request_time 字段值大于 60 且 request_method 字段值以 Ge 开头的日志。 addr* 表示在所有日志中查找以 addr 开头的 100 个词，并返回包含这些词的日志。 host:www.yl* 表示在所有日志中查找 host 字段值以 www.yl 开头的 100 个词，并返回包含这些词的日志。 更多信息，请参见 [如何模糊查询日志？](how-do-i-query-logs-by-using-fuzzy-match.md) 。 |
