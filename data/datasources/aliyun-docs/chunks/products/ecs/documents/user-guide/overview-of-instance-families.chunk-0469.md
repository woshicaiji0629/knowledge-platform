](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
vgn6i-vws包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | GPU | GPU 显存 | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.vgn6i-m4-vws.xlarge | 4 | 23 | NVIDIA T4 * 1/4 | 16GB * 1/4 | 2 | 50 万 | 4/2 | 3 | 10 | 1 |
| ecs.vgn6i-m8-vws.2xlarge | 10 | 46 | NVIDIA T4 * 1/2 | 16GB * 1/2 | 4 | 80 万 | 8/2 | 4 | 10 | 1 |
| ecs.vgn6i-m16-vws.5xlarge | 20 | 92 | NVIDIA T4 * 1 | 16GB * 1 | 7.5 | 120 万 | 6 | 4 | 10 | 1 |

说明
上表中的GPU列对应的指标包括GPU卡型号和GPU分片信息。其中，GPU分片表示1块GPU分成多片，每个实例上使用1片。例如：
NVIDIA T4 * 1/4中的NVIDIA T4表示GPU卡型号；1/4表示GPU的分片，即1块GPU分成4片，每个实例上使用1片。
