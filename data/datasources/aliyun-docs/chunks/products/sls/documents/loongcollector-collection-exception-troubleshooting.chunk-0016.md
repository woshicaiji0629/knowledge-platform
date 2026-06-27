| LOG_REGEX_FIND_ALARM | processor_split_log_regex 以及 processor_split_log_string 插件错误，无法从日志中获取到配置中指定的 SplitKey 。 | 查看详细报错，检查是否存在配置错误的情况。 |
| LUMBER_CONNECTION_ALARM | service_lumberjack 插件错误，停止插件时关闭服务器错误。 | 查看详细报错，根据具体错误信息进一步排查，此错误一般可忽略。 |
| LUMBER_LISTEN_ALARM | service_lumberjack 插件错误，初始化进行监听时发生错误。 | 查看详细报错，报错根据内容分为如下类型。 init tls error... ：请结合具体的错误信息检查 TLS 相关的配置是否正确 listen init error... ：请结合具体的错误信息检查地址相关的配置是否正确。 |
| LZ4_COMPRESS_FAIL_ALARM | 执行 LZ4 压缩发生错误。 | 查看详细报错，根据其中的 log lines、project、category、region 等值来进行进一步排查。 |
| MYSQL_CHECKPOINT_ALARM | MySQL 插件错误，检查点相关错误。 | 查看详细报错，报错根据内容分为如下类型。 init checkpoint error... ：初始化检查点失败，请根据错误信息检查配置指定的检查点列以及所获取的值是否正确。 not matched checkpoint... ：检查点信息不匹配，请根据错误信息检查是否是由于配置更新等人为原因导致的错误，如果是则可忽略。 |
| NGINX_STATUS_COLLECT_ALARM | nginx_status 插件错误，获取状态发生错误。 | 查看详细报错，根据其中的 URL 以及具体的错误信息来进行进一步排查。 |
| NGINX_STATUS_INIT_ALARM | nginx_status 插件错误，初始化解析配置中指定的 URL 失败。 | 查看详细报错，根据其中的 URL 检查地址是否正确配置。 |
| OPEN_FILE_LIMIT_ALARM | 已打开文件数量超过限制，无法打开新的文件 | 查看详细报错，根据其中的日志文件路径、Project、LogStore 等信息进行进一步排查。 |
| OPEN_LOGFILE_FAIL_ALARM | 打开文件出错。 | 查看详细报错，根据其中的日志文件路径、Project、LogStore 等信息进行进一步排查。 |
| PARSE_DOCKER_LINE_ALARM | service_docker_stdout 插件错误，解析日志失败。 | 查看详细报错，报错根据内
