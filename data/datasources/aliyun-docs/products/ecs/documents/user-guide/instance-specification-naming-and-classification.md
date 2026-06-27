# 实例规格分类命名与核心指标解读-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/user-guide/instance-specification-naming-and-classification

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 实例规格分类与命名

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

阿里云提供了丰富多样的实例来满足客户不同业务场景及使用场景的需求。 阅读本文了解实例规格族群、实例规格族、实例规格之间的关系，掌握实例规格的命名规范。

## 视频介绍

## 规格族群差异比较

阿里云根据CPU架构及适用的业务场景将实例划分为x86及ARM架构的计算型服务器、弹性裸金属服务器、高性能计算服务器、超级计算集群服务器以及以GPU为主的异构计算型服务器。

- 

- 

- 

- 

- 

- 

- 

| 规格族群 | 介绍 |
| --- | --- |
| x86 计算规格族、ARM 计算规格族群 | x86 计算规格族：基于 x86 架构，每一个 vCPU 都对应一个处理器核心的超线程，具有性能稳定的特点，常见的品牌有：Intel、AMD、海光等。 企业级 x86 计算规格族 ：适用于各种类型和规模的企业级应用、数据库系统、视频编解码、数据分析等场景。 入门级 x86 计算规格族 ：主要面向一般中小网站或个人开发。与企业级规格相比，共享型规格在资源利用上更多强调资源性能的共享，所以无法保证实例计算性能的稳定，但是成本相对较低。 ARM 计算规格族：基于 ARM 架构，每一个 vCPU 都对应一个处理器的物理核心，具有性能稳定且资源独享的特点，适用于容器、微服务、网站和应用服务器、高性能计算、基于 CPU 的机器学习等场景。常见的品牌有：倚天 710，Ampere ® Altra ® 等。 |
| 弹性裸金属服务器（ebm）规格族群 | 弹性裸金属服务器融合了物理机与云服务器的优势，实现超强超稳的计算能力。通过阿里云自主研发的虚拟化 2.0 技术，您的业务应用可以直接访问弹性裸金属服务器的处理器和内存，无任何虚拟化开销。弹性裸金属服务器具备物理机级别的完整处理器特性（例如 Intel VT-x），以及物理机级别的资源隔离优势，特别适合上云部署传统非虚拟化场景的应用。 |
| 高性能计算（HPC）实例规格族群 | 高性能计算优化型实例（HPC）是专为提升 HPC 工作负载性能，同时优化大规模运行成本而打造的最具性价比的实例。 |
| 超级计算集群（SCC）实例规格族群 | 超级计算集群 SCC（Super Computing Cluster）在弹性裸金属服务器基础上，加入高速 RDMA（Remote Direct Memory Access）互联支持，大幅提升网络性能，提高大规模集群加速比。因此 SCC 在提供高带宽、低延迟优质网络的同时，还具备弹性裸金属服务器的所有优点。 |
| 异构计算规格族群 | GPU 云服务器 ： GPU 云服务器提供了 GPU 加速计算能力，实现 GPU 计算资源的即开即用和弹性伸缩。作为阿里云弹性计算家族的一员，其结合了 GPU 计算力与 CPU 计算力，满足您在人工智能、高性能计算、专业图形图像处理等场景中的需求，例如，在并行运算方面，使用 GPU 云服务器可显著提高计算效率。 异构服务型 ：异构服务型实例 video-trans 适用于视频转码、图像与视频内容处理以及帧图像提取等场景 视觉计算型 ：视觉计算型实例规格族 ebmgi6s，基于阿里云神龙架构及 Intel ® Server GPU，为您提供快速弹性扩展的安全架构及最新高密度云手游渲染实例。 |


## 规格族&规格的关系

实例规格族是一组具有相同处理器、相似业务场景和使用场景的实例规格的集合。根据CPU、内存等配置，一种实例规格族又分为多种实例规格。ECS实例规格定义了实例的基本属性：CPU和内存（包括CPU型号、主频等）。但是，ECS实例只有同时配合块存储、镜像和网络类型，才能唯一确定一台实例的具体服务形态。

规格族与规格的关系说明如下：

说明

下图仅展示部分规格族与实例规格，更多实例规格说明，请参见[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)。

