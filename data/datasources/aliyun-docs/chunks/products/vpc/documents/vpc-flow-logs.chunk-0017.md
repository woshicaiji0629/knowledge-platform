2_traffic.total_vpc2_traffic, 0)), 0)) AS vpc1_percentage, (COALESCE(vpc2_traffic.total_vpc2_traffic, 0) * 100/ NULLIF((COALESCE(vpc1_traffic.total_vpc1_traffic, 0) + COALESCE(vpc2_traffic.total_vpc2_traffic, 0)), 0)) AS vpc2_percentage FROM vpc1_traffic FULL OUTER JOIN vpc2_traffic ON vpc1_traffic.minute = vpc2_traffic.minute ORDER BY minute
单击查看SQL语句详细说明。
过滤条件：
srcaddr：192.168.*，过滤源地址以192.168.*开头的日志。
dstaddr：10.1.*，过滤目的地址以10.1.*开头的日志。
action：ACCEPT，过滤action字段取值为ACCEPT的日志。
主查询
使用FULL OUTER JOIN将vpc1_traffic和vpc2_traffic的结果根据minute字段连接在一起。
计算每分钟内两个VPC流量的百分比：
vpc1_percentage表示VPC1的流量在总流量中的占比。
vpc2_percentage表示VPC2的流量在总流量中的占比。
查询结果按minute升序排序。
WITH子查询：
SQL语句中包含vpc1_traffic和vpc2_traffic两个子查询，以vpc1_traffic子查询为例进行说明：
使用date_trunc函数将Unix 时间戳（__time__字段）的精度降低为分钟，并命名为minute。
使用SUM函数得到某一分钟内总的流量速率，单位bit/s，并命名为total_vpc1_traffic。
过滤源地址为192.168.20.*（VPC1下的网段）的流量记录。
按照分钟进行分组。
效果预览
查询结果的可视化配置方式与场景二类似，选择面积图类型，展示不同 VPC 流量占比随时间的变化趋势。
在14:50-15:50这段时间内，VPC1流入本地IDC的流量占比较高。
