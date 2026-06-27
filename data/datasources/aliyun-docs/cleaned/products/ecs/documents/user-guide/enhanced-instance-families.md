# 增强型实例规格-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/enhanced-instance-families

# 增强型实例规格
增强型实例规格包括存储增强、网络增强、安全增强和内存增强，主要针对需要更高性能、更稳定处理能力的应用场景而设计。
说明
[查看实例可购买地域](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion)：不同地域的实例规格可能有所不同，建议先了解各地域的可购买情况。
[查看实例规格选型指导](best-practices-for-instance-type-selection.md)：您可以先了解业务场景下实例规格族选择，再结合本文确定具体规格。
[查看实例规格指标说明](instance-specification-naming-and-classification.md)：建议提前阅读以掌握相关实例规格指标的信息。
[使用](https://www.aliyun.com/price/product#/commodity/vm)[ECS](https://www.aliyun.com/price/product#/commodity/vm)[价格计算器](https://www.aliyun.com/price/product#/commodity/vm)：您可以通过价格计器预估实例费用。
## 增强型实例规格介绍
存储增强型：相比于同代系实例，在云盘带宽、云盘IOPS等EBS相关能力上进行了优化，更适用于存储密集型应用场景。
网络增强型：网络增强型实例，针对网络密集型应用场景专门优化，各项网络指标得到提升，远高于同代通用实例规格，满足垂直场景需求。特别适用于需要网络性能高于通用实例的场景。
安全增强型：通过可信计算、机密计算等技术方案，对实例中的数据安全保护能力进行增强。
内存增强型：相比内存型（r系列）实例规格，内存增强型（re系列）vCPU与内存容量配比更高（超过1:8），内存容量更大。
| 存储增强型 | 网络增强型 | 安全增强型 | 内存增强型 |
| --- | --- | --- | --- |
| [存储增强通用型实例规格族](enhanced-instance-families.md) [g8ise](enhanced-instance-families.md) [存储增强通用型实例规格族](enhanced-instance-families.md) [g7se](enhanced-instance-families.md) [存储增强计算型实例规格族](enhanced-instance-families.md) [c7se](enhanced-instance-families.md) [存储增强内存型实例规格族](enhanced-instance-families.md) [r7se](enhanced-instance-families.md) | [网络增强通用型实例规格族](enhanced-instance-families.md) [g8ine](enhanced-instance-families.md) [网络增强计算型实例规格族](enhanced-instance-families.md) [c8ine](enhanced-instance-families.md) [网络增强通用型实例规格族](enhanced-instance-families.md) [g7nex](enhanced-instance-families.md) [网络增强计算型实例规格族](enhanced-instance-families.md) [c7nex](enhanced-instance-families.md) [网络增强通用型实例规格族](enhanced-instance-families.md) [g7ne](enhanced-instance-families.md) [网络增强通用型实例规格族](enhanced-instance-families.md) [g5ne](enhanced-instance-families.md) | [安全增强通用型实例规格族](enhanced-instance-families.md) [g9it](enhanced-instance-families.md) [安全增强内存型实例规格族](enhanced-instance-families.md) [r9it](enhanced-instance-families.md) [安全增强通用型实例规格族](enhanced-instance-families.md) [g7t](enhanced-instance-families.md) [安全增强计算型实例规格族](enhanced-instance-families.md) [c7t](enhanced-instance-families.md) [安全增强内存型实例规格族](enhanced-instance-families.md) [r7t](enhanced-instance-families.md) [安全增强通用型实例规格族](enhanced-instance-families.md) [g6t](enhanced-instance-families.md) [安全增强计算型实例规格族](enhanced-instance-families.md) [c6t](enhanced-instance-families.md) | 推荐 [内存增强型实例规格族](enhanced-instance-families.md) [re8](enhanced-instance-families.md) [内存增强型实例规格族](enhanced-instance-families.md) [re7p](enhanced-instance-families.md) [持久内存型实例规格族](enhanced-instance-families.md) [re6p](enhanced-instance-families.md) [内存增强型实例规格族](enhanced-instance-families.md) [re6](enhanced-instance-families.md) 不推荐（如果售罄，建议使用推荐规格族） [内存增强型实例规格族](enhanced-instance-families.md) [re4](enhanced-instance-families.md) [内存增强型实例规格族](enhanced-instance-families.md) [re4e](enhanced-instance-families.md) |
## 网络增强通用型实例规格族g8ine
规格族介绍：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎。
适用场景： 适用于网络密集型场景，转发、连接性能出色，尤其适用于做网络接入层网关，流量、数据转发或预处理中间件等。作为云上解决方案中的一部分，在大型网站、电商、AI等场景下都可应用。
计算：
处理器与内存配比为1:4。
处理器：采用Intel®Xeon®Emerald Rapids或者Intel®Xeon®Sapphire Rapids，主频不低于2.7 GHz，全核睿频3.2 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
小规格实例云盘IOPS和云盘带宽具备突发能力。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](jumbo-frame.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
安全：支持可信计算（vTPM）特性。更多信息，请参见[可信计算能力概述](overview-of-trusted-computing-capabilities.md)。
g8ine包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络带宽基础/突发（Gbit/s） | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | EBS 多队列 | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.g8ine.large | 2 | 8 | 4/最高 24 | 60 万 | 2 | 3 | 10 | 10 | 1 | 2 万/最高 8 万 | 2/最高 8 |
| ecs.g8ine.xlarge | 4 | 16 | 7/最高 28 | 120 万 | 4 | 4 | 15 | 15 | 1 | 4 万/最高 8 万 | 2.5/最高 8 |
| ecs.g8ine.2xlarge | 8 | 32 | 12/最高 35 | 200 万 | 8 | 6 | 15 | 15 | 2 | 5 万/最高 8 万 | 4/最高 8 |
| ecs.g8ine.4xlarge | 16 | 64 | 23/最高 44 | 350 万 | 16 | 8 | 30 | 30 | 2 | 8 万/最高 10 万 | 6/最高 10 |
| ecs.g8ine.8xlarge | 32 | 128 | 44/无 | 700 万 | 32 | 8 | 30 | 30 | 4 | 10 万/无 | 10/无 |
## 网络增强计算型实例规格族c8ine
规格族介绍：采用阿里云全新CIPU架构，可提供稳定的算力输出、更强劲的I/O引擎。
适用场景： 适用于网络密集型场景，转发、连接性能出色，尤其适用于做网络接入层网关，流量、数据转发或预处理中间件等。作为云上解决方案中的一部分，在大型网站、电商、AI等场景下都可应用。
计算：
处理器与内存配比为1:2。
处理器：采用Intel®Xeon®Emerald Rapids或者Intel®Xeon®Sapphire Rapids，主频不低于2.7 GHz，全核睿频3.2 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：ESSD云盘、ESSD AutoPL云盘及ESSD 同城冗余云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
小规格实例云盘IOPS和云盘带宽具备突发能力。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](jumbo-frame.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
安全：支持可信计算（vTPM）特性。更多信息，请参见[可信计算能力概述](overview-of-trusted-computing-capabilities.md)。
c8ine包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络带宽基础/突发（Gbit/s） | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | EBS 多队列 | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.c8ine.large | 2 | 4 | 4/最高 24 | 60 万 | 2 | 3 | 10 | 10 | 1 | 2 万/最高 8 万 | 2/最高 8 |
| ecs.c8ine.xlarge | 4 | 8 | 7/最高 28 | 120 万 | 4 | 4 | 15 | 15 | 1 | 4 万/最高 8 万 | 2.5/最高 8 |
| ecs.c8ine.2xlarge | 8 | 16 | 12/最高 35 | 200 万 | 8 | 6 | 15 | 15 | 2 | 5 万/最高 8 万 | 4/最高 8 |
| ecs.c8ine.4xlarge | 16 | 32 | 23/最高 44 | 350 万 | 16 | 8 | 30 | 30 | 2 | 8 万/最高 10 万 | 6/最高 10 |
| ecs.c8ine.8xlarge | 32 | 64 | 44/无 | 700 万 | 32 | 8 | 30 | 30 | 4 | 10 万/无 | 10/无 |
## 存储增强通用型实例规格族g8ise
规格族介绍：采用阿里云全新CIPU架构，可提供稳定的算力输出，单位vCPU提供更高的存储IO能力。
适用场景：I/O密集型业务场景（例如中大型OLTP类核心数据库），中大型NoSQL数据库，搜索、实时日志分析，大型企业级商用软件（例如SAP）。
计算：
处理器与内存配比为1:4。
处理器：采用Intel®Xeon®Emerald Rapids或者Intel®Xeon®Sapphire Rapids，主频不低于2.7 GHz，全核睿频3.2 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
支持高级矩阵扩展（Intel®AMX）。
说明
关于Intel®AMX的更多信息，请参见[Tuning Guide for AI on the 4th Generation Intel® Xeon® Scalable Processors](https://www.intel.com/content/www/us/en/developer/articles/technical/tuning-guide-for-ai-on-the-4th-generation.html)。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[弹性临时盘](elastic-ephemeral-disks.md)、[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
最多支持挂载48块数据盘。
创建实例时最多挂载16块数据盘，如果实例需要更多数据盘，请在创建实例后继续挂载。具体操作，请参见[挂载数据盘](attach-a-data-disk.md)。
实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强），详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用](configure-erdma-on-a-cpu-instance.md)[eRDMA](configure-erdma-on-a-cpu-instance.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](jumbo-frame.md)。
小规格实例网络带宽具备突发能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
安全
支持vTPM特性，依托TPM/TCM芯片，实现从物理服务器到实例的启动链可信度量，提供超高安全能力。
采用英特尔TME（Total Memory Encryption）运行内存加密。
与操作系统的兼容性说明：更多信息，请参见[Intel](../intel-instance-specifications-and-operating-system-compatibility.md)[实例规格与操作系统兼容性说明](../intel-instance-specifications-and-operating-system-compatibility.md)。
g8ise包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.g8ise.large | 2 | 8 | 2.5/最高 15 | 100 万 | 最高 30 万 | 2 | 3 | 6 | 6 | 4 万/最高 20 万 | 3/最高 12 |
| ecs.g8ise.xlarge | 4 | 16 | 4/最高 15 | 120 万 | 最高 30 万 | 4 | 4 | 15 | 15 | 8 万/最高 20 万 | 4/最高 12 |
| ecs.g8ise.2xlarge | 8 | 32 | 6/最高 15 | 160 万 | 最高 30 万 | 8 | 4 | 15 | 15 | 10 万/最高 20 万 | 6/最高 12 |
| ecs.g8ise.3xlarge | 12 | 48 | 10/最高 15 | 240 万 | 最高 30 万 | 12 | 8 | 15 | 15 | 12 万/最高 20 万 | 8/最高 12 |
| ecs.g8ise.4xlarge | 16 | 64 | 12/最高 25 | 300 万 | 35 万 | 16 | 8 | 30 | 30 | 15 万/最高 20 万 | 10/最高 12 |
| ecs.g8ise.6xlarge | 24 | 96 | 15/最高 25 | 450 万 | 50 万 | 24 | 8 | 30 | 30 | 20 万/无 | 12/无 |
| ecs.g8ise.8xlarge | 32 | 128 | 20/最高 25 | 500 万 | 80 万 | 32 | 8 | 30 | 30 | 30 万/无 | 16/无 |
| ecs.g8ise.12xlarge | 48 | 192 | 25/无 | 600 万 | 100 万 | 48 | 8 | 30 | 30 | 40 万/无 | 25/无 |
## 存储增强通用型实例规格族g7se
规格族介绍：依托第三代神龙架构，采用Ice Lake处理器，全面优化了存储I/O性能。
适用场景：I/O密集型业务场景（例如中大型OLTP类核心数据库），中大型NoSQL数据库，搜索、实时日志分析，大型企业级商用软件（例如SAP）。
计算：
处理器与内存配比为1:4。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.9 GHz，全核睿频3.5 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
最多支持挂载64块数据盘。创建实例时最多挂载16块数据盘，如果实例需要更多数据盘，请在创建实例后继续挂载。具体操作，请参见[挂载数据盘](attach-a-data-disk.md)。
单实例顺序读写性能最高可达64 Gbit/s，IOPS最高可达100万。
实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
g7se包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 最大挂载数据盘数量 | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.g7se.large | 2 | 8 | 1.2/最高 3 | 45 万 | 最高 25 万 | 2 | 3 | 6 | 6 | 16 | 3 万/最高 15 万 | 3/10 |
| ecs.g7se.xlarge | 4 | 16 | 2/最高 5 | 50 万 | 最高 25 万 | 4 | 4 | 15 | 15 | 16 | 6 万/最高 15 万 | 4/10 |
| ecs.g7se.2xlarge | 8 | 32 | 3/最高 8 | 80 万 | 最高 25 万 | 8 | 4 | 15 | 15 | 16 | 10 万/最高 15 万 | 6/10 |
| ecs.g7se.3xlarge | 12 | 48 | 4.5/最高 10 | 120 万 | 最高 25 万 | 8 | 8 | 15 | 15 | 16 | 12 万/最高 15 万 | 8/10 |
| ecs.g7se.4xlarge | 16 | 64 | 6/最高 10 | 150 万 | 30 万 | 8 | 8 | 30 | 30 | 24 | 15 万/无 | 10/无 |
| ecs.g7se.6xlarge | 24 | 96 | 8/最高 10 | 225 万 | 45 万 | 12 | 8 | 30 | 30 | 24 | 20 万/无 | 12/无 |
| ecs.g7se.8xlarge | 32 | 128 | 10/无 | 300 万 | 60 万 | 16 | 8 | 30 | 30 | 30 | 30 万/无 | 16/无 |
| ecs.g7se.16xlarge | 64 | 256 | 16/无 | 600 万 | 120 万 | 32 | 8 | 30 | 30 | 56 | 50 万/无 | 32/无 |
## 存储增强计算型实例规格族c7se
规格族介绍：依托第三代神龙架构，采用Ice Lake处理器，全面优化了存储I/O性能。
适用场景：I/O密集型业务场景（例如中大型OLTP类核心数据库），中大型NoSQL数据库，搜索、实时日志分析，大型企业级商用软件（例如SAP）。
计算：
处理器与内存配比为1:2。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.9 GHz，全核睿频3.5 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
最多支持挂载64块数据盘。创建实例时最多挂载16块数据盘，如果实例需要更多数据盘，请在创建实例后继续挂载。具体操作，请参见[挂载数据盘](attach-a-data-disk.md)。
单实例顺序读写性能最高可达64 Gbit/s，IOPS最高可达100万。
实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
c7se包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 最大挂载数据盘数量 | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.c7se.large | 2 | 4 | 1.2/最高 3 | 45 万 | 最高 25 万 | 2 | 3 | 6 | 6 | 16 | 3 万/最高 15 万 | 3/10 |
| ecs.c7se.xlarge | 4 | 8 | 2/最高 5 | 50 万 | 最高 25 万 | 4 | 4 | 15 | 15 | 16 | 6 万/最高 15 万 | 4/10 |
| ecs.c7se.2xlarge | 8 | 16 | 3/最高 8 | 80 万 | 最高 25 万 | 8 | 4 | 15 | 15 | 16 | 10 万/最高 15 万 | 6/10 |
| ecs.c7se.3xlarge | 12 | 24 | 4.5/最高 10 | 120 万 | 最高 25 万 | 8 | 8 | 15 | 15 | 16 | 12 万/最高 15 万 | 8/10 |
| ecs.c7se.4xlarge | 16 | 32 | 6/最高 10 | 150 万 | 30 万 | 8 | 8 | 30 | 30 | 24 | 15 万/无 | 10/无 |
| ecs.c7se.6xlarge | 24 | 48 | 8/最高 10 | 225 万 | 45 万 | 12 | 8 | 30 | 30 | 24 | 20 万/无 | 12/无 |
| ecs.c7se.8xlarge | 32 | 64 | 10/无 | 300 万 | 60 万 | 16 | 8 | 30 | 30 | 30 | 30 万/无 | 16/无 |
| ecs.c7se.16xlarge | 64 | 128 | 16/无 | 600 万 | 120 万 | 32 | 8 | 30 | 30 | 56 | 50 万/无 | 32/无 |
## 存储增强内存型实例规格族r7se
规格族介绍：依托第三代神龙架构，采用Ice Lake处理器，全面优化了存储I/O性能。
适用场景：
I/O密集型业务场景，例如中大型OLTP类核心数据库。
中大型NoSQL数据库。
搜索、实时日志分析。
大型企业级商用软件，例如SAP。
容器高密场景。
计算：
处理器与内存配比为1:8。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.9 GHz，全核睿频3.5 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
最多支持挂载64块数据盘。创建实例时最多挂载16块数据盘，如果实例需要更多数据盘，请在创建实例后继续挂载。具体操作，请参见[挂载数据盘](attach-a-data-disk.md)。
单实例顺序读写性能最高可达64 Gbit/s，IOPS最高可达100万。
实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
r7se包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 最大挂载数据盘数量 | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.r7se.large | 2 | 16 | 1.2/最高 3 | 45 万 | 最高 25 万 | 2 | 3 | 6 | 6 | 16 | 3 万/最高 15 万 | 3/10 |
| ecs.r7se.xlarge | 4 | 32 | 2/最高 5 | 50 万 | 最高 25 万 | 4 | 4 | 15 | 15 | 16 | 6 万/最高 15 万 | 4/10 |
| ecs.r7se.2xlarge | 8 | 64 | 3/最高 8 | 80 万 | 最高 25 万 | 8 | 4 | 15 | 15 | 16 | 10 万/最高 15 万 | 6/10 |
| ecs.r7se.3xlarge | 12 | 96 | 4.5/最高 10 | 120 万 | 最高 25 万 | 8 | 8 | 15 | 15 | 16 | 12 万/最高 15 万 | 8/10 |
| ecs.r7se.4xlarge | 16 | 128 | 6/最高 10 | 150 万 | 30 万 | 8 | 8 | 30 | 30 | 24 | 15 万/无 | 10/无 |
| ecs.r7se.6xlarge | 24 | 192 | 8/最高 10 | 225 万 | 45 万 | 12 | 8 | 30 | 30 | 24 | 20 万/无 | 12/无 |
| ecs.r7se.8xlarge | 32 | 256 | 10/无 | 300 万 | 60 万 | 16 | 8 | 30 | 30 | 30 | 30 万/无 | 16/无 |
| ecs.r7se.16xlarge | 64 | 512 | 16/无 | 600 万 | 120 万 | 32 | 8 | 30 | 30 | 56 | 50 万/无 | 32/无 |
## 网络增强通用型实例规格族g7nex
规格族介绍：依托第四代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。
适用场景：
网络密集型应用场景，例如NFV/SD-WAN、移动互联网、视频弹幕、电信业务转发等。
中小型数据库系统、缓存、搜索集群。
各种类型和规模的企业级应用。
计算：
处理器与内存配比为1:4。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)）。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](jumbo-frame.md)。
大幅提升单实例的网络带宽能力和网络收发包能力，单实例最高支持3000万PPS网络收发包能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
g7nex包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络带宽基础/突发（Gbit/s） | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | EBS 多队列 | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.g7nex.large | 2 | 8 | 3/最高 20 | 45 万 | 2 | 3 | 10 | 10 | 1 | 1 万/最高 5 万 | 1.5/最高 8 |
| ecs.g7nex.xlarge | 4 | 16 | 5/最高 24 | 90 万 | 4 | 4 | 15 | 15 | 1 | 2 万/最高 5 万 | 2/最高 8 |
| ecs.g7nex.2xlarge | 8 | 32 | 10/最高 32 | 175 万 | 8 | 6 | 15 | 15 | 2 | 2.5 万/最高 5 万 | 3/最高 8 |
| ecs.g7nex.4xlarge | 16 | 64 | 20/最高 40 | 300 万 | 16 | 8 | 30 | 30 | 2 | 4 万/最高 5 万 | 5/最高 8 |
| ecs.g7nex.8xlarge | 32 | 128 | 40/无 | 600 万 | 32 | 8 | 30 | 30 | 4 | 7.5 万/无 | 8/无 |
| ecs.g7nex.16xlarge | 64 | 256 | 80/无 | 800 万 | 32 | 15 | 50 | 50 | 4 | 15 万/无 | 16/无 |
| ecs.g7nex.32xlarge | 128 | 512 | 160/无 | 1600 万 | 32 | 15 | 50 | 50 | 4 | 30 万/无 | 32/无 |
说明
对于ecs.g7nex.32xlarge，实例上至少需要绑定两张弹性网卡，每张弹性网卡连接到不同的网卡索引，以实现160 Gbit/s的网络带宽；所有弹性网卡连接到相同的网卡索引，实例最高可达到100 Gbit/s的网络带宽。更多信息，请参见[AttachNetworkInterface](../api-attachnetworkinterface.md)。
## 网络增强计算型实例规格族c7nex
规格族介绍：依托第四代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。
适用场景：
网络密集型应用场景，例如NFV/SD-WAN、移动互联网、视频弹幕、电信业务转发等。
中小型数据库系统、缓存、搜索集群。
各种类型和规模的企业级应用。
计算：
处理器与内存配比为1:2。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)）。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](jumbo-frame.md)。
大幅提升单实例的网络带宽能力和网络收发包能力，单实例最高支持3000万PPS网络收发包能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
c7nex包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络带宽基础/突发（Gbit/s） | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | EBS 多队列 | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.c7nex.large | 2 | 4 | 3/最高 20 | 45 万 | 2 | 3 | 10 | 10 | 1 | 1 万/最高 5 万 | 1.5/最高 8 |
| ecs.c7nex.xlarge | 4 | 8 | 5/最高 24 | 90 万 | 4 | 4 | 15 | 15 | 1 | 2 万/最高 5 万 | 2/最高 8 |
| ecs.c7nex.2xlarge | 8 | 16 | 10/最高 32 | 175 万 | 8 | 6 | 15 | 15 | 2 | 2.5 万/最高 5 万 | 3/最高 8 |
| ecs.c7nex.4xlarge | 16 | 32 | 20/最高 40 | 300 万 | 16 | 8 | 30 | 30 | 2 | 4 万/最高 5 万 | 5/最高 8 |
| ecs.c7nex.8xlarge | 32 | 64 | 40/无 | 600 万 | 32 | 8 | 30 | 30 | 4 | 7.5 万/无 | 8/无 |
| ecs.c7nex.16xlarge | 64 | 128 | 80/无 | 800 万 | 32 | 15 | 50 | 50 | 4 | 15 万/无 | 16/无 |
| ecs.c7nex.32xlarge | 128 | 256 | 160/无 | 1600 万 | 32 | 15 | 50 | 50 | 4 | 30 万/无 | 32/无 |
说明
对于ecs.c7nex.32xlarge，实例上至少需要绑定两张弹性网卡，每张弹性网卡连接到不同的网卡索引，以实现160 Gbit/s的网络带宽；所有弹性网卡连接到相同的网卡索引，实例最高可达到100 Gbit/s的网络带宽。更多信息，请参见[AttachNetworkInterface](../api-attachnetworkinterface.md)。
## 网络增强通用型实例规格族g7ne
规格族介绍：大幅提升单实例的网络带宽能力和网络收发包能力，单实例最高支持2400万PPS网络收发包能力。
适用场景：
网络密集型应用场景，例如NFV/SD-WAN、移动互联网、视频弹幕、电信业务转发等。
中小型数据库系统、缓存、搜索集群。
各种类型和规模的企业级应用。
大数据分析和机器学习。
计算：
处理器与内存配比为1:4。
处理器：采用Intel®Xeon®Platinum 8369HB（Cooper Lake）或者Intel®Xeon®Platinum 8369HC（Cooper Lake），睿频3.8 GHz，主频不低于3.3 GHz，计算性能稳定。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](jumbo-frame.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
g7ne包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘基础 IOPS | 云盘基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.g7ne.large | 2 | 8 | 1.5/10 | 90 万 | 45 万 | 2 | 3 | 10 | 10 | 1 万 | 0.75 |
| ecs.g7ne.xlarge | 4 | 16 | 3/10 | 100 万 | 90 万 | 4 | 4 | 15 | 15 | 2 万 | 1 |
| ecs.g7ne.2xlarge | 8 | 32 | 6/15 | 160 万 | 175 万 | 8 | 6 | 15 | 15 | 2.5 万 | 1.2 |
| ecs.g7ne.4xlarge | 16 | 64 | 12/25 | 300 万 | 350 万 | 16 | 8 | 30 | 30 | 4 万 | 2 |
| ecs.g7ne.8xlarge | 32 | 128 | 25/无 | 600 万 | 600 万 | 32 | 8 | 30 | 30 | 7.5 万 | 5 |
| ecs.g7ne.12xlarge | 48 | 192 | 40/无 | 1200 万 | 800 万 | 32 | 8 | 30 | 30 | 10 万 | 8 |
| ecs.g7ne.24xlarge | 96 | 384 | 80/无 | 2400 万 | 1600 万 | 48 | 15 | 50 | 50 | 24 万 | 16 |
## 网络增强通用型实例规格族g5ne
规格族介绍：大幅提升单实例的网络吞吐能力和网络包转发能力。
适用场景：
DPDK类应用。
网络密集型应用场景，例如NFV/SD-WAN、移动互联网、视频弹幕、电信业务转发等。
中小型数据库系统、缓存、搜索集群。
各种类型和规模的企业级应用。
大数据分析和机器学习。
计算：
处理器与内存配比为1:4。
处理器：2.5 GHz主频的Intel®Xeon®Platinum 8163（Skylake）或者8269CY（Cascade Lake），计算性能稳定。
存储：
I/O优化实例。
支持的云盘类型：SSD云盘、高效云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与计算规格对应，规格越高网络性能越强。
说明
建议DPDK类应用优先选择g5ne实例规格进行部署。
g5ne包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘基础 IOPS | 云盘基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.g5ne.large | 2 | 8 | 1 | 40 万 | 45 万 | 2 | 3 | 10 | 10 | 1 万 | 1 |
| ecs.g5ne.xlarge | 4 | 16 | 2 | 75 万 | 90 万 | 4 | 4 | 15 | 15 | 1.5 万 | 1 |
| ecs.g5ne.2xlarge | 8 | 32 | 3.5 | 150 万 | 175 万 | 8 | 6 | 15 | 15 | 3 万 | 1 |
| ecs.g5ne.4xlarge | 16 | 64 | 7 | 300 万 | 350 万 | 16 | 8 | 30 | 30 | 6 万 | 2 |
| ecs.g5ne.8xlarge | 32 | 128 | 15 | 600 万 | 700 万 | 32 | 8 | 30 | 30 | 11 万 | 4 |
| ecs.g5ne.16xlarge | 64 | 256 | 30 | 1200 万 | 1400 万 | 32 | 8 | 30 | 30 | 13 万 | 8 |
| ecs.g5ne.18xlarge | 72 | 288 | 33 | 1350 万 | 1500 万 | 32 | 15 | 50 | 50 | 16 万 | 9 |
## 安全增强通用型实例规格族g9it
规格族介绍：
支持Intel®SGX加密计算，最大支持192 GiB加密内存，保障关键代码和数据的机密性与完整性不受恶意软件的破坏。
支持虚拟机形态的SGX技术，您可以按需灵活选择实例规格。
默认关闭超线程，独享物理核，降低侧信道攻击风险，内存加密算法升级至AES-256。
重要
如果您在Intel SGX Enclave中使用了与硬件相绑定的密钥加密数据（例如基于SGX Sealing），实例所在的宿主机发生变化后将导致无法解密对应数据。建议您在应用层做好数据冗余和备份，以保证应用的可靠性。
依托TPM/TCM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。
采用阿里云全新CIPU架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。
适用场景：
涉及个人身份信息、医疗保健、金融和知识产权数据等敏感信息的场景。
多方计算中需要共享机密数据。
区块链场景。
机密机器学习。
高安全可信要求场景，例如金融、政务、企业等。
各种类型和规模的企业级应用。
计算：
处理器与内存配比为1:4，其中加密内存在内存中的占比约为50%。
处理器：采用Intel®Xeon®Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，计算性能稳定。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用](configure-erdma-on-a-cpu-instance.md)[eRDMA](configure-erdma-on-a-cpu-instance.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](jumbo-frame.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
g9it包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 加密内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 支持 vTPM | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.g9it.large | 2 | 8 | 4 | 4/15 | 120 万 | 是 | 50 万 | 4 | 4 | 15 | 15 | 5 万/20 万 | 2.5/10 |
| ecs.g9it.xlarge | 4 | 16 | 8 | 6/15 | 160 万 | 是 | 50 万 | 8 | 4 | 15 | 15 | 6 万/20 万 | 4/10 |
| ecs.g9it.2xlarge | 8 | 32 | 16 | 12/25 | 300 万 | 是 | 50 万 | 16 | 8 | 30 | 30 | 10 万/20 万 | 6/10 |
| ecs.g9it.4xlarge | 16 | 64 | 32 | 20/32 | 600 万 | 是 | 80 万 | 32 | 8 | 30 | 30 | 20 万/30 万 | 10/12 |
| ecs.g9it.8xlarge | 32 | 128 | 64 | 28/36 | 1200 万 | 是 | 200 万 | 64 | 8 | 30 | 30 | 30 万/40 万 | 16/24 |
| ecs.g9it.16xlarge | 64 | 256 | 128 | 36/50 | 2000 万 | 是 | 400 万 | 64 | 15 | 30 | 30 | 40 万/65 万 | 24/28 |
| ecs.g9it.24xlarge | 96 | 384 | 192 | 64 | 2400 万 | 是 | 600 万 | 64 | 15 | 50 | 50 | 50 万/80 万 | 32 |
说明
Intel® Xeon® Granite Rapids仅支持基于Intel SGX DCAP的远程证明方式，不支持基于Intel EPID的远程证明方式，您可能需要适配程序后才能正常使用远程证明功能。更多远程证明的信息，请参见[attestation-service](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions/attestation-services.html)。
Intel SGX特性与宿主机的硬件绑定，本实例规格族不支持热迁移。
实例变配规格、触发节省停机等操作均可能造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。
实例默认未开启宕机自动迁移，您可以自行修改。具体操作，请参见[修改实例维护属性](modify-instance-maintenance-attributes.md)。宕机自动迁移会造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。
在创建安全增强型实例时，需要选择专用的镜像才可以使用相关安全特性，更多信息，请参见[创建可信实例](create-a-security-enhanced-instance.md)。
产品处于邀测阶段，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。
## 安全增强内存型实例规格族r9it
规格族介绍：
支持Intel®SGX加密计算，最大支持384 GiB加密内存，保障关键代码和数据的机密性与完整性不受恶意软件的破坏。
支持虚拟机形态的SGX技术，您可以按需灵活选择实例规格。
默认关闭超线程，独享物理核，降低侧信道攻击风险，内存加密算法升级至AES-256。
重要
如果您在Intel SGX Enclave中使用了与硬件相绑定的密钥加密数据（例如基于SGX Sealing），实例所在的宿主机发生变化后将导致无法解密对应数据。建议您在应用层做好数据冗余和备份，以保证应用的可靠性。
依托TPM/TCM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。
采用阿里云全新CIPU架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。
适用场景：
涉及个人身份信息、医疗保健、金融和知识产权数据等敏感信息的场景。
多方计算中需要共享机密数据。
区块链场景。
机密机器学习。
高安全可信要求场景，例如金融、政务、企业等。
各种类型和规模的企业级应用。
计算：
处理器与内存配比为1:8，其中加密内存在内存中的占比约为50%。
处理器：采用Intel®Xeon®Granite Rapids，主频3.2 GHz，全核睿频3.6 GHz，计算性能稳定。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用](configure-erdma-on-a-cpu-instance.md)[eRDMA](configure-erdma-on-a-cpu-instance.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](jumbo-frame.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
r9it包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 加密内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 支持 vTPM | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.r9it.large | 2 | 16 | 8 | 4/15 | 120 万 | 是 | 50 万 | 4 | 4 | 15 | 15 | 5 万/20 万 | 2.5/10 |
| ecs.r9it.xlarge | 4 | 32 | 16 | 6/15 | 160 万 | 是 | 50 万 | 8 | 4 | 15 | 15 | 6 万/20 万 | 4/10 |
| ecs.r9it.2xlarge | 8 | 64 | 32 | 12/25 | 300 万 | 是 | 50 万 | 16 | 8 | 30 | 30 | 10 万/20 万 | 6/10 |
| ecs.r9it.4xlarge | 16 | 128 | 64 | 20/32 | 600 万 | 是 | 80 万 | 32 | 8 | 30 | 30 | 20 万/30 万 | 10/12 |
| ecs.r9it.8xlarge | 32 | 256 | 128 | 28/36 | 1200 万 | 是 | 200 万 | 64 | 8 | 30 | 30 | 30 万/40 万 | 16/24 |
| ecs.r9it.16xlarge | 64 | 512 | 256 | 36/50 | 2000 万 | 是 | 400 万 | 64 | 15 | 30 | 30 | 40 万/65 万 | 24/28 |
| ecs.r9it.24xlarge | 96 | 768 | 384 | 64 | 2400 万 | 是 | 600 万 | 64 | 15 | 50 | 50 | 50 万/80 万 | 32 |
说明
Intel® Xeon® Granite Rapids仅支持基于Intel SGX DCAP的远程证明方式，不支持基于Intel EPID的远程证明方式，您可能需要适配程序后才能正常使用远程证明功能。更多远程证明的信息，请参见[attestation-service](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions/attestation-services.html)。
Intel SGX特性与宿主机的硬件绑定，本实例规格族不支持热迁移。
实例变配规格、触发节省停机等操作均可能造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。
实例默认未开启宕机自动迁移，您可以自行修改。具体操作，请参见[修改实例维护属性](modify-instance-maintenance-attributes.md)。宕机自动迁移会造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。
在创建安全增强型实例时，需要选择专用的镜像才可以使用相关安全特性，更多信息，请参见[创建可信实例](create-a-security-enhanced-instance.md)。
产品处于邀测阶段，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。
## 安全增强通用型实例规格族g7t
规格族介绍：
支持Intel®SGX加密计算，最大支持256 GiB加密内存，保障关键代码和数据的机密性与完整性不受恶意软件的破坏。
支持虚拟机形态的SGX技术，您可以按需灵活选择实例规格。
重要
如果您在Intel SGX Enclave中使用了与硬件相绑定的密钥加密数据（例如基于SGX Sealing），实例所在的宿主机发生变化后将导致无法解密对应数据。建议您在应用层做好数据冗余和备份，以保证应用的可靠性。
依托TPM/TCM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。
依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。
适用场景：
涉及个人身份信息、医疗保健、金融和知识产权数据等敏感信息的场景。
多方计算中需要共享机密数据。
区块链场景。
机密机器学习。
高安全可信要求场景，例如金融、政务、企业等。
各种类型和规模的企业级应用。
计算：
处理器与内存配比为1:4，其中加密内存在内存中的占比约为50%。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
g7t包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 加密内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 支持 vTPM | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.g7t.large | 2 | 8 | 4 | 2/最高 10 | 90 万 | 是 | 最高 25 万 | 2 | 3 | 6 | 6 | 2 万/最高 11 万 | 1.5/最高 6 |
| ecs.g7t.xlarge | 4 | 16 | 8 | 3/最高 10 | 100 万 | 是 | 最高 25 万 | 4 | 4 | 15 | 15 | 4 万/最高 11 万 | 2/最高 6 |
| ecs.g7t.2xlarge | 8 | 32 | 16 | 5/最高 10 | 160 万 | 是 | 最高 25 万 | 8 | 4 | 15 | 15 | 5 万/最高 11 万 | 3/最高 6 |
| ecs.g7t.3xlarge | 12 | 48 | 24 | 8/最高 10 | 240 万 | 是 | 最高 25 万 | 8 | 8 | 15 | 15 | 7 万/最高 11 万 | 4/最高 6 |
| ecs.g7t.4xlarge | 16 | 64 | 32 | 10/最高 25 | 300 万 | 是 | 30 万 | 8 | 8 | 30 | 30 | 8 万/最高 11 万 | 5/最高 6 |
| ecs.g7t.6xlarge | 24 | 96 | 48 | 12/最高 25 | 450 万 | 是 | 45 万 | 12 | 8 | 30 | 30 | 11 万/无 | 6/无 |
| ecs.g7t.8xlarge | 32 | 128 | 64 | 16/最高 25 | 600 万 | 是 | 60 万 | 16 | 8 | 30 | 30 | 15 万/无 | 8/无 |
| ecs.g7t.16xlarge | 64 | 256 | 128 | 32/无 | 1200 万 | 是 | 120 万 | 32 | 8 | 30 | 30 | 30 万/无 | 16/无 |
| ecs.g7t.32xlarge | 128 | 512 | 256 | 64/无 | 2400 万 | 是 | 240 万 | 32 | 15 | 30 | 30 | 60 万/无 | 32/无 |
说明
Intel Ice Lake仅支持基于Intel SGX DCAP的远程证明方式，不支持基于Intel EPID的远程证明方式，您可能需要适配程序后才能正常使用远程证明功能。更多远程证明的信息，请参见[attestation-service](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions/attestation-services.html)。
Intel SGX特性与宿主机的硬件绑定，本实例规格族不支持热迁移。
实例变配规格、触发节省停机等操作均可能造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。
实例默认未开启宕机自动迁移，您可以自行修改。具体操作，请参见[修改实例维护属性](modify-instance-maintenance-attributes.md)。宕机自动迁移会造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。
在创建安全增强型实例时，需要选择专用的镜像才可以使用相关安全特性，更多信息，请参见[创建可信实例](create-a-security-enhanced-instance.md)。
如需使用ecs.g7t.32xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。
## 安全增强计算型实例规格族c7t
规格族介绍：
支持Intel®SGX加密计算，最大支持128 GiB加密内存，保障关键代码和数据的机密性与完整性不受恶意软件的破坏。
支持虚拟机形态的SGX技术，您可以按需灵活选择实例规格。
重要
如果您在Intel SGX Enclave中使用了与硬件相绑定的密钥加密数据（例如基于SGX Sealing），实例所在的宿主机发生变化后将导致无法解密对应数据。建议您在应用层做好数据冗余和备份，以保证应用的可靠性。
依托TPM/TCM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。
依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。
适用场景：
涉及个人身份信息、医疗保健、金融和知识产权数据等敏感信息的场景。
多方计算中需要共享机密数据。
区块链场景。
机密机器学习。
高安全可信要求场景，例如金融、政务、企业等。
各种类型和规模的企业级应用。
计算：
处理器与内存配比为1:2，其中加密内存在内存中的占比约为50%。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强）。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
c7t包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 加密内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 支持 vTPM | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.c7t.large | 2 | 4 | 2 | 2/最高 10 | 90 万 | 是 | 最高 25 万 | 2 | 3 | 6 | 6 | 2 万/最高 11 万 | 1.5/最高 6 |
| ecs.c7t.xlarge | 4 | 8 | 4 | 3/最高 10 | 100 万 | 是 | 最高 25 万 | 4 | 4 | 15 | 15 | 4 万/最高 11 万 | 2/最高 6 |
| ecs.c7t.2xlarge | 8 | 16 | 8 | 5/最高 10 | 160 万 | 是 | 最高 25 万 | 8 | 4 | 15 | 15 | 5 万/最高 11 万 | 3/最高 6 |
| ecs.c7t.3xlarge | 12 | 24 | 12 | 8/最高 10 | 240 万 | 是 | 最高 25 万 | 8 | 8 | 15 | 15 | 7 万/最高 11 万 | 4/最高 6 |
| ecs.c7t.4xlarge | 16 | 32 | 16 | 10/最高 25 | 300 万 | 是 | 30 万 | 8 | 8 | 30 | 30 | 8 万/最高 11 万 | 5/最高 6 |
| ecs.c7t.6xlarge | 24 | 48 | 24 | 12/最高 25 | 450 万 | 是 | 45 万 | 12 | 8 | 30 | 30 | 11 万/无 | 6/无 |
| ecs.c7t.8xlarge | 32 | 64 | 32 | 16/最高 25 | 600 万 | 是 | 60 万 | 16 | 8 | 30 | 30 | 15 万/无 | 8/无 |
| ecs.c7t.16xlarge | 64 | 128 | 64 | 32/无 | 1200 万 | 是 | 120 万 | 32 | 8 | 30 | 30 | 30 万/无 | 16/无 |
| ecs.c7t.32xlarge | 128 | 256 | 128 | 64/无 | 2400 万 | 是 | 240 万 | 32 | 15 | 30 | 30 | 60 万/无 | 32/无 |
说明
Intel Ice Lake仅支持基于Intel SGX DCAP的远程证明方式，不支持基于Intel EPID的远程证明方式，您可能需要适配程序后才能正常使用远程证明功能。更多远程证明的信息，请参见[attestation-service](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions/attestation-services.html)。
Intel SGX特性与宿主机的硬件绑定，本实例规格族不支持热迁移。
实例变配规格、触发节省停机等操作均可能造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。
实例默认未开启宕机自动迁移，您可以自行修改。具体操作，请参见[修改实例维护属性](modify-instance-maintenance-attributes.md)。宕机自动迁移会造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。
在创建安全增强型实例时，需要选择专用的镜像才可以使用相关安全特性，更多信息，请参见[创建可信实例](create-a-security-enhanced-instance.md)。
如需使用ecs.c7t.32xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。
## 安全增强内存型实例规格族r7t
规格族介绍：
支持Intel®SGX加密计算，最大支持512 GiB加密内存，保障关键代码和数据的机密性与完整性不受恶意软件的破坏。
支持虚拟机形态的SGX技术，您可以按需灵活选择实例规格。
重要
如果您在Intel SGX Enclave中使用了与硬件相绑定的密钥加密数据（例如基于SGX Sealing），实例所在的宿主机发生变化后将导致无法解密对应数据。建议您在应用层做好数据冗余和备份，以保证应用的可靠性。
依托TPM/TCM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。
依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。
适用场景：
数据库加密计算应用。
涉及个人身份信息、医疗保健、金融和知识产权数据等敏感信息的场景。
多方计算中共享机密数据。
区块链场景。
机密机器学习。
高安全可信要求场景，例如金融、政务、企业等。
各种类型和规模的企业级应用。
计算：
处理器与内存配比为1:8，其中加密内存在内存中的占比约为50%。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强）。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
r7t包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 加密内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 支持 vTPM | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.r7t.large | 2 | 16 | 8 | 2/最高 10 | 90 万 | 是 | 最高 25 万 | 2 | 3 | 6 | 6 | 2 万/最高 11 万 | 1.5/最高 6 |
| ecs.r7t.xlarge | 4 | 32 | 16 | 3/最高 10 | 100 万 | 是 | 最高 25 万 | 4 | 4 | 15 | 15 | 4 万/最高 11 万 | 2/最高 6 |
| ecs.r7t.2xlarge | 8 | 64 | 32 | 5/最高 10 | 160 万 | 是 | 最高 25 万 | 8 | 4 | 15 | 15 | 5 万/最高 11 万 | 3/最高 6 |
| ecs.r7t.3xlarge | 12 | 96 | 48 | 8/最高 10 | 240 万 | 是 | 最高 25 万 | 8 | 8 | 15 | 15 | 7 万/最高 11 万 | 4/最高 6 |
| ecs.r7t.4xlarge | 16 | 128 | 64 | 10/最高 25 | 300 万 | 是 | 30 万 | 8 | 8 | 30 | 30 | 8 万/最高 11 万 | 5/最高 6 |
| ecs.r7t.6xlarge | 24 | 192 | 96 | 12/最高 25 | 450 万 | 是 | 45 万 | 12 | 8 | 30 | 30 | 11 万/无 | 6/无 |
| ecs.r7t.8xlarge | 32 | 256 | 128 | 16/最高 25 | 600 万 | 是 | 60 万 | 16 | 8 | 30 | 30 | 15 万/无 | 8/无 |
| ecs.r7t.16xlarge | 64 | 512 | 256 | 32/无 | 1200 万 | 是 | 120 万 | 32 | 8 | 30 | 30 | 30 万/无 | 16/无 |
| ecs.r7t.32xlarge | 128 | 1024 | 512 | 64/无 | 2400 万 | 是 | 240 万 | 32 | 15 | 30 | 30 | 60 万/无 | 32/无 |
说明
Intel Ice Lake仅支持基于Intel SGX DCAP的远程证明方式，不支持基于Intel EPID的远程证明方式，您可能需要适配程序后才能正常使用远程证明功能。更多远程证明的信息，请参见[attestation-service](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions/attestation-services.html)。
Intel SGX特性与宿主机的硬件绑定，本实例规格族不支持热迁移。
实例变配规格、触发节省停机等操作均可能造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。
实例默认未开启宕机自动迁移，您可以自行修改。具体操作，请参见[修改实例维护属性](modify-instance-maintenance-attributes.md)。宕机自动迁移会造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。
在创建安全增强型实例时，需要选择专用的镜像才可以使用相关安全特性，更多信息，请参见[创建可信实例](create-a-security-enhanced-instance.md)。
如需使用ecs.r7t.32xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。
## 安全增强通用型实例规格族g6t
g6t的特点如下：
规格族介绍：
依托TPM/TCM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。
支持vTPM，通过完整性监控，提供IaaS层可信能力。
依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。
适用场景：
高安全可信要求场景，例如金融、政务、企业等。
高网络包收发场景，例如视频弹幕、电信业务转发等。
各种类型和规模的企业级应用。
网站和应用服务器。
游戏服务器。
中小型数据库系统、缓存、搜索集群。
数据分析和计算。
计算集群、依赖内存的数据处理。
计算：
处理器与内存配比约为1:4。
处理器：2.5 GHz主频、3.2 GHz睿频的Intel®Xeon®Platinum 8269CY（Cascade Lake），计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
g6t包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 支持 vTPM | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘基础 IOPS | 云盘基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.g6t.large | 2 | 8 | 1.2/最高 10 | 90 万 | 是 | 最高 25 万 | 2 | 3 | 6 | 1 | 2 万 | 1 |
| ecs.g6t.xlarge | 4 | 16 | 2/最高 10 | 100 万 | 是 | 最高 25 万 | 4 | 4 | 15 | 1 | 4 万 | 1.5 |
| ecs.g6t.2xlarge | 8 | 32 | 3/最高 10 | 160 万 | 是 | 最高 25 万 | 8 | 4 | 15 | 1 | 5 万 | 2 |
| ecs.g6t.4xlarge | 16 | 64 | 6/最高 10 | 300 万 | 是 | 30 万 | 8 | 8 | 30 | 1 | 8 万 | 3 |
| ecs.g6t.8xlarge | 32 | 128 | 10/无 | 600 万 | 是 | 60 万 | 16 | 8 | 30 | 1 | 15 万 | 5 |
| ecs.g6t.13xlarge | 52 | 192 | 16/无 | 900 万 | 是 | 90 万 | 32 | 7 | 30 | 1 | 24 万 | 8 |
| ecs.g6t.26xlarge | 104 | 384 | 32/无 | 2400 万 | 是 | 180 万 | 32 | 15 | 30 | 1 | 48 万 | 16 |
说明
网络能力为单项测试最高能力。例如，单项测试网络带宽能力时，不会对网络收发包能力和其他指标同时做压力测试。
## 安全增强计算型实例规格族c6t
规格族介绍：
依托TPM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。
支持完整监控，提供IaaS层可信能力。
依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。
适用场景：
高安全可信要求场景，例如金融、政务、企业等。
高网络包收发场景，例如视频弹幕、电信业务转发等。
Web前端服务器。
大型多人在线游戏（MMO）前端。
数据分析、批量计算、视频编码。
高性能科学和工程应用。
计算：
处理器与内存配比约为1:2。
处理器：2.5 GHz主频、3.2 GHz睿频的Intel®Xeon®Platinum 8269CY（Cascade Lake），计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
c6t包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 支持 vTPM | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘基础 IOPS | 云盘基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.c6t.large | 2 | 4 | 1.2/最高 10 | 90 万 | 是 | 最高 25 万 | 2 | 3 | 6 | 1 | 2 万 | 1 |
| ecs.c6t.xlarge | 4 | 8 | 2/最高 10 | 100 万 | 是 | 最高 25 万 | 4 | 4 | 15 | 1 | 4 万 | 1.5 |
| ecs.c6t.2xlarge | 8 | 16 | 3/最高 10 | 160 万 | 是 | 最高 25 万 | 8 | 4 | 15 | 1 | 5 万 | 2 |
| ecs.c6t.4xlarge | 16 | 32 | 6/最高 10 | 300 万 | 是 | 30 万 | 8 | 8 | 30 | 1 | 8 万 | 3 |
| ecs.c6t.8xlarge | 32 | 64 | 10/无 | 600 万 | 是 | 60 万 | 16 | 8 | 30 | 1 | 15 万 | 5 |
| ecs.c6t.13xlarge | 52 | 96 | 16/无 | 900 万 | 是 | 90 万 | 32 | 7 | 30 | 1 | 24 万 | 8 |
| ecs.c6t.26xlarge | 104 | 192 | 32/无 | 2400 万 | 是 | 180 万 | 32 | 15 | 30 | 1 | 48 万 | 16 |
说明
网络能力为单项测试最高能力。例如，单项测试网络带宽能力时，不会对网络收发包能力和其他指标同时做压力测试。
## 内存增强型实例规格族re8
规格族介绍：采用阿里云全新CIPU架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。
适用场景： 内存数据库（SAP HANA）、高性能数据库和其他内存密集型企业应用。
计算：
处理器与内存配比为1:17，最大内存容量支持16TB。
处理器：采用Intel®Xeon®Sapphire Rapids处理器，主频1.9 GHz，全核睿频2.9 GHz，计算性能稳定。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)及[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)）。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在企业级实例上启用](configure-erdma-on-a-cpu-instance.md)[eRDMA](configure-erdma-on-a-cpu-instance.md)。
支持巨型帧（Jumbo frames）。更多信息，请参见[巨型帧（Jumbo Frames）](jumbo-frame.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
安全：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](overview-of-trusted-computing-capabilities.md)。
re8包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 云盘基础 IOPS | 云盘基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.re8.30xlarge | 120 | 2048 | 32/最高 48 | 750 万 | 32 | 15 | 30 | 15 万/最高 30 万 | 12/最高 25 |
| ecs.re8.60xlarge | 240 | 4096 | 64 | 1500 万 | 32 | 15 | 30 | 30 万 | 25 |
| ecs.re8.90xlarge | 360 | 6144 | 96 | 2250 万 | 64 | 15 | 30 | 40 万 | 36 |
| ecs.re8.120xlarge | 480 | 8192 | 128 | 3000 万 | 64 | 15 | 40 | 60 万 | 50 |
| ecs.re8.180xlarge | 720 | 12288 | 192 | 4500 万 | 64 | 15 | 40 | 90 万 | 75 |
| ecs.re8.240xlarge | 960 | 16384 | 200 | 5000 万 | 64 | 15 | 50 | 120 万 | 100 |
## 内存增强型实例规格族re7p
规格族介绍：
基于持久内存技术，提供性价比更高的内存介质。
说明
本规格族提供的内存混合了普通内存与持久内存。建议您在上线应用前进行充分的测试，必要的时候，需要对应用进行适当改造以获得最佳的性价比。
依托第三代神龙架构，提供稳定可预期的超高性能。同时通过芯片快速路径加速手段，完成存储、网络性能以及计算稳定性的数量级提升。
提供高达1:20的超大处理器与内存配比，极大幅度降低内存型应用单GiB内存的成本。
适用场景：
内存型数据库，例如Redis。关于如何快速部署Redis应用，请参见[在配备持久内存的实例上部署](deploy-redis-on-persistent-memory-optimized-instances.md)[Redis](deploy-redis-on-persistent-memory-optimized-instances.md)[应用](deploy-redis-on-persistent-memory-optimized-instances.md)。
学习与训练应用下的参数服务器（Parameter Server）。
需要大容量Page Cache的应用，例如RocketMQ等消息中间件。
数据分析与挖掘、分布式内存缓存。
Hadoop集群、Spark集群以及其他企业大内存需求应用。
计算：
处理器与内存（内存+持久内存）配比约为1:20。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
小规格实例存储I/O性能具备突发能力
实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强）
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
小规格实例网络带宽具备突发能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
re7p包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 持久内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.re7p.large | 2 | 8 | 31.5 | 2/10 | 90 万 | 25 万 | 2 | 3 | 6 | 6 | 2 万/11 万 | 1.5/6 |
| ecs.re7p.xlarge | 4 | 16 | 63 | 3/10 | 100 万 | 25 万 | 4 | 4 | 15 | 15 | 4 万/11 万 | 2/6 |
| ecs.re7p.2xlarge | 8 | 32 | 126 | 5/10 | 160 万 | 25 万 | 8 | 4 | 15 | 15 | 5 万/11 万 | 3/6 |
| ecs.re7p.16xlarge | 64 | 256 | 1008 | 32/无 | 1200 万 | 100 万 | 32 | 8 | 30 | 30 | 30 万/无 | 16/无 |
| ecs.re7p.32xlarge | 128 | 512 | 2016 | 64/无 | 2400 万 | 200 万 | 32 | 15 | 30 | 30 | 60 万/无 | 32/无 |
## 持久内存型实例规格族re6p
有关持久内存型实例的常见问题，请参见[实例](instance-faq.md)[FAQ](instance-faq.md)。
re6p的特点如下：
规格族介绍：
采用Intel®傲腾TM持久内存。
重要
持久内存中数据的可靠性取决于物理服务器和持久内存设备的可靠性，因此存在单点故障风险。建议您在应用层做好数据冗余，将需要长期保存的业务数据存储到云盘上，以保证应用数据的可靠性。
部分实例规格支持设置不同的持久内存使用方式（作为内存或本地SSD盘使用）。
说明
具体操作，请参见[配置使用持久内存](configure-the-usage-mode-of-persistent-memory.md)。
为Redis应用提供专用实例规格ecs.re6p-redis.<nx>large。
说明
ecs.re6p-redis.<nx>large是为Redis应用提供的专用实例规格，专用实例规格默认已将持久内存配置为内存使用，不支持重新配置为本地SSD盘使用。关于如何快速部署Redis应用，请参见[在配备持久内存的实例上部署](deploy-redis-on-persistent-memory-optimized-instances.md)[Redis](deploy-redis-on-persistent-memory-optimized-instances.md)[应用](deploy-redis-on-persistent-memory-optimized-instances.md)。
适用场景：
Redis数据库及其他NoSQL数据库（例如Cassandra、MongoDB等）。
结构化数据库（例如MySQL等）。
电商、游戏、媒体等I/O密集型应用。
Elasticsearch搜索。
视频直播、即时通讯、房间式强联网网游。
高性能关系型数据库、联机事务处理（OLTP）系统。
计算：
处理器：2.5 GHz主频的Intel®Xeon®Platinum 8269CY（Cascade Lake），睿频3.2 GHz，计算性能稳定。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)、[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
re6p包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 持久内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 连接数 | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘基础 IOPS | 云盘基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.re6p.large | 2 | 8 | 31.5 | 1/3 | 30 万 | 最高 25 万 | 2 | 2 | 6 | 1 | 1 万 | 1 |
| ecs.re6p.xlarge | 4 | 16 | 63 | 1.5/5 | 50 万 | 最高 25 万 | 4 | 3 | 10 | 1 | 2 万 | 1.5 |
| ecs.re6p.2xlarge | 8 | 32 | 126 | 2.5/无 | 80 万 | 最高 25 万 | 8 | 4 | 20 | 1 | 2.5 万 | 2 |
| ecs.re6p.13xlarge | 52 | 192 | 756 | 12.5/无 | 300 万 | 90 万 | 32 | 7 | 20 | 1 | 10 万 | 8 |
| ecs.re6p.26xlarge | 104 | 384 | 1512 | 25/无 | 600 万 | 180 万 | 32 | 15 | 20 | 1 | 20 万 | 16.4 |
| ecs.re6p-redis.large | 2 | 8 | 31.5 | 1/3 | 30 万 | 最高 25 万 | 2 | 2 | 6 | 1 | 1 万 | 1 |
| ecs.re6p-redis.xlarge | 4 | 16 | 63 | 1.5/5 | 50 万 | 最高 25 万 | 4 | 3 | 10 | 1 | 2 万 | 1.5 |
| ecs.re6p-redis.2xlarge | 8 | 32 | 126 | 2.5/无 | 80 万 | 最高 25 万 | 8 | 4 | 20 | 1 | 2.5 万 | 2 |
| ecs.re6p-redis.13xlarge | 52 | 192 | 756 | 12.5/无 | 300 万 | 90 万 | 32 | 7 | 20 | 1 | 10 万 | 8 |
## 内存增强型实例规格族re6
re6的特点如下：
规格族介绍：针对高性能数据库、内存数据库和其他内存密集型企业应用程序进行了优化。
适用场景：
高性能数据库、内存型数据库（例如SAP HANA）
内存密集型应用
大数据处理引擎（例如Apache Spark或Presto）
计算：
处理器与内存配比为1:16（部分规格约为1:15），高内存资源占比，最大支持3 TiB内存
处理器：2.5 GHz主频的Intel®Xeon®Platinum 8269CY（Cascade Lake），睿频3.2 GHz，计算性能稳定
存储：
I/O优化实例
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)、[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
re6包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 云盘基础 IOPS | 云盘基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.re6.4xlarge | 16 | 256 | 5 | 180 万 | 8 | 7 | 20 | 1 | 2.5 万 | 2 |
| ecs.re6.8xlarge | 32 | 512 | 10 | 180 万 | 16 | 7 | 20 | 1 | 5 万 | 4 |
| ecs.re6.13xlarge | 52 | 768 | 10 | 180 万 | 16 | 7 | 20 | 1 | 5 万 | 4 |
| ecs.re6.16xlarge | 64 | 1024 | 16 | 300 万 | 32 | 7 | 20 | 1 | 10 万 | 8 |
| ecs.re6.26xlarge | 104 | 1536 | 16 | 300 万 | 32 | 7 | 20 | 1 | 10 万 | 8 |
| ecs.re6.32xlarge | 128 | 2048 | 32 | 600 万 | 32 | 15 | 20 | 1 | 20 万 | 16 |
| ecs.re6.52xlarge | 208 | 3072 | 32 | 600 万 | 32 | 15 | 20 | 1 | 20 万 | 16 |
说明
如需使用ecs.re6.32xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。
## 内存增强型实例规格族re4
规格族介绍：
针对高性能数据库、内存数据库和其他内存密集型企业应用程序进行了优化。
ecs.re4.20xlarge和ecs.re4.40xlarge规格通过SAP HANA认证。
适用场景：
高性能数据库、内存型数据库（例如SAP HANA）。
内存密集型应用。
大数据处理引擎（例如Apache Spark或Presto）。
计算：
处理器与内存配比为1:12，高内存资源占比，最大支持1920 GiB内存。
处理器：2.2 GHz主频的Intel®Xeon®E7 8880 v4（Broadwell），最大睿频2.4 GHz，计算性能稳定。
存储：
I/O优化实例。
支持的云盘类型：SSD云盘、高效云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
re4包括的实例规格及指标数据如下表所示：
| 实例规格 | vCPU | 内存（GiB） | 网络带宽（Gbit/s） | 网络收发包 PPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.re4.10xlarge | 40 | 480 | 8 | 100 万 | 8 | 4 | 10 | 1 |
| ecs.re4.20xlarge | 80 | 960 | 15 | 200 万 | 16 | 2 | 10 | 1 |
| ecs.re4.40xlarge | 160 | 1920 | 30 | 400 万 | 16 | 2 | 10 | 1 |
## 内存增强型实例规格族re4e
如需使用re4e，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。
规格族介绍：针对高性能数据库、内存数据库和其他内存密集型企业应用程序进行了优化
计算：
处理器与内存配比为1:24，高内存资源占比，最大支持3840 GiB内存
处理器：2.2 GHz主频的Intel®Xeon®E7 8880 v4（Broadwell），最大睿频2.4 GHz，计算性能稳定
适用场景：
高性能数据库、内存型数据库（例如SAP HANA）
内存密集型应用
大数据处理引擎（例如Apache Spark或Presto）
存储：
I/O优化实例
支持的云盘类型：SSD云盘、高效云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
re4e包括的实例规格及指标数据如下表所示。
| 实例规格 | vCPU | 内存（GiB） | 网络带宽（Gbit/s） | 网络收发包 PPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡私有 IPv6 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.re4e.40xlarge | 160 | 3840 | 30 | 450 万 | 16 | 15 | 10 | 1 |
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
