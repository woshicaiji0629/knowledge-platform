"use_default": false, "repeat_interval": "6m0s" } | 告警策略 ID 为 ${policy.alert_policy_id} 。 |
| region | 地域。 | string | cn-hangzhou | 告警触发的地域为 ${region} 。 |
| drill_down_query | 用于下钻分析的查询语句。在自定义告警中值为空，目前适用于日志审计服务、成本管家和 SLB 日志中心的告警内容模板。 | string | * | select count(1) as cnt | 无 |
| alert_url | 告警的详细 URL 地址。 | string | https://sls.console.aliyun.com/lognext/project/test-xxxx/alert/alert-1617164106-940166 | 告警 URL 为 ${alert_url} 。 |
| query_url | 查询统计中第一个查询页面的 URL 地址。 | string | https://sls-stg.console.aliyun.com/lognext/project/test-xxx/logsearch/test-alert-access?encode=base64&endTime=1617175989&queryString=KiB8IHNlbGVjdCBjb3VudCgxKSBhcyBjbnQ%3D&queryTimeType=99&startTime=1617175089 | 查询统计中第一个查询页面的 URL 地址为 ${query_url} 。 |
| alert_history_dashboard_url | 告警历史统计报表的 URL 地址。 | string | https://sls.console.aliyun.com/lognext/project/test-xx/dashboard/internal-alert-analysis | 告警历史统计报表的 URL 地址为 ${alert_history_dashboard_url} 。 |
| condition | 触发告警的评估表达式。其中，以触发告警的值替换您所配置的变量，并使用中括号（[ ]）包裹。格式为 Count:数量表达式; Condition:匹配表达式 。 | string | Count:[5] > 3;Condition:[example.com]=='example.com' | 告警评估表达式为 ${condition} 。 |
| raw_condition | 原始的评估表达式，即变量未被替换为真实值的原始表达式。格式为 Count:数量表达式; Condition:匹配表达式
