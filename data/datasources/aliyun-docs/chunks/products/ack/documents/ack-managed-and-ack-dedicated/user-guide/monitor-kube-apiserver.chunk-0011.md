| 名称 | PromQL | 说明 |
| --- | --- | --- |
| GET 读请求时延 | histogram_quantile($quantile, sum(irate(apiserver_request_duration_seconds_bucket{verb="GET",resource!="",subresource!~"log|proxy"}[$interval])) by (pod, verb, resource, subresource, scope, le)) | 展示 GET 请求的响应时间，维度包括 API Server Pod、Verb（GET）、Resources、Scope。 |
| LIST 读请求时延 | histogram_quantile($quantile, sum(irate(apiserver_request_duration_seconds_bucket{verb="LIST"}[$interval])) by (pod_name, verb, resource, scope, le)) | 展示 LIST 请求的响应时间，维度包括 API Server Pod、Verb（LIST）、Resources、Scope。 |
| 写请求时延 | histogram_quantile($quantile, sum(irate(apiserver_request_duration_seconds_bucket{verb!~"GET|WATCH|LIST|CONNECT"}[$interval])) by (cluster, pod_name, verb, resource, scope, le)) | 展示 Mutating 请求的响应时间，维度包括 API Server Pod、Verb（GET、WATCH、LIST、CONNECT）、Resources、Scope。 |
| 在处理读请求数量 | apiserver_current_inflight_requests{request_kind="readOnly"} | API Server 正在处理的读请求数量。 |
| 在处理写请求数量 | apiserver_current_inflight_requests{request_kind="mutating"} | API Server 正在处理的写请求数量。 |
| 请求限流速率 | sum(irate(apiserver_dropped_requests_total{request_kind="readOnly"}[$interval])) by (name) sum(irate(apiserver_dropped_requests_total{request_kind="mutating"}[$
