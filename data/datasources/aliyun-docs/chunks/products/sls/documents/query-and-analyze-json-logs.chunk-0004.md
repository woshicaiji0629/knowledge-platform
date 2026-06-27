## 步骤三：查询和分析日志
您可以在LogStore的查询和分析页面，输入查询和分析语句，选择时间范围，进行日志查询操作。对于分析语句（SELECT语句），必须使用双引号（""）包裹字段名称，使用单引号（''）包裹字符串。查询和分析日志的详细步骤，请参见[查询与分析快速指引](quick-guide-to-query-and-analysis.md)。查询分析JSON日志的常见问题，请参见[查询和分析](faq-about-the-query-and-analysis-of-json-logs.md)[JSON](faq-about-the-query-and-analysis-of-json-logs.md)[日志的常见问题](faq-about-the-query-and-analysis-of-json-logs.md)。
查询请求状态为200的日志。
content.status:200
查询请求长度大于70的日志。
content.request.request_length > 70
查询GET请求的日志。
content.request.request_method:GET
统计不同请求状态对应的日志数量。
* | SELECT "content.status", COUNT(*) AS PV GROUP BY "content.status"
查询结果将以表格形式展示各请求状态码（如200、null）及其对应的页面访问量（PV）。
计算不同请求时长对应的请求数量，并按照请求时长进行升序排序。
* | SELECT "content.time.request_time", COUNT(*) AS count GROUP BY "content.time.request_time" ORDER BY "content.time.request_time"
计算不同请求方法对应的平均请求时长。
* | SELECT avg("content.time.request_time") AS avg_time,"content.request.request_method" GROUP BY "content.request.request_method"
查询结果显示，GET 请求方法的avg_time为 45，PUT 请求方法的avg_time为 11。
