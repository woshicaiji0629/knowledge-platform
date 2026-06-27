[CPU](loongcollector-management-linux.md) [使用上限或网络发送并发限制](loongcollector-management-linux.md) 。 |
| SEND_DATA_FAIL_ALARM | 发送数据失败，可能原因： 阿里云账号未创建 AccessKey。 客户端所在机器与日志服务无法连通或者网络链路质量较差。 日志服务端写入配额不足。 | 使用阿里云账号创建 AccessKey。 检查本地配置文件 /usr/local/ilogtail/ilogtail_config.json ，执行 curl <服务器地址> ，查看是否有内容返回。 为 LogStore [增加](manage-shards.md) [Shard](manage-shards.md) [数量](manage-shards.md) ，以支持更大数据量的写入。 |
| SEND_QUOTA_EXCEED_ALARM | 日志写入流量超出限制。 | 在控制台上 [增加](manage-shards.md) [Shard](manage-shards.md) [数量](manage-shards.md) 。 |
| READ_LOG_DELAY_ALARM | 日志采集进度落后于日志产生进度，一般是由于配置使用的 CPU 资源不够或是网络发送流控导致。 | [修改](loongcollector-management-linux.md) [CPU](loongcollector-management-linux.md) [使用上限或网络发送并发限制](loongcollector-management-linux.md) 。 导入历史数据时，短时间会采集大量数据，若出现该错误可忽略。 |
| DROP_LOG_ALARM | 开始丢弃日志：日志采集进度落后于日志产生进度，且未处理的日志轮转超过 20 个，一般是由于配置使用的 CPU 资源不够或是网络发送流控导致。 | [修改](loongcollector-management-linux.md) [CPU](loongcollector-management-linux.md) [使用上限或网络发送并发限制](loongcollector-management-linux.md) 。 |
| LOGDIR_PERMINSSION_ALARM | 没有日志监控目录读取权限。 | 检查日志监控目录是否存在。如果存在，请检查目录权限设置。 |
| ENCODING_CONVERT_ALARM | 编码转换失败。 | 检查日志编码格式配置是否与日志编码格式一致。 |
| OUTDATED_LOG_ALARM | 过期的日志：日志时间落后 12 小时以上。可能原因： 日志解析进度落后 12 小时以
