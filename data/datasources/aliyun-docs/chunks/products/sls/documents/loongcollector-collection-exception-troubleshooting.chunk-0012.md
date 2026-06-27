| 检查日志监控目录是否存在。如果存在，请检查目录权限设置。 |
| ENCODING_CONVERT_ALARM | 编码转换失败。 | 检查日志编码格式配置是否与日志编码格式一致。 |
| OUTDATED_LOG_ALARM | 过期的日志：日志时间落后 12 小时以上。可能原因： 日志解析进度落后 12 小时以上。 用户自定义时间字段配置错误。 日志记录程序时间输出异常。 | 查看是否存在 READ_LOG_DELAY_ALARM。 若存在参考 READ_LOG_DELAY_ALARM 处理方式解决。 若不存在则检查时间字段配置。如果时间字段配置正确，请检查日志记录程序时间输出是否正常。 |
| STAT_LIMIT_ALARM | 日志采集配置目录中的文件数超限。 | 检查采集的目录下是否有较多文件和子目录并合理设置监控目录最大深度。 修改 [启动参数配置文件（ilogtail_config.json）](loongcollector-management-linux.md) 中 mem_usage_limit 参数。 详细的解决方案： [使用](https://help.aliyun.com/practice_detail/458757?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [CloudLens](https://help.aliyun.com/practice_detail/458757?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [排查文件、目录数超限问题](https://help.aliyun.com/practice_detail/458757?spm=5176.2020520112.0.0.5f8634c0sLkkbX) 。 |
| DROP_DATA_ALARM | 进程退出时日志落盘到本地超时，此时会丢弃未落盘完成的日志。 | 该报错通常为采集严重阻塞导致，请 [修改](loongcollector-management-linux.md) [CPU](loongcollector-management-linux.md) [使用上限或网络发送并发限制](loongcollector-management-linux.md) 。 |
| INPUT_COLLECT_ALARM | 输入源采集异常。 | 根据错误提示处理。 |
| HTTP_LOAD_ADDRESS_ALARM | HTTP 数据采集配置中，设置的 Addresses 不合法。 | 检查 Addresses 合法性。 |
| HTTP_COLLECT_ALARM | HTTP 数据采集异常。 | 根据错误提示排查，一般超时导致。 |
| FILTER_INIT_ALARM | 过滤器初始化
