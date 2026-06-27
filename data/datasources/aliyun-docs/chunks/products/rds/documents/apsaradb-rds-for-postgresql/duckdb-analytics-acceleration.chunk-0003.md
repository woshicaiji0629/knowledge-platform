## 开启方式
在正式使用分析加速能力前，请先完成实例配置。RDS PostgreSQL提供以下两种方式，您可以根据业务负载特征进行选择：

| 开启方式 | 资源模式 | 推荐场景 | 操作文档 |
| --- | --- | --- | --- |
| 主实例开启分析加速 | PostgreSQL 与 DuckDB 共享主实例资源，部署简单、成本较低。 | TP 负载较轻或允许 AP 查询占用部分主实例资源的业务，希望快速验证加速效果。 | [主实例开启](enable-duckdb-for-the-master-instance.md) [AP](enable-duckdb-for-the-master-instance.md) [加速](enable-duckdb-for-the-master-instance.md) |
| DuckDB 分析实例 | 独立部署 DuckDB 分析实例，与主实例进行数据同步，AP 与 TP 负载在物理资源上完全隔离。 | 对在线业务延迟敏感的核心业务，需要保障 TP 稳定性，同时承载大规模 AP 分析查询。 | [DuckDB](add-a-duckdb-read-only-instance.md) [分析实例](add-a-duckdb-read-only-instance.md) |

说明
如果您不确定如何选择，建议优先采用DuckDB分析实例方式，将分析负载与在线事务隔离，避免AP查询影响核心业务的性能与稳定性。
