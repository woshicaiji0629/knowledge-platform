## 如何选择Store类型
日志服务提供日志库（LogStore），指标库（Metricstore），事件库（Eventstore）三种类型的Store，不同类型的Store主要区别在于对数据类型的兼容性上。请根据数据类型选择对应Store，如无特殊需要可默认使用LogStore。

| Store 类型 | 适用场景 |
| --- | --- |
| 日志库（LogStore） | [日志数据（Log）](manage-sls-store.md) ：系统运行过程中变化的一种抽象数据，其内容为指定对象的操作和其操作结果按时间的有序集合。广义上来说包含了几乎所有类型的数据，默认情况下可使用 LogStore。 [链路数据（Trace）](manage-sls-store.md) ：用于记录单次请求范围内的处理信息，其中包括服务调用和处理时长等数据。 |
| 时序库（MetricStore） | [时序数据（Metric）](manage-sls-store.md) ：由时序标识和数据点组成，相同时序标识的数据组成时间线。当数据需要时序存储时使用 MetricStore。 |
| 事件库（EventStore） | [事件数据（Event）](manage-sls-store.md) ：事件（Event）是指值得关注的、有价值的数据。例如监控告警数据、定期巡检作业的结果等。当数据需要事件存储时使用 EventStore。 |
