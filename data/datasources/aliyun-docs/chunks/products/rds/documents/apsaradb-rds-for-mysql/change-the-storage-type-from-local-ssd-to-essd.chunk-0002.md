| 对比项 | 高性能本地盘 | 高性能云盘 | ESSD 云盘 |
| --- | --- | --- | --- |
| I/O 性能 | ★★★★★ IO 延迟低，性能好： IOPS：由实例规格决定。 IO 延迟：10~50 微秒 | ★★★★★★ 提供了 [Buffer Pool Extension（BPE）功能](buffer-pool-extension-bpe.md) 、 [IO](i-o-performance-burst.md) [性能突发功能](i-o-performance-burst.md) 和 [数据归档功能](rds-mysql-data-archiving-function.md) 三种功能。IO 性能如下： IOPS：由磁盘规格及实例规格共同决定。 IO 延迟：100~200 微秒 | ★★★★★ 相对 SSD 云盘有大幅提升： IOPS：由磁盘规格及实例规格共同决定。 IO 延迟：100~200 微秒 |
| 规格配置灵活性 | ★★★★ 可选配置较多，磁盘空间可单独调整。仅部分高性能本地盘实例的磁盘空间大小与实例规格绑定，无法单独调整。 | ★★★★★ 可选配置较多，支持扩容或缩容磁盘空间。 说明 仅 MySQL 部分满足条件的实例支持缩容，具体请参见 [实例变更项概览](configuration-items-for-an-apsaradb-rds-for-mysql-instance.md) 和 [变更配置](../apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) 。 | ★★★★★ 可选配置较多，支持扩容或缩容磁盘空间。 说明 仅 MySQL 部分满足条件的实例支持缩容，具体请参见 [实例变更项概览](configuration-items-for-an-apsaradb-rds-for-mysql-instance.md) 和 [变更配置](../apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 备份方法 | Xtrabackup 物理备份 | ESSD 云盘快照备份 | ESSD 云盘快照备份 |
| 备份、只读实例创建、实例克隆操作速度 | ★★★ 与磁盘大小相关，耗时为小时级。 | ★★★★★ 耗时为秒级。 | ★★★★★ 耗时为秒级。 |
| 扩容时长 | ★★★★ 需要拷贝数据，可能需要几个小时。 | ★★★★★ 在线升级，秒级扩容。 | ★★★★★ 在线升级，秒级扩容。 |
| 扩容影响 |
