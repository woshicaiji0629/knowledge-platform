## 阅读引导
日志服务提供查询和分析日志功能。具体操作，请参见[查询与分析快速指引](quick-guide-to-query-and-analysis.md)。
如果您要查询与分析日志，则必须将日志采集到Standard LogStore中，参考[管理](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。[创建索引](create-indexes.md)后，查询与分析只针对增量日志生效。当您需要对[历史日志文件](import-historical-logs.md)查询分析，需要[重建索引](reindex-logs-for-a-logstore.md)。
如果您需要查询百亿级的日志数据量，您可以参见[控制台提示“查询结果不精确”，如何解决？](what-are-the-reasons-for-inaccurate-queries.md)。
日志服务默认存在保留字段。如果您要分析保留字段，请参见[保留字段](reserved-fields.md)。
