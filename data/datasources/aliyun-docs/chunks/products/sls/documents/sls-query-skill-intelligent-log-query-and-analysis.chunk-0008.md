### 场景一：查询最近 15 分钟的 5xx 错误日志
提示词
查询 SLS 日志库 Project=prod-web，Logstore=nginx-access，最近 15 分钟 status 大于等于 500 的请求，按时间倒序。
Agent 输出示例
查询模式：索引查询。 原因：用户需要按条件返回原始日志，不涉及聚合、排序分析或字段投影；status 字段已配置数值类型索引，可直接使用范围查询。 执行命令： aliyun sls get-logs-v2 \ --project prod-web \ --logstore nginx-access \ --from 1777016700 \ --to 1777017600 \ --query 'status>=500' \ --line 100 \ --offset 0 \ --reverse true 查询结果： | 时间 | status | request_uri | upstream_status | request_time | message | | --- | ---: | --- | ---: | ---: | --- | | 2026-04-24 15:59:31 | 502 | /api/order/create | 502 | 1.238 | upstream connect timeout | | 2026-04-24 15:58:44 | 500 | /api/pay/notify | 500 | 0.412 | internal server error | | 2026-04-24 15:57:09 | 502 | /api/order/create | 502 | 1.104 | bad gateway | 结论：已按时间倒序返回最近 15 分钟内的 5xx 原始日志，最新错误集中出现在 /api/order/create。
