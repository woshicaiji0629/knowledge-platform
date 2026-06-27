## 配置时间范围
您可通过以下三种方式设置日志查询 / 分析的时间范围。如果在分析语句中设置了时间范围，则查询分析结果以该时间范围为准。
在页面顶端的下拉列表中，选择时间范围例如15分钟。
在分析语句中通过__time__字段指定时间范围（闭合区间），例如：
* | SELECT * FROM log WHERE __time__>1731297600 AND __time__< 1731310038
在分析语句中指定时间时，使用[from_unixtime](date-and-time-functions-1.md)[函数](date-and-time-functions-1.md)或[to_unixtime](date-and-time-functions-1.md)[函数](date-and-time-functions-1.md)转换时间格式。例如：
- * | SELECT * FROM log WHERE from_unixtime(__time__) > from_unixtime(1731297600) AND from_unixtime(__time__) < now()
- * | SELECT * FROM log WHERE __time__ > to_unixtime(date_parse('2024-10-19 15:46:05', '%Y-%m-%d %H:%i:%s')) AND __time__ < to_unixtime(now())
说明
执行查询和分析语句后，默认只返回100行。如果您希望返回更多数据，可使用LIMIT语法。更多信息，请参见[LIMIT](limit-clause.md)[子句](limit-clause.md)。
