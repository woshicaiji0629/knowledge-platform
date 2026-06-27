### 发送日志
Logtail将采集到的日志聚合并发送到日志服务。如果数据发送失败，Logtail自动根据错误信息决定重试或放弃发送。

| 错误信息 | 说明 | Logtail 处理方式 |
| --- | --- | --- |
| 401 错误 | 当前账号没有权限采集数据。为该账号授予数据接入相关权限。具体操作，请参见 [配置权限助手](configure-the-permission-assistant-feature.md) 。 | 直接丢弃日志包。 |
| 404 错误 | Logtail 采集配置中指定的 Project 或 LogStore 不存在。 | 直接丢弃日志包。 |
| 403 错误 | Shard Quota 超出限制。 | 等待 3 秒后重试。 |
| 500 错误 | 服务端异常。 | 等待 3 秒后重试。 |

说明
如果要调整数据的发送速度和最大并发数，您可以设置启动参数配置文件中的max_bytes_per_sec参数和send_request_concurrency参数。具体操作，请参见[设置](configure-the-startup-parameters-of-logtail.md)[Logtail](configure-the-startup-parameters-of-logtail.md)[启动参数](configure-the-startup-parameters-of-logtail.md)。
