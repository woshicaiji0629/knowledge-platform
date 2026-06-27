| 名称 | PromQL | 说明 |
| --- | --- | --- |
| etcd 存活状态 | etcd_server_has_leader etcd_server_is_leader == 1 | etcd Member 是否存活。正常值为 3。 etcd Member 是否是主节点。正常情况下，必须有一个 Member 为主节点。 |
| 过去一天切主次数 | changes(etcd_server_leader_changes_seen_total{job="etcd"}[1d]) | 过去一天内 etcd 集群切主次数，即 Leader 更换的次数。 |
| 内存使用量 | memory_utilization_byte{container="etcd"} | 内存使用量。单位：字节。 |
| CPU 使用量 | cpu_utilization_core{container="etcd"}*1000 | CPU 使用量。单位：毫核。 |
| 内存资源水位 | resource_utilization_level{resource="memory",container="etcd",utilization_level="high"} resource_utilization_level{resource="memory",container="etcd",utilization_level="normal"} | 当 resource_utilization_level{utilization_level="high",...} == 1，表明容器资源利用率（水位）>= 80%。 当 resource_utilization_level{utilization_level="normal",...} == 1，表明容器资源利用率（水位）< 80%。 |
| CPU 资源水位 | resource_utilization_level{resource="cpu",container="etcd",utilization_level="high"} resource_utilization_level{resource="cpu",container="etcd",utilization_level="normal"} |  |
| 磁盘大小 | etcd_mvcc_db_total_size_in_bytes | etcd Backend DB 总大小，即 etcd 后端数据库总大小。 |
| etcd_mvcc_db_total_size_in_use_in_bytes | etcd Backend DB 实际使用大小，即 etcd 后端数据库实际使用大小。 |  |
| kv 总数 | etcd_debugging_mvcc_keys_
