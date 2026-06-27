### 大数据存储密集型实例规格族d2s
规格族介绍：实例配备大容量、高吞吐SATA HDD本地盘，辅以最大35 Gbit/s实例间网络带宽。
适用场景：
Hadoop MapReduce、HDFS、Hive、Hbase等大数据计算和存储业务场景。
Spark内存计算、MLlib等机器学习场景。
ElasticSearch、Kafka等搜索和日志数据处理场景。
支持在线更换坏盘，支持热插拔坏盘，避免导致实例停机。
如果单块本地盘出现故障，您会收到系统事件，确认响应事件即可发起坏盘修复流程，更多说明请参见[本地盘实例运维场景和系统事件](operations-and-maintenance-scenarios-and-system-events-for-instances-equipped-with-local-disks.md)。
重要
确认发起坏盘修复流程后，坏盘中的数据不可恢复。
计算：
处理器：2.5 GHz主频的Intel®Xeon®Platinum 8163（Skylake）。
存储：
I/O优化实例。
支持的云盘类型：ESSD云盘、ESSD AutoPL云盘、SSD云盘和高效云盘。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
d2s包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | 本地存储 | 网络基础带宽（Gbit/s） | 网络收发包 PPS（万） |
| --- | --- | --- | --- | --- | --- |
| ecs.d2s.5xlarge | 20 | 88.0 | 8 * 7838 GB (8 * 7300 GiB) | 12.0 | 160 |
| ecs.d2s.10xlarge | 40 | 176.0 | 15 * 7838 GB (15 * 7300 GiB) | 20.0 | 200 |
| ecs.d2s.20xlarge | 80 | 352.0 | 30 * 7838 GB (30 * 7300 GiB) | 35.0 | 450 |
