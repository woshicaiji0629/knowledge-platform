### 场景二：统计 5xx 错误接口 Top 10
提示词
统计 SLS 日志库 prod-web/nginx-access 中最近 1 小时内 5xx 数量 Top 10 的接口。
Agent 输出示例
查询模式：索引查询 + SQL。 原因：需要统计 5xx 数量 Top10 的接口，因此先用索引查询过滤 500 到 599 状态码，再用 SQL 按 request_uri 分组、计数并排序。 执行命令： aliyun sls get-logs-v2 \ --project prod-web \ --logstore nginx-access \ --from 1777014000 \ --to 1777017600 \ --query 'status in [500 599] | SELECT request_uri, count(*) AS errors FROM log GROUP BY request_uri ORDER BY errors DESC LIMIT 10' 查询结果： | 排名 | request_uri | errors | | --- | --- | ---: | | 1 | /api/order/create | 186 | | 2 | /api/pay/notify | 73 | ..... | 10 | /api/user/login | 1 | 结论：最近 1 小时内 5xx 数量最高的接口是 /api/order/create，其错误量明显高于其他接口，建议优先排查该接口及其后端依赖。
