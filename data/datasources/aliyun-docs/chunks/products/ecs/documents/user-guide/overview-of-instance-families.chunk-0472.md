-instance-configuration-erdma.md)[实例上启用](on-the-gpu-instance-configuration-erdma.md)[eRDMA](on-the-gpu-instance-configuration-erdma.md)。
gn9gc包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | GPU 显存 | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 多队列（主网卡/辅助网卡） | 弹性网卡 | 最大挂载数据盘数 | 云盘最大带宽（GB/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.gn9gc.4xlarge | 16 | 128 | 72 GB * 1 | 16 | 360 万 | 30 | 30 | 8/32 | 8 | 1 | 1 |
| ecs.gn9gc.8xlarge | 32 | 192 | 72 GB * 1 | 32 | 750 万 | 30 | 30 | 16/64 | 8 | 1 | 1 |
| ecs.gn9gc-2x.16xlarge | 64 | 384 | 72 GB * 2 | 65 | 1500 万 | 30 | 30 | 32/64 | 15 | 2 | 2 |
| ecs.gn9gc-4x.32xlarge | 128 | 768 | 72 GB * 4 | 131 | 3000 万 | 50 | 50 | 64/64 | 15 | 4 | 4 |
| ecs.gn9gc-8x.64xlarge | 256 | 1536 | 72 GB * 8 | 204 | 3000 万 | 50 | 50 | 128/64 | 15 | 6 | 6 |

说明
gn9gc实例规格所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请确保该自定义镜像支持UEFI启动模式，并且镜像的启动模式属性已设置为UEFI模式。具体操作，请参见[通过](instance-startup-mode.md)[API](instance-startup-mode.md)[设置自定义镜像的启动模式为](instance-startup-mode.md)[UEFI](instance-startup-mode.md)[模式](instance-startup-mode.md)。
