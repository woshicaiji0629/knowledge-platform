分钟统计一次请求总数。
*| select avg(handled) * count(distinct(_address_)) as total_handled, avg(requests) * count(distinct(address)) as total_requests, from_unixtime( __time__ - __time__ % 300) as time group by __time__ - __time__ % 300 order by time limit 1440
每5分钟统计一次平均请求延迟。
*| select avg(_response_time_ms_) as avg_delay, from_unixtime( __time__ - __time__ % 300) as time group by __time__ - __time__ % 300 order by time limit 1440
统计请求成功的数量和失败的数量。
not _http_response_code_ : 200 | select count(1)_http_response_code_ : 200 | select count(1)
该文章对您有帮助吗？
反馈
