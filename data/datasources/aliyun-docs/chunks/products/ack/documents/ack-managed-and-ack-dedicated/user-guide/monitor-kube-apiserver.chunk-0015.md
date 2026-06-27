al{verb!~"GET|LIST|WATCH",verb=~"$verb",resource=~"$resource",code!~"2.*"}[$interval])) by (verb,resource,code) | 统计非 2xx 返回值（除成功以外的所有情况，例如 4xx、5xx 等）的写请求 QPS。 |
| Apiserver 对 etcd 请求时延 | histogram_quantile($quantile, sum(irate(etcd_request_duration_seconds_bucket[$interval])) by (le,operation,type,instance)) | 统计 API Server 对 etcd 的请求时延。 |
