## 注意事项
仅支持高性能本地盘到高性能云盘或ESSD云盘的单向变更，不支持逆向操作。
高性能本地盘与ESSD云盘支持的实例规格存在差异，部分规格的高性能本地盘实例变更为ESSD云盘时，需要变更实例规格。实例规格列表请参见[RDS MySQL](primary-apsaradb-rds-for-mysql-instance-types.md)[标准版（原](primary-apsaradb-rds-for-mysql-instance-types.md)[X86）主实例规格列表](primary-apsaradb-rds-for-mysql-instance-types.md)。
变更存储类型受多种因素影响，无法保证100%升级成功。影响因素请参见[RDS MySQL](../support/which-factors-affect-the-time-that-is-required-to-change-the-specifications-of-my-apsaradb-rds-for-mysql-instance.md)[实例变配时长受哪些因素影响？](../support/which-factors-affect-the-time-that-is-required-to-change-the-specifications-of-my-apsaradb-rds-for-mysql-instance.md)。
变更存储类型以增量数据同步的方式实现，若该过程中业务仍在写入大量数据，可能出现目标端数据无法追平源端的情况，导致存储类型变更无法结束。建议在升级期间降低数据写入频率，快速完成存储类型的变更。
变更存储类型前请预留10%以上存储空间，防止磁盘空间写满导致实例锁定。实例锁定的解决方法，请参见[RDS MySQL](../support/what-do-i-do-if-an-apsaradb-rds-for-mysql-instance-is-in-the-locked-state-because-its-storage-capacity-is-exhausted-by-data-files.md)[数据文件占满磁盘空间导致出现“锁定中”状态](../support/what-do-i-do-if-an-apsaradb-rds-for-mysql-instance-is-in-the-locked-state-because-its-storage-capacity-is-exhausted-by-data-files.md)。
