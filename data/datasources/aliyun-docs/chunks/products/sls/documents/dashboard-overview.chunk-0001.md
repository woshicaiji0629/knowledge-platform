## 快速开始
下面我们以[CLB](../../slb/documents/classic-load-balancer/user-guide/clb-access-logs.md)[访问日志](../../slb/documents/classic-load-balancer/user-guide/clb-access-logs.md)为例创建一个仪表盘，用于监控不同请求方法的PV趋势，并使用过滤器查看指定方法的PV趋势。日志样例如下：
{ "body_bytes_sent": "1346", "client_ip": "118.*.*.125", "host": "www.*.*.com", "http_host": "www.*.*.com", "request_length": "15**", "request_method": "PUT", "request_time": "26", "scheme": "https", "slbid": "slb-02", "status": "200", "upstream_addr": "133.*.*.113", "upstream_response_time": "18", "upstream_status": "200", "vip_addr": "39.*.*.121", "__pack_meta__": "1|MTcyNDE*==|120|119", "__topic__": "slb_layer7", "__source__": "127.0.0.1", "__tag__:__receive_time__": "1725349464", "__tag__:__receive_time___0": "1725349464", "__time__": "1725349464" }
在日志服务创建一个仪表盘，只需要3步：
添加仪表盘：我们先在日志服务的控制台添加一个仪表盘，用于容纳多个相关的统计图表。
添加统计图表：然后我们在仪表盘中添加一个统计图表，可视化展示日志的查询分析结果。
添加筛选器：接着我们为统计图表设置筛选条件，根据查询分析语句的字段对统计图表进行筛选。
