## 常见问题
为什么导入日志后查询不到日志？
检查已设置的分词符是否符合要求。
索引配置只对新增日志生效，如果您要查询和分析历史数据，请使用重建索引功能。具体操作，请参见[重建索引](reindex-logs-for-a-logstore.md)。
如何完成双重条件查询？
需要使用两个条件查询日志时，只需同时输入两个语句即可。需要在LogStore中查询数据状态不是OK或者Unknown的日志。 直接搜索not OK not Unknown即可得到符合条件的日志。
如何查询包括包含多个关键字的日志？
以查询http_user_agent字段值中包含like Gecko的日志为例。
短语查询。http_user_agent:#"like Gecko"。[短语查询](phrase-search.md)
like语法。* | Select * where http_user_agent like '%like Gecko%'
如何在日志中搜索包含空格的关键字？
例如，当您搜索POS version时，会得到包含POS或者version的所有日志。如果使用双引号包裹，例如“POS version”，则会得到包含关键字POS version的所有日志。
[日志查询常见问题](user-guide/faq-about-log-query.md)
[查询与分析日志的常见报错](resolve-common-errors-that-may-occur-when-i-query-and-analyze-logs.md)
[如何模糊查询日志？](how-do-i-query-logs-by-using-fuzzy-match.md)
[查询和分析](faq-about-the-query-and-analysis-of-json-logs.md)[JSON](faq-about-the-query-and-analysis-of-json-logs.md)[日志的常见问题](faq-about-the-query-and-analysis-of-json-logs.md)
[如何将日志下载到本地](how-do-i-download-logs-to-a-local-device.md)
[为什么查询和分析时，字段值会被截断？](index-and-query-faq.md)
该文章对您有帮助吗？
反馈
