### etcd存活状态

| 正常情况 | 异常情况 | 异常说明 |
| --- | --- | --- |
| 3 个 etcd Member 都有 Leader，且其中之一必须为 Leader，即 sum(etcd_server_has_leader)=3 ，且仅有一个 member etcd_server_is_leader == 1 。 | 单个 Member 异常。 | 对应的 member etcd_server_has_leader!=1 ，不影响整体 etcd 集群对外提供服务。 |
| 大于 1 个 Member 异常。 | 多个 member etcd_server_has_leader!=1 ，Member 异常大于 1，此时 etcd 集群无法对外提供服务。 同时，请观察是否存在 Member 的 etcd_server_is_leader == 1 。如果没有，etcd 则处于无主状态，无法对外提供服务。 |  |
