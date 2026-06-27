| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定值为 processor_parse_regex_native 。 | # ...在 spec.config 下... processors: # 配置 Apache Combined 日志解析插件（基于正则表达式） - Type: processor_parse_regex_native # 原始日志字段来源，通常为 content SourceKey: content # 正则表达式用于匹配并提取 Apache combined 格式日志 Regex: >- ([0-9.-]+)\s # remote_addr ([\w.-]+)\s # remote_ident ([\w.-]+)\s # remote_user (\[[^\[\]]+\]|-)\s # time_local "((?:[^"]|\")+)"\s # request_method + request_uri + request_protocol "((?:[^"]|\")+)"\s # request_uri（重复捕获？需注意逻辑） "((?:[^"]|\")+)"\s # request_protocol (\d{3}|-)\s # status (\d+|-)\s # response_size_bytes "((?:[^"]|\")+)"\s # http_referer "((?:[^"]|\"|')+)" # http_user_agent # 提取字段列表，按正则分组顺序对应 Keys: - remote_addr - remote_ident - remote_user - time_local - request_method - request_uri - request_protocol - status - response_size_bytes - http_referer - http_user_agent # 插件附加信息（非必须，用于说明日志格式） Extra: Format: >- LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined LogType: Apache SubType: combined |
| SourceKey String （必选） 源字段名。 |  |
| Regex integer （必选） 正则表达式。 |  |
| Keys String （必选） 提取的字段列表。 |  |
| Extra Format String （必选） Apache 配置文件中的日志配置部分，通常以 LogFormat 开头。 Lo
