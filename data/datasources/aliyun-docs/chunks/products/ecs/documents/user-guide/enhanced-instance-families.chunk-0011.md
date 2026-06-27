## 存储增强通用型实例规格族g7se
规格族介绍：依托第三代神龙架构，采用Ice Lake处理器，全面优化了存储I/O性能。
适用场景：I/O密集型业务场景（例如中大型OLTP类核心数据库），中大型NoSQL数据库，搜索、实时日志分析，大型企业级商用软件（例如SAP）。
计算：
处理器与内存配比为1:4。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.9 GHz，全核睿频3.5 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
最多支持挂载64块数据盘。创建实例时最多挂载16块数据盘，如果实例需要更多数据盘，请在创建实例后继续挂载。具体操作，请参见[挂载数据盘](attach-a-data-disk.md)。
单实例顺序读写性能最高可达64 Gbit/s，IOPS最高可达100万。
实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
实例网络性能与实例规格
