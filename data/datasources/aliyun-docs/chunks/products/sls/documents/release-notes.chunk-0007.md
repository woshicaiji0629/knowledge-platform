## 2025年03月

| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 高性能完全精确查询与分析（SQL 独享版） | SQL 独享版是 日志服务 提供的计费资源，用于 SQL 分析。当您对大规模（百亿到千亿级）数据有分析需求时，可使用 SQL 独享版。 | [开服地域](sls-supported-regions1.md) | [高性能完全精确查询与分析（SQL](dedicated-sql.md) [独享版）](dedicated-sql.md) |
| Project 回收站 | 日志服务支持 Project 回收站功能，开启回收站功能的 Project，在用户执行删除操作后，对应 Project 数据临时放入回收站空间，回收站里的 Project 不可读写，但可以重新恢复。恢复范围包括 Project 下的所有数据及相关配置（ LogStore 实例及对应的 LogStore 配置、仪表盘、数据加工作业、告警等），同时需要保持与应用之间的数据关联。 | [全部地域](sls-supported-regions1.md) | [管理](manage-project-recycle-bin.md) [Project](manage-project-recycle-bin.md) [回收站](manage-project-recycle-bin.md) |
| 采集配置生成器 | 若您计划通过 CRD-AliyunPipelineConfig 或 API 接口来配置 Logtail 采集任务，利用采集配置生成器来自动构建所需的 CRD 定义和 API 参数脚本。该工具可帮您快速完成配置，减少手动操作。 | [全部地域](sls-supported-regions1.md) | [采集配置生成器](collection-configuration-generator.md) |
