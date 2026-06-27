ring 的日志。字段值中存在空格。 | * | select * where errorContent like '%The body is not valid json string%' |
| 查询采集于 192.0.2.1 主机的日志。 | "__tag__:__client_ip__":192.0.2.1 |

- 在分析语句中
当字段名、表名等专有名词中存在特殊字符（空格、中文、:、-等）、语法关键词（and、or等）等内容时，需要使用""包裹。
表示字符串的字符必须使用''（单引号）包裹。无符号包裹或被""（双引号）包裹的字符表示字段名或列名。例如：'status'表示字符串status，status或"status"表示日志字段status。

| 查询需求 | 查询语句 |
| --- | --- |
| 查询包含 192.168.XX.XX 的日志。 | * | select * from log where key like '192.168.%.%' |
| 计算请求时长的前 10 名。 | 列名 top 10 中存在空格，需使用双引号（""）包裹。 * | SELECT max(request_time,10) AS "top 10" |
| 统计不同请求状态对应的日志数量。 | 此处 content 字段的索引为 JSON 类型。更多信息，请参见 [如何查询和分析有索引的](faq-about-the-query-and-analysis-of-json-logs.md) [JSON](faq-about-the-query-and-analysis-of-json-logs.md) [字段](faq-about-the-query-and-analysis-of-json-logs.md) 。 * | SELECT "content.status", COUNT(*) AS PV GROUP BY "content.status" |
