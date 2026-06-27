unctions.md)得出本周与上周的环比。其中，website_log为LogStore名称。
* | SELECT diff[1] as this_week, diff[2] as last_week, time FROM (SELECT ts_compare(pv, 604800) as diff, time FROM (SELECT COUNT(*) as pv, date_trunc('week', __time__) as time FROM website_log GROUP BY time ORDER BY time) GROUP BY time)
统计客户端地址分布情况。
使用[ip_to_province](ip-functions.md)[函数](ip-functions.md)获取IP地址对应的省份并根据省份进行分组，然后再使用[count](aggregate-function.md)[函数](aggregate-function.md)计算每个地址出现的次数并根据次数进行排序。
* | SELECT count(*) as count, ip_to_province(client_ip) as address GROUP BY address ORDER BY count DESC
执行该语句的示例查询结果为：广东省 451 次、江苏省 447 次、北京市 433 次、山东省 425 次。
统计访问前10的请求路径。
根据请求路径进行分组，然后使用[count](aggregate-function.md)[函数](aggregate-function.md)计算每个路径的访问次数并根据访问次数排序。
* | SELECT count(*) as PV, request_uri as PATH GROUP BY PATH ORDER BY PV DESC LIMIT 10
执行该查询语句后，返回的示例结果展示了访问量排名前10的请求路径（PATH）及其对应的访问次数（PV）。
查询request_uri字段的值以%file-7结尾的日志。
重要
在查询语句中，模糊查询的通配符星号（*）和问号（?）只能出现在词的中间或末尾。如果您要查询以某字符结尾的字段，可以在分析语句中使用LIKE语法进行查询。
* | select * from website_log where request_uri like '%file-7'
其中，website_log为LogStore名称。
统计请求路径访问情况。
使用[regexp_extract](regular-expression-functions-1.md)[函数](regular-expression-functions-1.md)提取request_uri字段中的文件部分，然后再使
