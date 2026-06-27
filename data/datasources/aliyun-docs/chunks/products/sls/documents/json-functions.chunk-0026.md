### 示例
返回status字段中元素的数量。
字段样例
Results:[{"EndTime":1626314920,"FireResult":2,"RawResults":[{"_col0":"1094"}]}]
查询和分析语句
* | SELECT json_size(Results, '$.0.RawResults')
查询和分析结果为1。
