### 通用算力型实例规格族u2a
规格族介绍：采用阿里云全新CIPU架构，兼容多代际AMD EPYC™处理器（支持 AMD Turin 处理器），可提供企业级的算力输出。
适用场景：
中小型数据库（Redis/Mysql等）
APP应用服务器
中间件（MQ/Kafka等）
网站或网络接入层（Apache/Nginx等）
其他企业内部系统（如开发测试、邮件系统等）
计算：
支持 CPU 核心数量与内存容量配比为1:1/1:2/1:4的实例规格。
处理器：AMD EPYC™处理器，睿频最高3.7 GHz。
与操作系统的兼容性说明，请参见[AMD](../compatibility-between-amd-instance-types-and-operating-systems.md)[实例规格与操作系统兼容性说明](../compatibility-between-amd-instance-types-and-operating-systems.md)。
存储：
I/O优化实例
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：ESSD Entry云盘、[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)及[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
小规格实例云盘IOPS和云盘带宽具备突发能力（实例存储I/O性能与计算规格对应，规格越高存储I/O性能越强 ，详情请参见[存储](storage-i-or-o-performance.md)[I/O](storage-i-or-o-performance.md)[性能](storage-i-or-o-performance.md)）。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
支持ERI（Elastic RDMA Interface）。关于ERI的使用说明，请参见[在
