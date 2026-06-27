### 安全增强内存型实例规格族r7t
规格族介绍：
支持Intel®SGX加密计算，最大支持512 GiB加密内存，保障关键代码和数据的机密性与完整性不受恶意软件的破坏。
支持虚拟机形态的SGX技术，您可以按需灵活选择实例规格。
重要
如果您在Intel SGX Enclave中使用了与硬件相绑定的密钥加密数据（例如基于SGX Sealing），实例所在的宿主机发生变化后将导致无法解密对应数据。建议您在应用层做好数据冗余和备份，以保证应用的可靠性。
依托TPM/TCM芯片，从底层服务器硬件到GuestOS的启动链均进行度量和验证，实现可信启动。
依托第三代神龙架构，将大量虚拟化功能卸载到专用硬件，降低虚拟化开销，提供稳定可预期的超高性能。
适用场景：
数据库加密计算应用。
涉及个人身份信息、医疗保健、金融和知识产权数据等敏感信息的场景。
多方计算中共享机密数据。
区块链场景。
机密机器学习。
高安全可信要求场景，例如金融、政务、企业等。
各种类型和规模的企业级应用。
计算：
处理器与内存配比为1:8，其中加密内存在内存中的占比约为50%。
处理器：采用第三代Intel®Xeon®可扩展处理器（Ice Lake），基频2.7 GHz，全核睿频3.5 GHz，计算性能稳定。
支持超线程配置。默认开启超线程配置，详情请参见[更改](specify-and-view-cpu-options.md)[CPU](specify-and-view-cpu-options.md)[选项](specify-and-view-cpu-options.md)。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)和[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
实例存储I/O性能与计算规格对应（规格越高存储I/O性能越强）。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发
