### 海光通用型实例规格族g9h
规格族介绍：采用阿里云CIPU架构，搭配海光4号C86-4G平台处理器，可提供稳定的国产化算力输出、更强劲的I/O引擎以及芯片级的安全加固。
适用场景：数据库，网络Web类应用，大数据分析（Spark/Flink/ES等），搜索/推荐/广告（ps-worker），核心交易系统，音视频转码，AI训练与推理，通用的企业级应用（Java）等。
计算：
处理器与内存配比为1:4。
处理器：采用海光4代可扩展处理器Hygon C86-4G，睿频最高3.1 GHz，国产化算力，安全可靠，计算性能稳定。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[弹性临时盘](elastic-ephemeral-disks.md)、[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)）。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用](configure-erdma-on-a-cpu-instance.md)[eRDMA](configure-erdma-on-a-cpu-instance.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](j
