### GPU计算型弹性裸金属服务器实例规格族ebmgn7ex
规格族介绍：ebmgn7ex是阿里云为了应对日益增长的大规模AI训练需求开发的高带宽实例。ebmgn7ex依托第四代神龙架构，采用阿里云全新CIPU架构，多台裸金属之间通过eRDMA网络互联，在160 Gbit/s的互联带宽下实现RDMA通信。打开eRDMA后，您可以根据训练需求弹性选择集群中的机器数量，快速满足大规模AI训练的需求。
适用场景：
各类深度学习训练开发业务。
HPC加速计算和仿真。
重要
在使用高通信负载的AI训练业务如Transformer等模型时，务必启用NVLink进行GPU间的数据通信，否则可能由于PCIe链路大规模数据传输引起非预期的故障，导致数据受损。如不确定您使用的训练通信链路拓扑，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)由阿里云技术专家为您提供技术支持。
计算：
处理器：基于Intel®第三代 Xeon®Scalable计算平台（Icelake），2.9 GHz主频，全核睿频3.5 GHz，支持PCIe 4.0接口。
存储：
I/O优化实例。
支持的云盘类型：[弹性临时盘](elastic-ephemeral-disks.md)、[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持物理网卡。
超高网络性能，2400万PPS网络收发包能力。
支持ERI（Elastic RDMA Interface），可以在VPC网络下实现RDMA直通加速互联。实例上绑定两张弹性RDMA网卡（Elastic RDMA Interface，简称ERI），每张弹性网卡连接到不同的网卡索引，可以实现160 Gbit/s的网络带宽；所有ERI连接到相同的