## 实例规格命名说明

实例规格族名称格式为ecs.<规格族>，实例规格名称为ecs.<规格族>.<规格大小>。具体命名规则说明如下所示：

- 

ecs：云服务器ECS的产品代号。

- 

<规格族>：由规格族主体+规格族后缀组成。

- 

<规格大小>：由small、large或<nx>large组成，表示vCPU核数。small表示1 vCPU，large表示2 vCPU，xlarge表示4 vCPU。<n>中的n越大，表示vCPU核数越多，如2xlarge代表2 * 4 = 8 vCPU，3xlarge代表3 * 4 = 12 vCPU等等，以此类推。

### x86计算规格族和ARM计算规格族

例如，ecs.g8ae.4xlarge为通用型实例规格族中的一个实例规格，配备增强型AMD CPU，拥有4 * 4 = 16 vCPU，且由通用型规格族的处理器与内存配比为1:4可知，内存为64GiB。

规格的命名主要在于规格族的差异，下方表格详细介绍了规格族的组成部分。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 规格族主体（小写字母+数字） | 规格族后缀 |  |
| --- | --- | --- |
| 小写字母 | 数字 | 小写字母 |
| 某个单词的缩写，标志着实例规格族的性能领域。 c：表示计算型（computational） 处理器与内存配比为 1:2，适用于数据库、Web 服务器、高性能科学和工程应用、游戏服务器、数据分析、批量计算、视频编码、机器学习等场景。 g：表示通用型（general） 处理器与内存配比为 1:4，适用于通用互联网应用、数据库、Web 网站、Java 应用服务、游戏服务、搜索推广等场景。 u：表示通用算力型（universal） U 实例处理器部署在不同的服务器平台，处理器与内存配比为 1:1、1:2、1:4、1:8，适用于对价格敏感的企业级客户，主要应用于中小型和大型企业级应用、网站和应用服务器，中小型数据库系统、缓存、搜索集群等场景。 r：表示内存型（ram） 处理器与内存配比为 1:8（部分规格不为 1:8），适用于内存数据库、数据分析与挖掘、分布式内存缓存（Redis）、大数据类应用（Kafka、ElasticSearch 等），以及对内存容量要求较高的通用企业级应用（Java）等场景。 re：表示内存增强型（ram enhanced) hf（c/g/r）：表示高主频型（high frequency） 处理器与内存配比为 1:2、1:4、1:8，适用于大型多人在线游戏、HPC 等高性能科学计算场景以及中大型数据库系统等。 i：表示本地 SSD 型（instance family with local SSDs） 处理器与内存配比为 1:4、1:8，适用于 OLTP、高性能关系型数据库、NoSQL 数据库（例如 Cassandra、MongoDB 等）、Elasticsearch 等搜索场景以及 EMR 大数据存算分离场景。 d：表示大数据型（big data） 处理器与内存配比为 1:4（部分规格不为 1:4），适用于 Hadoop MapReduce、HDFS、Hive、HBase 等大数据计算和存储业务场景，以及 Elasticsearch、Kafka 等搜索和日志数据处理场景。 s：表示共享型（share） t：表示突发型（burst） e：表示经济型（economy） | 一般用于区分同类型规格族间的发布时间。 更大的数字代表新一代规格族，拥有更高的性价比。 如：8、7、6、5 等。 | 一般用于说明规格族的其他特性。 y：表示采用阿里云自研倚天 710 ARM 架构 CPU（Yitian） a：表示采用 AMD CPU ae：表示 AMD 增强型（AMD enhanced） i：表示采用 intel CPU h：表示采用海光处理器 re：表示 RDMA 增强型（RDMA enhanced） se：表示存储增强型（storage enhanced） ne/nex：表示网络增强型（network enhanced） t：表示安全增强型（tpm） p：表示持久内存型（persistent ram） g：表示通用型（general） r：表示内存型（ram） c：表示计算密集型（computational） 说明 特殊规格（例如 ecs.e-c1m4.xlarge）后缀中 c1m4 表示 vCPU:内存=1:4. c：core，即 vCPU。 m：memory。 |


### 异构计算规格族、弹性裸金属服务器、高性能计算、超级计算集群（SCC）实例规格族

