| 指标 | 类型 | 说明 |
| --- | --- | --- |
| cpu_utilization_core | Gauge | CPU 使用量。单位：核（Core）。 |
| etcd_server_has_leader | Gauge | etcd 基于 Raft 实现一致性算法。在 Raft 中，etcd 会将集群中的某个成员（Member）选举为“Leader”，即主节点，而其他成员则作为“Follower”，即从节点。Leader 会定期向所有 Member 发送心跳，以保持集群稳定。 此指标表示 etcd Member 中是否存在 Leader。 1：有主节点。 0：没有主节点。 |
| etcd_server_is_leader | Gauge | etcd Member 是否是 Leader。 1：是。 0：不是。 |
| etcd_server_leader_changes_seen_total | Counter | 过去一段时间内，etcd Member 的切主次数，即 Leader 更换的次数。 |
| etcd_mvcc_db_total_size_in_bytes | Gauge | etcd Member Database（数据库）的总大小。 |
| etcd_mvcc_db_total_size_in_use_in_bytes | Gauge | etcd Member Database 的实际使用大小。 |
| etcd_disk_backend_commit_duration_seconds_bucket | Histogram | etcd 后端 commit 延时，即在 etcd 中，数据变更写入到存储后端并成功提交（commit）所花费的时间。 Bucket 阈值为 [0.001, 0.002, 0.004, 0.008, 0.016, 0.032, 0.064, 0.128, 0.256, 0.512, 1.024, 2.048, 4.096, 8.192] 。 |
| etcd_debugging_mvcc_keys_total | Gauge | etcd 中存储的所有键（Key）的数量 |
| etcd_server_proposals_committed_total | Gauge | etcd 基于 Raft 实现一致性算法。在 Raft 中，任何试图更改系统状态的动作都以提案（Proposal）的形式被提出。 此指标指在 etcd 中，成功提交到 Raft 日志中的 Proposal 数量。 |
| etcd_server_proposals_applied_total | Gauge | 成功应用或执行（Apply）的 Proposal 数量。 |
| etcd_server_proposa
