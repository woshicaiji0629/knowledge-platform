### GPU计算型实例规格族gn7
适用场景：
深度学习，例如图像分类、无人驾驶、语音识别等人工智能算法的训练应用。
高GPU负载的科学计算，例如计算流体动力学、计算金融学、分子动力学、环境分析等。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
gn7包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | GPU 显存 | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.gn7-c12g1.3xlarge | 12 | 94 | 40GB * 1 | 4 | 250 万 | 4 | 8 | 10 | 1 |
| ecs.gn7-c13g1.13xlarge | 52 | 378 | 40GB * 4 | 16 | 900 万 | 16 | 8 | 30 | 30 |
| ecs.gn7-c13g1.26xlarge | 104 | 756 | 40GB * 8 | 30 | 1800 万 | 16 | 15 | 10 | 1 |
