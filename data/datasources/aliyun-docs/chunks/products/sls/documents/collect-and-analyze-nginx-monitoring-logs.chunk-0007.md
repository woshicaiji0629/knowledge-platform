## 步骤三：查询和分析日志
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
输入查询和分析语句，然后单击最近15分钟，设置查询和分析的时间范围。
更多信息，请参见[步骤一：配置索引](quick-guide-to-query-and-analysis.md)。
查询日志
查询某IP地址的相关信息。
_address_: 10.10.0.0
查询响应时间超过100毫秒的请求。
_response_time_ms_ > 100
查询状态码不为200的请求。
not _http_response_code_ : 200
分析日志
每5分钟统计一次waiting、reading、writing、connection的平均值。
*| select avg(waiting) as waiting, avg(reading) as reading, avg(writing) as writing, avg(connection) as connection, from_unixtime( __time__ - __time__ % 300) as time group by __time__ - __time__ % 300 order by time limit 1440
统计最大等待连接数排名前十的服务器。
*| select max(waiting) as max_waiting, _address_, from_unixtime(max(__time__)) as time group by address order by max_waiting desc limit 10
统计IP地址数量。
* | select count(distinct(_address_)) as total
统计请求失败的IP地址数量。
not _result_ : success | select count(distinct(_address_))
统计最近十次请求失败的IP地址。
not _result_ : success | select _address_ as address, from_unixtime(__time__) as time order by __time__ desc limit 10
每5分钟统计一次请求总数。
*| select avg(handled) * count(distinct(_address_)) as total_handled, avg(requests) * count(distinct(address)) as total_requests, from_unixtime( __t
