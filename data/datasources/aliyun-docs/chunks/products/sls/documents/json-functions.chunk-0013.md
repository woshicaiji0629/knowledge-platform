### 示例
SQL
从Results字段中获取RawResultCount字段的值，并将该值转换为bigint类型进行求和。
字段样例
Results:[{"EndTime":1626314920},{"RawResultCount":1}]
查询和分析语句
* | SELECT sum(cast(json_extract_scalar(Results,'$.1.RawResultCount') AS bigint) )
查询和分析结果为288。
SPL
从Results字段中获取RawResultCount字段的值。
字段样例
Results:[{"EndTime":1626314920},{"RawResultCount":1}]
SPL语句
* | extend a = json_extract_scalar(Results, '$.1.RawResultCount')
SPL结果中，字段a的值为1。
