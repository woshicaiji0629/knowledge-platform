.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
i3包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | 本地存储 | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 云盘基础 IOPS | 云盘基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.i3.xlarge | 4 | 32 | 1 * 959 GB (1 * 894 GiB) | 1.5/10 | 100 万 | 4 万 | 1.5 |
| ecs.i3.2xlarge | 8 | 64 | 1 * 1919 GB (1 * 1788 GiB) | 2.5/10 | 160 万 | 5 万 | 2 |
| ecs.i3.4xlarge | 16 | 128 | 2 * 1919 GB (2 * 1788 GiB) | 5/10 | 300 万 | 8 万 | 3 |
| ecs.i3.8xlarge | 32 | 256 | 4 * 1919 GB (4 * 1788 GiB) | 10/无 | 600 万 | 15 万 | 5 |
| ecs.i3.13xlarge | 52 | 384 | 6 * 1919 GB (6 * 1788 GiB) | 16/无 | 900 万 | 24 万 | 8 |
| ecs.i3.26xlarge | 104 | 768 | 12 * 1919 GB (12 * 1788 GiB) | 32/无 | 2400 万 | 48 万 | 16 |

说明
该实例规格族仅支持Linux镜像，创建实例时请选择Linux镜像，否则会创建失败。
