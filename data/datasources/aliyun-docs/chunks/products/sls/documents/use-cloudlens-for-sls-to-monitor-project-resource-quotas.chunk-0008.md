count_logstore FROM "resource.sls.cmdb.logstore" as B GROUP BY project ) AS B ON A.id = B.project LEFT JOIN ( SELECT project, COUNT(*) AS count_machine_group FROM "resource.sls.cmdb.machine_group" as C GROUP BY project ) AS C ON A.id = C.project LEFT JOIN ( SELECT project, COUNT(*) AS count_logtail_config FROM "resource.sls.cmdb.logtail_config" as D GROUP BY project ) AS D ON A.id = D.project group by A.id, A.quota, A.region) where quota_logstore is not null and quota_machine_group is not null and quota_logtail_config is not null and (logstore_ratio > 80 or machine_group_ratio > 80 or logtail_config_ratio > 80) limit 10000 |
| 分组评估 | 标签自动 |
| 触发条件 | 说明 当有 Project 的 LogStore 数、机器组数、Logtail 采集配置其中一个水位超过额度的 90%时告警级别为严重。 当有 Project 的 LogStore 数、机器组数、Logtail 采集配置其中一个水位超过额度的 80%时告警级别为中。 当有数据匹配 logstore_ratio > 90 || machine_group_ratio > 90 || logtail_config_ratio > 90 时，严重度：严重。 当有数据匹配 logstore_ratio > 80 || machine_group_ratio > 80 || logtail_config_ratio > 80 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](create-an-action-policy.md) 。 |
