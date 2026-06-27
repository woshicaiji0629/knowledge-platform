### 高性能计算优化型实例规格族hpc7ip
规格族介绍：hpc7ip专为芯片设计等需要大量内存容量的HPC工作负载而设计。依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。提供高达1:32的超大处理器与内存配比，搭配Intel傲腾持久内存介质，极大幅度降低内存型应用单GiB内存的成本。
适用场景：芯片设计、其他高性能计算场景。
计算：
处理器与内存（内存+持久内存）配比约为1:32。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.9 GHz，全核睿频3.5 GHz，计算性能稳定。
最大支持2560 GiB内存（512 GiB DRAM内存+2048 GiB Intel®傲腾TM持久内存）。
不支持开启超线程配置。
与操作系统的兼容性说明：仅支持经过验证和性能优化的操作系统，包括Alibaba Cloud Linux 2.1903 LTS 64位和Alibaba Cloud Linux 3.2104 LTS 64位。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
hpc7ip包括的实例规格及指标数据如下表所示。

| 实例规格 | 物理内核 | 内存（GiB） | 持久内存（GiB） | 网络基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- |
| ecs.hpc7ip.32xlarge | 64 | 512 | 2048 | 64 |
