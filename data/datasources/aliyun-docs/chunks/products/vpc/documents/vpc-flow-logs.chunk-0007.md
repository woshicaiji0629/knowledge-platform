### 控制台
自定义分析：通过Logstore日志库
前往专有网络控制台[流日志页面](https://vpc.console.aliyun.com/flowlog/cn-hangzhou/flowlogs)，在目标流日志的日志服务列单击Logstore的实例名称，进入Logstore的详情页面。在此页面可以：
查看原始日志获取流日志条目明细。
输入语句[查询分析流日志](../../sls/documents/quick-guide-to-query-and-analysis.md)。
Logstore 查询界面提供原始日志、统计图表和日志聚类三个标签页，支持设置查询时间范围。上方展示日志量的时序分布图，下方展示包含 srcaddr、dstaddr、protocol 等字段的查询结果表格。
通过预设模板分析：Flowlog日志中心
Flowlog日志中心预设了一组可视化模板，支持VPC的策略统计、弹性网卡流量统计以及网段间流量统计，帮助您快速分析VPC流日志。
前往[Flowlog](https://sls.console.aliyun.com/lognext/app/flowlog)[日志中心](https://sls.console.aliyun.com/lognext/app/flowlog)页面，在右上方单击添加。
在创建实例面板中，填入实例名称、已有流日志对应的Project和Logstore，单击确定。
实例创建成功后，单击Flowlog日志中心列表的实例ID。在Flowlog详情页面，可以查看并分析流日志的信息。
监控中心提供以下仪表盘和自定义查询功能：
概览：展示流日志的Accept和Reject趋势、进出流量趋势、每个VPC的总数据包数和总字节数、每个ENI的总数据包数和总字节数、来源IP和目标IP的地理分布。
策略统计：展示Accept趋势、Reject趋势、Accept次数统计（由五元组构成）、Reject次数统计（由五元组构成）等信息。五元组是由源IP、源端口、协议类型、目标IP和目标端口组成的集合。
Accept：安全组和网络ACL允许记录的流量。
Reject：安全组和网络ACL拒绝记录的流量。
ENI流量：展示弹性网卡入方向和出方向的流量信息。
ECS间流量：展示ECS实例之间的流量情况。
自定义查询：可以自行[查询与分析快速指引](../../sls/documents/quick-guide-to-query-and-analysis.md)。
开启域间分析（可选）：在Flowlog详情页面，单击网段设置，在网段设置页签，打开开启“域间分析”开关。
开启域间分析功能后，系统将自动创建数据加工任务，生成具有网段信息的VPC流日志，用于分析不同网段之间的流量情况。数据加工功能会[收取一定的费用](../../sls/docu
