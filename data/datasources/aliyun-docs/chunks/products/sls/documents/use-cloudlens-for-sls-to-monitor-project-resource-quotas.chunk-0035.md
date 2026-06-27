nt_ratio desc limit 1000 |
| 分组评估 | 标签自动 |
| 触发条件 | 说明 当有 Project 写入次数超过额度的 90%时告警级别为严重。 当有 Project 写入次数超过额度的 80%时告警级别为中。 当有数据匹配 inflow_ratio > 90 时，严重度：严重。 当有数据匹配 inflow_ratio > 80 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](create-an-action-policy.md) 。 |
