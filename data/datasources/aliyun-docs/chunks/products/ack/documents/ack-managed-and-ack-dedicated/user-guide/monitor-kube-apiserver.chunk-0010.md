## 关键指标
可观测性展示功能解析

| 名称 | PromQL | 说明 |
| --- | --- | --- |
| API QPS | sum(irate(apiserver_request_total[$interval])) | API Server 的总 QPS。 |
| 读请求成功率 | sum(irate(apiserver_request_total{code=~"20.*",verb=~"GET|LIST"}[$interval]))/sum(irate(apiserver_request_total{verb=~"GET|LIST"}[$interval])) | API Server 处理读请求的成功率。 |
| 写请求成功率 | sum(irate(apiserver_request_total{code=~"20.*",verb!~"GET|LIST|WATCH|CONNECT"}[$interval]))/sum(irate(apiserver_request_total{verb!~"GET|LIST|WATCH|CONNECT"}[$interval])) | API Server 处理写请求的成功率。 |
| 在处理读请求数量 | sum(apiserver_current_inflight_requests{requestKind="readOnly"}) | API Server 当前在处理的读请求数量。 |
| 在处理写请求数量 | sum(apiserver_current_inflight_requests{requestKind="mutating"}) | API Server 当前在处理的写请求数量。 |
| 请求限流速率 | sum(irate(apiserver_dropped_requests_total[$interval])) | Dropped Request Rate。 API Server 限流策略过程中，主动丢弃掉的请求数所占总请求数的比例。 |
