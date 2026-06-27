### GPU计算型超级计算集群实例规格族sccgn7ex
规格族介绍：sccgn7ex是阿里云为了面对日益增长的大规模AI训练需求开发的高带宽超算集群实例。多台裸金属服务器之间采用第三代RDMA SCC网络互联，支持800 G的互联带宽。您可以根据训练需求弹性选择线上集群数量，快速满足大规模AI参数训练的需求。
适用场景：超大规模AI训练场景。
计算：
支持NVSwitch，算力高达312T（TF32）。
处理器与内存配比为1:8。
处理器：采用第三代Intel®Xeon®8369可扩展处理器（Ice Lake），基频2.9 GHz，全核睿频3.5 GHz，支持PCIe 4.0接口。
存储：
I/O优化实例
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
仅支持专有网络VPC。
超高网络性能，2400万PPS网络收发包能力。
sccgn7ex实例间支持800 Gbit/s的互联带宽（4 * 双口100 Gbit/s RDMA），支持GPUDirect，每颗GPU直连一个100 Gbit/s网口。
sccgn7ex包括的实例规格及指标数据如下表所示。

| 实例规格 | vCPU | 内存（GiB） | GPU 显存（GB） | 网络基础带宽（Gbit/s） | 网络收发包 PPS | RoCE 网络（Gbit/s） | 弹性网卡 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.sccgn7ex.32xlarge | 128 | 1024 | 80 GB * 8 | 64 | 2400 万 | 800 | 15 |
