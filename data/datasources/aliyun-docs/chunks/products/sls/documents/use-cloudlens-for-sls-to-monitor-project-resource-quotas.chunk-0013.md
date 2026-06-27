| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | 资源配额超限次数监控 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：日志库 授权方式：默认 日志库：internal-error_log 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 ((* and (ErrorCode: ExceedQuota or ErrorCode: QuotaExceed or ErrorCode: ProjectQuotaExceed or ErrorCode:WriteQuotaExceed or ErrorCode: ShardWriteQuotaExceed or ErrorCode: ShardReadQuotaExceed)))| SELECT Project, CASE WHEN ErrorMsg like '%Project write quota exceed: inflow%' then 'Project 写入流量超限' WHEN ErrorMsg like '%Project write quota exceed: qps%' then 'Project 写入次数超限' WHEN ErrorMsg like '%dashboard quota exceed%' then '报表额度超限' WHEN ErrorMsg like '%config count%' then 'Logtail 采集配置超限' WHEN ErrorMsg like '%machine group count%' then '机器组超限' WHEN ErrorMsg like '%Alert count %' then '告警超限' WHEN ErrorMsg like '%logstore count %' then 'LogStore 数超限' WHEN ErrorMsg like '%shard count%' then 'Shard 数超限' WHEN ErrorMsg like '%shard write bytes%' then 'Shard 写入超限' WHEN ErrorMsg like '%shard write quota%' then 'Shard 写入超限' WHEN ErrorMsg like '%user can only run%' then 'SQL 分析操作并发数超限' ELSE ErrorMsg END AS ErrorMsg, COUNT(1) AS count GROUP BY Project, ErrorMsg Limit 1000 |
| 分组评估 | 不分组 |
| 触发条件
