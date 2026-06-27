## 地域和可用区

| 变更项 | 说明 | 变更方法 |
| --- | --- | --- |
| 地域 | 实例的地域无法变更，您可以在目标地域创建实例后，通过数据传输服务 DTS 迁移数据，然后修改业务连接地址，确认业务正常后 [释放原实例](release-or-unsubscribe-from-an-instance.md) 。 | [迁移数据](migrate-data-between-apsaradb-rds-for-mysql-instances.md) |
| 可用区 | 实例可以迁移至同一地域内的其它可用区。迁移可用区后，实例的所有属性、配置和连接地址都不会改变。 MySQL 5.7 从高可用系列升级到三节点企业系列（原金融版）时，需要变更实例所在的可用区。 说明 集群系列实例不支持迁移可用区。 迁移可用区需要迁移数据，数据量越大，所需时间越长。 | [迁移可用区](migrate-an-apsaradb-rds-for-mysql-instance-across-zones-in-the-same-region.md) |
