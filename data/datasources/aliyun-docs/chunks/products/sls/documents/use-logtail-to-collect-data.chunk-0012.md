gtail 提供了自定义的日志时间格式，方便您从不同格式的日志数据中提取必要的日志时间戳信息。 |
| 自动同步 Logtail 采集配置 | 您在日志服务控制台上新建或更新 Logtail 采集配置，一般情况下，Logtail 在 3 分钟内即可接收并生效。更新过程中不会丢失日志数据。 |
| 自我监控状态 | Logtail 会实时监控自身 CPU 和内存消耗，避免 Logtail 消耗您太多资源而影响您的其他服务。Logtail 在运行过程中，如果资源使用超出限制将会自动重启，避免影响服务器上的其他服务。同时，Logtail 有主动的网络限流保护措施，防止过度消耗带宽。更多信息，请参见 [启动参数配置文件（ilogtail_config.json）](logtail-configuration-files-and-record-files.md) 。 |
| 签名数据发送 | 为保证您的数据在发送过程中不会被篡改，Logtail 会通过可信通道从服务端获取私密 Token，并对所有发送日志的数据包进行数据签名。 说明 Logtail 在获取私密 Token 时采用 HTTPS 通道，保障相关安全性。 |
