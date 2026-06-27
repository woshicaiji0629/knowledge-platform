### 示例3
日志内容中有status字段，执行分析语句* | SELECT status, count(*) AS PV GROUP BY status。
只建立全文索引，无法查询到相关日志。
为status建立字段索引，返回结果是不同的状态码及对应的PV总数。
