re_results} 。 |
| fire_results_count | 触发告警的数据的总条数，可能多于 100，比如笛卡尔积操作后的总条数。 | int | 3 | 告警触发时产生的总数据条数为 ${fire_results_count} 。 |
| fire_results_as_kv | 触发告警的数据，即集合操作后的数据，最多 100 条。以 [key1:value1,key2:value2] 形式展示。 | array | [host:example.com,pv:836,status:200][host:example.com,pv:780,status:200] | 告警触发时产生的数据详情为 ${fire_results_as_kv} 。 |
