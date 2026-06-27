## 分析专线内流量占比
如图，某企业在阿里云某地域使用两个VPC部署不同业务，并通过高速通道物理专线+云企业网实现本地IDC接入阿里云。
现在IT部门准备使用流日志监控分析VPC中不同业务流量对物理专线资源的占用情况，为网络资源规划、改善网络性能提供指导。
创建流日志
创建2个流日志，集中投递到同1个logstore，每个流日志的关键配置如下：
资源实例分别选择专有网络VPC1和VPC2。
采样路径选择转发路由器（TR）。
投递配置选择投递至日志服务，2个流日志选择同1个logstore，并开启流日志分析报表功能。
其他选项保持默认。
分析流日志
查询分析语句
分析不同VPC流入本地IDC流量的占比情况：
action: ACCEPT and srcaddr: 192.168.* and dstaddr:10.1.* | WITH vpc1_traffic AS ( SELECT date_trunc('minute',__time__) AS minute, SUM(bytes*8/(case WHEN "end"-start=0 THEN 1 else "end"-start end)) AS total_vpc1_traffic FROM log WHERE srcaddr LIKE '192.168.20.%' GROUP BY date_trunc('minute',__time__) ), vpc2_traffic AS ( SELECT date_trunc('minute',__time__) AS minute, SUM(bytes*8/(case WHEN "end"-start=0 THEN 1 else "end"-start end)) AS total_vpc2_traffic FROM log WHERE srcaddr LIKE '192.168.10.%' GROUP BY date_trunc('minute',__time__) ) SELECT COALESCE(vpc1_traffic.minute, vpc2_traffic.minute) AS minute, (COALESCE(vpc1_traffic.total_vpc1_traffic, 0) * 100/ NULLIF((COALESCE(vpc1_traffic.total_vpc1_traffic, 0) + COALESCE(vpc2_traffic.total_vpc2_traffic, 0)), 0)) AS vpc1_percentage, (COALESCE(vpc2_traffic.total_vpc2_traffic, 0) * 100/ NULLIF((COALESCE(vpc1_traffic.total_vpc1_traffic
