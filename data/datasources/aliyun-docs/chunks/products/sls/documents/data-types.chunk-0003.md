## JSON类型
日志样例
JSON日志样例如下所示，除日志服务保留字段外，还包括class字段、latency字段、status字段和info字段。其中info字段的值是JSON对象，并存在多层嵌套。
配置索引
相关说明如下：
IP字段和data字段的值为JSON数组，所以您无法为IP字段和data字段建立索引，也无法通过这两个字段进行查询和分析。
region字段和CreateTime字段在JSON数组中，所以您无法为region字段和CreateTime字段建立索引，也无法通过这两个字段进行查询和分析。
查询和分析语句示例
查询usedTime字段的值大于60秒的日志：info.usedTime > 60。
查询success字段的值为true的日志：info.success : true。
查询usedTime字段的值大于60秒且projectName的值不为project01的日志：info.usedTime > 60 not info.param.projectName : project01。
计算获取Project信息的平均时长：methodName = getProjectInfo | SELECT avg("info.usedTime") AS avg_time。
在配置索引时，请注意以下规则：
全文索引属性和键值索引属性必须至少启用一种。
字段索引配置会覆盖全文索引中同名字段的设置。例如，全文索引中已对某个字段进行分词检索，如果在键值索引中对该字段单独配置了类型和属性，则以键值索引中的配置为准。
索引类型为 long/double 时，大小写敏感和分词符属性无效。
目前只支持缩短索引保存时间。
索引配置修改（包括新增字段、修改类型、开启统计/查询开关等）后约 1 分钟生效，但仅对索引生效后写入的新数据可查询。如需查询历史数据，需对历史数据执行重建索引操作。具体操作请参见[重建索引](reindex-logs-for-a-logstore.md)。
重建索引仅支持最近 30 天且至少 15 分钟前的数据。
该文章对您有帮助吗？
反馈
