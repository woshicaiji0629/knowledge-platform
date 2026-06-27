roposal）的形式被提出。 此指标指在 etcd 中，成功提交到 Raft 日志中的 Proposal 数量。 |
| etcd_server_proposals_applied_total | Gauge | 成功应用或执行（Apply）的 Proposal 数量。 |
| etcd_server_proposals_pending | Gauge | 正在等待处理的 Proposal 数量。 |
| etcd_server_proposals_failed_total | Counter | 处理失败的 Proposal 数量。 |
| memory_utilization_byte | Gauge | 内存使用量。单位：字节（Byte）。 |
| resource_utilization_level | Gauge | 资源使用水位。 resource：资源类型，包括 cpu 和 memory。 utilization_level：水位等级，high（使用率 ≥80%）或 normal（使用率 <80%）。 container：目标容器。包括 kube-apiserver、kube-scheduler、kube-controller-manager、cloud-controller-manager 和 etcd。 |
