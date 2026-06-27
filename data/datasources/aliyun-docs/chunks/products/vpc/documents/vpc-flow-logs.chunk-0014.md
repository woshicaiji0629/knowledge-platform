分析流日志
查询分析语句
在ECS到NAT网关的这段路径上，分析去往特定公网IP地址的流量：
direction: 'in' and srcaddr: 10.0.0.* and dstaddr: 120.26.XX.XX | select -- 过滤ECS访问特定公网IP地址的日志 date_format(from_unixtime(__time__ - __time__% 60), '%H:%i:%S') as time, srcaddr, -- 将Unix时间戳转换为可读的时间格式 sum(bytes*8/60) as bandwidth -- 将字节转换为比特，并除以采集窗口时间1分钟 group by time,srcaddr -- 以时间、源ip分组 order by time asc -- 按时间升序 limit 100 -- 显示前100条结果
其他常用语句
在NAT网关到ECS的这段路径上，筛选某一特定公网IP到所有ECS实例的入流量信息：
direction: 'out' and dstaddr: 10.0.0.* and srcaddr: 120.26.XX.XX | select -- 过滤ECS访问特定公网IP地址的日志 date_format(from_unixtime(__time__ - __time__% 60), '%H:%i:%S') as time, -- 将Unix时间戳转换为可读的时间格式 dstaddr, sum(bytes*8/60) as bandwidth -- 将字节转换为比特，并除以采集窗口时间1分钟 group by time,dstaddr -- 以时间、目的ip分组 order by time asc -- 按时间升序 limit 100 -- 显示前100条结果
在ECS到NAT网关的这段路径上，筛选ECS实例去往所有公网IP的出流量信息：
direction: 'in' and srcaddr: 10.0.0.* | select -- 过滤ECS访问所有公网IP的日志 date_format(from_unixtime(__time__ - __time__% 60), '%H:%i:%S') as time, -- 将Unix时间戳转换为可读的时间格式 concat(srcaddr,'->', dstaddr), -- 拼接IP会话对，格式为“源ip->目的ip” sum(bytes*8/60) as bandwidth -- 将字节转换为比特，并除以采集窗口时间1分钟 group by time,srcaddr,dstaddr -- 以时间、源ip分组 order by time asc -- 按时间升序 limit 100 -- 显示前100条结果
效果预览
查询结果的可视化配置方式与场
