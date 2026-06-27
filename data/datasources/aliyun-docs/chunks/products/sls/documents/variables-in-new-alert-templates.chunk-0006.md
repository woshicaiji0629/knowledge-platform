## Policy结构
policy变量中可引用的变量说明如下表所示。

| 变量 | 说明 | 数据类型 | 取值示例 |
| --- | --- | --- | --- |
| alert_policy_id | 告警策略 ID。 | string | sls.test-alert |
| action_policy_id | 告警监控规则指定的行动策略 ID，仅在告警策略使用动态行动策略时有用。 | string | sls.test-action |
| repeat_interval | 重复等待时间，仅在告警策略使用动态行动策略时有用。 | string | 4h |