例如，ecs.ebmgn7ix.32xlarge为搭载NVIDIA GPU卡的GPU计算型弹性裸金属服务器实例规格族中的一个实例规格，配备增强型AMD CPU，拥有32 * 4 = 128 vCPU，7表示采用Ampere架构，GPU类型为A10且GPU显存为24 GB。

重要

hpc规格族仅提供物理内核，为优化性能不支持开启超线程配置，即不支持vCPU。例如ecs.hpc8i.32xlarge表示物理内核为64。

规格的命名主要在于规格族的差异，下方表格详细介绍了规格族的组成部分。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 规格族主体（小写字母） | 规格族后缀（小写字母+数字） |
| --- | --- |
| gn：表示搭载 NVIDIA GPU 的计算型实例 vgn：表示采用 NVIDIA GRID vGPU 加速的独享型实例 sgn：表示采用 NVIDIA GRID vGPU 加速的共享型实例 gi：表示搭载 Intel GPU 的计算型实例 f：表示 FPGA 计算型实例 ebm（c/g/r/gn/hf）：表示弹性裸金属服务器（elastic bare metal） scc（c/g/h/gn/hf）：表示超级计算集群（super computing cluster） hpc：表示高性能计算型实例（High-performance Computing ） | 6v：6 表示采用 Volta/Turing 架构；v 表示 GPU 类型为 V100 且 GPU 显存为 16 GB。 例如，gn6v 表示采用 Volta/Turing 架构，显存为 16 GB，且搭载 NVIDIA V100 GPU 的计算型实例。 6e：6 表示采用 Volta/Turing 架构；e（extend）表示第 2 代 GPU 类型为 V100 且显存为 32 GB。 例如，gn6e 表示采用 Volta/Turing 架构，显存为 32 GB，且搭载 NVIDIA V100 GPU 的计算型实例。 6i：6 表示采用 Volta/Turing 架构；i（inference）表示 GPU 类型为 T4。 例如，gn6i 表示采用 Volta/Turing 架构且搭载 NVIDIA 的 T4 GPU 计算型实例。 6s：6 表示采用 Volta/Turing 架构；s 表示第 6 代 SG-1。 例如，ebmgi6s 表示采用 Intel ® Server GPU 卡和第 6 代 SG-1 芯片的视觉计算型实例。 7：表示采用 Ampere 架构。 7i：7 表示采用 Ampere 架构；i（inference）表示 GPU 类型为 A10 且显存为 24 GB。 7e：7 表示采用 Ampere 架构；ｅ表示同一款 GPU 的大显存版本，例如 V100 的 32 GB（相对 V100 16 GB 来说）。 7s：7 表示采用 Ampere 架构；s 表示用于第 7 代 A30 GPU。 说明 一些特殊规格（例如 ecs.gn7i-c8g1.2xlarge）后缀中 c8g1 表示 vCPU:GPU=8:1. c：core，即 vCPU。 g：GPU。 |


