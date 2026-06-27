g like '%user can only run%' then 'SQL 分析操作并发数超限' ELSE ErrorMsg END AS ErrorMsg, COUNT(1) AS count GROUP BY Project, ErrorMsg Limit 1000 |
| 分组评估 | 不分组 |
| 触发条件 | 说明 当有任意额度超限 10 次错误告警级别为严重。 当有任意额度发生超限 1 次错误时告警级别为中。 当有数据匹配 count > 10 时，严重度：严重。 当有数据匹配 count > 1 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](create-an-action-policy.md) 。 |
