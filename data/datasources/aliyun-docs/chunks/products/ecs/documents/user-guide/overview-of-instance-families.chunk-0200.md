md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
i4p包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | 持久内存（GiB） | 网络带宽基础/突发（Gbit/s） | 网络收发包 PPS | 云盘 IOPS 基础/突发 | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.i4p.2xlarge | 8 | 32 | 1 * 126 | 5/10 | 160 万 | 5 万/11 万 | 3/6 |
| ecs.i4p.4xlarge | 16 | 64 | 2 * 126 | 10/25 | 300 万 | 8 万/11 万 | 5/6 |
| ecs.i4p.6xlarge | 24 | 96 | 3 * 126 | 12/25 | 450 万 | 11 万/无 | 6/无 |
| ecs.i4p.8xlarge | 32 | 128 | 4 * 126 | 16/25 | 600 万 | 15 万/无 | 8/无 |
| ecs.i4p.16xlarge | 64 | 256 | 1 * 1008 | 32/无 | 1200 万 | 30 万/无 | 16/无 |
| ecs.i4p.32xlarge | 128 | 512 | 2 * 1008 | 64/无 | 2400 万 | 60 万/无 | 32/无 |
