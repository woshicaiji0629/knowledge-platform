| 名称 | PromQL | 说明 |
| --- | --- | --- |
| APF 请求并发限制（维度：PL） | sum by(priority_level) (apiserver_flowcontrol_request_concurrency_limit) | 按 PL 或 Instance + PL 维度统计 APF 请求并发限制，即某个优先级队列理论上允许同时处理的最大请求数。 apiserver_flowcontrol_request_concurrency_limit 在 Kubernetes 1.30 版本变为 Deprecated，自 1.31 版本起移除 ， 1.31 及以上版本的集群中建议使用 apiserver_flowcontrol_nominal_limit_seats 指标代替。 |
| APF 请求并发限制（维度：Instance + PL） | sum by(instance,priority_level) (apiserver_flowcontrol_request_concurrency_limit) |  |
| APF 当前执行请求数量（维度：FS + PL） | sum by(flow_schema,priority_level) (apiserver_flowcontrol_current_executing_requests) | 按 FS + PL 或 Instance + FS + PL 维度统计 APF 当前正在执行的请求数量。 |
| APF 当前执行请求数量（维度：Instance + FS + PL） | sum by(instance,flow_schema,priority_level)(apiserver_flowcontrol_current_executing_requests) |  |
| APF 当前在队列中待处理请求数量（维度：FS + PL） | sum by(flow_schema,priority_level) (apiserver_flowcontrol_current_inqueue_requests) | 按 FS + PL 或 Instance + FS + PL 维度统计当前队列中待处理的请求数量。 |
| APF 当前队列中待处理请求数量（维度：Instance + FS + PL） | sum by(instance,flow_schema,priority_level) (apiserver_flowcontrol_current_inqueue_requests) |  |
| APF 名义并发限制席位数量 | sum by(instance,priority_level) (apiserver_flowcontrol_nominal_limit_s
