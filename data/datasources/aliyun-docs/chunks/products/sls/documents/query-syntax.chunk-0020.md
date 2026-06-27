### 关键词转义示例
- 在查询语句中
使用""（双引号）包裹一个语法关键词，可以将该语法关键词转换成普通字符。在字段查询中""内的所有词被当成一个整体。
当字段名或字段值中存在特殊字符（空格、中文、:、-等）、语法关键词（and、or等）等内容时，需要使用""包裹。例如"and"表示查询包含and的日志，此处的and不代表运算符。
日志服务保留以下运算符的使用权，如果需要使用以下运算符作为查询关键字，请使用""包裹：sort、asc、desc、group by、avg、sum、min、max和limit。
通过数据加工或者Logtail插件处理的日志，其tag中的key会被转换成普通key，即查询时需使用""包裹字段名，例如"__tag__:__client_ip__":192.0.2.1，此处的__tag__:__client_ip__为日志服务保留字段，表示日志所在主机的IP地址。更多信息，请参见[保留字段](reserved-fields.md)。

| 查询需求 | 查询语句 |
| --- | --- |
| 查询 request method 字段值为 PUT 的日志。字段名 request method 中存在空格，需使用双引号（""）包裹。 | "request method":PUT |
| 查询 system error description 字段值中包含 DB 的日志。字段名 system error description 中存在空格。 | "system error description":DB* |
| 查询 region 字段值包含 cn* 的日志。这里的 cn* 为一个字符串。如果日志内容为 region:cn*,en ，分词符为半角逗号（,），则该日志内容被拆分为 region 、 cn* 和 en ，可通过右侧语句查询到该日志。 | region:"cn*" |
| 查询 remote_user 字段值为空的日志。 | remote_user:"" |
| 查询 Authorization 字段值为 Bearer 12345 的日志。字段值 Bearer 12345 中存在空格。 | "Authorization": "Bearer 12345" |
| 分析 errorContent 字段值包含 The body is not valid json string 的日志。字段值中存在空格。 | * | select * where errorContent like '%The body is not valid json string%' |
| 查询采集于 192.0.2.1 主机的日志。 | "__tag__:__client_ip__":192.0.2.1 |
