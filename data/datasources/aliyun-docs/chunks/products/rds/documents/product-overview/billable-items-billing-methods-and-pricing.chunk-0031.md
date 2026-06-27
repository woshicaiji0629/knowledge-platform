### 应急恢复

| 类别 | 说明 |
| --- | --- |
| 定义 | RDS MySQL 高性能本地盘实例的应急恢复功能涉及的计费项如下： CDM 本地盘存储容量（CapacitySandboxStorageSize） ：开启 数据灾备 沙箱功能后，每个数据库实例将对应一个沙箱存储。系统会自动将对应数据库实例的数据同步至沙箱存储中，生成多个沙箱快照。 数据灾备 将根据沙箱存储中的数据量收取沙箱存储费用。 CDM 沙箱实例规格（SandboxDatabaseSpec） ：恢复到临时沙箱实例后， 数据灾备 将根据临时沙箱实例的规格和使用时长收取临时沙箱实例费用（按小时扣费）。如果您没有恢复临时沙箱实例，则不会产生临时沙箱实例费用。 功能详情，请参见 [RDS MySQL](../apsaradb-rds-for-mysql/create-an-rds-emergency-instance.md) [应急恢复](../apsaradb-rds-for-mysql/create-an-rds-emergency-instance.md) 。 |
| 账单产品 | 数据库备份。 |
| 计费公式 | CDM 本地盘存储容量费用 = CDM 本地盘存储容量单价 * 使用时长 * CDM 本地盘存储容量 CDM 沙箱实例规格费用 = 沙箱实例规格单价 * 使用时长 说明 CDM 本地盘存储容量单价，请参见 [沙箱存储费用](https://help.aliyun.com/zh/dbs/product-overview/dbs-sandbox-fees#section-zem-2el-l1d) 。 沙箱实例规格单价，请参见 [临时沙箱实例费用](https://help.aliyun.com/zh/dbs/product-overview/dbs-sandbox-fees#section-kbj-aba-mlq) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | [CDM](https://help.aliyun.com/zh/dbs/product-overview/dbs-sandbox-fees#7b28e1cf9fpmy) [沙箱存储包](https://help.aliyun.com/zh/dbs/product-overview/dbs-sandbox-fees#7b28e1cf9fpmy) 可以抵扣 包年包月或按量付费 RDS MySQL 高性能本地盘 实例的 CDM 本地盘存储容量（CapacitySandboxStorageSize） 费用。 |
