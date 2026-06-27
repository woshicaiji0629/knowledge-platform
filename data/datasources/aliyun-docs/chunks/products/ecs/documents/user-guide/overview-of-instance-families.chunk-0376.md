### 通用型弹性裸金属服务器实例规格族ebmc8a
规格族介绍：采用阿里云全新CIPU架构，搭配AMD EPYC™Genoa 处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。
适用场景：
需要直接访问物理资源，或者需要License绑定硬件等要求的工作负载。
兼容第三方Hypervisor，满足混合云和多云部署诉求。
容器（包括但不限于Docker、Clear Container、Pouch等）。
高网络包收发场景，例如视频弹幕、电信业务转发等。
Web前端服务器。
大型多人在线游戏（MMO）前端。
数据分析、批量计算、视频编码。
高性能科学和工程应用。
计算：
处理器与内存配比为1:2。
处理器：AMD EPYC™Genoa处理器，睿频最高3.7 GHz，计算性能稳定。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用](configure-erdma-on-a-cpu-instance.md)[eRDMA](configure-erdma-on-a-cpu-instance.md)。
ebmc8a包括的实例规格及指标数据如下表所示：
