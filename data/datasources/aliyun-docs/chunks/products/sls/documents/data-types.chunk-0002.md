## text、long、double类型
日志样例
配置索引
查询和分析语句示例
查询请求时间大于60秒的日志：request_time > 60。
查询请求时间大于等于60秒，并且小于200秒的日志：request_time in [60 200)或者request_time >= 60 and request_time < 200。
查询请求状态码为200的日志：status = 200。
查询非GET请求的日志：not request_method : GET。
查询以cn开头的日志：cn*。
统计客户端分布情况：* | SELECT ip_to_province(client_ip) as province, count(*) AS pv GROUP BY province ORDER BY pv。
