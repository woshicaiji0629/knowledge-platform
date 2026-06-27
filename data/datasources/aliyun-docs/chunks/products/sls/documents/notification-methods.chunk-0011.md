## 通用Webhook
设置告警通知渠道为通用Webhook，则当触发告警时，日志服务会向自定义的Webhook地址发送告警通知。
前提条件
已创建Webhook。具体操作，请参见[Webhook](create-a-webhook.md)[集成](create-a-webhook.md)。
配置参数
选择通用Webhook渠道时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。

| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 通用 Webhook 。 |
| 选择 Webhook | 选择您已创建的 Webhook。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
