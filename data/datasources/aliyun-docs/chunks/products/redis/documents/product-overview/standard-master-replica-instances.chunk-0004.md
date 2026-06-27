## 常见问题
Q：原有业务为Redis哨兵模式，迁移上云应该选什么架构？
A：推荐选择标准架构（高可用版）。创建实例后，您可以开启[Sentinel](../user-guide/use-the-sentinel-compatible-mode-to-connect-to-an-apsaradb-for-redis-instance.md)[兼容模式](../user-guide/use-the-sentinel-compatible-mode-to-connect-to-an-apsaradb-for-redis-instance.md)，然后可以像连接开源Redis Sentinel一样连接Tair（以及Redis开源版）实例。
Q：若当前实例为8 GB、标准架构，如何在不升级内存容量的情况下升级实例性能？
A：根据业务需求，分别推荐如下升级方案。
若现有实例的连接数或实例带宽不足，表示该实例可能无法满足超高的读流量。您可以考虑[开启读写分离](../user-guide/enable-read-write-splitting.md)（推荐），无需升级内存规格，即可快速提升实例读性能。
该方案无需修改业务代码（也无需修改连接地址），即开即用，也支持随时关闭。开启后，实例能够自动识别读、写请求并进行对应转发，满足高并发读写的业务场景。
若现有实例的CPU使用率总是过高，您可以考虑将实例升级为集群架构，通过增加数据分片解决单分片CPU使用率过高的问题。
但该方案将修改实例架构，集群架构与标准架构的大部分命令是兼容的，但仍然存在部分不兼容的命令（更多信息请参见[集群架构的命令限制](../developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)）。建议您评估后再进行升级。
以下为Redis开源版8 GB实例不同架构的性能对比：

| 架构 | 内存（GB） | CPU（核） | 带宽（MB/s） | 最大连接数 | QPS 参考值 |
| --- | --- | --- | --- | --- | --- |
| 标准架构（主备节点） | 8 | 2 | 96 | 20,000 | 100,000 |
| 标准架构（开启读写分离，1 个主节点、1 个只读节点） | 8 | 4（2 * 2） | 192（96 * 2） | 40,000（20,000 * 2） | 200,000 |
| 集群架构（2 分片） | 8（4 GB * 2 分片） | 4（2 * 2） | 192（96 * 2） | 40,000（20,000 * 2） | 200,000 |
