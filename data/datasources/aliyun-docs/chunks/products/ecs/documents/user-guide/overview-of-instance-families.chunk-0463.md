[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
sgn8ia包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | GPU 显存 | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 多队列 | 弹性网卡 | 单网卡私有 IPv4/IPv6 地址数 | 最大支持云盘数量 | 云盘基础 IOPS | 云盘基准 BPS（M） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.sgn8ia-m2.xlarge | 4 | 16 | 2 GB | 2.5 | 100 万 | 4 | 4 | 15/15 | 9 | 3 万 | 244 |
| ecs.sgn8ia-m4.2xlarge | 8 | 32 | 4 GB | 4 | 160 万 | 8 | 4 | 15/15 | 9 | 4.5 万 | 305 |
| ecs.sgn8ia-m8.4xlarge | 16 | 64 | 8 GB | 7 | 200 万 | 16 | 8 | 30/30 | 17 | 6 万 | 427 |
| ecs.sgn8ia-m16.8xlarge | 32 | 128 | 16 GB | 10 | 300 万 | 32 | 8 | 30/30 | 33 | 8 万 | 610 |
| ecs.sgn8ia-m24.12xlarge | 48 | 192 | 24 GB | 16 | 450 万 | 48 | 8 | 30/30 | 33 | 12 万 | 1000 |
| ecs.sgn8ia-m48.24xlarge | 96 | 384 | 48 GB | 32 | 900 万 | 64 | 15 | 30/30 | 33 | 24 万 | 2000 |

说明
上表中的GPU均为采用vGPU技术切分后的vGPU分片。
sgn8ia实例的内存和GPU显存均为实例独享，CPU为共享资源，超售比约为1:1.5。如对CPU算力有特殊要求，请购买直通GPU的独享型实例（例如GPU计算型实例gn7i等）。
