### 存储空间

| 类别 | 说明 |
| --- | --- |
| 定义 | 包年包月、按量付费 或 Serverless 的 RDS 实例（包括常规实例、只读实例、灾备实例、 、DuckDB 分析实例 ）的存储空间的费用。计费项名称为 存储空间（rds_storage 或 Storage） 。 创建实例后，会产生该计费项。实例的存储空间增加或减少，会导致该计费项的费用变化。 |
| 计费公式 | 包年包月或按量付费的基础系列、高可用系列：存储空间费用=实例存储空间单价 * 实例存储空间容量 * 时长 包年包月或按量付费的集群系列：存储空间费用=单节点存储空间单价 * 单节点存储空间容量 * 节点数 * 时长 RDS MySQL Serverless 实例、RDS PostgreSQL Serverless 实例：存储空间费用=单节点存储空间单价*单节点存储空间容量 * 节点数 * 时长 RDS SQL Server Serverless 实例：存储空间费用=实例存储空间单价 * 实例存储空间容量 * 时长 说明 RDS 存储空间单价与地域、产品系列、存储类型和计费方式相关，具体价格请以控制台为准。 不同计费方式下，计算公式中的时长会有所不同。 包年包月实例：计算时长为购买时长。 按量付费 或 Serverless 实例：计算时长为计费时长，计费周期为 1 小时。 开启存储压缩功能后，实例的单位存储空间的计费公式会发生变化，详情请参见 [存储压缩](billable-items-billing-methods-and-pricing.md) 。 |
| 计费方式 | 包年包月、按量付费 和 Serverless 。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [存储包](storage-plans.md) 可以抵扣 按量付费 的 RDS 实例（不包括高性能云盘和 SSD 云盘）的存储空间费用。 [通用型节省计划](savings-plan-introduction.md) 可以抵扣 按量付费 和 Serverless 的 RDS 实例的存储空间费用。 [弹性型（特惠版）节省计划](../apsaradb-rds-for-mysql/elastic-savings-plan.md) 可以抵扣 Serverless 的 RDS 实例的存储空间费用。 |
