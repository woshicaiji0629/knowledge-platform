### 非集群架构（标准架构）的分片规格
非集群架构即为标准架构，以下规格适用于非集群架构的云原生实例。
说明
若标准架构开启读写分离，请参见下方[读写分离架构的分片规格](instance-types-of-cloud-native-community-edition-instances.md)。

| 规格名称 | 规格代码（API 使用） | CPU 核数 | 内存（GB） | ESSD 云盘（GB） | 带宽 | 最大连接数 | QPS 参考值 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 256 MB | redis.shard.micro.ce | 3 | 0.25 | 1 | 192 Mbps（24 MB/s） | 10,000 | 100,000 |
| 1 GB | redis.shard.small.2.ce | 3 | 1 | 5 | 384 Mbps（48 MB/s） | 10,000 | 100,000 |
| 2 GB | redis.shard.mid.2.ce | 3 | 2 | 10 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 4 GB | redis.shard.large.ce | 3 | 4 | 20 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 8 GB | redis.shard.xlarge.ce | 3 | 8 | 40 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 16 GB | redis.shard.2xlarge.ce | 3 | 16 | 80 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 24 GB | redis.shard.3xlarge.ce | 3 | 24 | 120 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
| 32 GB | redis.shard.4xlarge.ce | 3 | 32 | 160 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
| 64 GB | redis.shard.8xlarge.ce | 3 | 64 | 320 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
