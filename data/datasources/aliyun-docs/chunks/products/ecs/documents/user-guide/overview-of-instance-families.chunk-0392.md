### 通用型弹性裸金属服务器实例规格族ebmg9ae
规格族介绍：采用阿里云全新 CIPU 架构，搭配 AMD 最新EPYC™Turin 处理器，可提供稳定的算力输出、更强劲的 I/O 引擎以及芯片级的安全加固。
适用场景：
需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。
兼容第三方Hypervisor，满足混合云和多云部署诉求。
容器（包括但不限于Docker、Clear Container、Pouch等）。
高网络包收发场景，例如视频弹幕、电信业务转发等。
各种类型和规模的企业级应用。
网站和应用服务器。
游戏服务器。
中小型数据库系统、缓存、搜索集群。
数据分析和计算。
高性能科学和工程应用。
计算：
处理器与内存配比为1:4。
处理器：AMD EPYC™Turin处理器，睿频最高3.7 GHz，采用物理核设计，计算性能稳定。
存储：
支持调整存储基础带宽。
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)及[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持调整网络基础带宽。
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用](configure-erdma-on-a-cpu-instance.md)[eRDMA](configure-erdma-on-a-cpu-instance.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](jumbo-frame.md)。
ebmg9ae包括的实例规格及指标数据如下表所示：
