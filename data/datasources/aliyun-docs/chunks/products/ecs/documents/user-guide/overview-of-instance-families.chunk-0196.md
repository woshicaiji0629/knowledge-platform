-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
i4g包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | 本地存储 | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 云盘基础 IOPS | 云盘基础带宽（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.i4g.4xlarge | 16 | 64 | 1 * 959 GB (1 * 894 GiB) | 8/25 | 300 万 | 10 万 | 6 |
| ecs.i4g.8xlarge | 32 | 128 | 1 * 1919 GB (1 * 1788 GiB) | 16/25 | 600 万 | 15 万 | 8 |
| ecs.i4g.16xlarge | 64 | 256 | 2 * 1919 GB (2 * 1788 GiB) | 32/无 | 1200 万 | 30 万 | 16 |
| ecs.i4g.32xlarge | 128 | 512 | 4 * 1919 GB (4 * 1788 GiB) | 64/无 | 2400 万 | 60 万 | 32 |

说明
该实例规格族仅支持Linux镜像，创建实例时请选择Linux镜像，否则会创建失败。
