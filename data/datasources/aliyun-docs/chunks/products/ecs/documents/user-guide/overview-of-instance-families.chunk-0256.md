### 网络增强通用型实例规格族g7nex
规格族介绍：依托第四代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。
适用场景：
网络密集型应用场景，例如NFV/SD-WAN、移动互联网、视频弹幕、电信业务转发等。
中小型数据库系统、缓存、搜索集群。
各种类型和规模的企业级应用。
计算：
处理器与内存配比为1:4。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)）。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](jumbo-frame.md)。
大幅提升单实例的网络带宽能力和网络收发包能力，单实例最高支持3000万PPS网络收发包能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
g7nex包括的实例规格及指标数据如下表所示
