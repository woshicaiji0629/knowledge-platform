### 高性能计算优化型实例规格族hpc9a
规格族介绍：hpc9a专为芯片设计等需要大量内存容量的HPC工作负载而设计，提供高达1:24的超大处理器与内存配比。采用阿里云全新 CIPU 架构，搭配 AMD 最新EPYC™Turin 处理器，采用物理核设计，可提供稳定的算力输出、更强劲的 I/O 引擎以及芯片级的安全加固。
适用场景：芯片设计、其他高性能计算场景。
计算：
处理器与内存（物理核：内存）配比为1:24。最大支持3072GiB内存。
处理器：采用第五代AMD EPYC™Turin处理器，睿频最高5.0GHz，采用物理核设计，计算性能稳定。
不支持开启超线程配置。
与操作系统的兼容性说明：仅支持经过验证和性能优化的操作系统，包括Alibaba Cloud Linux 3/4。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用](configure-erdma-on-a-cpu-instance.md)[eRDMA](configure-erdma-on-a-cpu-instance.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](jumbo-frame.md)。
hpc9a包括的实例规格及指标数据如下表所示：
