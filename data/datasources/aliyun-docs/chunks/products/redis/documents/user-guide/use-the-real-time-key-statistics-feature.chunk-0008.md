## 相关文档
若业务中存在超过10万个元素的排行榜（采用Zset数据结构），建议考虑使用Tair自研的数据结构[exZset](../developer-reference/tairzset-command.md)。
结合TairJedis客户端，您可以轻松实现[分布式架构排行榜](../use-cases/implementation-of-distributed-architecture-ranking-list-based-on-tairzset.md)。即您只需关注和操作一个Key，而Tair会自动将数据以及计算任务分布至多个子Key中，从而有效避免产生超大Key和热Key的问题。
排查Redis CPU使用率高的原因，请参见[排查实例](troubleshoot-high-cpu-utilization-on-an-apsaradb-for-redis-instance.md)[CPU](troubleshoot-high-cpu-utilization-on-an-apsaradb-for-redis-instance.md)[使用率高的问题](troubleshoot-high-cpu-utilization-on-an-apsaradb-for-redis-instance.md)。
排查Redis内存使用率高的原因，请参见[排查实例内存使用率高的问题](troubleshoot-the-high-memory-usage-of-an-apsaradb-for-redis-instance.md)。
该文章对您有帮助吗？
反馈
