## 归档备份空间

| 类别 | 说明 |
| --- | --- |
| 定义 | 备份天数超过 730 天的数据备份自动转为归档备份，产生的计费项名称为 长期备份（ArchivedBackupCharged） 。 功能详情，请参见 [自动备份](../apsaradb-rds-for-mysql/enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md) 。 |
| 账单产品 | 关系型数据库。 |
| 计费公式 | 归档备份空间费用= 归档备份空间单价 * 归档备份空间用量 * 时长 说明 归档备份空间单价，请参见 [备份费用](../apsaradb-rds-for-mysql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md) 。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [存储包](storage-plans.md) 可以抵扣 包年包月或按量付费 的 RDS 实例的归档备份空间。 [通用型节省计划](savings-plan-introduction.md) 可以抵扣 包年包月、按量付费以及 Serverless RDS 实例的归档备份空间费用。 |

说明
跨地域备份产生的计费项，账单产品包括关系型数据库和数据库备份，详情请参见[数据灾备：跨地域备份、已删除实例备份空间、下载备份](billable-items-billing-methods-and-pricing.md)。
已删除实例的备份空间、下载备份产生的计费项，账单产品是数据库备份，详情请参见[数据灾备：跨地域备份、已删除实例备份空间、下载备份](billable-items-billing-methods-and-pricing.md)。
