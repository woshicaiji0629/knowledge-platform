P 读取错误，插件将等待一段时间后重试。 |
| SERVICE_SYSLOG_PACKET_ALARM | service_syslog 插件错误，通过 UDP 采集时发生错误。 | 查看详细报错，报错根据内容分为如下类型。 connection i/o timeout... ：通过 UDP 读取时超时，插件将重设超时并继续读取。 read from error... ：UDP 读取错误，插件将等待一段时间后重试。 |
| PARSE_TIME_FAIL_ALARM | 解析日志时间失败。 | 正则表达式提取的时间字段是否正确。 指定的时间字段内容是否匹配配置中的时间表达式。 详细的解决方案： [使用](https://developer.aliyun.com/article/1488856) [CloudLens](https://developer.aliyun.com/article/1488856) [排查日志时间解析错误问题](https://developer.aliyun.com/article/1488856) 。 |
| BINARY_UPDATE_ALARM | 二进制数据更新警告。 | 查看详细报错，根据具体错误信息进一步排查。 |
| CAST_SENSITIVE_WORD_ALARM | 敏感词类型转换相关错误。 | 查看详细报错，根据具体错误信息进一步排查。 |
| CHECKPOINT_ALARM | checkpoint 相关错误。 | 查看详细报错，根据具体错误信息进一步排查。 |
| CHECKPOINT_V2_ALARM | （CheckpointManagerV2 专用） | 查看详细报错，根据具体错误信息进一步排查。 |
| COMPRESS_FAIL_ALARM | 压缩失败，失败后会直接丢弃。 | 查看详细报错，根据具体错误信息进一步排查。 |
| CONFIG_UPDATE_ALARM | 配置拉取/重启错误。 | 查看详细报错，根据具体错误信息进一步排查。 |
| DISCARD_SECONDARY_ALARM | （DiskBufferWriter 专用） | 查看详细报错，根据具体错误信息进一步排查。 |
| DOMAIN_SOCKET_BIND_ALARM | （ShennongManager 专用） | 查看详细报错，根据具体错误信息进一步排查。 |
| ENCRYPT_DECRYPT_FAIL_ALARM | （DiskBufferWriter 专用） | 查看详细报错，根据具体错误信息进一步排查。 |
| EPOLL_ERROR_ALARM | faild to init inotify fd | 查看详细报错，根据具体错误信息进一步排查。 |
| EXACTLY_ONCE_ALARM | dr
