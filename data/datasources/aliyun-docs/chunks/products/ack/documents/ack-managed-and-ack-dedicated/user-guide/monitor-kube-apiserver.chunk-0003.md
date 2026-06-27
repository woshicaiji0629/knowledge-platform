评估 Quorum Read 类型的 LIST 请求可以定位是否存在过多的此类请求以及发起相应请求的客户端，以便优化客户端的请求行为，提高集群性能。请求的维度包括 Group、Version、Resource、Scope 和 Client。 |
| apiserver_current_inflight_requests | Gauge | API Server 当前处理的请求数量。请求包括两种： ReadOnly：这类请求不会改变集群的状态，通常为读取资源的操作，例如获取 Pods 列表、查询节点状态等。 Mutating：这类请求会改变集群的状态，通常为创建、更新或删除资源的操作，例如新建 Pod、更新 Service 配置等。 |
| apiserver_dropped_requests_total | Counter | API Server 执行限流策略过程中，主动丢弃掉的请求数。HTTP 返回值为 429 'Try again later' 。 |
| etcd_request_duration_seconds_bucket | Histogram | 该指标用于统计 API Server 对 etcd 请求的访问时延分布。 请求的维度包括操作（Operation）和操作对象的类型（Type）。 Bucket 阈值为 {0.005, 0.025, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.25, 1.5, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 45, 60} 。单位：秒。 |
| apiserver_flowcontrol_request_concurrency_limit | Gauge | APF 请求并发限制。表示某个优先级队列的最大并发限制，即该队列理论上允许同时处理的最大请求数，供您了解 API Server 如何通过流量控制策略将资源分配给不同优先级的队列，从而确保高优先级请求可以及时处理。 该指标在 Kubernetes 1.30 版本变为 Deprecated，自 1.31 版本起移除，1.31 及以上版本的集群中建议使用 apiserver_flowcontrol_nominal_limit_seats 指标代替。 |
| apiserver_flowcontrol_current_executing_requests | Gauge | 某个优先级队列中当前正在执行的请求数量，即该队列的实际并发负载，供您了解 API Server 的实际负载情况，判断是否接近系统最大并发限制，防止过载。 |
| apiserver_flowcontrol_current_inqueue_requests | Gauge | 某个优先级队列中当前在队列中等待处理的请求数量，即该队列的
