个主节点、3 个或以上的备节点，您至少需要在主可用区部署 1 个主节点、1 个备节点，然后您可以自定义将剩余的备节点部署在主可用区或备可用区。 |
| 部署模式 | 云原生 ：基于新一代管控架构，扩容、弹性能力强，规格配置更加灵活。 经典 ：基于传统管控架构。 更多信息请参见 [云原生实例和经典实例对比](comparison-between-tair-instances-that-cloud-native-and-classic.md) 。 |
| 系列 | 标准版 ：CPU 为 X86 架构，支持单节点、主备、集群、读写分离四种架构，扩展性强。 倚天版 ：CPU 为 ARM（倚天）架构，仅支持主备架构，具有价格优势，更多信息请参见 [倚天版实例](cost-efficient-instances.md) 。 |
| 存储介质 | Tair 实例支持 3 种存储介质，其特点和应用场景如下： Redis 开源版 ：以内存为存储介质，提供高性能、低时延的服务。 应用场景：开源 Redis 使用场景。 [内存](dram-based-instances.md) ：以内存为存储介质，额外采用多线程模型，性能约为同规格 Redis 开源版 实例的 3 倍。支持半同步、数据按时间点恢复（PITR）、全球多活等功能，同时提供多种增强型数据结构模块简化开发。 应用场景：超高性能场景、全球多活等。 [持久内存](persistent-memory-optimized-instances-1.md) ：数据在持久内存中存取，提供命令级强持久化能力。 应用场景：适用于对性能要求较高，同时对数据一致性有要求的场景。 [磁盘](essd-based-instances-1.md) ：数据存储在 ESSD、SSD 磁盘中，大容量、提供命令级强持久化能力，性能约为 Redis 开源版 的 60%，但价格最低为 Redis 开源版 的 15%。 应用场景：对性能要求不高，但是对成本有控制要求的场景。 |
| 版本兼容性 | 兼容 Redis 的版本，支持 Redis 7.0、Redis 6.0、Redis 5.0、Redis 4.0。 |
| 逐出策略 | 与 Redis 的逐出策略保持一致，详情请参见 [Key eviction](https://valkey.io/topics/lru-cache/) 。 |
| DB | Database， Tair 支持 256 个 DB（0 ~ 255），默认写入到第 0 个 DB 中，无法修改总 DB 数。 |
