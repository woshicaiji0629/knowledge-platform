### 内存型实例规格族r7
规格族介绍：依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。
适用场景：
高性能数据库、内存数据库。
高网络包收发场景，例如视频弹幕、电信业务转发等。
数据分析与挖掘、分布式内存缓存。
Hadoop、Spark集群以及其他企业大内存需求应用。
安全可信计算场景。
计算：
处理器与内存配比为1:8
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定
支持开启或关闭超线程配置
说明
该规格族的实例可能运行在不同的服务器平台，包括 Ice Lake 或更高性能的Intel® Xeon® 可扩展处理器平台上，实际计算性能不低于基线配置（Ice Lake平台）。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)）。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](jumbo-frame.md)。
具备超高网络收发包PPS能力。
小规格实例网络带宽具备突发能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
安全：
支持可信计算（vTPM）特性。更多信息，请参见[可信计算能力概述](overview-of-trusted-
