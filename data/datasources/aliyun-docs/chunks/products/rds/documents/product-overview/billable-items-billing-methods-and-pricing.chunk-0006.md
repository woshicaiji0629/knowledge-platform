### 性能自动扩容

| 类别 | 说明 |
| --- | --- |
| 定义 | 开启 [性能自动扩容](../apsaradb-rds-for-mysql/enable-the-automatic-scale-up-feature-for-an-apsaradb-rds-for-mysql-instance.md) 功能不收费。但开启后，如果当 CPU 使用率达到阈值，会触发 RDS MySQL 实例计算资源的变配，增加的计算资源会按量计费。 云盘实例，性能自动扩容时会变配到其他 RDS 规格，系统会按新的规格收取实例的 [RDS](billable-items-billing-methods-and-pricing.md) [规格](billable-items-billing-methods-and-pricing.md) 费用。费用变化规则与变更配置相同，详情请参见 [变更配置](specification-changes.md) 。 高性能本地盘实例，性能自动扩容时会自动增加 CPU 核数，产生新的计费项，名称为 弹性计算资源（CPU+IOPS） ，计费项 Code 为 cpu_cores_flexible。 |
| 计费公式 | 高性能本地盘实例弹性计算资源费用=CPU 单价 * 增加的 CPU 核数 * 时长 云盘实例新的 RDS 规格费用=RDS 规格实例单价 * 时长 说明 高性能本地盘实例性能自动扩容的 CPU 单价，请参见 [设置性能自动扩容](../apsaradb-rds-for-mysql/enable-the-automatic-scale-up-feature-for-an-apsaradb-rds-for-mysql-instance.md) 。 云盘实例 RDS 规格实例单价与售卖页的 RDS 规格实例单价相同。 |
| 计费方式 | 按量付费。 |
| 是否支持节省计划或资源包抵扣 | 支持。 [计算包](compute-plans.md) 和 [通用型节省计划](savings-plan-introduction.md) 可以抵扣 按量付费的 RDS 云盘实例的 RDS 规格（rds_class） 费用。 |
