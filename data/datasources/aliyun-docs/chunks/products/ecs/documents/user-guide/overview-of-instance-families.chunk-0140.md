### 内存型实例规格族r7p
规格族介绍：
基于持久内存技术，提供性价比更高的内存介质。
说明
本规格族提供的内存混合了普通内存与持久内存。建议您在上线应用前进行充分的测试，必要的时候，需要对应用进行适当改造以获得最佳的性价比。
依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。
适用场景：
内存型数据库，例如Redis。关于如何快速部署Redis应用，请参见[在配备持久内存的实例上部署](deploy-redis-on-persistent-memory-optimized-instances.md)[Redis](deploy-redis-on-persistent-memory-optimized-instances.md)[应用](deploy-redis-on-persistent-memory-optimized-instances.md)。
需要大容量Page Cache的应用，例如RocketMQ等消息中间件。
数据分析与挖掘、分布式内存缓存。
Hadoop集群、Spark集群以及其他企业大内存需求应用。
计算：
处理器与内存（内存+持久内存）配比约为1:12。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)）。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supp
