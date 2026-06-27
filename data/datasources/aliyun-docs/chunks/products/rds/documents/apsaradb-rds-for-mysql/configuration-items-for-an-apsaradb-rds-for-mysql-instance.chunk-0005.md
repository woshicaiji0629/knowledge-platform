## 产品系列和产品类型

| 变更项 | 说明 | 变更方法 |
| --- | --- | --- |
| 产品系列 | 当前仅支持如下几种系列变更： MySQL 8.0 和 5.7 基础系列：变更为高可用系列。 MySQL 8.0 和 5.7 高可用系列：变更为集群系列。 说明 除上述场景外均不支持变更系列，如果需要进行其他系列变更，您可以执行如下步骤： [创建新实例](../create-an-apsaradb-rds-for-mysql-instance.md) ，选择目标系列。 [原实例数据迁移至新实例](migrate-data-between-apsaradb-rds-for-mysql-instances.md) [释放原实例](release-or-unsubscribe-from-an-instance.md) | [基础系列升级为高可用系列](upgrade-an-apsaradb-rds-for-mysql-instance-from-basic-edition-to-high-availability-edition.md) [高可用系列升级为集群系列](upgrade-an-apsaradb-rds-for-mysql-instance-from-rds-high-availability-edition-to-rds-cluster-edition.md) |
| [产品类型](../product-overview/product-types.md) | 高可用和集群系列：支持在标准版和倚天版间互相变更。 基础系列：仅支持倚天版变更为标准版。 说明 如果变更时无法选择目标类型，可能实例所在可用区暂无对应资源在售。 您可以先到实例售卖页查看目标类型的在售可用区情况，然后通过 [迁移可用区](migrate-an-apsaradb-rds-for-mysql-instance-across-zones-in-the-same-region.md) 功能，将当前实例迁移至目标可用区后，再进行变更配置。 如果需要变更产品类型，需要确保变更后内核小版本大于等于当前实例内核小版本，如果当前实例内核小版本高于变更后内核小版本，则不支持变更。 | [变更配置](change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md) |
