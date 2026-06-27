| 命令 | 集群架构 | 是否允许在集群架构的事务中执行 | 读写分离架构 | 是否允许在读写分离架构的事务中执行 |
| --- | --- | --- | --- | --- |
| CLUSTER ADDSLOTS ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER ADDSLOTSRANGE | ❌ | ❌ | ❌ | ❌ |
| CLUSTER BUMPEPOCH | ❌ | ❌ | ❌ | ❌ |
| CLUSTER COUNT-FAILURE-REPORTS ② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER COUNTKEYSINSLOT ② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER DELSLOTS ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER DELSLOTSRANGE | ❌ | ❌ | ❌ | ❌ |
| CLUSTER FAILOVER ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER FLUSHSLOTS | ❌ | ❌ | ❌ | ❌ |
| CLUSTER FORGET ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER GETKEYSINSLOT ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER INFO ② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER KEYSLOT ② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER LINKS | ❌ | ❌ | ❌ | ❌ |
| CLUSTER MEET ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER MYID | ❌ | ❌ | ❌ | ❌ |
| CLUSTER NODES ② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER REPLICAS | ❌ | ❌ | ❌ | ❌ |
| CLUSTER REPLICATE ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER RESET ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER SAVECONFIG ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER SET-CONFIG-EPOCH ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER SETSLOT ①② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER SHARDS | ❌ | ❌ | ❌ | ❌ |
| CLUSTER SLAVES ② | ✔️ | ❌ | ✔️ | ❌ |
| CLUSTER SLOTS ② | ✔️ | ❌ | ✔️ | ❌ |
| READONLY ①② | ✔️ | ❌ | ✔️️ | ❌ |
| READWRIT
