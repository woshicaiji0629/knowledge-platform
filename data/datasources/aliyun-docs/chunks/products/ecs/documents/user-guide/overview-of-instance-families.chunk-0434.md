### 持久内存型弹性裸金属服务器实例规格族ebmre7p
规格族介绍：提供专属硬件资源和物理隔离。
适用场景：
内存型数据库，例如Redis。
高性能数据库，例如SAP HANA。
其他内存密集型应用，例如AI应用、智能搜索应用。
计算：
采用Intel®傲腾TM持久内存，针对Redis应用进行了全链路优化，性价比超高。
最大支持2560 GiB内存（512 GiB DRAM内存+2048 GiB Intel®傲腾TM持久内存），CPU与内存配比接近1:20，满足内存密集型应用的需求。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)、[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
高网络性能，2400万PPS网络收发包能力。
ebmre7p包括的实例规格及指标数据如下表所示。

| 实例规格 | vCPU | 内存（GiB） | 持久内存（GiB） | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘基础 IOPS | 云盘基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.ebmre7p.32xlarge | 128 | 512 | 2048 | 64 | 2400 万 | 32 | 15 | 1 | 60 万 | 32 |
