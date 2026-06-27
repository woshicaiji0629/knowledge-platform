### 功能计费模式下LogStore对比
查询型仅支持功能计费，因此按使用功能计费模式下，标准型和查询型两种类型的LogStore对比如下：

| 对比项 | 标准型（Standard 规格 ） | 查询型（Query 规格 ） |  |
| --- | --- | --- | --- |
| 费用 | [索引流量](billable-items.md) | 0.350 元 /GB | 0.1 元 /GB |
| 功能 | [数据采集](data-collection-overview.md) （仅业务系统日志场景） | 支持 | 不支持采集云产品日志。 |
| [开启智能存储分层](enable-hot-and-cold-tiered-storage-for-a-logstore.md) | 支持 | 支持 |  |
| [查询](log-search-overview.md) | 支持 | 支持 |  |
| [分析](log-analysis-overview.md) （SQL 语句） | 支持 | 不支持 |  |
| [上下文查询](contextual-query.md) | 支持 | 支持 |  |
| [LiveTail](livetail.md) | 支持 | 支持 |  |
| [日志聚类](logreduce.md) | 支持 | 不支持 |  |
| [重建索引](reindex-logs-for-a-logstore.md) | 支持 | 支持 |  |
| [仪表盘](dashboard.md) | 支持 | 不支持 |  |
| [告警](user-guide/the-alerting-feature-of-log-service.md) | 支持 | 仅支持基于查询语句的告警 |  |
| [定时](how-scheduled-sql-works.md) [SQL](how-scheduled-sql-works.md) | 支持 | 不支持 |  |
| [数据加工](data-transformation-overview.md) | 支持 | 支持 |  |
| [数据投递](data-shipping-overview.md) | 支持 | 支持 |  |
| [普通消费](overview-of-real-time-consumption.md) | 支持 | 支持 |  |
