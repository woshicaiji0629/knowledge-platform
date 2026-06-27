ackend DB 总大小，即 etcd 后端数据库总大小。 |
| etcd_mvcc_db_total_size_in_use_in_bytes | etcd Backend DB 实际使用大小，即 etcd 后端数据库实际使用大小。 |  |
| kv 总数 | etcd_debugging_mvcc_keys_total | etcd 集群 KV 对（键对）总数。 |
| backend commit 延迟 | histogram_quantile(0.99, sum(rate(etcd_disk_backend_commit_duration_seconds_bucket{job="etcd"}[5m])) by (instance, le)) | 后端 Commit 时延，即 Proposal 在 etcd 数据库完成持久化存储所需要的时间。 |
| raft proposal 情况 | rate(etcd_server_proposals_failed_total{job="etcd"}[1m]) | Raft Proposal 提交失败的速率（分钟）。 |
| etcd_server_proposals_pending{job="etcd"} | Pending 的 Raft Proposal 总数。 |  |
| etcd_server_proposals_committed_total{job="etcd"} - etcd_server_proposals_applied_total{job="etcd"} | Raft Proposal 中，Committed 和 Applied 的数量差值，即已提交但尚未执行的 Proposal 数量。 |  |
