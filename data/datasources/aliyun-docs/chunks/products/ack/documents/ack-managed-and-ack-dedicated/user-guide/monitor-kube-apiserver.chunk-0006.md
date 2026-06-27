ver_admission_webhook_admission_duration_seconds_bucket | Histogram | 准入 Webhook（Admission Webhook）的处理延时。标签包括 Admission Controller 名称、操作（CREATE、UPDATE、CONNECT 等）、API 资源、操作类型（validate，校验请求的合法性，或 admit，在请求合法的情况下，决定是否允许该请求）和请求是否被拒绝（true 或 false）。 Bucket 的阈值为 {0.005, 0.025, 0.1, 0.5, 2.5} 。单位：秒。 |
| apiserver_admission_webhook_admission_duration_seconds_count | Counter | 准入 Webhook（Admission Webhook）的处理请求统计。标签包括 Admission Controller 名称、操作（CREATE、UPDATE、CONNECT 等）、API 资源、操作类型（validate 或 admit）和请求是否被拒绝（true 或 false）。 |
| cpu_utilization_core | Gauge | CPU 使用量。单位：核（Core）。 |
| memory_utilization_byte | Gauge | 内存使用量。单位：字节（Byte）。 |
| resource_utilization_level | Gauge | 资源使用水位。 resource：资源类型，包括 cpu 和 memory。 utilization_level：水位等级，high（使用率 ≥80%）或 normal（使用率 <80%）。 container：目标容器。包括 kube-apiserver、kube-scheduler、kube-controller-manager、cloud-controller-manager 和 etcd。 |
| up | Gauge | 服务可用性。 1：表示服务可用。 0：表示服务不可用。 |
