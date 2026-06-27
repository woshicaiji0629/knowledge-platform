## 查询与分析日志
单击下一步，进入结束页面。单击查询日志，系统将自动跳转到目标LogStore的查询分析页面，编写SQL分析语句，从结构化日志中提取关键业务与运维指标。指定时间范围为最近15分钟：
说明
如果出现错误弹窗，原因是索引还未配置完成，关闭后等待1分钟，即可查看access.log文件中的日志内容。
示例1：网站总访问量（PV）
统计指定时间范围内的日志总条数。
* | SELECT count(*) AS pv
示例2：按分钟统计请求量与错误率
计算每分钟的总请求数、错误请求数（HTTP状态码≥400）以及错误率。
* | SELECT date_trunc('minute', __time__) as time, count(1) as total_requests, count_if(status >= 400) as error_requests, round(count_if(status >= 400) * 100.0 / count(1), 2) as error_rate GROUP BY time ORDER BY time DESC LIMIT 100
示例3：统计不同请求方法（GET, POST等）的PV
按分钟和请求方法（GET/POST等）对访问量进行分组统计。
* | SELECT date_format(minute, '%m-%d %H:%i') AS time, request_method, pv FROM ( SELECT date_trunc('minute', __time__) AS minute, request_method, count(*) AS pv FROM log GROUP BY minute, request_method ) ORDER BY minute ASC LIMIT 10000
