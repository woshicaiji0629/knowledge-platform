ttp_user_agent like '%Chrome%' then 'Chrome' when http_user_agent like '%Firefox%' then 'Firefox' when http_user_agent like '%Safari%' then 'Safari' else 'unKnown' end as http_user_agent, count(1) as pv group by case when http_user_agent like '%Chrome%' then 'Chrome' when http_user_agent like '%Firefox%' then 'Firefox' when http_user_agent like '%Safari%' then 'Safari' else 'unKnown' end order by pv desc limit 10
前十访问来源图展示最近一天PV数最多的前十个访问来源页面，所关联的查询分析语句如下所示：
* | select http_referer, count(1) as pv group by http_referer order by pv desc limit 10
访问前十地址展示最近一天PV数最多的前十个访问地址，所关联的查询分析语句如下所示：
* | select split_part(request_uri,'?',1) as path, count(1) as pv group by split_part(request_uri,'?',1) order by pv desc limit 10
请求时间前十地址图展示最近一天请求响应延时最长的前十个地址，所关联的查询分析语句如下所示：
* | select request_uri as top_latency_request_uri, request_time_sec order by request_time_sec desc limit 10 10
该文章对您有帮助吗？
反馈
