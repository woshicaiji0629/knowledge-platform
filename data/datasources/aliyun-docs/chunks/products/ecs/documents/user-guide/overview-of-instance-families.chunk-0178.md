### 大数据计算密集型实例规格族d3c
d3c的特点如下：
规格族介绍：实例配备大容量、高吞吐本地盘，辅以最大40 Gbit/s实例间网络带宽。
适用场景：
Hadoop MapReduce、HDFS、Hive、HBase等大数据计算和存储业务场景。
EMR JindoFS配合OSS实现大数据冷热数据分层和存储计算分离的场景。
Spark内存计算、MLlib等机器学习场景。
ElasticSearch、Kafka等搜索和日志数据处理场景。
支持在线更换坏盘，支持热插拔坏盘，避免导致实例停机。
如果单块本地盘出现故障，您会收到系统事件，确认响应事件即可发起坏盘修复流程，更多说明请参见[本地盘实例运维场景和系统事件](operations-and-maintenance-scenarios-and-system-events-for-instances-equipped-with-local-disks.md)。
重要
确认发起坏盘修复流程后，坏盘中的数据不可恢复。
计算：
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），主频2.9 GHz，全核睿频3.5 GHz，计算性能稳定。
存储：
I/O优化实例。
支持的云盘类型：ESSD云盘和ESSD AutoPL云盘。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
d3c包括的实例规格及指标数据如下表所示：
