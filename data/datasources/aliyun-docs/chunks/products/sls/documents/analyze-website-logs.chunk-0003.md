%i') as time, count(1) as PV group by time order by time limit 1000
配置x轴为time，y轴为PV，统计图表如下所示。
通过流图展示最近15分钟不同方法的请求次数随时间的变化趋势。
* | select date_format(from_unixtime(__time__ - __time__% 60), '%H:%i:%S') as minute, count(1) as c, request_method group by minute, request_method order by minute asc limit 100000
配置x轴为minute，y轴为c，聚合列为request_method，统计图表如下所示。
添加统计图表到仪表盘。
您可以单击添加到仪表盘，完成操作。具体操作，请参见[添加统计图表到仪表盘](add-a-chart-to-a-dashboard-1.md)。
该文章对您有帮助吗？
反馈
