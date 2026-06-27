### AOF
AOF持久化是指以日志的形式记录所有的写入类操作（例如SET）。当AOF文件过大时，实例会自动执行AOF Rewrite，重组AOF文件，降低其占用的存储空间。
云数据库 Tair（兼容 Redis）的AOF持久化策略为AOF_FSYNC_EVERYSEC，每秒异步将AOF缓冲区中的命令写入磁盘。此策略能相对降低AOF开启对实例的性能影响。
