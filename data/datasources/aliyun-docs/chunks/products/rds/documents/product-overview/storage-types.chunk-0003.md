各存储类型之间的性能对比（单盘容量、最大IOPS、最大吞吐量等），请参见[块存储性能](../../../ecs/documents/user-guide/block-storage-performance.md)。
说明
这几种存储类型的可靠性、持久性和读写性能均会满足产品SLA承诺。
高性能本地盘：所属的RDS实例都是一主一备（[高可用系列](../apsaradb-rds-for-mysql/rds-high-availability-edition.md)）架构，主节点故障时，主备节点秒级完成切换。
云盘（SSD云盘、ESSD云盘、高性能云盘）：分布式云盘，通过多副本冗余确保数据可靠性。如果所属RDS实例为高可用系列、集群系列，则具备秒级自动切换能力。
