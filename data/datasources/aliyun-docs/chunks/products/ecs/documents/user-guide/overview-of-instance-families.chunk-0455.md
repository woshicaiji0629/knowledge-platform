### 通用型超级计算集群实例规格族sccg7
规格族介绍：具备弹性裸金属服务器的所有特性。更多信息，请参见[弹性裸金属服务器规格](elastic-bare-metal-server-overview.md)。
适用场景： 大规模机器学习训练；大规模高性能科学计算和仿真计算；大规模数据分析、批量计算、视频编码。
计算：
处理器与内存配比为1:4。
处理器：2.9 GHz主频的Intel®Xeon®Platinum 8369（Ice lake），全核睿频3.5 GHz。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)、[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
同时支持RoCE网络和VPC网络，其中RoCE网络专用于RDMA通信。
sccg7包括的实例规格及指标数据如下表所示。

| 实例规格 | vCPU | 物理内核 | 内存（GiB） | 网络基础带宽（Gbit/s） | 网络收发包 PPS | RoCE 网络（Gbit/s） | 弹性网卡 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.sccg7.32xlarge | 128 | 64 | 512.0 | 100 | 2400 万 | 200 | 32 |
