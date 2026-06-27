## 配置示例
登录[日志服务控制台](https://sls.console.aliyun.com)。在Project列表区域，单击目标Project。
在左侧导航栏中，选择仪表盘>仪表盘列表。在仪表盘列表中，单击目标仪表盘。在目标仪表盘右上角，单击编辑。在仪表盘编辑模式下，单击添加>添加新图表。
在页面右侧配置图表类型、查询分析配置和图形配置，在页面左侧配置查询时间范围、LogStore、查询分析语句。然后单击页面上方的应用查看图表配置效果。
对于网络请求的数据进行汇总的查询分析语句为：
* | select COALESCE(client_ip, slbid, host) as source, COALESCE(host, slbid, client_ip) as dest, sum(request_length) as inflow group by grouping sets( (client_ip, slbid), (slbid, host))
其中，Logstore选择website_log，图表类型选择桑基图。查询分析配置中，起点列设为source，终点列设为dest，数值列设为inflow。图形配置中，连线颜色设为源节点，对齐方式设为居中对齐。
您还可以通过配置多条查询分析语句，可视化地表示多个节点之间的流向。配置slbid、client_ip和host节点之间的流向。
选择图表类型为桑基图，数据源为website_log。在查询分析配置中，查询 A 的起点列设为slbid、终点列设为client_ip、数值列设为inflow；查询 B 的起点列设为client_ip、终点列设为host、数值列设为inflow。
查询分析语句A：统计不同客户端通过不同负载均衡器的总请求流量。
* | select slbid,client_ip,sum(request_length) as inflow group by client_ip,slbid order by client_ip limit 10
查询分析语句B：统计客户端与主机的流量分布。
* | select client_ip,host,sum(request_length) as inflow group by host,client_ip order by client_ip limit 10
日志服务联合传统型负载均衡CLB推出7层访问日志功能，用于记录所有发送到CLB的请求的详细信息，包括请求时间、客户端IP地址、延迟、请求路径和服务器响应等。您可以通过7层访问日志绘制桑基图。更多信息请参见[开通访问日志功能](enable-the-access-log-management-feature.md)。
