### 示例
示例1：计算Results字段值中JSON元素的数量。
字段样例
Results:[{"EndTime":1626314920},{"FireResult":2}]
查询和分析语句
* | SELECT json_array_length(Results)
查询和分析结果为2。
示例2：计算time字段值中JSON元素的数量。
字段样例
time:["time_local","request_time","upstream_response_time"]
查询和分析语句
* | SELECT json_array_length(time)
查询和分析结果为3。
