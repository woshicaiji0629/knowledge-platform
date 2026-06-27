### 示例1
计算各个请求方法对应的请求数量，然后获取最小的请求数量。
查询和分析语句
* | SELECT min(PV) FROM ( SELECT count(1) as PV FROM log GROUP BY request_method )
查询和分析结果
