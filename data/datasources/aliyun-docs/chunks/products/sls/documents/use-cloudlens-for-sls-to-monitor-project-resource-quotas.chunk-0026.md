实时水位监控
单击新建告警，配置告警规则。
选择创建告警需要挂载的Project为存储全局错误日志和监控指标所在Project。
根据业务场景配置告警触发条件、以及告警策略。
根据下表完成配置，其余参数保持默认即可，具体信息，可参见[创建日志告警监控规则](alarm-settings-quick-start.md)。

| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | Logtail 采集配置水位监控 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：指标库 授权方式：默认 指标库：internal-monitor-metric 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 * | select Project, region, round(count_logtail_config/quota_logtail_config * 100, 3) as logtail_config_ratio from (SELECT A.id as Project , A.region as region, COALESCE(SUM(B.count_logtail_config), 0) AS count_logtail_config , cast(json_extract(A.quota, '$.config') as double) as quota_logtail_config FROM "resource.sls.cmdb.project" as A LEFT JOIN ( SELECT project, COUNT(*) AS count_logtail_config FROM "resource.sls.cmdb.logtail_config" as B GROUP BY project ) AS B ON A.id = B.project group by A.id, A.quota, A.region) where quota_logtail_config is not null order by logtail_config_ratio desc limit 1000 |
| 分组评估 | 标签自动 |
| 触发条件 | 说明 当有 Project 的 Logtail 采集配置数超过额度的 90%时告警级别为严重。 当有 Project 的 Logtail 采集配置数超过额度的 80%时告警级别为中。 当有数据匹配 logtail_config_ratio > 90 时，严重度：严重。 当有数据匹配 logtail_config_ratio > 80 时，严重度：中。 |
| 输出目标 | SLS 通知 |
| 告警策略 | 普通模式 |
| 行动策略 | 按需选择或单击 新增 创建行动策略，具体操作，请参见 [行动策略](create-an-action-policy.md) 。 |
