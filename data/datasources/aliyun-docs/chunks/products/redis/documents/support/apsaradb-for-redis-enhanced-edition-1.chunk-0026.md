| 6.2.3.1 | LOW | 2023-01-04 | 功能优化 | 优化读写分离架构实例的 HA 稳定性。 |
| 6.2.3.0 | LOW | 2022-12-26 | 功能优化 | TairVector 支持集群代理模式，新增 FLOAT16 的向量数据类型，新增多向量索引查询。 |
| 6.2.2.0 | LOW | 2022-11-22 | 功能优化 | TairVector 支持 Jaccard 距离函数。 TairVector 支持统计每个索引的内存占用（ index_data_size 和 attribute_data_size ）。 |
| 6.2.1.5 | LOW | 2022-11-14 | 功能优化 | 修复 Blocking 接口问题，增强稳定性。 |
| 6.2.1.3 | LOW | 2022-10-28 | 功能优化 | 增强 TairVector 的稳定性。 |
| 6.2.1.2 | LOW | 2022-10-14 | 功能优化 | 增强 TairVector 的稳定性。 |
| 6.2.1.1 | LOW | 2022-10-13 | 首次发布 | 首发版本，兼容至 Redis 开源社区 6.2 版本以及 Tair 自研数据结构（暂未支持 TairSearch 结构）。 支持 KEYS、SMEMBERS、HGETALL、EXHGETALL 等命令的慢查询识别与隔离。 进一步优化性能，相比较 Redis 开源版 同规格实例，所有接口的性能均提升 2 倍以上，例如 PUB/SUB、Lua 命令等。 新增自研的向量检索 TairVector，支持 HNSW 和 FLAT 两种索引算法，提供高性能、实时，集存储、检索于一体的向量数据库服务。 |
