Count:[5] > 3;Condition:[example.com]=='example.com' | 告警评估表达式为 ${condition} 。 |
| raw_condition | 原始的评估表达式，即变量未被替换为真实值的原始表达式。格式为 Count:数量表达式; Condition:匹配表达式 。 | string | Count:__count__ > 3;Condition:host=='example.com' | 原始评估表达式为 ${raw_condition} 。 |
| dashboard | 告警关联的仪表盘名称。 | string | mydashboard | 告警关联的仪表盘名称为 ${dashboard} 。 |
| dashboard_url | 告警关联的仪表盘地址。 | string | https://sls.console.aliyun.com/next/project/myproject/dashboard/mydashboard | 告警关联的仪表盘地址为 ${dashboard_url} 。 |
| fire_results | 触发告警的数据，即集合操作后的数据，最多 100 条。 | array | [{ "host":example.com", "host__1":"example.com", "pv":"836", "slbid":"slb-02", "status":"200"},{ "host":"example.com", "host__1":"example.org", "pv":"836", "slbid":"slb-02", "status":"200" },{ "host":"example.com", "host__1":"example.com", "pv":"836", "slbid":"slb-02", "status":"200" },{ "host":"example.com", "host__1":"example.com", "pv":"836", "slbid":"slb-02", "status":"200" },{ "host":"example.com", "host__1":"example.com", "pv":"780", "slbid":"slb-01", "status":"200" }] | 告警触发时产生的数据为 ${fire_results} 。 |
| fire_results_count | 触发告警的数据的总条数，可能多于 100，比如笛卡尔积操作后的总条数。 | int | 3 | 告警触发时产生的总数据条数为 ${fire_results_count} 。 |
| fire_results_as_kv | 触发告警的数据，即
