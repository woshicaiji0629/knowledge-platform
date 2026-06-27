int | 0 | 告警恢复的时间为 ${resolve_time} 。 |
| results | 查询参数和中间结果，数组类型。变量取值说明，请参见 [QueryData](variables-in-original-alert-templates.md) [结构](variables-in-original-alert-templates.md) 。 | array | [ { "store_type": "log", "region": "cn-hangzhou", "project": "sls-alert-test", "store": "test", "query": "* | select count(1) as cnt", "start_time": 1616741485, "end_time": 1616745085, "dashboard_id": "mydashboard", "raw_results": [{"cnt": "4"}], "raw_result_count": 1, "truncated": false, "role_arn": "" } ] | 第一个查询的开始时间为 ${results[0].start_time} ；结束时间为 ${results[0].end_time} 。 说明 其中 0 为图表编号。 |
| labels | 标签列表。 | map | {"env":"test"} | 告警标签为 ${labels} 。 |
| annotations | 标注列表。 | map | { "title": "告警标题","desc": "告警描述" } | 告警标注为 ${annotations} 。 |
| severity | 告警严重度。 10：严重 8：高 6：中 4：低 2：仅报告 | int | 10 | 告警严重度为 ${severity} 。 |
| policy | 告警策略或者行动策略。变量取值说明，请参见 [Policy](variables-in-original-alert-templates.md) [结构](variables-in-original-alert-templates.md) 。 | map | { "alert_policy_id": "sls.test-alert", "action_policy_id": "sls.test-action", "use_default": false, "repeat_interval": "6m0s" } | 告警策略 ID 为 ${policy.alert_policy_id} 。 |
| region | 地域。 | string | cn-hangzhou | 告警触发的地域为 ${region} 。 |
| dr
