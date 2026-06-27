### 计算型实例规格族c9i
规格族介绍：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔®至强®6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。
适用场景：机器学习推理应用，数据分析、批量计算、视频编码，游戏服务器前端，高性能科学和工程应用，Web前端服务器。
计算：
处理器与内存配比为1:2。
处理器：采用Intel®Xeon®Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，单核最大睿频3.9GHz。
说明
该实例在系统中可能会存在不同的频率显示，其中单核最高睿频3.9 GHz，属于突发性能，突发能力与物理机CPU整机负载相关，无法作为SLA承诺。
与操作系统的兼容性说明，请参见[Intel](../intel-instance-specifications-and-operating-system-compatibility.md)[实例规格与操作系统兼容性说明](../intel-instance-specifications-and-operating-system-compatibility.md)。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：ESSD云盘、ESSD AutoPL云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)）。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用](configure-erdma-on-a-cpu-instance.md)[eRDMA](configure-erdma-on-a-cpu-ins
