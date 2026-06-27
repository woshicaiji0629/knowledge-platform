## 如何在查询时判断日志的来源机器
Logtail采集配置应用于机器组，如果机器组类型为[IP](create-an-ip-address-based-machine-group.md)[地址机器组](create-an-ip-address-based-machine-group.md)，则可以使用内网IP对机器进行区分。
[创建索引](create-indexes.md)后，日志服务默认为__tag__:__hostname__创建索引，查询时输入__tag__:__hostname__:XXX。__tag__字段的设置和说明，请参见[保留字段](reserved-fields.md)。例如，执行以下语句，统计日志中不同hostname出现的次数。
* | select '__tag__:__hostname__' , count(1) as count group by '__tag__:__hostname__'
