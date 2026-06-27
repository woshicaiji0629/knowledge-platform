### 高性能计算优化型实例规格族hpc6id
规格族介绍：hpc6id专为芯片设计等需要大量内存容量和本地数据访问的HPC工作负载而设计。依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。提供超大内存和2块3.8 TB本地数据盘，降低内存和数据受限应用的使用成本。
适用场景：芯片设计、地震油藏和结构模拟、其他高性能计算场景。
计算：
处理器与内存配比约为1:38。
处理器：Intel®Xeon®可扩展处理器（Cascade Lake），基频 3.1 GHz，全核睿频3.5 GHz，计算性能稳定。
不支持开启超线程配置。
与操作系统的兼容性说明：仅支持经过验证和性能优化的操作系统，包括Alibaba Cloud Linux 2.1903 LTS 64位和Alibaba Cloud Linux 3.2104 LTS 64位。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
hpc6id包括的实例规格及指标数据如下表所示。

| 实例规格 | 物理内核 | 内存（GiB） | 本地存储（GB） | 网络基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- |
| ecs.hpc6id.20xlarge | 40 | 1536 | 2 * 3840 | 32 |

说明
该规格族支持Rocky Linux 8、Rocky Linux 9镜像。
