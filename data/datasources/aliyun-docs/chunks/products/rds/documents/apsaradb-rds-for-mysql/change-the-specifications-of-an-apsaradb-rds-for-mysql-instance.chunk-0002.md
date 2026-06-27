## 限制
变配订单操作限制：提交配置变更订单后无法取消，请在执行变配前详细评估业务需求。
只读实例变配限制：
变更只读实例配置时，其所属主实例必须处于运行中状态。
只读实例的存储空间必须大于或等于主实例当前存储空间。建议先完成所有只读实例的存储扩容，再扩容主实例存储空间。
DuckDB分析只读实例的存储空间需要大于等于主实例的一半。
存储空间缩容限制：
高性能本地盘实例缩容
缩容后的空间必须大于或等于当前已使用存储空间的120%。
示例：实例存储空间100 GB（已用50 GB），缩容后至少需保留60 GB（50×120%）。
通用缩容限制
基础系列或高可用系列：支持同一系列、同一架构下缩容。
最小缩容值计算：min{当前使用量×1.3, 当前使用量+400 GB}，且需大于或等于当前规格支持的最小存储空间。
调整步长：存储空间调整单位为5 GB。
当实例Binlog产生较快时，需要本地保留足够多的日志，才允许实例进行缩容。日志备份的开启方法，请参见[修改](enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)[RDS](enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)[备份策略](enable-the-automatic-backup-feature-for-an-apsaradb-rds-for-mysql-instance.md)。
产品类型变配限制：
可用区兼容性：相比标准版，倚天版[支持的可用区](../product-overview/product-types.md)更少。如果因可用区限制导致无法变更，请先[变更实例可用区](migrate-an-apsaradb-rds-for-mysql-instance-across-zones-in-the-same-region.md)，再变更产品类型。
内核版本约束：变更后内核小版本必须大于或等于当前版本。若当前版本更高，则不支持变更。
系列约束：基础系列仅支持从倚天版变更为标准版，高可用和集群系列可在倚天版与标准版间互相变更。
[历史规格实例](primary-apsaradb-rds-for-mysql-instance-types.md)变配限制：无法直接变配，需先升级配置至线上售卖规格，才能进行后续变更操作。
如果实例使用的是SSD云盘，需先将存储类型升级为ESSD云盘，否则变配时会报Commodity.InvalidComponent错误。具体操作请参见[变更存储类型](../support/how-do-i-change-the-storage-type-from-standa
