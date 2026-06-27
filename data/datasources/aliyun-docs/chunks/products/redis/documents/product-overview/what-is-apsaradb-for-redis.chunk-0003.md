## 支持的实例类型与架构
支持Redis开源版、Tair（企业版）和Tair Serverless KV三种实例类型。

| 实例类型 | 简介 |
| --- | --- |
| Redis 开源版 | 兼容 Redis 的高性能内存数据库产品，支持标准（主备）、集群、读写分离等架构。 |
| [Tair（企业版）](overview-1.md) | Tair（企业版） 作为在 Redis 开源版 的基础上开发的强化版 Redis 服务，从访问延时、持久化需求、整体成本这三个核心维度考量，基于 DRAM（Dynamic Random Access Memory）、NVM（Non-Volatile Memory）和 ESSD 云盘等存储介质，推出了多种不同形态的产品，为您提供更强的性能、更多的数据结构和更灵活的存储方式，满足不同场景下的业务需求。 [内存型](dram-based-instances.md) ：采用多线程模型，集成阿里巴巴 Tair 的部分特性，支持多种 Tair 数据结构，对于部分特殊业务有很高的适用性。 [持久内存型](persistent-memory-optimized-instances-1.md) ：基于持久内存技术，为您提供大容量、兼容 Redis 的内存数据库产品。数据持久化不依赖传统磁盘，保证每个操作持久化的同时提供近乎 Redis 开源版 的吞吐和延时，极大提升业务数据可靠性。 [磁盘型](essd-based-instances-1.md) ：基于 ESSD 与 SSD 研发，兼容 Redis 核心数据结构与接口，成本最低为 Redis 开源版 的 15%，性能约为 Redis 开源版 的 60%。可提供大容量、低成本、强持久化的数据库服务，适用于兼容 Redis、需要大容量且较高访问性能的温冷数据存储场景。 |
| [Tair Serverless KV](tair-serverless-kv-redis-compatible-edition.md) | Tair Serverless KV 实例为分布式集群架构，具备自动扩缩容以及按实际用量计费的能力。高峰时自动扩容保障业务平稳，低峰时自动缩容节省成本。全程自动化无缝伸缩，业务无感知，能够显著降低运维的复杂度。 |

支持灵活的多种部署架构，能够满足不同的业务场景。
