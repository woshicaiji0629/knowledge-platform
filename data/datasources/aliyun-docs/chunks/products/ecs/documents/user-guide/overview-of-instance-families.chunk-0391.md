### 计算型弹性裸金属服务器实例规格族ebmc6
规格族介绍：提供专属硬件资源和物理隔离。
适用场景：
需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。
兼容第三方Hypervisor，满足混合云和多云部署诉求。
容器（包括但不限于Docker、Clear Container、Pouch等）。
视频编解码、渲染等。
大型多人在线游戏（MMO）前端。
高性能科学和工程应用。
计算：
处理器与内存配比约为1:2。
处理器：2.5 GHz主频的Intel®Xeon®Platinum 8269CY（Cascade Lake），全核睿频3.2 GHz。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)、[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
高网络性能，600万PPS网络收发包能力。
ebmc6包括的实例规格及指标数据如下表所示。

| 实例规格 | vCPU | 内存（GiB） | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 连接数 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘基础 IOPS | 云盘基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.ebmc6.26xlarge | 104 | 192 | 32 | 600 万 | 180 万 | 32 | 20 | 1 | 20 万 | 16 |
