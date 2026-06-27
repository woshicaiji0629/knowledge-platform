### 示例
从JSON数组Results中提取double值。
字段样例
Results:[{"EndTime":1626314920},{"FireResult":2}]
查询和分析语句
* | SELECT json_extract_double(Results, '$.0.EndTime')
查询和分析结果
返回结果为1626314920.0。
