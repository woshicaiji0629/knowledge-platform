## 常见问题
Q：云盘版实例如何变更为高性能本地盘实例？
A：请参见[云盘如何变更为高性能本地盘](../support/how-do-i-change-the-storage-type-from-standard-ssd-to-premium-local-ssd.md)。
Q：仅扩容存储空间，需要迁移数据到新实例吗？
A：
云盘实例：不需要。
高性能本地盘实例：需要检查实例所在主机上是否有足够存储空间用于扩容。
如果有足够存储空间，则直接扩容，不需要迁移数据。
如果没有足够存储空间，则需要迁移数据到拥有足够存储空间的主机上。
Q：如何缩容存储空间？
A：
本地盘实例，建议使用大版本升级功能，将实例升级到云盘高版本，在升级的同时支持存储空间缩容。更多信息，请参见[升级数据库大版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md)。
云盘实例，请参见[ESSD](reduce-the-storage-capacity-of-an-apsaradb-rds-for-postgresql-instance-that-uses-essds.md)[云盘缩容](reduce-the-storage-capacity-of-an-apsaradb-rds-for-postgresql-instance-that-uses-essds.md)。
Q：CPU、内存、磁盘同时升配，会闪断多久？
A：无论是单独升配CPU、内存、磁盘中的一个，还是三个同时升配，闪断的时间都是一样的，一般是分钟级的。切换过程中，可能会出现业务闪断或实例重启，而且与数据库、账号、网络等相关的大部分操作都无法执行，请选择在可维护时间段内执行变配操作。各变更项的业务影响，请参见[变更项的业务影响](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)。
Q：单独变更只读实例配置是否会对主实例产生影响？
A：单独变更只读实例配置通常不会对主实例产生影响。然而，仍需与主实例保持一定的关联，详情请参见本文[注意事项](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)。
