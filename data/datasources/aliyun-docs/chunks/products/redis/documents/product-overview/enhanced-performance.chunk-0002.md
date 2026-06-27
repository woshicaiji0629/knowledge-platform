### 集群架构代理模式与读写分离架构的分片规格
以下规格适用于集群架构代理模式与读写分离架构实例。
表 2.集群架构代理模式与读写分离架构的分片规格

| 规格名称 | 规格代码（API 使用） | CPU 核数 | 内存（GB） | ESSD 云盘（GB） | 带宽 | 最大连接数 | QPS 参考值 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 GB | tair.rdb.with.proxy.1g | 7 | 1 | 5 | 768 Mbps（96 MB/s） | 30,000 | 300,000 |
| 2 GB | tair.rdb.with.proxy.2g | 7 | 2 | 10 | 768 Mbps（96 MB/s） | 30,000 | 300,000 |
| 4 GB | tair.rdb.with.proxy.4g | 7 | 4 | 20 | 768 Mbps（96 MB/s） | 40,000 | 300,000 |
| 8 GB | tair.rdb.with.proxy.8g | 7 | 8 | 40 | 768 Mbps（96 MB/s） | 40,000 | 300,000 |
| 16 GB | tair.rdb.with.proxy.16g | 7 | 16 | 80 | 768 Mbps（96 MB/s） | 40,000 | 300,000 |
| 24 GB | tair.rdb.with.proxy.24g | 7 | 24 | 120 | 768 Mbps（96 MB/s） | 50,000 | 300,000 |
| 32 GB | tair.rdb.with.proxy.32g | 7 | 32 | 160 | 768 Mbps（96 MB/s） | 50,000 | 300,000 |
| 64 GB | tair.rdb.with.proxy.64g | 7 | 64 | 320 | 768 Mbps（96 MB/s） | 50,000 | 300,000 |

说明
集群架构代理模式与读写分离架构实例的最大连接数不直接与分片规格相关，具体计算规则参考[最大连接数说明](enhanced-performance.md)。
