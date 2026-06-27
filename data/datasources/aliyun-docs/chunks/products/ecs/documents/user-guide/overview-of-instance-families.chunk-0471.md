e： 196 TFLOPS | 3 * Video Encoder 3 * Video Decoder | PCIe 接口：PCIe Gen5 x16 带宽：128 GB/s，支持 P2P | DX12、OpenGL 4.6、Vulkan 1.3、CUDA 12.8、OpenCL 3.0、DirectCompute |

存储：
I/O优化实例。
支持NVMe协议。详情参见[NVMe](nvme-protocol.md)[协议概述](nvme-protocol.md)。
支持的云盘类型：[弹性临时盘](elastic-ephemeral-disks.md)、[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
网络：
支持IPv4、IPv6。关于IPv6通信，请参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
超高网络性能，最大3000万PPS网络收发包能力（8卡实例）。
支持ERI（Elastic RDMA Interface），可以在VPC网络下实现RDMA直通加速互联，将带宽提升至360 Gbit/s，可用于自驾、具身智能、CV和传统模型的训练业务。
说明
关于ERI的使用说明，请参见[在企业级实例上启用](configure-erdma-on-a-cpu-instance.md)[eRDMA](configure-erdma-on-a-cpu-instance.md)或[在](on-the-gpu-instance-configuration-erdma.md)[GPU](on-the-gpu-instance-configuration-erdma.md)[实例上启用](on-the-gpu-instance-configuration-erdma.md)[eRDMA](on-the-gpu-instance-configuration-erdma.md)。
gn9gc包括的实例规格及指标数据如下表所示：
