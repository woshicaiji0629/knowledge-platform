## 额度超限监控
单击新建告警，配置告警规则。
选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。
根据业务场景配置告警触发条件、以及告警策略。
根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](alarm-settings-quick-start.md)。

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | Project 写入次数额度超限 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：日志库 授权方式：默认 日志库：internal-error_log 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 * and (ErrorCode: ExceedQuota or ErrorCode: QuotaExceed or ErrorCode: ProjectQuotaExceed or ErrorCode:WriteQuotaExceed)| SELECT Project, COUNT(1) AS count where ErrorMsg like '%Project write quota exceed: qps%' GROUP BY Project ORDER BY count DESC LIMIT 1000 |
| 分组评估 | 不分组 |
| 触发条件 | 说明 当有 Project 写入次数发生超限 10 次错误告警级别为严重。 当有 Project 写入次数发生超限 1 次错误时告警级别为中。 当有数据匹配 count > 10 时，严重度：严重。 当有数据匹配 count > 1 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](create-an-action-policy.md) 。 |

参数配置完成后，单击确定。
