## Webhook-自定义
设置告警通知方式为Webhook-自定义，当触发告警时，日志服务会向自定义的Webhook地址发送告警通知。
注意事项
Webhook方式对应的超时时间为5秒，如果发出请求后5秒内没有返回，则表示发送失败。
前提条件
已获取Webhook地址。
配置参数
选择Webhook-自定义渠道时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。
说明
Webhook调用成功时返回的状态码需为200，否则会被日志服务认为请求失败，导致重复调用。

| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 WebHook-自定义 。 |
| 请求地址 | Webhook 地址，必须为公网地址（例如外网域名、IP:Port 格式的 URL）。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 使用自定义 Webhook 时，建议设置内容模板中的内容为 JSON 格式。 |
| 请求方式 | 支持 GET、POST、DELETE、PUT 和 OPTIONS。 无特殊需求时，推荐使用 POST 方法。该方法在各个 Web 框架中的支持程度最好。 |
| 请求头 | 单击 添加请求头 ，可添加请求头信息。例如 Content-Type: application/json;charset=utf-8 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
