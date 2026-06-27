### 计算型弹性裸金属服务器实例规格族ebmc9i
规格族介绍：采用阿里云全新CIPU架构，搭载P-core（性能核）的英特尔®至强®6处理器，可提供稳定的算力输出、更强劲的I/O引擎以及芯片级的安全加固。
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
处理器：采用Intel®Xeon®Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，计算性能稳定。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：ESSD云盘、ESSD AutoPL云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用](configure-erdma-on-a-cpu-instance.md)[eRDMA](configure-erdma-on-a-cpu-instance.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](jumbo-frame.md)。
ebmc9i包括的实例规格及指标数据如下表所示。
