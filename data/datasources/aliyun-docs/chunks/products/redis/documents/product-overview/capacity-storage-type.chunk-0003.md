### SSD型集群架构代理模式的分片规格
以下规格适用于集群架构代理模式的磁盘（SSD）型实例。

| 规格名称 | 规格代码（API 使用） | CPU 核数 | 内存（GB） | 存储容量（GB） | 最大连接数 | 带宽 |
| --- | --- | --- | --- | --- | --- | --- |
| 4C-32GB | tair.localssd.c1m8.with.proxy.xlarge | 4 | 32 | 640 | 60,000 | 1,500 Mbps（187.5 MB/s） |
| 8C-64GB | tair.localssd.c1m8.with.proxy.2xlarge | 8 | 64 | 1,280 | 60,000 | 2,500 Mbps（312.5 MB/s） |
| 16C-128GB | tair.localssd.c1m8.with.proxy.4xlarge | 16 | 128 | 2,560 | 60,000 | 5,000 Mbps（625 MB/s） |
| 32C-256GB | tair.localssd.c1m8.with.proxy.8xlarge | 32 | 256 | 5,120 | 100,000 | 10,000 Mbps（1,250 MB/s） |

说明
集群架构代理模式与读写分离架构实例的最大连接数不直接与分片规格相关，具体计算规则参考[最大连接数计算规则](capacity-storage-type.md)。
