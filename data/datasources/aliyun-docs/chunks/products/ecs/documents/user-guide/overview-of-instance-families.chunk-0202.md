md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
i3g包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | 本地存储 | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 云盘基础 IOPS | 云盘基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.i3g.2xlarge | 8 | 32 | 1 * 479 GB (1 * 447 GiB) | 3/10 | 175 万 | 5.25 万 | 2 |
| ecs.i3g.4xlarge | 16 | 64 | 1 * 959 GB (1 * 894 GiB) | 5/10 | 350 万 | 8.4 万 | 3 |
| ecs.i3g.8xlarge | 32 | 128 | 2 * 959 GB (2 * 894 GiB) | 12/无 | 700 万 | 15.75 万 | 5 |
| ecs.i3g.13xlarge | 52 | 192 | 3 * 959 GB (3 * 894 GiB) | 16/无 | 1200 万 | 25.2 万 | 8 |
| ecs.i3g.26xlarge | 104 | 384 | 6 * 959 GB (6 * 894 GiB) | 32/无 | 2400 万 | 50 万 | 16 |

说明
该实例规格族仅支持Linux镜像，创建实例时请选择Linux镜像，否则会创建失败。
