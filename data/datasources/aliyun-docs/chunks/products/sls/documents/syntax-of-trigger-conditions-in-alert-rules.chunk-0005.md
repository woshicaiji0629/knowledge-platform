## 示例
示例1：如果1天（相对）内任务成功率低于90%且延时超过60秒则产生告警。告警名称设置为任务延时告警，关联两个图表：图表0名称为任务成功率，查询语句为* | select round(sum(case when code = 200 then 1 else 0 end) * 100.0 / count(*), 2) as success，查询区间为1天（相对）；图表1名称为延时情况，查询语句为delay > 0 | select time_series(__time__, '10m', '%m-%d %H:%i', '0') as time, round(avg(delay)/100, 3) as delay group by time order by time limit 14400，查询区间为1天（相对）。检查频率为固定间隔15分钟，触发条件为$0.success < 90 && $1.delay > 60。
示例2：如果15分钟内状态码500出现10次则产生告警。告警名称设置为500 状态码报警，关联图表0名称为响应状态分布，查询语句为* | SELECT status, COUNT(*) as total GROUP BY status，查询区间为15分钟（相对）。检查频率为固定间隔15分钟，触发条件为$0.status == 500 && $0.total > 10。
示例3：如果1小时内加工速率低于1000条则产生告警。告警名称设置为数据加工速率过低告警，关联图表0名称为加工速率 (lines/s)，查询语句为__topic__: __etl-log-status__ AND __tag__: __schedule_type__: Resident and event_id: "shard_worker:metrics:checkpoint" | select time_series(__time__, '1m', '%y/%m/%d %H:%i', '0') as dt, round(sum("progress.accept") / 60.0, 3) as "accept", round(sum("progress.dropped") / 60.0, 3) as "dropped", round(sum("progress.delivered") / 60.0, 3) as "delivered", round(sum("progress.failed") / 60.0, 3) as "failed" group by dt order by dt asc limit 10000，查询区间为1小时（相对）。检查频率为固定间隔1小时，触发条件为$0.accept < 1000。
该文章对您有帮助吗？
反馈
