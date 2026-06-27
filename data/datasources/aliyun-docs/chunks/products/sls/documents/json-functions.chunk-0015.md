### 示例
从JSON数组Results中提取boolean值。
字段样例
Results:[{"ret":true},{"status":FALSE}]
查询和分析语句
* | SELECT json_extract_bool(Results, '$.0.ret')
查询和分析结果
返回结果为true。
