QPS | sum(irate(apiserver_flowcontrol_dispatched_requests_total[$interval]))by(instance,flow_schema,priority_level) | 成功调度并处理的请求 QPS。 |
| APF 拒绝请求 QPS | sum(irate(apiserver_flowcontrol_rejected_requests_total[$interval]))by(instance,flow_schema,priority_level) | 因超出并发限制或队列容量而被拒绝的请求 QPS。 |
