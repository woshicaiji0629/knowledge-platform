### GPU计算型实例规格族gn7e
gn7e的特点如下：
规格族介绍：
您可以根据需要选择不同数量的卡和不同CPU资源的规格，灵活适应其不同的AI业务需求。
依托第三代神龙架构，VPC和云盘网络带宽相比上一代平均提升一倍。
适用场景：
中小规模的AI训练业务。
使用CUDA进行加速的HPC业务。
对GPU处理能力或显存容量需求较高的AI推理业务。
深度学习，例如图像分类、无人驾驶、语音识别等人工智能算法的训练应用。
高GPU负载的科学计算，例如计算流体动力学、计算金融学、分子动力学、环境分析等。
重要
在使用高通信负载的AI训练业务如Transformer等模型时，务必启用NVLink进行GPU间的数据通信，否则可能由于PCIe链路大规模数据传输引起非预期的故障，导致数据受损。如不确定您使用的训练通信链路拓扑，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)由阿里云技术专家为您提供技术支持。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
gn7e包括的实例规格及指标数据如下表所示：
