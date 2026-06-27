| 类别 | 名称 | 阈值 | 说明 |
| --- | --- | --- | --- |
| 内存驱逐相关 | EvictionDel | 30ms | 在逐出周期中删除 Key 的耗时。 |
| EvictionLazyFree | 30ms | 在逐出周期中，等待后台线程释放内存的耗时。 |  |
| EvictionCycle | 30ms | 一次逐出周期的耗时，包含逐出数据的选择、删除操作，及后台线程等待的时间。 |  |
| 内存碎片整理 | ActiveDefragCycle | 100ms | 内存碎片整理过程的耗时。 |
| Rehash | Rehash | 100ms | 发生 Rehash 过程的耗时。 |
| 数据结构升级 | ZipListConvertHash | 30ms | Hash 编码类型转换耗时（Ziplist 转换为 Dict）。 |
| IntsetConvertSet | 30ms | Set 编码类型转换耗时（Intset 转换为 Set）。 |  |
| ZipListConvertZset | 30ms | Zset 编码类型转换耗时（Ziplist 转换为 Skiplist）。 |  |
| AOF 相关 | AofWriteAlone | 30ms | 一次正常写入 AOF 文件的耗时。 |
| AofWrite | 30ms | 写入 AOF（AppendOnly File）的耗时。每次成功写入 AOF 文件后，会记录 AofWrite 事件以及 AofWriteAlone、AofWriteActiveChild、AofWritePendingFsync 三者中的一种事件。 |  |
| AofFstat | 30ms | Fstat 的耗时。 |  |
| AofRename | 30ms | Rename 的耗时统计。 |  |
| AofReWriteDiffWrite | 30ms | 子进程重写完 AOF 后，主进程把 buffer 中的增量 AOF 写入的耗时。 |  |
| AofWriteActiveChild | 30ms | 写入 AOF 文件的耗时，写入过程中存在其他子进程也在向磁盘写数据等情况。 |  |
| AofWritePendingFsync | 30ms | 写入 AOF 文件的耗时，写入过程中存在后台进程正在执行 fsync。 |  |
| RDB 相关 | RdbUnlinkTempFile | 50ms | bgsave 子进程中断后删除临时 RDB 文件的耗时。 |
| 其他 | Commands | 30ms | 常规命令（未被标为@fast）的耗时。 |
| FastCommand | 30ms | 被标为@fast 的命令（命令的时间复杂度为 O(
