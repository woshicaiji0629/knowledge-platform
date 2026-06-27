## 影响

| [实例存储类型](../product-overview/storage-types.md) | 变配项目 | 影响 |
| --- | --- | --- |
| 高性能本地盘实例 | 规格、系列、存储空间 | 本地无资源可用的情况下执行变更规格或系列会引发自动数据迁移，迁移完成后根据您选择的切换时间进行切换（期间保持增量同步）。 重要 变配会出现实例切换，通常切换影响时间约 15 秒（但若客户端配置不合理或驱动版本太低可能导致影响时间较久），请在业务低峰期进行变配，并确保您的应用有 [自动重连机制](change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md) 。 实例切换期间，与数据库、账号、网络等相关的大部分操作都无法执行，详情请参见 [实例切换的影响](untitled-document-1701914031929.md) 。 |
| 云盘实例 | 规格或系列 | 变配耗时为分钟级别，不受数据量大小的影响。 重要 变配会出现实例切换，通常切换影响时间约 15 秒（但若客户端配置不合理或驱动版本太低可能导致影响时间较久），请在业务低峰期进行变配，并确保您的应用有 [自动重连机制](change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md) 。 实例切换期间，与数据库、账号、网络等相关的大部分操作都无法执行，详情请参见 [实例切换的影响](untitled-document-1701914031929.md) 。 |
| 存储空间 | 扩容时：SSD 云盘扩容会有闪断，ESSD 云盘和高性能云盘扩容没有闪断。 缩容时：云盘缩容会有闪断影响，详情请参见 [云盘存储空间缩容（SSD](../support/reduce-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-that-uses-essds.md) [云盘不支持缩容）](../support/reduce-the-storage-capacity-of-an-apsaradb-rds-for-mysql-instance-that-uses-essds.md) 。 说明 当云盘存在快照任务时，云盘扩容和云盘性能等级变更会等待快照任务执行结束后才执行。 |  |

说明
变配操作无需您手动重启实例，且变配操作不会导致已存储数据的丢失。
变配操作不会导致实例ID和连接地址改变，但如果实例发生了跨机迁移，连接地址对应的IP会发生变化，建议业务侧使用RDS连接地址访问数据库。