## 实例规格指标说明

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 指标名称 | 说明 |
| --- | --- |
| 处理器 | 云服务器的物理 CPU 型号，不同处理器的性能不同： CPU 基频 ：也称为核心频率，是指处理器在未进行任何形式的超频或者特别优化的情况下的标准运行频率。基频是处理器设计者为其规定的运行速度，是在典型工作负载下保持可靠运行时的典型时钟速度。 CPU 睿频 ：是指处理器在需要时可以临时提高其核心频率来达到的最大时钟频率。 |
| vCPU | 基于 X86 架构的实例规格，每一个 vCPU 都对应一个处理器核心的超线程。 基于 ARM 架构的实例规格，每一个 vCPU 都对应一个处理器的物理核心，具有性能稳定且资源独享的特点。 |
| 突发性能 | 平均基准 CPU 计算性能 ：实例可以持续稳定地提供的 CPU 性能。 CPU 积分/小时： 实例开机后即消耗 CPU 积分维持计算性能，同时按固定速度获得 CPU 积分，CPU 积分的获得速度由实例规格决定，请参见实例规格指标数据的 CPU 积分/小时列，该指标为单台实例所有 vCPU 每小时可以获得的 CPU 积分。 最大 CPU 积分余额： 一台突发性能实例 24 小时可以获得的 CPU 积分，CPU 积分余额最多保存 24 小时，保持动态平衡。对指定实例规格来说，CPU 积分获得速度是固定的，因此 CPU 积分余额有上限。 |
| 内存 | 内存 ：用于存储和检索服务器中能够快速访问的数据。内存在服务器运行程序和处理数据时扮演着临时数据存储的角色。内存中存储的信息通常是暂时的，即当服务器关闭或重新启动时，存储在内存中的数据将会丢失。 持久内存 ：可以作为内存或本地存储使用，在支持持久内存的实例规格指标明细表格中与内存呈并列关系，持久内存支持的使用方式和实例规格有关，更多信息，请参见 [配置使用持久内存](products/ecs/documents/user-guide/configure-the-usage-mode-of-persistent-memory.md) 。 加密内存 ：基于 Intel ® SGX 技术提供的加密内存，在支持的实例规格指标明细表格中内存为总内存，包含加密内存，更多信息，请参见 [构建](products/ecs/documents/user-guide/build-an-sgx-encrypted-computing-environment.md) [SGX](products/ecs/documents/user-guide/build-an-sgx-encrypted-computing-environment.md) [机密计算环境](products/ecs/documents/user-guide/build-an-sgx-encrypted-computing-environment.md) 。 |
| 网络带宽 | 网络基础带宽 ：网络基础带宽是指在一个网络连接中的初始带宽配置，它表示在正常情况下网络连接可以传输的最大数据量。您可以根据自己的需求选择不同的基础带宽配置。更多信息，请参见 [网络带宽](products/ecs/documents/user-guide/network-bandwidth.md) 。 网络突发带宽 ：指实例在基础带宽之上，短时期内能够达到的最大数据传输速率，通过网络突发积分实现。六代及之后规格族的部分实例规格开始支持突发网络带宽。网络突发带宽是利用闲置资源的让利，不承诺 SLA。如果您的业务有明确的带宽需求，实例选型请参考实例基础网络带宽。更多信息，请参见 [突发带宽](products/ecs/documents/user-guide/network-bandwidth.md) 。 网络全双工带宽 ：7 代及以后的实例规格开始支持全双工网络带宽。在全双工网络带宽下，接收和发送两个方向的带宽可以同时达到实例预设的带宽规格（请参见规格描述中的带宽参数），而不会互相影响。您可以在全速率发送数据包的同时，也能享受全速率的接收带宽。更多信息，请参见 [内网带宽](products/ecs/documents/user-guide/network-bandwidth.md) 。 说明 实例规格指标均在纯转发测试环境下验证获得。在实际业务场景中，受实例负载类型、包长大小，长短连接，镜像版本、组网模型等其他因素的影响，实例的性能表现可能存在差异。建议您先进行业务压测，以了解实例的性能表现，从而选择合适的实例规格。 |
| 网络收发包 PPS | 网络收发包能力指出方向和入方向相加能达到的最大能力。测试网络收发包 PPS 能力的操作方法，请参见 [网络性能测试方法](products/ecs/documents/user-guide/best-practices-for-testing-network-performance.md) 。 说明 实例规格指标均在纯转发测试环境下验证获得。在实际业务场景中，受实例负载类型、包长大小，长短连接，镜像版本、组网模型等其他因素的影响，实例的性能表现可能存在差异。建议您先进行业务压测，以了解实例的性能表现，从而选择合适的实例规格。 |
| 连接数 | 连接又称网络会话，是客户端与服务器建立连接并传输数据的过程。网络五元组（包括源 IP、目的 IP、源端口、目的端口、协议）唯一确定一个连接，ECS 实例的连接数包括通过 TCP、UDP、ICMP 协议建立的连接。如果您的业务对网络并发敏感，请根据业务需求选择明确标注了连接数参数的实例。 |
| 队列数 | 实例规格支持的 单块网卡最大队列数 ，更多的队列通常意味着网络数据可以更高效地被分发和处理，减少数据包等待处理的时间，从而提升网络性能，降低数据包丢失率和网络延迟。 合理的队列数配置需要根据实际的网络负载、硬件性能和系统设置来决定。详细信息，请参见 [网卡多队列](products/ecs/documents/user-guide/nic-multi-queue.md) 。 |
| 弹性网卡数 | 实例规格支持绑定的弹性网卡数量。每台 ECS 实例可以附加一个或多个弹性网卡。辅助弹性网卡可以在不同 ECS 实例之间进行解绑和绑定操作，这使得网络配置更加灵活和可扩展，以满足不同业务场景下的网络需求。例如，实现多 IP 地址、多网卡、高可用网络方案等。详细信息，请参见 [弹性网卡](products/ecs/documents/user-guide/eni-overview.md) 。 |
| 支持挂载启用弹性 RDMA 接口的网卡（ERI）数 | 实例规格支持挂载 ERI 的数量。ERI（Elastic RDMA Interface），弹性 RDMA 网卡，完全兼容 RDMA 通信协议。ERI 完全复用普通 VPC 弹性网卡（ENI）所属的网络，让您无需改变业务组网，即可在原有网络下使用 RDMA 功能，体验 RDMA 带来的超低延迟。详细信息，请参见 [弹性](products/ecs/documents/user-guide/erdma-overview.md) [RDMA](products/ecs/documents/user-guide/erdma-overview.md) [网络](products/ecs/documents/user-guide/erdma-overview.md) 。 |
| 支持巨型帧（Jumbo frames） | 实例规格是否支持巨型帧。阿里云支持 8500 字节的巨型帧，允许您发送 8500 字节载荷的以太网帧。增大的有效载荷有助于提高链路利用率，获得更好的网络性能。关于如何开启巨型帧，请参见 [巨型帧（Jumbo Frames）](products/ecs/documents/user-guide/jumbo-frame.md) 。 |
| 单网卡私有 IPv4 地址数 | 实例规格支持的单张弹性网卡的私有 IPv4 地址数量。 |
| 单网卡 IPv6 地址数 | 实例规格支持的单张弹性网卡的 IPv6 地址数量。 |
| I/O 优化实例 | I/O 优化为实例与云盘之间提供更好的网络能力，可保证云盘存储性能的发挥。对于 I/O 优化的实例，挂载 ESSD 云盘时能够获得 ESSD 云盘的全部存储性能。 |
| 本地存储 | 本地存储，是指挂载在云服务器 ECS 所在物理机（宿主机）上的本地磁盘，是一种临时块存储，无法单独创建，控制台中使用二进制单位 GiB。 警告 本地盘的数据可靠性取决于物理机的可靠性，存在单点故障风险。使用本地盘存储数据有丢失数据的风险，请勿在本地盘上存储需要长期保存的业务数据。更多信息，请参见 [本地盘](products/ecs/documents/user-guide/local-disks.md) 。 |
| 云盘带宽 | 基础带宽 ：每个实例规格可以持续支持的最大云盘带宽能力，有 SLA 保证。 突发带宽 ：每个实例规格允许更高的带宽能力，但突发能力有时间限制，同时也要依赖整机的带宽资源，没有 SLA 保证。 |
| 云盘 IOPS | 基础 IOPS ：每个实例规格可以持续支持的最大云盘 IOPS 能力，有 SLA 保证。 突发 IOPS ：每个实例规格允许更高的 IOPS 能力，但突发能力有时间限制，同时也要依赖整机的 I/O 资源，没有 SLA 保证。 |
| vTPM | 可信计算能力：可信实例底层物理服务器搭载可信平台模块 TPM（Trusted Platform Module）/可信密码模块 TCM（Trusted Cryptography Module）作为硬件可信根 TCB（Trusted Computing Base），实现服务器的可信启动，确保零篡改。在虚拟化层面，支持虚拟可信能力 vTPM，提供实例启动过程核心组件的校验能力。 |


[上一篇：选择实例规格](products/ecs/documents/user-guide/instance-families.md)[下一篇：实例规格选型指导](products/ecs/documents/user-guide/best-practices-for-instance-type-selection.md)

该文章对您有帮助吗？

反馈

### 为什么选择阿里云

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)

### 大模型

[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)

### 产品和定价

[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)

### 技术内容

[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)

### 权益

[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)

### 服务

[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)

### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

联系我们：4008013260

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
