## 产品优势
持久内存型基于持久内存技术，提供大容量、兼容Redis的内存数据库产品，数据持久化不依赖传统磁盘，保证每个操作持久化的同时提供近乎Redis开源版的吞吐和延时，极大提升业务数据可靠性。适用于兼容Redis、大容量、服务抖动稳定可控，数据持久化要求高的热温数据存储场景。

| 优势项 | 说明 |
| --- | --- |
| 超高性价比 | 相同容量下对比阿里云 Redis 开源版 ，价格降低 30%左右。 性能可达到 Redis 的 90%。 |
| 数据结构模块集成 | 支持 [exString](../developer-reference/tairsting-command.md) （包含 [Redis String](../developer-reference/cas-cad-command.md) [命令增强](../developer-reference/cas-cad-command.md) ）、 [exHash](../developer-reference/the-tairhash-command.md) 和 [Cpc](../developer-reference/taircpc-command.md) 。 |
| 大规格优化 | 解决大规格下执行 AOF 重写调用 fork 引起的延时抖动、服务数据加载慢等问题，无需在性能与持久化中取舍。 |
| 更高可靠性 | 提供命令级持久化保障，每个写操作请求将在主节点持久化成功之后返回。 |
| 高兼容性 | 完全适配现有阿里云 Redis 数据库体系，具备高可用、弹性扩容缩容、日志、智能诊断与灵活的备份还原服务能力。 兼容 Redis 6.0 版本及以下版本接口和数据结构。 |
