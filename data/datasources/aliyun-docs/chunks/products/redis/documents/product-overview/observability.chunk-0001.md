：记录一次请求从接收到处理完成整个生命周期内的调用链路。
同时，云数据库 Tair（兼容 Redis）还基于三大数据支柱进行信息聚合，提供数据分析能力，下表为云数据库 Tair（兼容 Redis）与Redis的可观测性能力对比。为便于浏览和内容表达，表格约定使用下述注释：
✔️表示支持。
❌表示不支持。
➖表示不涉及。

| 可观测性能力 | Redis | 阿里云 Redis 开源版 | Tair（企业版） |  |
| --- | --- | --- | --- | --- |
| 指标 | [性能指标](../user-guide/view-monitoring-data.md) | ✔️ | ✔️（更细化） | ✔️（更细化） |
| 日志 | [运行日志](../user-guide/view-active-logs.md) | ✔️ | ✔️ | ✔️ |
| [慢日志](../user-guide/view-slow-logs.md) | ✔️ | ✔️ | ✔️ |  |
| [审计日志](../user-guide/view-audit-logs.md) | ❌ | ✔️ | ✔️ |  |
| [时延洞察](../user-guide/latency-insights.md) | ❌ | ✔️ | ✔️ |  |
| 链路追踪 | ➖ | ➖ | ➖ | ➖ |
| 分析能力 | [实时热](../user-guide/use-the-real-time-key-statistics-feature.md) [Key](../user-guide/use-the-real-time-key-statistics-feature.md) [分析](../user-guide/use-the-real-time-key-statistics-feature.md) | ❌ | ✔️ | ✔️ |
| [实时大](../user-guide/use-the-real-time-key-statistics-feature.md) [Key](../user-guide/use-the-real-time-key-statistics-feature.md) [分析](../user-guide/use-the-real-time-key-statistics-feature.md) | ❌ | ✔️ | ✔️ |  |
| [离线全量](../user-guide/offline-key-analysis.md) [Key](../user-guide/offline-key-analysis.md) [分析](../user-guide/offline-key-analysis.md) | ❌ | ✔️ | ✔️ |  |
| [实例诊断](../user-guide/create-a-diagnostic-report.md) | ❌ | ✔️ | ✔️ |  |
