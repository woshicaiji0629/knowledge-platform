B 相关 | RdbUnlinkTempFile | 50ms | bgsave 子进程中断后删除临时 RDB 文件的耗时。 |
| 其他 | Commands | 30ms | 常规命令（未被标为@fast）的耗时。 |
| FastCommand | 30ms | 被标为@fast 的命令（命令的时间复杂度为 O(1)和 O(log N)）的耗时。 |  |
| EventLoop | 50ms | Main Loop 一次的耗时。 |  |
| Fork | 100ms | 调用 Fork 操作的耗时。 |  |
| Transaction | 50ms | 实际事务执行的耗时。 |  |
| PipeLine | 50ms | 多线程 Pipeline 耗时。 |  |
| ExpireCycle | 30ms | 一次清理过期 Key 周期的耗时。 |  |
| ExpireDel | 30ms | 在清理过期 Key 周期中，删除 Key 的耗时。 |  |
| SlotRdbsUnlinkTempFile | 30ms | Slot bgsave 子进程中断后删除临时 RDB 文件的耗时。 |  |
| LoadSlotRdb | 100ms | Slot 载入至（load）RDB 的耗时。 |  |
| SlotreplTargetcron | 50ms | Slot 子进程载入至（load）RDB 到一个临时的数据库（DB）后，再将其移动至目标数据库（DB）的耗时。 |  |
