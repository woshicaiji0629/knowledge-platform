### 分析语句
统计网站访问PV。
使用[count](aggregate-function.md)[函数](aggregate-function.md)统计网站访问PV。
* | SELECT count(*) AS PV
查询结果显示PV值为9685。
根据每分钟的时间粒度，统计网站访问PV。
使用[date_trunc](date-and-time-functions-1.md)[函数](date-and-time-functions-1.md)将时间对齐到每分钟并根据时间进行分组，然后使用[count](aggregate-function.md)[函数](aggregate-function.md)计算每分钟的访问PV并根据时间排序。
* | SELECT count(*) as PV, date_trunc('minute', __time__) as time GROUP BY time ORDER BY time
查询结果以折线图展示每分钟的PV趋势。
根据每5分钟的时间粒度，统计每个请求方法的请求次数。
使用__time__ - __time__ %300将时间对齐到5分钟并根据时间进行分组，然后使用[count](aggregate-function.md)[函数](aggregate-function.md)计算每5分钟的请求次数并根据时间进行排序。
* | SELECT request_method, count(*) as count, __time__ - __time__ %300 as time GROUP BY time, request_method ORDER BY time
执行该查询语句后，返回的示例结果为：GET 请求 778 次、PUT 请求 242 次、POST 请求 231 次、DELETE 请求 101 次、HEAD 请求 4 次，对应时间戳均为 1610673300。
环比上周的网站访问PV。
使用[count](aggregate-function.md)[函数](aggregate-function.md)计算总PV数，再使用[ts_compare](interval-valued-and-periodicity-valued-comparison-functions.md)[函数](interval-valued-and-periodicity-valued-comparison-functions.md)得出本周与上周的环比。其中，website_log为LogStore名称。
* | SELECT diff[1] as this_week, diff[2] as last_week, time FROM (SELECT ts_compare(pv, 604800) as diff, time
