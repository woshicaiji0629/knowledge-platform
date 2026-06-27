### 通用平衡增强型实例规格族g6e
规格族介绍：依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。
适用场景：
高网络包收发场景，例如视频弹幕、电信业务转发等。
各种类型和规模的企业级应用。
网站和应用服务器。
游戏服务器。
中小型数据库系统、缓存、搜索集群。
数据分析和计算。
计算集群、依赖内存的数据处理。
计算：
处理器与内存配比约为1:4。
处理器：2.5 GHz主频、3.2 GHz睿频的Intel®Xeon®Platinum 8269CY（Cascade Lake），计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
说明
该规格族不支持FreeBSD 13.2及更早版本，存在兼容性问题，请使用FreeBSD 13.3或更高版本。
该规格族的实例可能运行在不同的服务器平台，包括 Cascade Lake 或更高性能的Intel® Xeon® 可扩展处理器平台上，实际计算性能不低于基线配置（Cascade Lake平台）。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-support
