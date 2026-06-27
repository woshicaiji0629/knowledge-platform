### 高主频计算型实例规格族hfc6
规格族介绍：依托神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。
适用场景：
高网络包收发场景，例如视频弹幕、电信业务转发等。
Web前端服务器。
大型多人在线游戏（MMO）前端。
数据分析、批量计算、视频编码。
高性能科学和工程应用。
计算：
处理器与内存配比为1:2。
处理器：3.1 GHz主频的Intel®Xeon®Platinum 8269CY（Cascade Lake），睿频3.5 GHz，计算性能稳定。
说明
本实例规格族处理器提供3.1 GHz主频。由于Intel ISS特性原因，您查看到的主频可能显示为更低的数字。阿里云正在紧急修复该显示问题。该显示问题不影响您购买规格的主频频率。
您可以分别运行以下命令，使用turbostat工具来观察CPU运行的主频：
yum install kernel-toolsturbostat
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)、[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)）。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
超高网络收发包PPS能力。
实例网
