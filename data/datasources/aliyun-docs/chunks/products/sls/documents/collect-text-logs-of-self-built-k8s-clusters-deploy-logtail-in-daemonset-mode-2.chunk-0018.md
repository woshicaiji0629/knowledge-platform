## 正则解析
通过正则表达式提取日志字段，并将日志解析为键值对形式。

| 关键字段 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定为 processor_parse_regex_native 。 | # ...在 spec.config 下... processors: # 使用正则表达式解析插件解析日志内容 - Type: processor_parse_regex_native # 指定原始日志字段来源，通常为 content SourceKey: content # 正则表达式用于匹配并提取日志字段 Regex: >- (\S+)\s-\s(\S+)\s$$([^]]+)$$\s" (\w+)\s(\S+)\s([^"]+)" \s(\d+)\s(\d+)\s" ([^"]+)"\s" ([^"]+).* # 提取字段列表，按正则分组顺序对应 Keys: - remote_addr - remote_user - time_local - request_method - request_uri - request_protocol - status - body_bytes_sent - http_referer - http_user_agent # 解析失败时是否保留原始字段 KeepingSourceWhenParseFail: true # 解析成功时是否保留原始字段 KeepingSourceWhenParseSucceed: true # 如果保留原始字段，可以指定重命名后的字段名 RenamedSourceKey: fail |
| SourceKey String （必选） 源字段名。 |  |
| Regex String （必选） 匹配日志的正则表达式。 |  |
| Keys String （必选） 提取的字段列表。 |  |
| KeepingSourceWhenParseFail boolean （可选） 解析失败时，是否保留源字段，默认为 false 。 |  |
| KeepingSourceWhenParseSucceed boolean （可选） 解析成功时，是否保留源字段，默认为 false 。 |  |
| RenamedSourceKey String （可选） 保留源字段时，用于存储源字段的字段名，默认不改名。 |  |
