### GPU计算型弹性裸金属服务器实例规格族ebmgn7ix
规格族介绍：
ebmgn7ix是阿里云基于近期AI生成业务的发展推出的一款新型弹性裸金属实例规格族，每个实例为一台采用了8个A10 GPU计算卡的裸金属主机。
采用最新的CIPU 1.0云处理器，解耦计算和存储能力，可以灵活选择所需存储资源。相对于上一代，该实例规格的机器间带宽提升至160 Gbit/s，可以更快地完成数据传输和处理，并应对小规模的多机训练业务。
提供了裸金属规格能力，相对于传统虚拟化实例，可以支持GPU实例之间的P2P通信，大幅提升多GPU的计算效率。
适用场景：
结合云市场的GRID镜像启动A10的图形能力，提供高效的图形处理能力，适用于动漫、影视特效制作和渲染。
结合ACK容器化管理能力，更高效、低成本地支撑AIGC图形生成和LLM大模型推理（最大支持130 B）。
其他通用AI识别场景、图像识别、语音识别等。
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
支持ERI（Elastic RDMA Interface），可以在VPC网络下实现RDMA直通加速互联，将带宽提升至160 Gbit/s。
说明
关于ERI的使用说明，请参见[在企业级实例上启用](configure-erdma-on-a-cpu-instance.md)[eRDMA](configure-erdma-on-a-cpu-insta
