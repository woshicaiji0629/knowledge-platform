### 本地SSD型实例规格族i2
规格族介绍：配备高性能（高IOPS、大吞吐、低访问延迟）NVMe SSD本地盘。
适用场景：OLTP、高性能关系型数据库；NoSQL数据库（例如Cassandra、MongoDB、HBase等）；Elasticsearch等搜索场景。
计算：
处理器与内存配比为1:8，为高性能数据库等场景设计。
处理器：2.5 GHz主频的Intel®Xeon®Platinum 8163（Skylake）。
存储：
I/O优化实例。
支持的云盘类型：SSD云盘和高效云盘。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
i2包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | 本地存储 | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 云盘带宽（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- |
| ecs.i2.xlarge | 4 | 32 | 1 * 959 GB (1 * 894 GiB) | 1 | 50 万 | 最高 16 |
| ecs.i2.2xlarge | 8 | 64 | 1 * 1919 GB (1 * 1788 GiB) | 2 | 100 万 | 最高 16 |
| ecs.i2.4xlarge | 16 | 128 | 2 * 1919 GB (2 * 1788 GiB) | 3 | 150 万 | 最高 16 |
| ecs.i2.8xlarge | 32 | 256 | 4 * 1919 GB (4 * 1788 GiB) | 6 | 200 万 | 最高 16 |
| ecs.i2.16xlarge | 64 | 512 | 8 * 1919 GB (8 * 1788 GiB) | 10 | 400 万 | 最高 16 |
