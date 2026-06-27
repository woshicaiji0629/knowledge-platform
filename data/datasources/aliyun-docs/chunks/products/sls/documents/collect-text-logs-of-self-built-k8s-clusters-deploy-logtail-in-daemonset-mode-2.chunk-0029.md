### 内容过滤
通过配置processor_filter_regex_native插件，基于正则表达式匹配日志字段值，仅保留满足条件的日志。

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定值 processor_filter_regex_native 。 | # ...在 spec.config 下... processors: # 配置正则表达式过滤插件（可用于日志脱敏或敏感词过滤） - Type: processor_filter_regex_native # 定义正则表达式列表，用于匹配日志字段的内容 FilterRegex: # 示例：匹配日志字段值中包含 "WARNING" 或 "ERROR" 的内容 - WARNING|ERROR # 指定需要匹配的日志字段名，示例为对 level 字段进行过滤 FilterKey: - level |
| FilterRegex String （必选） 匹配日志字段的正则表达式。 |  |
| FilterKey String （必选） 匹配的日志字段名。 |  |
