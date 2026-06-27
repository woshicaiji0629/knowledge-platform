## 操作步骤
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
输入查询和分析语句，然后单击最近15分钟，设置查询和分析的时间范围。
更多信息，请参见[步骤一：配置索引](quick-guide-to-query-and-analysis.md)。
通过表格展示最近1天客户端访问情况，并降序排列。
* | SELECT remote_addr, count(*) as count GROUP BY remote_addr ORDER BY count DESC
通过折线图展示最近15分钟PV、UV以及平均响应时间的变化情况。
* | select date_format(from_unixtime(__time__ - __time__% 60), '%H:%i:%S') as minutes, approx_distinct(remote_addr) as uv, count(1) as pv, avg(request_time) as avg group by minutes order by minutes asc limit 100000
在查询分析配置中，设置x轴字段为minutes，y轴字段为pv、uv和avg，统计图表如下所示。
通过柱状图展示最近15分钟不同来源地址的访问次数。
* | select referer, count(1) as count group by referer
通过条形图展示最近15分钟访问前十的页面。
* | select request_uri, count(1) as count group by request_uri order by count desc limit 10
通过饼图展示最近15分钟页面访问情况。
* | select request_uri as uri , count(1) as c group by uri limit 10
通过单值图展示最近15分钟的PV数。
* | select count(1) as PV
通过面积图展示最近1天某IP地址的访问情况。
remote_addr: 10.0.XX.XX | select date_format(date_trunc('hour', __time__), '%m-%d %H:%i') as time, count(1) as PV group by time order by time limit 1000
配置x轴为time，y轴为PV，统计图表如下所示。
通过流图展示最近15分钟不同方法的请求次数随时间的变化趋势。
* | select date_format(from_unixtim
