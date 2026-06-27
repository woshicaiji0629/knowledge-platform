pv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
仅支持专有网络VPC。
s6包括的实例规格及指标数据如下表所示。

| 实例规格 | vCPU | 内存（GiB） | 网络基础带宽（Gbit/s） | 网络收发包 PPS（万） | 多队列 | 弹性网卡 | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.s6-c1m1.small | 1 | 1.0 | 0.1 | 15 | 1 | 2 | 2 | 1 |
| ecs.s6-c1m2.small | 1 | 2.0 | 0.1 | 15 | 1 | 2 | 2 | 1 |
| ecs.s6-c1m4.small | 1 | 4.0 | 0.1 | 15 | 1 | 2 | 2 | 1 |
| ecs.s6-c1m2.large | 2 | 4.0 | 0.2 | 20 | 1 | 2 | 2 | 1 |
| ecs.s6-c1m4.large | 2 | 8.0 | 0.4 | 20 | 1 | 2 | 2 | 1 |
| ecs.s6-c1m2.xlarge | 4 | 8.0 | 0.4 | 30 | 1 | 2 | 6 | 1 |
| ecs.s6-c1m4.xlarge | 4 | 16.0 | 0.8 | 30 | 1 | 2 | 6 | 1 |
| ecs.s6-c1m2.2xlarge | 8 | 16.0 | 0.8 | 60 | 2 | 2 | 6 | 1 |
| ecs.s6-c1m4.2xlarge | 8 | 32.0 | 1.2 | 60 | 2 | 2 | 6 | 1 |

说明
本规格族不支持在创建实例时添加辅助弹性网卡，可以在创建实例后添加。绑定和解绑辅助弹性网卡时，部分实例规格的实例必须处于已停止状态，包括ecs.s6-c1m1.small、ecs.s6-c1m2.large、ecs.s6-c1m2.small、ecs.s6-c1m4.large、ecs.s6-c1m4.small。
指标的含义请参见[实例规格族](overview-of-instance-families.md)。由于业务场景的不同，网络收发包PPS会存在明显差异。因此，我们建议您进行业务压测以了解实例的性能表现，以便选择合适的实例规格。
