N_LOGFILE_FAIL_ALARM | 打开文件出错。 | 查看详细报错，根据其中的日志文件路径、Project、LogStore 等信息进行进一步排查。 |
| PARSE_DOCKER_LINE_ALARM | service_docker_stdout 插件错误，解析日志失败。 | 查看详细报错，报错根据内容分为如下类型。 parse docker line error: empty line ：日志为空。 parse json docker line error... ：以 JSON 格式解析日志失败，请根据错误信息以及日志的前 512 个字节进行排查。 parse cri docker line error... ：以 CRI 格式解析日志失败，请根据错误信息以及日志的前 512 个字节进行排查。 |
| PLUGIN_ALARM | 插件初始化及相关调用发生错误。 | 查看详细报错，报错根据内容分为如下类型，请根据具体的错误信息进行进一步排查。 init plugin error... ：初始化插件失败。 hold on error... ：暂停插件运行失败。 resume error... ：恢复插件运行失败。 start service error... ：启动 service input 类型的插件失败。 stop service error... ：停止 service input 类型的插件失败。 |
| PROCESSOR_INIT_ALARM | processor_regex 插件错误，编译配置中指定的 Regex 正则表达式失败。 | 查看详细报错，检查其中的正则表达式是否正确。 |
| PROCESS_TOO_SLOW_ALARM | 日志解析速度过慢。 | 查看详细报错，根据其中的日志数量、缓冲区大小、解析时间来确定是否正常。 如果不正常，检查是否有其他进程占用了过多的 CPU 资源或是存在效率较低的复杂正则表达式等不合理的解析配置。 |
| REDIS_PARSE_ADDRESS_ALARM | redis 插件错误，配置中提供的 ServerUrls 存在解析失败的情况。 | 查看详细报错，对其中报错的 URL 进行检查。 |
| REGEX_FIND_ALARM | processor_regex 插件错误，无法从日志中找到配置中 SourceKey 指定的字段。 | 查看详细报错，检查是否存在 SourceKey 配置错误或日志不合法的情况。 |
| REGEX_UNMATCHED_ALARM | processor_regex 插件错误，匹配失败。 | 查看详细报错，报错根据内容分为如下类型，请根据具体的错误信息进行排查。 unmatch this log content... ：日志无法匹配配置中的正则表达
