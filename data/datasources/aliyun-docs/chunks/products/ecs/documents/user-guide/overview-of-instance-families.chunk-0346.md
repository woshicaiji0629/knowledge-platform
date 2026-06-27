iguration-erdma.md)[eRDMA](on-the-gpu-instance-configuration-erdma.md)。
ebmgn9gc包括的实例规格及指标数据如下表所示。
说明
如需更大内存的版本，可选用[ebmgn9ge](overview-of-instance-families.md)。

| 实例规格 | vCPU | 内存（GiB） | GPU 显存 | 网络基础带宽（Gbit/s） | 网络收发包 PPS | 单网卡私有 IPv4 地址数 | 单网卡 IPv6 地址数 | 多队列（主网卡/辅助网卡） | 弹性网卡 | 最大挂载数据盘数 | 云盘最大带宽（GB/s） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.ebmgn9gc.64xlarge | 256 | 1536 | 72GB * 8 | 360（180 * 2） | 3000 万 | 30 | 30 | 64/16 | 38 | 33 | 8 |

说明
ebmgn9gc实例规格所使用的镜像启动模式必须为UEFI模式。如果您需要使用自定义镜像，请确保该自定义镜像支持UEFI启动模式，并且镜像的启动模式属性已设置为UEFI模式。具体操作，请参见[实例启动模式](instance-startup-mode.md)。
