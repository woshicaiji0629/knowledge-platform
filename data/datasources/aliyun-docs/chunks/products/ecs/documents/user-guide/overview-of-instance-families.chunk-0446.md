### 高性能计算优化型实例规格族hpc8i
hpc8i正在邀测中，如需使用，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。
规格族介绍：hpc8i实例针对计算密集的应用（如隐式有限元分析、分子动力学和计算化学等）进行了优化，采用最新的Intel®Xeon®Emerald Rapids处理器，全核睿频3.6 GHz，支持Intel丰富的软件工具生态系统，如Intel数学库和高级矢量扩展（AVX-512）。
适用场景：
工业仿真中计算流体动力学（Computational Fluid Dynamics，CFD）、有限元分析（Finite Element Analysis，FEA）。
EDA仿真。
地质勘探。
气象预报。
分子动力学模拟。
其他高性能计算场景。
计算：
处理器与内存配比为1:8。
处理器：采用Intel®Xeon®Emerald Rapids处理器，主频不低于2.8 GHz，全核睿频3.6 GHz，计算性能稳定。
不支持开启超线程配置。
与操作系统的兼容性说明：仅支持经过验证和性能优化的操作系统，包括Alibaba Cloud Linux 2.1903 LTS 64位和Alibaba Cloud Linux 3.2104 LTS 64位。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[弹性临时盘](elastic-ephemeral-disks.md)、[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见
