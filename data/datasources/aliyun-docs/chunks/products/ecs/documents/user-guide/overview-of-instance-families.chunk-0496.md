d)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
gn6v包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | GPU | GPU 显存 | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 云盘基础 IOPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.gn6v-c8g1.2xlarge | 8 | 32 | NVIDIA V100 * 1 | 16GB * 1 | 2.5 | 80 万 | 无 | 4 | 4 | 10 | 1 |
| ecs.gn6v-c8g1.4xlarge | 16 | 64 | NVIDIA V100 * 2 | 16GB * 2 | 5 | 100 万 | 无 | 4 | 8 | 20 | 1 |
| ecs.gn6v-c8g1.8xlarge | 32 | 128 | NVIDIA V100 * 4 | 16GB * 4 | 10 | 200 万 | 无 | 8 | 8 | 20 | 1 |
| ecs.gn6v-c8g1.16xlarge | 64 | 256 | NVIDIA V100 * 8 | 16GB * 8 | 20 | 250 万 | 无 | 16 | 8 | 20 | 1 |
| ecs.gn6v-c10g1.20xlarge | 82 | 336 | NVIDIA V100 * 8 | 16GB * 8 | 35 | 450 万 | 25 万 | 16 | 8 | 20 | 1 |
