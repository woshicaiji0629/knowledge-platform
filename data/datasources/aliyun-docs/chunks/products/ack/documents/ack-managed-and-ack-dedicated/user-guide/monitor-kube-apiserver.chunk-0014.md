| 名称 | PromQL | 说明 |
| --- | --- | --- |
| 按 Verb 维度分析 QPS | sum(irate(apiserver_request_total{verb=~"$verb"}[$interval]))by(verb) | 按 Verb 维度，统计单位时间（1s）内的请求 QPS。 |
| 按 Verb+Resource 维度分析 QPS | sum(irate(apiserver_request_total{verb=~"$verb",resource=~"$resource"}[$interval]))by(verb,resource) | 按 Verb+Resource 维度，统计单位时间（1s）内的请求 QPS。 |
| 按 Verb 维度分析请求时延 | histogram_quantile($quantile, sum(irate(apiserver_request_duration_seconds_bucket{verb=~"$verb", verb!~"WATCH|CONNECT",resource!=""}[$interval])) by (le,verb)) | 按 Verb 维度，分析请求时延。 |
| 按 Verb+Resource 维度分析请求时延 | histogram_quantile($quantile, sum(irate(apiserver_request_duration_seconds_bucket{verb=~"$verb", verb!~"WATCH|CONNECT", resource=~"$resource",resource!=""}[$interval])) by (le,verb,resource)) | 按 Verb+Resource 维度，分析请求时延。 |
| 非 2xx 返回值的读请求 QPS | sum(irate(apiserver_request_total{verb=~"GET|LIST",resource=~"$resource",code!~"2.*"}[$interval])) by (verb,resource,code) | 统计非 2xx 返回值（除成功以外的所有情况，例如 4xx、5xx 等）的读请求 QPS。 |
| 非 2xx 返回值的写请求 QPS | sum(irate(apiserver_request_total{verb!~"GET|LIST|WATCH",verb=~"$verb",resource=~"$resource",code!~"2.*"}[$interval])) by (verb,resource,code) | 统计非 2xx 返回值（除成功以外的所有情况，例如 4xx、5xx 等）的写请求 QPS。
