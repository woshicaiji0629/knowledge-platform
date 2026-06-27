### 存储压缩

| 类别 | 说明 |
| --- | --- |
| 定义 | 开启 [存储压缩](../apsaradb-rds-for-mysql/storage-compression.md) 功能后，实例的单位存储空间的计费公式会发生变化。 |
| 计费公式 | 包年包月或按量付费的高可用系列：存储空间费用 = 1.25 * 实例存储空间单价 * 实例存储空间 * 使用时长 包年包月或按量付费的集群系列：存储空间费用 = 1.25 * 单节点存储空间单价 * 单节点存储空间 * 节点数 * 使用时长 |
| 计费方式 | 包年包月、按量付费。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [存储包](storage-plans.md) 可以抵扣 按量付费 的 RDS 实例（不包括高性能云盘和 SSD 云盘）的存储空间费用。 [通用型节省计划](savings-plan-introduction.md) 可以抵扣 按量付费 和 Serverless 的 RDS 实例的存储空间费用。 [弹性型（特惠版）节省计划](../apsaradb-rds-for-mysql/elastic-savings-plan.md) 可以抵扣 Serverless 的 RDS 实例的存储空间费用。 |
