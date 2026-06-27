| 变量 | 说明 | 数据类型 | 取值示例 | 引用示例 |
| --- | --- | --- | --- | --- |
| aliuid | Project 所属的阿里云账号 ID。 | string | 117918664953**** | ${aliuid} 用户的告警规则已触发。 |
| alert_instance_id | 告警触发的实例的 ID。 | string | ee16a8f435485f3f-5be6b81edc520-3d6**** | 实例 ID 为 ${alert_instance_id} 。 |
| project | 告警规则所属 Project。 | string | my-project | ${project} 项目中的告警规则已触发。 |
| alert_id | 告警规则 ID，Project 内唯一。 | string | 0fdd88063a611aa114938f9371daeeb6-1671a52**** | 告警规则 ID 是 ${alert_id} 。 |
| alert_type | 告警类型。 sls_alert：由告警监控规则触发的告警。 sls_pub：来自于开放告警中的告警。 | string | sls_alert | 告警类型是 ${alert_type} 。 |
| alert_name | 告警规则名称。 | string | 告警规则 new2 | 告警规则 ${alert_name} 已经触发。 |
| next_eval_interval | 下一次评估间隔。 | int | 900 | 下一次评估时间为 ${next_eval_interval} 秒后。 |
| alert_time | 本次评估时间。 | int | 1616744734 | 本次评估告警的时间为 ${alert_time} 。 |
| fire_time | 首次触发时间。 | int | 1616059834 | 告警首次触发时间为 ${fire_time} 。 |
| status | 告警状态。 firing：触发告警。 resolved：恢复通知。 | string | firing | 告警状态为 ${status} 。 |
| resolve_time | 告警恢复时间。 如果告警状态是 firing，取值为 0。 如果告警状态是 resolved，取值为具体恢复时间。 | int | 0 | 告警恢复的时间为 ${resolve_time} 。 |
| results | 查询参数和中间结果，数组类型。变量取值说明，请参见 [QueryData](variables-in-original-alert-templates.md) [结构](variables-in-original-a
