e。
Tag值：audit_log。
是否丢弃该Tag字段：开启后上传的日志中不包含该Tag字段。
查询分析配置：
系统默认开启[全文索引](create-indexes.md)，支持对日志原始内容进行关键词搜索。
如需按字段进行精确查询，请在页面加载出预览数据后，单击自动生成索引，日志服务将根据预览数据中的第一条内容生成[创建索引](create-indexes.md)。
配置完成后，单击下一步，完成整个采集流程的设置。
完成配置并保存后，LoongCollector将根据日志中的action字段自动将日志分发到对应的日志库。
audit_log日志库中应只包含带有action字段的日志记录。
查询audit_log日志库的原始日志，可以看到日志记录均包含action字段，取值包括ACCESS_DENIED、DELETE、LOGIN等，验证分类存储结果符合预期。
service_log日志库中应只包含普通服务日志。
查询service_log日志库的原始日志，可以看到日志条目均为 INFO 级别的普通服务日志，例如Processed 200 requests in the last minute、Cache refreshed、Connected to database等，不包含错误日志或其他类型日志。
