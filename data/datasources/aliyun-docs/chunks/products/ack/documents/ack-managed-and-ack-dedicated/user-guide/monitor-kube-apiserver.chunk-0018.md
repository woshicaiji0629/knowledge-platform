,priority_level) (apiserver_flowcontrol_current_inqueue_requests) |  |
| APF 名义并发限制席位数量 | sum by(instance,priority_level) (apiserver_flowcontrol_nominal_limit_seats) | 按 Instance + PL 维度统计 APF 席位数量的相关指标。包括以下指标： 名义并发限制：不同优先级队列的名义最大并发席位限制。 当前并发限制：不同优先级队列中，在动态调整后实际允许的最大并发席位数量。 在执行：不同优先级队列中当前正在执行的请求数对应的席位数量。 队列中：不同优先级队列中排队中的请求数对应的席位数量。 |
| APF 当前并发限制席位数量 | sum by(instance,priority_level) (apiserver_flowcontrol_current_limit_seats) |  |
| APF 当前在执行的席位数量 | sum by(instance,priority_level) (apiserver_flowcontrol_current_executing_seats) |  |
| APF 当前队列中席位数量 | sum by(instance,priority_level) (apiserver_flowcontrol_current_inqueue_seats) |  |
| APF 请求执行时间 | histogram_quantile($quantile, sum(irate(apiserver_flowcontrol_request_execution_seconds_bucket[$interval])) by (le,instance, flow_schema,priority_level)) | 请求从开始执行到最终完成所花费的时间。 |
| APF 请求等待时间 | histogram_quantile($quantile, sum(irate(apiserver_flowcontrol_request_wait_seconds_bucket[$interval])) by (le,instance, flow_schema,priority_level)) | 请求从进入队列到开始执行之间的等待时间。 |
| APF 成功调度并处理的请求 QPS | sum(irate(apiserver_flowcontrol_dispatched_requests_total[$interval]))by(instance,flow_schema,priority_level) | 成功调度并处理的请求 QPS。 |
| APF 拒绝请求 QPS | sum(ira
