### Cluster management
Cluster命令族的命令不适用于标准架构。
通过代理节点连接实例时，会兼容支持部分Cluster命令族的命令，具体为CLUSTER INFO、CLUSTER KEYSLOT、CLUSTER NODES、CLUSTER SLAVES、CLUSTER SLOTS。

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| CLUSTER ADDSLOTS | ❌ | ❌ | ❌ |
| CLUSTER ADDSLOTSRANGE | ➖ | ➖ | ❌ |
| CLUSTER BUMPEPOCH | ❌ | ❌ | ❌ |
| CLUSTER COUNT-FAILURE-REPORTS | ❌ | ❌ | ❌ |
| CLUSTER COUNTKEYSINSLOT ① | ❌ | ❌ | ❌ |
| CLUSTER DELSLOTS | ❌ | ❌ | ❌ |
| CLUSTER DELSLOTSRANGE | ➖ | ➖ | ❌ |
| CLUSTER FAILOVER | ❌ | ❌ | ❌ |
| CLUSTER FLUSHSLOTS | ❌ | ❌ | ❌ |
| CLUSTER FORGET | ❌ | ❌ | ❌ |
| CLUSTER GETKEYSINSLOT | ❌ | ❌ | ❌ |
| CLUSTER INFO ① | ✔️ | ✔️ | ✔️ |
| CLUSTER KEYSLOT ① | ✔️ | ✔️ | ✔️ |
| CLUSTER LINKS | ➖️ | ➖️ | ❌ |
| CLUSTER MEET | ❌ | ❌ | ❌ |
| CLUSTER MYID | ❌ | ❌ | ❌ |
| CLUSTER NODES ① | ✔️ | ✔️ | ✔️ |
| CLUSTER REPLICAS | ❌ | ❌ | ❌ |
| CLUSTER REPLICATE | ❌ | ❌ | ❌ |
| CLUSTER RESET | ❌ | ❌ | ❌ |
| CLUSTER SAVECONFIG | ❌ | ❌ | ❌ |
| CLUSTER SET-CONFIG-EPOCH | ❌ | ❌ | ❌ |
| CLUSTER SETSLOT | ❌ | ❌ | ❌ |
| CLUSTER SHARDS | ➖ | ➖ | ✔️ |
| CLUSTER SLAVES | ❌ | ❌ | ❌ |
| CLUSTER SLOTS | ✔️ | ✔️ | ✔️ |
| READONLY | ✔️️ | ✔️ | ✔️ |
| READWRITE | ✔️ | ✔️ | ✔️ |
