### GPU计算型弹性裸金属服务器实例规格族ebmgn6e
规格族介绍：
ebmgn6e是基于神龙架构，实现软件定义硬件计算，灵活弹性与强悍性能兼备的实例规格族。
采用NVIDIA V100（32 GB NVLink） GPU计算卡。
GPU加速器为V100（SXM2封装） ，特点如下：
创新的Volta架构。
单GPU显存32 GB HBM2（GPU显存带宽900 GB/s）。
单GPU 5120个CUDA Cores。
单GPU 640个Tensor Cores。
单GPU支持6个NVLink链路（NVLink属于双向链路），单向链路的带宽为25 GB/s，总带宽为6×25×2=300 GB/s。
适用场景：
深度学习，例如图像分类、无人驾驶、语音识别等人工智能算法的训练以及推理应用。
科学计算，例如计算流体动力学、计算金融学、分子动力学、环境分析等。
计算：
处理器与内存配比为1:8。
处理器：2.5 GHz主频的Intel®Xeon®Platinum 8163（Skylake）。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)、[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与计算规格对应（规格越高网络性能越强）。
ebmgn6e包括的实例规格及指标数据如下表所示。
