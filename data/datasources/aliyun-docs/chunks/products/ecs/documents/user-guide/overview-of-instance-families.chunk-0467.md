](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
vgn7i-vws包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | GPU | GPU 显存 | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.vgn7i-vws-m4.xlarge | 4 | 30 | NVIDIA A10 * 1/6 | 24GB * 1/6 | 3 | 100 万 | 4 | 4 | 10 | 1 |
| ecs.vgn7i-vws-m8.2xlarge | 10 | 62 | NVIDIA A10 * 1/3 | 24GB * 1/3 | 5 | 200 万 | 8 | 6 | 10 | 1 |
| ecs.vgn7i-vws-m12.3xlarge | 14 | 93 | NVIDIA A10 * 1/2 | 24GB * 1/2 | 8 | 300 万 | 8 | 6 | 15 | 1 |
| ecs.vgn7i-vws-m24.7xlarge | 30 | 186 | NVIDIA A10 * 1 | 24GB * 1 | 16 | 600 万 | 12 | 8 | 30 | 1 |

说明
上表中的GPU列对应的指标包括GPU卡型号和GPU分片信息。其中，GPU分片表示1块GPU分成多片，每个实例上使用1片。例如：
NVIDIA A10 * 1/6中的NVIDIA A10表示GPU卡型号；1/6表示GPU的分片，即1块GPU分成6片，每个实例上使用1片。
