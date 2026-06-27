| 变量 | 说明 | 数据类型 | 取值示例 | 引用示例 |
| --- | --- | --- | --- | --- |
| aliuid | Project 所属的阿里云账号 ID。 | string | 117918634953**** | {{ alert.aliuid }} 用户的告警规则已触发。 |
| alert_instance_id | 告警触发的实例的 ID。 | string | ee16a8f435485f3f-5be6b81edc520-3d6**** | 实例 ID 为 {{ alert.alert_instance_id }} 。 |
| alert_id | 告警规则 ID，Project 内唯一。 | string | alert-12345 | 告警规则 ID 是 {{ alert.alert_id }} 。 |
| alert_name | 告警规则名称。 | string | 测试告警规则 | 告警规则 {{ alert.alert_name }} 已经触发。 |
| alert_type | 告警类型。 sls_alert：由告警监控规则触发的告警。 sls_pub：来自于开放告警的告警。 sls_ml：由智能巡检触发的告警。 | string | sls_alert | 告警类型是 {{ alert.alert_type }} ，格式化显示为 {{ alert.alert_type | format_type }} 。 |
| region | 地域。 | string | cn-hangzhou | 告警触发的地域为 {{ alert.region }} 。 |
| project | 告警规则所属 Project。 | string | my-project | {{ alert.project }} 项目中的告警规则已触发。 |
| next_eval_interval | 下一次评估间隔，单位为秒。 | int | 300 | 下一次评估时间为 {{ alert.next_eval_interval }} 秒后。 |
| alert_time | 本次评估时间。 | int | 1616744734 | 本次评估告警的时间为 {{ alert.alert_time }} ，格式化显示为 {{ alert.alert_time | format_date }} 。 |
| fire_time | 首次触发时间。 | int | 1616059834 | 告警首次触发时间为 {{ alert.fire_time }} ，格式化显示为 {{ alert.fire_time | format_date }} 。 |
| status | 告警状态。 firing：触发告警。 resolved：恢复通知。 |
