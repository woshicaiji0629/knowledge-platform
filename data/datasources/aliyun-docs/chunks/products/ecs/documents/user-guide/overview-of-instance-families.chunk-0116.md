### 密集计算型实例规格族ic5
适用场景：
Web前端服务器。
数据分析、批量计算、视频编码。
高网络包收发场景，例如视频弹幕、电信业务转发等。
大型多人在线游戏（MMO）前端。
计算：
处理器与内存配比为1:1。
处理器：2.5 GHz主频的Intel®Xeon®Platinum 8163（Skylake）或者8269CY（Cascade Lake），计算性能稳定，全核睿频2.7 GHz。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
仅支持IPv4。
具备超高网络收发包PPS能力。
实例网络性能与实例规格对应，规格越高网络性能越强。
ic5包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.ic5.large | 2 | 2 | 1 | 30 万 | 2 | 2 | 6 |
| ecs.ic5.xlarge | 4 | 4 | 1.5 | 50 万 | 2 | 3 | 10 |
| ecs.ic5.2xlarge | 8 | 8 | 2.5 | 80 万 | 2 | 4 | 10 |
| ecs.ic5.3xlarge | 12 | 12 | 4 | 90 万 | 4 | 6 | 10 |
| ecs.ic5.4xlarge | 16 | 16 | 5 | 100 万 | 4 | 8 | 20 |
| ecs.ic5.6xlarge | 24 | 24 | 7.5 | 150 万 | 6 | 8 | 20 |
| ecs.ic5.8xlarge | 32 | 32 | 10 | 200 万 | 8 | 8 | 20 |
| ecs.ic5.16xlarge | 64 | 64 | 20 | 300 万 | 16 | 8 | 20 |
