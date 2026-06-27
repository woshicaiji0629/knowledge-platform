ourceKey 配置错误或日志不合法的情况。 |
| REGEX_UNMATCHED_ALARM | processor_regex 插件错误，匹配失败。 | 查看详细报错，报错根据内容分为如下类型，请根据具体的错误信息进行排查。 unmatch this log content... ：日志无法匹配配置中的正则表达式 match result count less... ：匹配的结果数量少于配置中指定的 Keys 数量。 |
| SAME_CONFIG_ALARM | 同一个 LogStore 下存在同名的配置，后发现的配置会被抛弃。 | 查看详细报错，根据其中的配置路径等信息排查是否存在配置错误的情况。 |
| SPLIT_FIND_ALARM | split_char 以及 split_string 插件错误，无法从日志中找到配置中 SourceKey 指定的字段。 | 查看详细报错，检查是否存在 SourceKey 配置错误或日志不合法的情况。 |
| SPLIT_LOG_ALARM | processor_split_char 以及 processor_split_string 插件错误，解析得到的字段数量与 SplitKeys 中指定的不相同。 | 查看详细报错，检查是否存在 SourceKey 配置错误或日志不合法的情况。 |
| STAT_FILE_ALARM | 通过 LogFileReader 对象进行文件采集时发生错误。 | 查看详细报错，根据其中的文件路径、错误信息进行进一步排查。 |
| SERVICE_SYSLOG_INIT_ALARM | service_syslog 插件错误，初始化失败。 | 查看详细报错，检查配置中的 Address 是否正确。 |
| SERVICE_SYSLOG_STREAM_ALARM | service_syslog 插件错误，通过 TCP 采集时发生错误。 | 查看详细报错，报错根据内容分为如下类型，请根据详细报错中的具体错误信息进行排查。 accept error... ：执行 Accept 时发生错误，插件将等待一段时间后重试。 setKeepAlive error... ：设置 Keep Alive 失败，插件将跳过此错误并继续运行。 connection i/o timeout... ：通过 TCP 读取时超时，插件将重设超时并继续读取。 scan error... ：TCP 读取错误，插件将等待一段时间后重试。 |
| SERVICE_SYSLOG_PACKET_ALARM | service_syslog 插件错误，通过 UDP 采集时发生错误。 | 查看详细报错，报错根据内容分为如下类型。 connection i/o timeout... ：通过 UDP 读取时超时，插件将重设超
