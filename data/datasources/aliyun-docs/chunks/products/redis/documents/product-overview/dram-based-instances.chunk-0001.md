| 类别 | 说明 |
| --- | --- |
| 兼容性 | 100%兼容原生 Redis，无需修改业务代码，提供 兼容 Redis 7.0 、 兼容 Redis 6.0 与 兼容 Redis 5.0 版本。 |
| 性能 | 采用多线程模型，性能约为同规格 Redis 开源版 的 3 倍，能够突破热点数据高频读写受到的性能限制。 相比原生 Redis，高 QPS 场景下响应时间更低，性能表现更佳。 在大并发场景下运行稳定，可以极大地缓解突发大量请求导致的连接问题，从容应对业务高峰。 全量同步和增量同步在 IO 线程中进行，提高同步速度。 |
| 同步模式 | 额外支持 [半同步模式](../user-guide/modify-the-synchronization-mode-of-a-persistent-memory-optimized-instance.md) ，即客户端发起的更新在主节点执行完成后，主节点会将日志复制到备节点，待备节点确认接收后才返回信息给客户端，保证高可用切换后数据不丢失。 |
| 部署架构 | 支持标准、集群和读写分离部署架构。 |
| 数据结构模块集成 | 集成多个自研的 Tair 模块， 包括 [exString](../developer-reference/tairsting-command.md) （包含 [Redis String](../developer-reference/cas-cad-command.md) [命令增强](../developer-reference/cas-cad-command.md) ）、 [exHash](../developer-reference/the-tairhash-command.md) 、 [exZset](../developer-reference/tairzset-command.md) 、 [GIS](../developer-reference/tairgis-command.md) 、 [Bloom](../developer-reference/tairbloom-command.md) 、 [Doc](../developer-reference/tairdoc-command.md) 、 [TS](../developer-reference/the-tickets-command.md) 、 [Cpc](../developer-reference/taircpc-command.md) 、 [Roaring](../developer-reference/tairroaring-command.md) 、 [Search](../developer-reference/tairsearch.md) 和 [Vector](../developer
