| 类别 | 对比项 | Tair（企业版） | Redis 开源版 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [内存型](dram-based-instances.md) | [持久内存型](persistent-memory-optimized-instances-1.md) | [磁盘型](essd-based-instances-1.md) （ESSD） | [磁盘型](essd-based-instances-1.md) （SSD） | 2.8、4.0 及 5.0 版本 | 6.0、7.0 版本 | Redis 倚天版 |  |  |
| 基本性能 | 性能基准（以 Redis 开源版 为基准） | 300% | 90% | 读：40% | 读：60% | 一致 | 120% | 120% |
| 写：30% | 写：40% |  |  |  |  |  |  |  |
| 单个数据节点的最大连接数 | 30,000 | 10,000 | 10,000 | 40,000 | 10,000 | 10,000 | 10,000 |  |
| 单 Key 服务能力（QPS 参考值）① | 450,000 | 130,000 | 30,000~60,000 | 50,000~60,000 | 140,000 | 160,000 | 160,000 |  |
| 最大带宽（MB/s） | 96~2,048 | 96~2,048 | 187.5~1,000 | 187.5~2,048 | 10~2048 | 48~2,048 | 96~2,048 |  |
| 规格特性 | IO 与 Worker 模型 | 多 IO（Real Multi-IO）③ | 单线程 | 多 IO+多 Worker（Real Multi-IO） | 多 IO+多 Worker（Real Multi-IO） | 单线程 | 单线程 | 单线程 |
| 数据结构 | 基础数据结构及命令支持 | 不同形态支持的命令有所不同，详情请参见 [Tair（企业版）命令支持与限制](../developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md) 。 | 部分命令不支持，详情请参见 [Redis](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md) [开源版命令支持](../developer-reference/commands-supported-b
