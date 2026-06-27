### 高主频通用型弹性裸金属服务器实例规格族ebmhfg7
规格族介绍：
依托第三代神龙架构，通过芯片快速路径加速手段，提供稳定可预期的超高计算、存储和网络性能。
提供专属硬件资源和物理隔离。
适用场景：
需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。
高网络包收发场景，例如视频弹幕、电信业务转发等。
各种类型和规模的企业级应用。
游戏服务器。
中小型数据库系统、缓存、搜索集群。
高性能科学计算。
视频编码应用。
计算：
处理器与内存配比为1:4。
处理器：第三代Intel®Xeon®可扩展处理器（Cooper Lake架构），基频不低于3.3 GHz，全核睿频3.8 GHz。
存储：
I/O优化实例。
支持的云盘类型：[弹性临时盘](elastic-ephemeral-disks.md)、[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)及[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
超高网络性能，2400万PPS网络收发包能力。
ebmhfg7包括的实例规格及指标数据如下表所示。

| 实例规格 | vCPU | 内存（GiB） | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘基础 IOPS | 云盘基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.ebmhfg7.48xlarge | 192 | 768 | 64 | 2400 万 | 32 | 31 | 10 | 1 | 60 万 | 32 |
