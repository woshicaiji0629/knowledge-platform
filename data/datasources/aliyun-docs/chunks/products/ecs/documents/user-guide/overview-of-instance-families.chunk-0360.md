网卡 IPv6 地址数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.ebmgn7e.32xlarge | 128 | 1024 | 80GB * 8 | 64 | 2400 万 | 32/12 | 32 | 10 | 1 |

MIG（Multi-Instance GPU）功能需要您在ebmgn7e实例启动后自行检查并决定是否开启或关闭，系统无法保证MIG（Multi-Instance GPU）功能是开启或关闭状态。关于MIG（Multi-Instance GPU）的更多信息，请参见[NVIDIA Multi-Instance GPU User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#supported-gpus)。
ebmgn7e实例是否支持开启MIG功能的说明如下所示：

| 实例规格 | 是否支持开启 MIG 功能 | 说明 |
| --- | --- | --- |
| ecs.ebmgn7e.32xlarge | 是 | ebmgn7e 裸金属实例支持开启 MIG 功能。 |
