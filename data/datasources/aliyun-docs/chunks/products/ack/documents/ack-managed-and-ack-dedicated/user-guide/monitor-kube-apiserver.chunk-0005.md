mize-ack-pro-control-plane-component-parameters-1693464061811.md) 。 |
| apiserver_flowcontrol_current_inqueue_seats | Gauge | APF 当前队列中席位数量，表示某个优先级队列中当前等待处理的请求数对应的席位数量，反映了当前队列中等待处理的请求所占用的资源，以供您了解队列的积压情况。 |
| apiserver_flowcontrol_request_execution_seconds_bucket | Histogram | 请求的实际执行时间，记录了请求从开始执行到最终完成所花费的时间。 时间区间分布为{0, 0.005, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 15, 30}。单位：秒。 |
| apiserver_flowcontrol_request_wait_duration_seconds_bucket | Histogram | 请求在队列中等待的时间分布，记录了请求从进入队列到开始执行之间的等待时间 时间区间分布为{0, 0.005, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 15, 30}。单位：秒。 |
| apiserver_flowcontrol_dispatched_requests_total | Counter | 成功调度并处理的请求数量，反映了 API Server 成功处理的请求总数。 |
| apiserver_flowcontrol_rejected_requests_total | Counter | 因超出并发限制或队列容量而被拒绝的请求数量。 |
| apiserver_admission_controller_admission_duration_seconds_bucket | Histogram | 准入控制器（Admission Controller）的处理延时。标签包括 Admission Controller 名称、操作（CREATE、UPDATE、CONNECT 等）、API 资源、操作类型（validate 或 admit）和请求是否被拒绝（true 或 false）。 Bucket 阈值为 {0.005, 0.025, 0.1, 0.5, 2.5} 。单位：秒。 |
| apiserver_admission_webhook_admission_duration_seconds_bucket | Histogram | 准入 Webhook（Admission Webhook）的处理延时。标签包括 Admission Controller 名称、操作（CREATE、UPDATE、CONNECT 等
