## 备份的影响

| 实例系列 | 备份的影响 |
| --- | --- |
| [高可用系列](rds-high-availability-edition.md) 、 [集群系列](rds-cluster-edition.md) 或 [三节点企业系列](../rds-enterprise-edition.md) [高可用系列](rds-high-availability-edition.md) 或 [集群系列](rds-cluster-edition.md) | 备份在备实例执行，不占用主实例 CPU，不影响主实例性能。 说明 少数情况下，备实例不可用时，备份会在主实例执行。 |
| [基础系列](rds-basic-edition.md) | 由于是单节点架构，备份时会影响实例性能。 |
