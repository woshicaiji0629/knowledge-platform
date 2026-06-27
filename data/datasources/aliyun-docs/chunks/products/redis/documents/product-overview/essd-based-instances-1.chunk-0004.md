## ESSD型与SSD型
ESSD型支持自定义存储容量，支持云盘快照式备份，数据备份与迁移复制速度更快，但仅支持标准架构。
SSD型支持标准架构与集群架构，在同规格情况下性价比更高。

| 对比性 | ESSD 型 | SSD 型 |
| --- | --- | --- |
| 存储介质 | [ESSD](../../../ecs/documents/user-guide/essds.md) [云盘](../../../ecs/documents/user-guide/essds.md) ，支持 PL1-PL3，PL3 的性能优于 PL2 与 PL1。 | [SSD](../../../ecs/documents/user-guide/local-disks.md) [本地盘](../../../ecs/documents/user-guide/local-disks.md) 。 |
| 实例架构 | 标准架构。 | 标准架构、集群架构。 |
| 存储容量 | 支持以 10 GB 为粒度进行自定义。 | 固定规格。 |
| 备份恢复 | 云盘快照式备份，备份、恢复速度更快。 | 数据物理备份，备份、恢复速度取决于数据量。 |
