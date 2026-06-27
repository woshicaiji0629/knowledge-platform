### 大数据存储密集型实例规格族d3s
规格族介绍：实例配备12 TB大容量、高吞吐SATA HDD本地盘，辅以最大64 Gbit/s实例间网络带宽。
适用场景：
Hadoop MapReduce、HDFS、Hive、HBase等大数据计算和存储业务场景。
Spark内存计算、MLlib等机器学习场景。
ElasticSearch、Kafka等搜索和日志数据处理场景。
支持在线更换坏盘，支持热插拔坏盘，避免导致实例停机。
如果单块本地盘出现故障，您会收到系统事件，确认响应事件即可发起坏盘修复流程，更多说明请参见[本地盘实例运维场景和系统事件](operations-and-maintenance-scenarios-and-system-events-for-instances-equipped-with-local-disks.md)。
重要
确认发起坏盘修复流程后，坏盘中的数据不可恢复。
计算：
处理器：2.7 GHz主频的®Xeon®可扩展处理器（Ice Lake），全核睿频3.5 GHz，计算性能稳定。
存储：
I/O优化实例。
支持的云盘类型：ESSD云盘和ESSD AutoPL云盘。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
d3s包括的实例规格及指标数据如下表所示：
