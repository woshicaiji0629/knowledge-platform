d)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
gn6i包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | GPU | GPU 显存 | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 云盘基础 IOPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.gn6i-c4g1.xlarge | 4 | 15 | NVIDIA T4 * 1 | 16GB * 1 | 4 | 250 万 | 无 | 2 | 2 | 10 | 1 |
| ecs.gn6i-c8g1.2xlarge | 8 | 31 | NVIDIA T4 * 1 | 16GB * 1 | 5 | 250 万 | 无 | 2 | 2 | 10 | 1 |
| ecs.gn6i-c16g1.4xlarge | 16 | 62 | NVIDIA T4 * 1 | 16GB * 1 | 6 | 250 万 | 无 | 4 | 3 | 10 | 1 |
| ecs.gn6i-c24g1.6xlarge | 24 | 93 | NVIDIA T4 * 1 | 16GB * 1 | 7.5 | 250 万 | 无 | 6 | 4 | 10 | 1 |
| ecs.gn6i-c40g1.10xlarge | 40 | 155 | NVIDIA T4 * 1 | 16GB * 1 | 10 | 160 万 | 无 | 16 | 10 | 10 | 1 |
| ecs.gn6i-c24g1.12xlarge | 48 | 186 | NVIDIA T4 * 2 | 16GB * 2 | 15 | 450 万 | 无 | 12 | 6 | 10 | 1 |
| ecs.gn6i-c24g1.24xlarge | 96 | 372 | NVIDIA T4 * 4 | 16GB * 4 | 30 | 450 万 | 25 万 | 24 | 8 | 10 | 1 |
