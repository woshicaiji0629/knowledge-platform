| 计费项 | 主要计费公式 | 计费时长 |
| --- | --- | --- |
| [实例规格](instance-types.md) | 实例规格费用 = 实例规格单价 × 计费时长 同一实例规格在不同地域的价格可能不同，具体请参见 [云服务器](https://www.aliyun.com/price/product) [ECS](https://www.aliyun.com/price/product) [定价页](https://www.aliyun.com/price/product) 。 | 按秒计量，从实例创建开始，到实例释放时终止。 即使实例未运行业务，实例规格仍会在实例释放前持续计费。 |
| [云盘（系统盘/数据盘）](block-storage-devices.md) | 云盘容量费用 = 云盘单价 × 云盘容量× 计费时长 云盘容量为您在购买时的云盘配置容量，同一类型的 云盘 在不同地域的价格均可能不同，具体请参见 [块存储价格](https://www.aliyun.com/price/product#/disk/detail) ESSD AutoPL 云盘 、ESSD PL-X 云盘 若配置预配置性能、开启性能突发会产生额外费用，详见 [块存储计费](block-storage-devices.md) 。 | 按秒计量，从实例创建完成开始，至实例释放时终止。 |
| [镜像](images.md) | 镜像操作系统许可证费用 = 镜像单价 × 计费时长 公共镜像价格请参见 [镜像计费](images.md) 。 | 按秒计量。从使用付费镜像的实例创建完成开始计费，到实例释放或者更换为其他操作系统时结束计费。 |
| [公网带宽（按固定带宽）](public-bandwidth.md) | 公网带宽费用（按固定带宽） = 固定带宽单价 × 固定带宽大小 × 计费时长 不同地域的公网带宽价格请参见 [云服务器](https://www.aliyun.com/price/product#/ecs/detail) [ECS](https://www.aliyun.com/price/product#/ecs/detail) [定价](https://www.aliyun.com/price/product#/ecs/detail) 中的 带宽价格 页签。 | 按秒计量，从实例创建完成开始，至实例释放时或关闭公网带宽（带宽值为 0）后终止计费。 若实例创建后更换镜像，则更换后旧镜像终止计费，新镜像开始计费。 |
| [快照](snapshots-1.md) | 快照存储费用 = 快照单价 × 快照容量 × 计费时长 阿里云根据您使用的快照类型以及对应的快照容量，按每个地域单独结算快照费用，请参见 [ECS](https://www.
