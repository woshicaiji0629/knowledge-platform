## 适用场景

| 场景 | 说明 | 示例提示词 |
| --- | --- | --- |
| 日志检索 | 按关键字、字段、状态码、Trace ID、用户 ID 等条件查询日志明细。 | 查询最近 10 分钟 status>=500 的 NGINX 访问日志明细。 |
| SQL 统计分析 | 对日志进行聚合、分组、排序、Top-N、趋势分析或字段投影。 | 统计最近 1 小时 5xx 错误最多的接口 Top 10。 |
| 查询语句生成 | 将自然语言需求转换为 SLS 索引查询语句、SQL 语句或 SPL 语句。 | 生成按分钟统计平均延迟和 P95 延迟的查询语句。 |
| 查询优化 | 根据索引配置和字段类型优化现有查询，减少不必要的数据扫描。 | 优化现有查询语句，优先使用字段索引并减少不必要的数据扫描。 |

说明
日志服务也可通过[调用可观测](large-language-model-llm-application-calls-observable-mcp-service-to-implement-log-query-and-analysis.md)[MCP](large-language-model-llm-application-calls-observable-mcp-service-to-implement-log-query-and-analysis.md)[服务实现日志查询与分析](large-language-model-llm-application-calls-observable-mcp-service-to-implement-log-query-and-analysis.md)。
