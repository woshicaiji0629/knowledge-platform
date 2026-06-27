| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，Nginx 日志解析的插件类型为 processor_parse_regex_native 。 | # ...在 spec.config 下... processors: # NGINX 日志解析插件配置 - Type: processor_parse_regex_native # 原始日志字段来源 SourceKey: content # 正则表达式解析规则 Regex: >- (\S*)\s*-\s*(\S*)\s*\[ (\d+/\S+/\d+:\d+:\d+:\d+)\s+\S+\] \s*"(\S+)\s+(\S+)\s+\S+" \s*(\S*)\s*(\S*)\s*(\S*)\s*(\S*) \s*"([^"]*)"\s*"([^"]*)".* # 提取字段映射 Keys: - remote_addr - remote_user - time_local - request_method - request_uri - request_time - request_length - status - body_bytes_sent - http_referer - http_user_agent # NGINX 特定配置 Extra: Format: >- log_format main '$remote_addr - $remote_user [$time_local] "$request" ''$request_time $request_length ''$status $body_bytes_sent "$http_referer" ''"$http_user_agent"'; LogType: NGINX |
| SourceKey String （必选） 源字段名。 |  |
| Regex integer （必选） 正则表达式。 |  |
| Keys String （必选） 提取的字段列表。 |  |
| Extra Format String （必选） Nginx 配置文件中的日志配置部分，以 log_format 开头。 生产环境中，此处的 log_format 必须与 Nginx 配置文件（通常位于 /etc/nginx/nginx.conf 文件中）中的定义保持一致。 LogType String （必选） 解析日志类型，固定值为 NGINX 。 |  |
| KeepingSourceWhenParseFail boolean （可选） 解析失败时是否保留原始字段，默认为 false 。 |  |
| KeepingSourceWhenParseSucceed boolean （可选） 解析成功时是否保留原始字段
