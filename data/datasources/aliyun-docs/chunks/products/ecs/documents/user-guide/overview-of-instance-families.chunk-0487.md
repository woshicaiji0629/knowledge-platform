d)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
gn7s包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | GPU | GPU 显存 | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 多队列 | 弹性网卡 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.gn7s-c8g1.2xlarge | 8 | 60 | NVIDIA A30 * 1 | 24GB * 1 | 16 | 160 万 | 5 | 1 | 8 | 4 |
| ecs.gn7s-c16g1.4xlarge | 16 | 120 | NVIDIA A30 * 1 | 24GB * 1 | 16 | 300 万 | 5 | 1 | 8 | 8 |
| ecs.gn7s-c32g1.8xlarge | 32 | 250 | NVIDIA A30 * 1 | 24GB * 1 | 16 | 600 万 | 5 | 1 | 12 | 8 |
| ecs.gn7s-c32g1.16xlarge | 64 | 500 | NVIDIA A30 * 2 | 24GB * 2 | 32 | 1200 万 | 5 | 1 | 16 | 15 |
| ecs.gn7s-c32g1.32xlarge | 128 | 1000 | NVIDIA A30 * 4 | 24GB * 4 | 64 | 2400 万 | 10 | 1 | 32 | 15 |
| ecs.gn7s-c48g1.12xlarge | 48 | 380 | NVIDIA A30 * 1 | 24GB * 1 | 16 | 900 万 | 8 | 1 | 16 | 8 |
| ecs.gn7s-c56g1.14xlarge | 56 | 440 | NVIDIA A30 * 1 | 24GB * 1 | 16 | 1000 万 | 8 | 1 | 16 | 8 |
