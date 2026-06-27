## 分片规格
倚天版实例仅支持非集群（主备）架构，规格性能如下。

| 规格名称 | 规格代码（API 使用） | CPU 核数 | 内存（GB） | ESSD 云盘（GB） | 带宽 | 最大连接数 | QPS 参考值 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 GB（ 倚天版 ） | redis.shard.small.y.ee | 2 | 1 | 1 | 384 Mbps（48 MB/s） | 10,000 | 100,000 |
| 2 GB（ 倚天版 ） | redis.shard.mid.y.ee | 2 | 2 | 1 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 4 GB（ 倚天版 ） | redis.shard.large.y.ee | 2 | 4 | 1 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 8 GB（ 倚天版 ） | redis.shard.xlarge.y.ee | 2 | 8 | 1 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 16 GB（ 倚天版 ） | redis.shard.2xlarge.y.ee | 2 | 16 | 1 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 24 GB（ 倚天版 ） | redis.shard.3xlarge.y.ee | 2 | 24 | 1 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 32 GB（ 倚天版 ） | redis.shard.4xlarge.y.ee | 2 | 32 | 1 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 64 GB（ 倚天版 ） | redis.shard.8xlarge.y.ee | 2 | 64 | 1 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |

说明
ESSD云盘仅用于实例运行、存储日志，不作为数据存储的介质。
