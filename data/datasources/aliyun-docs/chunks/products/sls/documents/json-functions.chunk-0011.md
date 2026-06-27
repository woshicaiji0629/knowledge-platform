### 示例
SQL
获取Results字段中EndTime字段的值。
字段样例
Results:[{"EndTime":1626314920},{"FireResult":2}]
查询和分析语句
* | SELECT json_extract(Results, '$.0.EndTime')
查询和分析结果为1626314920。
SPL
获取Results字段中EndTime字段的值。
字段样例
Results:[{"EndTime":1626314920},{"FireResult":2}]
SPL语句
* | extend a = json_extract(Results, '$.0.EndTime')
SPL结果
返回结果中，字段a的值为1626314920。
