### 性能增强型本地盘实例规格族i4p
规格族介绍：基于Intel®第二代傲腾持久内存（BPS），提供性能极高的本地盘，初始化本地盘的具体操作，请参见[将持久内存初始化为本地盘](configure-the-usage-mode-of-persistent-memory.md)。
适用场景：
基因测序类应用，详情请参见[案例说明](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20220706/misz/客户案例-寻因生物.pdf)。
磁盘类KV型数据库，例如RocksDB、ClickHouse。
OLTP、高性能关系型数据库进行WAL优化等。
NoSQL数据库，例如Cassandra、MongoDB、HBase。
Elasticsearch等搜索场景。
其他频繁将数据写入磁盘的I/O密集型应用，例如消息中间件、容器。
计算：
处理器与内存配比为1:4。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake ），基频2.7 GHz，全核睿频3.2 GHz，计算性能稳定。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
i4p包括的实例规格及指标数据如下表所示：
