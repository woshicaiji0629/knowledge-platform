ine 是否可访问。 load checkpoint error ：加载检查点失败，如无影响可忽略此错误。 container... ：指定容器存在非法 Label 值，目前仅允许配置 stdout 和 stderr。请结合详细错误进行检查。 |
| DOCKER_STDOUT_START_ALARM | service_docker_stdout 插件采集时，stdout 大小超过限制。 | 一般因为首次采集时 stdout 已存在，可忽略。 |
| DOCKER_STDOUT_STAT_ALARM | service_docker_stdout 插件无法检测到 stdout。 | 一般因为容器退出时无法访问到 stdout，可忽略。 |
| FILE_READER_EXCEED_ALARM | 同时打开的文件对象数量超过限制。 | 一般因为当前处于采集状态的文件数过多，请检查采集配置是否合理。 |
| GEOIP_ALARM | processor_geoip 插件错误。 | 查看详细报错，报错根据内容分为如下类型。 invalid ip... ：获取 IP 地址失败，请检查配置中的 SourceKey 是否正确或是否存在不合法日志。 parse ip... ：根据 IP 地址解析城市失败，请查看详细错误信息进行排查。 cannot find key... ：无法从日志中查看到指定的 SourceKey ，请检查配置是否正确或是否存在不合法日志。 |
| HTTP_INIT_ALARM | metric_http 插件错误，配置中指定的 ResponseStringMatch 正则表达式编译错误。 | 查看详细报错，检查其中的正则表达式是否正确。 |
| HTTP_PARSE_ALARM | metric_http 插件错误，获取 HTTP 响应失败。 | 查看详细报错，根据其中的具体错误信息对配置内容或所请求的 HTTP 服务器进行检查。 |
| INIT_CHECKPOINT_ALARM | Binlog 插件错误，加载检查点失败，插件将忽略检查点并从头开始处理。 | 查看详细报错，根据其中的具体错误信息来确定是否可忽略此错误。 |
| LOAD_LOCAL_EVENT_ALARM | 执行了本地事件处理错误 | 此警告一般不会出现，查看详细报错，根据其中的文件名、配置名、project、LogStore 等信息进行进一步地排查。 |
| LOG_REGEX_FIND_ALARM | processor_split_log_regex 以及 processor_split_log_string 插件错误，无法从日志中获取到配置中指定的 SplitKey 。 | 查看详细报错，检查是否存在配置错误的情况。 |
| LUMBER_CONNECTION_A
