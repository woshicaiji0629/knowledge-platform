## 客户端分析
可观测性展示功能解析

| 名称 | PromQL | 说明 |
| --- | --- | --- |
| 按 Client 维度分析 QPS | sum(irate(apiserver_request_total{client!=""}[$interval])) by (client) | 按 Client 维度分析 QPS。用于分析访问 API Server 的客户端以及 QPS。 |
| 按 Verb+Resource+Client 维度分析 QPS | sum(irate(apiserver_request_total{client!="",verb=~"$verb", resource=~"$resource"}[$interval]))by(verb,resource,client) | 按 Verb+Resource+Client 维度分析 QPS。 |
| 按 Verb+Resource+Client 维度分析 LIST 请求 QPS（无 resourceVersion 字段） | sum(irate(apiserver_request_no_resourceversion_list_total[$interval]))by(resource,client) | 按 Verb+Resource+Client 维度分析 LIST 请求的 QPS（无 resourceVersion 字段）。 可以分析对 API Server 的全部 LIST 请求中、到 etcd 的部分 LIST 请求，帮助识别以及优化 API Server 客户端的 LIST 行为。 |
