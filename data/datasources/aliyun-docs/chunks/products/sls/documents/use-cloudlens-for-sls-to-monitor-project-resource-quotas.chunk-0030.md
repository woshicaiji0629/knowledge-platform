| 参数项 | 赋值 |
| --- | --- |
| 规则名称 | Project 写入流量水位监控 |
| 检查频率 | 固定间隔，15 分钟 |
| 查询统计 | 类型：指标库 授权方式：默认 指标库：internal-monitor-metric 查询区间：15 分钟（相对） 查询语句： 重要 查询 SQL 默认返回 100 条数据，若在 SQL 结尾添加 limit 1000，代表可返回 1000 条查询结果。 (*)| SELECT Project, region , round(count_inflow/cast(quota_inflow as double) * 100, 3) as inflow_ratio FROM (SELECT cmdb.id as Project, cmdb.region as region, COALESCE(M.name1,0) as count_inflow, round(cast(json_extract(cmdb.quota, '$.inflow_per_min') as double)/1000000000, 3) as quota_inflow from "resource.sls.cmdb.project" as cmdb LEFT JOIN ( select project, round(MAX(name1)/1000000000, 3) as name1 from (SELECT __time_nano__ as time, element_at( split_to_map(__labels__, '|', '#$#') , 'project') as project, sum(CASE WHEN __name__ = 'logstore_origin_inflow_bytes' THEN __value__ ELSE NULL END) AS name1 FROM "internal-monitor-metric.prom" where __name__ ='logstore_origin_inflow_bytes' and regexp_like(element_at( split_to_map(__labels__, '|', '#$#') , 'project') , '.*') group by project,time )group by project) AS M ON cmdb.id = M.project )order by inflow_ratio desc limit 1000 |
| 分组评估 | 标签自动 |
| 触发条件 | 说明 当有 Project 写入流量超过额度的 90%时告警级别为严重。 当有 Project 写入流量超过额度的 80%时告警级别为中。 当有
