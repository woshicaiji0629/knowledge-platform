LOAD_ADDRESS_ALARM | HTTP 数据采集配置中，设置的 Addresses 不合法。 | 检查 Addresses 合法性。 |
| HTTP_COLLECT_ALARM | HTTP 数据采集异常。 | 根据错误提示排查，一般超时导致。 |
| FILTER_INIT_ALARM | 过滤器初始化异常。 | 一般由于过滤器的正则表达式非法导致，请根据提示修复。 |
| INPUT_CANAL_ALARM | MySQL Binlog 运行异常。 | 根据错误提示排查。在配置更新时，canal 服务可能重启，服务重启的错误可以忽略。 |
| CANAL_INVALID_ALARM | MySQL Binlog 内部状态异常。 | 此错误一般由于运行时表的 schema 信息变更导致 meta 不一致。请确认报错期间是否修改过表的 schema。 |
| MYSQL_INIT_ALARM | MySQL 初始化异常。 | 根据错误提示处理。 |
| MYSQL_CHECKPOING_ALARM | MySQL Checkpoint 格式异常。 | 确认是否修改 Checkpoint 相关配置。 |
| MYSQL_TIMEOUT_ALARM | MySQL 查询超时。 | 确认 MySQL 服务器和网络是否异常。 |
| MYSQL_PARSE_ALARM | MySQL 查询结果解析失败。 | 确认 MySQL 配置的 Checkpoint 格式是否匹配对应字段的格式。 |
| AGGREGATOR_ADD_ALARM | 向聚合队列中添加数据失败。 | 数据发送过快。若真实数据量很大，可忽略。 |
| ANCHOR_FIND_ALARM | processor_anchor 插件错误、配置错误或存在不符合配置的日志。 | 查看详细报错，根据内容分为如下类型。检查相应的配置是否存在问题。 anchor cannot find key ：配置中指定了 SourceKey 但日志中不存在对应的字段。 anchor no start ：无法从 SourceKey 的值中找到 Start 对应的内容。 anchor no stop ：无法从 SourceKey 的值中找到 Stop 对应的内容。 |
| ANCHOR_JSON_ALARM | processor_anchor 插件错误：对已配置的 Start 和 Stop 所确定的内容执行 JSON 展开时发生错误。 | 查看详细报错，检查所处理的内容以及相关的配置，确定是否有配置错误或不合法日志。 |
| CANAL_RUNTIME_ALARM | MySQL Binlog 插件运行时错误。 | 查看详细报错进一步排查。一般与所连接的 MySQL master 相关。 |
| CHECKPOI
