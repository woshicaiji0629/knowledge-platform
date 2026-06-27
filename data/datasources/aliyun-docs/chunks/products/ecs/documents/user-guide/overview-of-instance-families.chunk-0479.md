eRDMA](on-the-gpu-instance-configuration-erdma.md)。
安全：支持可信计算（vTPM）特性。更多详情，请参见[可信计算能力概述](overview-of-trusted-computing-capabilities.md)。
gn8is包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | GPU | GPU 显存 | 网络基础带宽（Gbit/s） | 弹性网卡 | 队列数量（主） | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 最大支持云盘数量 | 云盘基础 IOPS | 云盘基础带宽（GB/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.gn8is.2xlarge | 8 | 64 | L20 * 1 | 48GB * 1 | 8 | 4 | 8 | 15 | 15 | 17 | 6 万 | 0.75 |
| ecs.gn8is.4xlarge | 16 | 128 | L20 * 1 | 48GB * 1 | 16 | 8 | 16 | 30 | 30 | 17 | 12 万 | 1.25 |
| ecs.gn8is-2x.8xlarge | 32 | 256 | L20 * 2 | 48GB * 2 | 32 | 8 | 32 | 30 | 30 | 33 | 25 万 | 2 |
| ecs.gn8is-4x.16xlarge | 64 | 512 | L20 * 4 | 48GB * 4 | 64 | 8 | 64 | 30 | 30 | 33 | 45 万 | 4 |
| ecs.gn8is-8x.32xlarge | 128 | 1024 | L20 * 8 | 48GB * 8 | 100 | 15 | 64 | 50 | 50 | 65 | 90 万 | 8 |
