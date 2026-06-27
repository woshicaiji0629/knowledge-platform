md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
d3c包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | 本地存储 | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS（万） | 云盘 IOPS 基础/突发（万） | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.d3c.3xlarge | 14 | 56.0 | 1 * 13743 GB (1 * 12800 GiB) | 8/最高 10 | 160 | 4/无 | 3/无 |
| ecs.d3c.7xlarge | 28 | 112.0 | 2 * 13743 GB (2 * 12800 GiB) | 16/最高 25 | 250 | 5/无 | 4/无 |
| ecs.d3c.14xlarge | 56 | 224.0 | 4 * 13743 GB (4 * 12800 GiB) | 40/无 | 500 | 10/无 | 8/无 |

说明
该实例规格族仅支持Linux镜像，创建实例时请选择Linux镜像，否则会创建失败。
