### GPU计算型弹性裸金属服务器实例规格族ebmgn7i
规格族介绍：ebmgn7i是基于神龙架构，实现软件定义硬件计算，灵活弹性与强悍性能兼备的实例规格族。
适用场景：
配备高性能CPU、内存、GPU，可以处理更多并发AI推理任务，适用于图像识别、语音识别、行为识别业务。
支持RTX功能，搭配高主频CPU，提供高性能的3D图形虚拟化能力，适用于远程图形设计、云游戏等高强度图形处理业务。
支持RTX功能，搭配高网络带宽和云盘带宽，适用于搭建高性能渲染农场。
配备多个GPU，搭配高网络带宽，适用于小规模深度学习训练业务。
计算：
采用NVIDIA A10 GPU计算卡：
创新的Ampere架构。
支持vGPU、RTX、TensorRT等常用加速功能。
处理器：2.9 GHz主频的Intel®Xeon®可扩展处理器（Ice Lake），全核睿频3.5 GHz。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
超高网络性能，2400万PPS网络收发包能力。
ebmgn7i包括的实例规格及指标数据如下表所示。

| 实例规格 | vCPU | 内存（GiB） | GPU | GPU 显存 | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.ebmgn7i.32xlarge | 128 | 768 | NVIDIA A10 * 4 | 24GB * 4 | 64 | 2400 万 | 32 | 32 | 10 | 1 |
