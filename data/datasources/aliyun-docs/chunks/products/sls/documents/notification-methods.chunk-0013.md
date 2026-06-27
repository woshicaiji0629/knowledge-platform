er-guide/event-overview#concept-1938024)。日志服务生成的事件字段说明如下：
重要
如果生成了多个告警，则每个告警都会发送告警事件，不会进行告警合并。
如果内容模板（事件总线）中的发送内容不是JSON格式，则告警事件发送成功后，在事件总线的事件规则中将无法使用data字段中的变量。

| 字段名称 | 说明 |
| --- | --- |
| id | 事件 ID，全局唯一。 |
| source | 事件源，固定为 acs.sls.alert。 |
| specversion | CloudEvents 协议版本，当前为 1.0 版本。 |
| type | 事件类型。 如果告警状态为触发告警，则事件类型为 sls:AlertEvent:Firing。 如果告警状态为恢复通知，则事件类型为 sls:AlertEvent:Resolved。 |
| datacontenttype | data 字段的内容格式，固定为 application/json。 |
| subject | 事件主题，对应内容模板中设置的 EventBridge 主题。 |
| time | 事件产生的时间，对应告警消息中的 alert_time 字段。 |
| data | 事件内容，对应内容模板中设置的 EventBridge 发送内容，必须为 JSON 格式。 |
