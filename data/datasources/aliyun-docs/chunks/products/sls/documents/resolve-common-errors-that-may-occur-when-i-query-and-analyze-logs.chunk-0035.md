## sql query must follow search query,please read syntax doc
报错原因
仅使用了分析语句。在日志服务中，分析语句必须与查询语句一起使用，格式为查询语句|分析语句。
解决方法
在分析语句前加上查询语句，例如* | SELECT status, count(*) AS PV GROUP BY status。更多信息，请参见[基础语法](log-analysis-overview.md)。
