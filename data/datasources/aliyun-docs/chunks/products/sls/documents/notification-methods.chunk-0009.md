## 飞书
设置告警通知渠道为飞书，则触发告警后，日志服务会通过飞书机器人向指定的飞书群发送告警通知。
前提条件
已创建Webhook。具体操作，请参见[Webhook](create-a-webhook.md)[集成](create-a-webhook.md)。
配置参数
选择飞书渠道时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。

| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 飞书 。 |
| 选择 Webhook | 选择您已创建的 Webhook。 |
| 提醒方式 | 支持在飞书群里提醒所有人，可选值为不提醒、所有人。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 说明 飞书支持 Markdown 格式。更多信息，请参见 [内容格式](custom-notification-content.md) 。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |
