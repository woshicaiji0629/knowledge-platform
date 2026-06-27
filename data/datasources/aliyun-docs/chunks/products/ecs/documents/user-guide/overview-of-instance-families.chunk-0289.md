### 安全增强计算型实例规格族c6t
规格族介绍：
依托TPM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。
支持完整监控，提供IaaS层可信能力。
依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。
适用场景：
高安全可信要求场景，例如金融、政务、企业等。
高网络包收发场景，例如视频弹幕、电信业务转发等。
Web前端服务器。
大型多人在线游戏（MMO）前端。
数据分析、批量计算、视频编码。
高性能科学和工程应用。
计算：
处理器与内存配比约为1:2。
处理器：2.5 GHz主频、3.2 GHz睿频的Intel®Xeon®Platinum 8269CY（Cascade Lake），计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
c6t包括的实例规格及指标数据如下表所示：
