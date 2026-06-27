### 日志服务SLS的日志丢失？
Project、LogStore丢失
如果主动删除LogStore、Project，日志无法恢复。您可以通过[操作审计](https://help.aliyun.com/zh/actiontrail/user-guide/query-events-in-the-actiontrail-console)功能查询最近90天的删除Project/LogStore事件。
没有采集到日志，参考[LoongCollector](loongcollector-collection-exception-troubleshooting.md)[采集异常问题汇总排查](loongcollector-collection-exception-troubleshooting.md)。
日志服务欠费：超过7天，将视为主动放弃服务，日志服务Project将被回收，数据会被清理且不可恢复。更多信息，请参见[欠费说明](overdue-payments.md)。
