分析语句为 {{ alert.results[0].query }} 。 |
| fire_results | 触发告警的数据，即集合操作后的数据，最多 100 条。 fire_results 变量值超过 2KB，并且查询结果字段内容的长度超过 1KB 时，超出部分会被截断。数据被截断处理方式请参见 [触发告警的日志太多，在告警通知中展示不完全时，如何处理？](faq-about-alert-notifications.md) | array | 参见本文末尾附录。 | 告警触发时产生的数据为 {{ alert.fire_results | to_json }} 。 |
| fire_results_count | 触发告警的数据的总条数，可能多于 100，例如笛卡尔积操作后的总条数。 | int | 3 | 告警触发时产生的总数据条数为 {{ alert.fire_results_count }} 。 |
| condition | 触发告警的评估表达式。其中，以触发告警的值替换您所配置的变量，并使用中括号（[ ]）包裹。格式为 Count:数量表达式;Condition:匹配表达式 。 | string | Count:[5] > 3;Condition:[example.com]=='example.com' | 告警评估表达式为 {{ alert.condition }} 。 |
| raw_condition | 原始的评估表达式，即变量未被替换为真实值的原始表达式。格式为 Count:数量表达式;Condition:匹配表达式 。 | string | Count:__count__ > 3;Condition:host=='example.com' | 原始评估表达式为 {{ alert.raw_condition }} 。 |
| policy | 告警策略或者行动策略。变量取值说明，请参见 [Policy](variables-in-new-alert-templates.md) [结构](variables-in-new-alert-templates.md) 。 | map | 参见本文末尾附录。 | 告警策略 ID 为 {{ alert.policy.alert_policy_id }} 。 |
| dashboard | 告警关联的仪表盘名称。 | string | mydashboard | 告警关联的仪表盘名称为 {{ alert.dashboard }} 。 |
| alert_url | 告警的详细 URL 地址。 | string | https://sls.console.aliyun.com/lognext/project/test-xxxx/alert/alert-1617164106-940166 | 告警 URL
