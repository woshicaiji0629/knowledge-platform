### Raft Proposal异常

| 正常情况 | 异常情况 | 异常说明 |
| --- | --- | --- |
| Raft Proposal Failed 速率为 0。 | raft proposal failed 大于 0。 | 有 Raft Proposal 提交失败。如果此值较大，需进一步排查。 |
| Pending 的 Raft Proposal 总数为 0。 | Pending 的 Raft Proposal 总数大于 0。 | 提交的 Raft Proposal 有积压，一般是由于 Apply 速度较慢，可结合后端 Commit 时延进行分析。 |
| Raft Proposal 的 Committed 和 Applied 数量差值为 0。 | Committed 和 Applied 数量差值大于 0。 | 客户端请求过多，etcd 压力较大。 若此值大于 5000，etcd 会拒绝接后续的请求，并返回 too many requests ，直至积压的 Proposal 全部处理完毕。 |
