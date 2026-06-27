### 集群架构代理模式与读写分离架构的分片规格
以下规格适用于集群架构代理模式与读写分离架构实例。
表 2.集群架构代理模式与读写分离架构的分片规格

| 规格名称 | 规格代码（API 使用） | CPU 核数 | 持久内存（GB） | ESSD 云盘（GB） | 带宽 | 最大连接数 | QPS 参考值 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 GB | tair.scm.with.proxy.standard.1m.4d | 3 | 8 | 24 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 8 GB | tair.scm.with.proxy.standard.2m.8d | 3 | 8 | 24 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 16 GB | tair.scm.with.proxy.standard.4m.16d | 3 | 16 | 48 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 32 GB | tair.scm.with.proxy.standard.8m.32d | 3 | 32 | 96 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
| 64 GB | tair.scm.with.proxy.standard.16m.64d | 3 | 64 | 192 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |

说明
集群架构代理模式不支持4 GB规格。
集群架构代理模式与读写分离架构实例的最大连接数不直接与分片规格相关，具体计算规则参考[最大连接数说明](persistent-memory-type.md)。
