### GPU计算型弹性裸金属服务器实例规格族ebmgn7e
规格族介绍：ebmgn7e是基于神龙架构，实现软件定义硬件计算，灵活弹性与强悍性能兼备的实例规格族。
适用场景：
各类深度学习训练开发业务。
HPC加速计算和仿真。
重要
在使用高通信负载的AI训练业务如Transformer等模型时，务必启用NVLink进行GPU间的数据通信，否则可能由于PCIe链路大规模数据传输引起非预期的故障，导致数据受损。如不确定您使用的训练通信链路拓扑，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)由阿里云技术专家为您提供技术支持。
计算：
处理器：基于Intel®Xeon®Scalable计算平台，2.9 GHz主频，全核睿频3.5 GHz，支持PCIe 4.0接口。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
超高网络性能，2400万PPS网络收发包能力。
ebmgn7e包括的实例规格及指标数据如下表所示。

| 实例规格 | vCPU | 内存（GiB） | GPU 显存 | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 多队列（主网卡/辅助网卡） | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.ebmgn7e.32xlarge | 128 | 1024 | 80GB * 8 | 64 | 2400 万 | 32/12 | 32 | 10 | 1 |
