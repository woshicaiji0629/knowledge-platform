d access | action=ACCESS_DENIED 2025-10-28 11:22:26 INFO User test deleted a record | action=DELETE 2025-10-28 11:22:26 INFO Cache refreshed 2025-10-28 11:22:29 INFO Processed 200 requests in the last minute
处理模式：选择SPL。
SPL语句：输入如下SPL语句
* | parse-regexp content, '^(\d+-\d+-\d+\s\d+:\d+:\d+)\s+(\w+)\s+(.*?)\s*(?:\|\s*action=(\w+))?$' as time, level, message, action | project-away content | extend "__tag__:type" = case when action = '' then 'service_log' else 'audit_log' end
SPL语句说明：
通过正则表达式提取出日志中的字段，包括time，level，message，action，并移除content字段。
新增一个Tag字段为type，当action字段不为空时，tag值为audit_log，否则tag值为service_log。
说明
Tag命名说明：在SPL中创建或引用Tag时，字段名必须以__tag__:为前缀，如__tag__:type。但在后续的路由规则配置中，仅需填写Tag名称type。
输出配置：单击展开输出配置，添加两个输出目标。
配置输出目标1：存储普通日志，type标签值为service_log的日志。
日志库：选择用于存储普通日志的日志库（如service_log日志库）。
压缩方式：支持lz4和zstd，默认为lz4。
路由配置：
Tag名称：Tag名称填写时直接使用字段名，无需添加__tag__:前缀。此处设置tag名为type。
Tag值：配置为service_log。
是否丢弃该Tag字段：开启后上传的日志中不包含该Tag字段。
配置输出目标2：存储审计日志，type标签值为audit_log的日志。
日志库：选择用于存储审计日志的日志库（如audit_log日志库）。
压缩方式：支持lz4和zstd，默认为lz4。
路由配置：
Tag名称：type。
Tag值：audit_log。
是否丢弃该Tag字段：开启后上传的日志中不包含该Tag字段。
查询分析配置：
系统默认开启[全文索引](create-indexes.md)，支持对日志原始内容进行关键词搜索。
如需按字段进行精确查询，请在页面加载出预览数据后，单击自动生成索引，日志服务将根据预览数据中的第一条内容
