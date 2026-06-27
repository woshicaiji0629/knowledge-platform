## 操作步骤
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在控制台左侧，选择仪表盘>仪表盘列表>中，单击${LogStore名称}_Apache访问日志。
apache_Apache访问日志仪表盘包括如下图表：
来源IP分布图展示访问IP地址的来源情况，所关联的查询分析语句如下所示：
* | select ip_to_province(remote_addr) as address, count(1) as c group by ip_to_province(remote_addr) limit 100
请求状态占比图展示最近一天各HTTP状态码的占比情况，所关联的查询分析语句如下所示：
* | select status, count(1) as pv group by status
请求方法占比图展示最近一天各请求方法的占比情况，所关联的查询分析语句如下所示：
* | select request_method, count(1) as pv group by request_method
访问PV/UV统计图展示最近一天内的PV数和UV数，所关联的查询分析语句如下所示：
* | select date_format(date_trunc('hour', __time__), '%m-%d %H:%i') as time, count(1) as pv, approx_distinct(remote_addr) as uv group by date_format(date_trunc('hour', __time__), '%m-%d %H:%i') order by time limit 1000
流入流出流量统计图展示流量的流入和流出情况，所关联的查询分析语句如下所示：
* | select date_format(date_trunc('hour', __time__), '%m-%d %H:%i') as time, sum(bytes_sent) as net_out, sum(bytes_received) as net_in group by time order by time limit 10000
请求UA占比图展示最近一天各种浏览器的占比情况，所关联的查询分析语句如下所示：
* | select case when http_user_agent like '%Chrome%' then 'Chrome' when http_user_agent like '%Firefox%' then 'Firefox' when http_user_agent like '%Safari%' then 'Safari' else 'unKno
