### GPU计算型实例规格族gn8v/gn8v-tee
该实例目前仅支持海外等部分地域，如有需求，请联系阿里云销售人员。
规格族介绍：
gn8v：阿里云针对AI模型训练和超大参数量模型推理任务推出的第8代加速计算规格族（GPU计算型实例规格族），针对不同应用需求，为您提供1卡、2卡、4卡和8卡多种机型。
gn8v-tee：为了满足您使用大模型进行模型训练和推理的安全性要求，阿里云基于gn8v推出一款具有机密计算特性的第8代实例规格族。该实例在GPU计算过程中对数据进行加密，确保用户数据的安全性。
适用场景：
对于70 B以上的LLM模型，进行多卡并行推理计算时性价比较高。
单个GPU提供39.5 TFLOPS FP32算力，在传统AI模型训练和自动驾驶训练业务中性能突出。
8卡之间支持NVLINK互联，适用于中小模型训练场景。
产品特色及定位：
高速&大容量显存：每个GPU配备了96 GB容量的HBM3显存，且显存带宽可以达到4 TB/s，大幅加快了模型训练和推理速度。
高卡间带宽：多个GPU卡之间通过900 GB/s NVLINK互联，多卡训练和推理的效率远超过历代GPU产品。
大模型量化技术：支持FP8算力，对大规模参数训练和推理过程的算力进行优化，大幅提升训练和推理的计算速度，降低显存占用。
（仅限gn8v-tee系列产品）高安全性：支持CPU机密计算（Intel TDX）和GPU机密计算（NVIDIA CC）功能，闭环全链路模型推理的机密计算能力。对于模型推理和训练的安全性，开启机密计算能力保障用户推理数据和企业模型的安全。
计算：
采用最新的CIPU 1.0云处理器。
具有解耦计算和存储能力，可以灵活选择所需存储资源。
提供裸金属能力，相对于传统虚拟化实例，可以支持GPU实例之间的P2P通信。
采用Intel第4代Xeon可扩展处理器，全核睿频可达3.1 GHz，基频可达2.8 GHz。
存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[弹性临时盘](elastic-ephemeral-disks.md)、[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，请参见[IPv6](step-1-create-a-vpc-th
