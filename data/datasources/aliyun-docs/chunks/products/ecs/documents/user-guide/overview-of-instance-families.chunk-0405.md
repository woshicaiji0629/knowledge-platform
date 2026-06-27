### 存储增强型弹性裸金属服务器实例规格族ebmg7se
规格族介绍：
依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。
提供专属硬件资源和物理隔离。
适用场景：
需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。
需要支持云盘多重挂载功能的高可用工作负载。
I/O密集型业务场景，例如中大型OLTP类核心数据库、中大型NoSQL数据库。
搜索、实时日志分析。
计算：
处理器与内存配比为1:4。
处理器：2.9 GHz主频的Intel®Xeon®Platinum 8369B（Ice Lake），全核睿频3.5 GHz。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[弹性临时盘](elastic-ephemeral-disks.md)、[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
单实例顺序读写性能最高可达64 Gbit/s，IOPS最高可达100万。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
超高网络性能，1200万PPS网络收发包能力。
ebmg7se包括的实例规格及指标数据如下表所示。
