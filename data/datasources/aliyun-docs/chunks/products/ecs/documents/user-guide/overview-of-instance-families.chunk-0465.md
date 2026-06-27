](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
sgn7i-vws包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | GPU | GPU 显存 | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.sgn7i-vws-m2.xlarge | 4 | 15.5 | NVIDIA A10 * 1/12 | 24GB * 1/12 | 1.5/5 | 50 万 | 4 | 2 | 2 | 1 |
| ecs.sgn7i-vws-m4.2xlarge | 8 | 31 | NVIDIA A10 * 1/6 | 24GB * 1/6 | 2.6/10 | 100 万 | 4 | 4 | 6 | 1 |
| ecs.sgn7i-vws-m8.4xlarge | 16 | 62 | NVIDIA A10 * 1/3 | 24GB * 1/3 | 5/20 | 200 万 | 8 | 4 | 10 | 1 |
| ecs.sgn7i-vws-m2s.xlarge | 4 | 8 | NVIDIA A10 * 1/12 | 24GB * 1/12 | 1.5/5 | 50 万 | 4 | 2 | 2 | 1 |
| ecs.sgn7i-vws-m4s.2xlarge | 8 | 16 | NVIDIA A10 * 1/6 | 24GB * 1/6 | 2.6/10 | 100 万 | 4 | 4 | 6 | 1 |
| ecs.sgn7i-vws-m8s.4xlarge | 16 | 32 | NVIDIA A10 * 1/3 | 24GB * 1/3 | 5/20 | 200 万 | 8 | 4 | 10 | 1 |

说明
上表中的GPU列对应的指标包括GPU卡型号和GPU分片信息。其中，GPU分片表示1块GPU分成多片，每个实例上使用1片。例如：
NVIDIA A10 * 1/12中的NVIDIA A10表示GPU卡型号；1/12表示GPU分片，即1块GPU分成12片，每个实例上使用1片。
