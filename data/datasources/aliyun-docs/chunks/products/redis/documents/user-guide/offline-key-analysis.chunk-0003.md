## 常见问题
Q：分析出大量已过期的Key怎么办？
A：当业务中数据设置了过期时间，且实例在同一时间（时间段）过期大量Key时，可能会出现该情况。此时，除了依靠实例自动清除过期数据外，您可以通过控制台上的清除数据功能快速清除过期Key，更多信息请参见[如何清除过期](../support/how-do-i-clear-expired-keys.md)[Key](../support/how-do-i-clear-expired-keys.md)。
Q：若使用RAM账号，操作时提示权限不足怎么办？
A：请对RAM账号进行授权并重试，更多信息请参见[常见自定义权限策略场景及示例](../custom-permission-policy-reference.md)。
Q：在同一个实例中，为什么执行离线分析任务的速度时快时慢？
A：离线分析任务是异步任务，分析速度还与CloudDBA的当前总任务数有关，当总任务数较多时，该离线分析任务需排队等待，分析任务的耗时就会变长。
Q：如何处理报错decode rdbfile error: rdb: unknown object type 116 for key？
A：该报错表示实例中存在非标准的Bloom结构，暂不支持分析。
Q：如何处理报错decode rdbfile error: rdb: invalid file format？
A：该报错表示所选的备份文件无效，请检查实例是否在该备份时间点后进行了变配；或者实例是否开启了透明数据加密TDE（该功能无法分析已加密的信息）。
Q：如何处理报错decode rdbfile error: rdb: unknown module type？
A：该报错表示备份文件中存在Tair自研数据结构，暂不支持分析。
Q：如何处理新建备份, 并使用最新的备份进行分析后报错XXX backup failed？
A：该实例当前存在正在执行的BGSAVE或BGREWRITEAOF命令，导致创建用于缓存分析任务的备份时出现了失败的情况。建议您选择业务低峰期新建备份，并使用最新的备份进行分析或者选择历史备份文件进行分析。
Q：为什么缓存分析结果展示的Key内存占有会比实际使用的内存小？
A：因为缓存分析结果实际只是解析了Key和对应value在RDB中序列化后占用的大小，这个只占用了used_memory中的一部分，used_memory还包含了如下部分：
Key和value所对应的struct和指针大小。在jemalloc分配后，字节对齐部分所占用的大小也没计算在used_memory中，例如在2.5亿Key的数量下，struct、指针、字节对齐这三部分的大小加起来约有2~3 GB。
客户端输出缓冲区、查询缓冲区、AOF重写缓冲区和主从复制的backlog，这些也没计算到缓存分析中。
Q：Red
