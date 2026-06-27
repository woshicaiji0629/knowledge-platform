## 事件总线（EventBridge）
设置告警通知渠道为事件总线（EventBridge），则触发告警后，日志服务会向事件总线发送一个告警事件。
前提条件
已在阿里云事件总线EventBridge服务中创建自定义总线。具体操作，请参见[创建自定义总线](https://help.aliyun.com/zh/eventbridge/user-guide/manage-custom-event-buses#section-sfl-pcs-6rh)。
说明
在创建自定义总线时，可忽略事件源的配置。如果要添加事件源，则需创建一个名为acs.sls.alert的事件源，与告警事件中source字段的值保持一致。
如果您使用的是RAM用户，需先授予该RAM用户AliyunEventBridgeReadOnlyAccess权限。
配置参数
选择事件总线（EventBridge）时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。

| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 事件总线(EventBridge) 。 |
| 地域 | 选择您已创建的事件总线的所在地域。 |
| 事件总线 | 选择您已创建的事件总线。日志服务将发送告警事件给该事件总线。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |

事件字段说明
触发告警后，日志服务会生成一个告警事件并发送给事件总线，事件规范请参见[事件概述](https://help.aliyun.com/zh/eventbridge/user-guide/event-overview#concept-1938024)。日志服务生成的事件字段说明如下：
重要
如果生成了多个告警，则每个告警都会发送告警事件，不会进行告警合并。
如果内容模板（事件总线）中的发送内容不是JSON格式，则告警事件发送成功后，在事件总线的事件规则中将无法使用data字段中的变量。
