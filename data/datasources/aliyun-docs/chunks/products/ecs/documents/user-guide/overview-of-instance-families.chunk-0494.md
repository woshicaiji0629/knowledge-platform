d)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
gn6e包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | GPU | GPU 显存 | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.gn6e-c12g1.3xlarge | 12 | 92 | NVIDIA V100 * 1 | 32GB * 1 | 5 | 80 万 | 8 | 6 | 10 | 1 |
| ecs.gn6e-c12g1.6xlarge | 24 | 184 | NVIDIA V100 * 2 | 32GB * 2 | 8 | 120 万 | 8 | 8 | 20 | 1 |
| ecs.gn6e-c12g1.12xlarge | 48 | 368 | NVIDIA V100 * 4 | 32GB * 4 | 16 | 240 万 | 8 | 8 | 20 | 1 |
| ecs.gn6e-c12g1.24xlarge | 96 | 736 | NVIDIA V100 * 8 | 32GB * 8 | 32 | 450 万 | 16 | 8 | 20 | 1 |
