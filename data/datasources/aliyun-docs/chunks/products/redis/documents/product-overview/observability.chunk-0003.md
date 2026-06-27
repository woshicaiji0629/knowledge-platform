## 指标
Redis提供了丰富的统计指标，包含Memory（内存分配、内存使用、内存碎片率情况等）， Stats（连接数、命令、网络、同步状态等）、CPU使用情况、Keyspace信息等。云数据库 Tair（兼容 Redis）结合用户的使用体验，在Redis的基础上增加了更细化的指标，例如读QPS、写QPS等，更多信息请参见[查看性能指标](../user-guide/view-monitoring-data.md)。
与此同时，云数据库 Tair（兼容 Redis）的指标可观测性能力还具备如下优势：
[实时性能](../user-guide/view-performance-metrics-in-real-time.md)：实时展示指标信息。
[实例会话](../user-guide/instance-sessions.md)：实时展示Redis实例与客户端间的会话信息。
[性能趋势](../user-guide/performance-trends.md)：支持绘制任意时间跨度的曲线。
