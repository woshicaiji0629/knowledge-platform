md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
实例网络性能与实例规格对应，规格越高网络性能越强。
d3s包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | 本地存储 | 网络基础带宽/突发（Gbit/s） | 网络收发包 PPS（万） | 云盘带宽基础/突发（Gbit/s） |
| --- | --- | --- | --- | --- | --- | --- |
| ecs.d3s.2xlarge | 8 | 32 | 4 * 11918 GB (4 * 11100 GiB) | 10/最高 15 | 200 | 3/最高 5 |
| ecs.d3s.4xlarge | 16 | 64 | 8 * 11918 GB (8 * 11100 GiB) | 25/无 | 300 | 5/无 |
| ecs.d3s.8xlarge | 32 | 128 | 16 * 11918 GB (16 * 11100 GiB) | 40/无 | 600 | 8/无 |
| ecs.d3s.12xlarge | 48 | 192 | 24 * 11918 GB (24 * 11100 GiB) | 60/无 | 900 | 12/无 |
| ecs.d3s.16xlarge | 64 | 256 | 32 * 11918 GB (32 * 11100 GiB) | 80/无 | 1200 | 16/无 |
