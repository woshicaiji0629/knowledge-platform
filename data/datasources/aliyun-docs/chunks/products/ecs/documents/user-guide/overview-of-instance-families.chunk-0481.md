d)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
gn7e包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | GPU 显存 | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.gn7e-c16g1.4xlarge | 16 | 125 | 80GB * 1 | 8 | 300 万 | 8 | 8 | 10 | 1 |
| ecs.gn7e-c16g1.8xlarge | 32 | 250 | 80GB * 2 | 16 | 600 万 | 16 | 8 | 10 | 1 |
| ecs.gn7e-c16g1.16xlarge | 64 | 500 | 80GB * 4 | 32 | 1200 万 | 32 | 8 | 10 | 1 |
| ecs.gn7e-c16g1.32xlarge | 128 | 1000 | 80GB * 8 | 64 | 2400 万 | 32 | 16 | 15 | 1 |
