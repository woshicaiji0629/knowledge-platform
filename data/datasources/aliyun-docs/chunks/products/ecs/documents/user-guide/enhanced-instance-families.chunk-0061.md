## 持久内存型实例规格族re6p
有关持久内存型实例的常见问题，请参见[实例](instance-faq.md)[FAQ](instance-faq.md)。
re6p的特点如下：
规格族介绍：
采用Intel®傲腾TM持久内存。
重要
持久内存中数据的可靠性取决于物理服务器和持久内存设备的可靠性，因此存在单点故障风险。建议您在应用层做好数据冗余，将需要长期保存的业务数据存储到云盘上，以保证应用数据的可靠性。
部分实例规格支持设置不同的持久内存使用方式（作为内存或本地SSD盘使用）。
说明
具体操作，请参见[配置使用持久内存](configure-the-usage-mode-of-persistent-memory.md)。
为Redis应用提供专用实例规格ecs.re6p-redis.<nx>large。
说明
ecs.re6p-redis.<nx>large是为Redis应用提供的专用实例规格，专用实例规格默认已将持久内存配置为内存使用，不支持重新配置为本地SSD盘使用。关于如何快速部署Redis应用，请参见[在配备持久内存的实例上部署](deploy-redis-on-persistent-memory-optimized-instances.md)[Redis](deploy-redis-on-persistent-memory-optimized-instances.md)[应用](deploy-redis-on-persistent-memory-optimized-instances.md)。
适用场景：
Redis数据库及其他NoSQL数据库（例如Cassandra、MongoDB等）。
结构化数据库（例如MySQL等）。
电商、游戏、媒体等I/O密集型应用。
Elasticsearch搜索。
视频直播、即时通讯、房间式强联网网游。
高性能关系型数据库、联机事务处理（OLTP）系统。
计算：
处理器：2.5 GHz主频的Intel®Xeon®Platinum 8269CY（Cascade Lake），睿频3.2 GHz，计算性能稳定。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)、[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-support
