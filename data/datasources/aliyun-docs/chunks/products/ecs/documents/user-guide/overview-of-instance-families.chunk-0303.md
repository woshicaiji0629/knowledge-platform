### 内存增强型实例规格族re4e
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
