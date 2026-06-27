### 集群架构代理模式与读写分离架构的分片规格
以下规格适用于集群架构代理模式与读写分离架构的云原生实例。

| 规格名称 | 规格代码（API 使用） | CPU 核数 | 内存（GB） | ESSD 云盘（GB） | 带宽 | 最大连接数 | QPS 参考值 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 GB | redis.shard.with.proxy.small.ce | 3 | 1 | 5 | 384 Mbps（48 MB/s） | 10,000 | 100,000 |
| 2 GB | redis.shard.with.proxy.mid.ce | 3 | 2 | 10 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 4 GB | redis.shard.with.proxy.large.ce | 3 | 4 | 20 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 8 GB | redis.shard.with.proxy.xlarge.ce | 3 | 8 | 40 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 16 GB | redis.shard.with.proxy.2xlarge.ce | 3 | 16 | 80 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 24 GB | redis.shard.with.proxy.3xlarge.ce | 3 | 24 | 120 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
| 32 GB | redis.shard.with.proxy.4xlarge.ce | 3 | 32 | 160 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
| 64 GB | redis.shard.with.proxy.8xlarge.ce | 3 | 64 | 320 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |

说明
集群架构代理模式与读写分离架构实例的最大连接数不直接与分片规格相关，具体计算规则参考[最大连接数说明](instance-types-of-cloud-native-community-edition-instances.md)。
