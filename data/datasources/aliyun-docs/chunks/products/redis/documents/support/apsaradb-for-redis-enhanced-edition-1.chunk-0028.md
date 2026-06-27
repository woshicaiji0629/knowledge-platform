缺陷修复 | 修复由于使用共享对象造成 QPS 统计错误的问题，当开启实时统计热 Key 功能后将不在使用共享对象。 |  |  |  |
| 5.0.49 | MEDIUM | 2024-04-24 | 功能优化 | INFO STATS 命令增加返回客户端输入、输出缓冲区超限断连的统计： client_query_buffer_limit_disconnections client_output_buffer_limit_disconnections 新增实时大 Key 统计阈值，默认为 2000。例如 String 类型的字符长度超过 2000 即判定为大 key；List、Set、Hash 等类型的元素个数超过 2000 个即判定为大 Key 等。 |
| 缺陷修复 | 修复 exZset 中 EXZRANKBYSCORE 和 EXZREVRANKBYSCORE 命令崩溃的问题，增加 Score 维度的判断。 |  |  |  |
| 5.0.48 | LOW | 2024-01-09 | 功能优化 | 优化主动过期的效率。 INFO CLIENTS 命令中增加 pubsub_clients 监控项。 TairSearch 支持 EXPAINSCORE 命令。 增强 TairSearch 的稳定性。 |
| 缺陷修复 | 修复 TairSearch 分词器内存膨胀的问题。 |  |  |  |
| 5.0.47 | LOW | 2023-10-18 | 功能优化 | 优化极端场景下 CPU 使用率达到 100%的问题。 |
| 5.0.46 | LOW | 2023-10-10 | 功能优化 | 优化集群架构下 Lua 脚本对连接类型（TCP or TLS）的判断。 |
| 5.0.45 | MEDIUM | 2023-09-20 | 功能优化 | 优化 CLUSTER SLOTS 、 CLUSTER NODES 命令的性能。 |
| 缺陷修复 | 修复 TairHash 概率性崩溃的问题。 |  |  |  |
| 5.0.44 | MEDIUM | 2023-08-24 | 功能优化 | 支持将流量拆分为数据流量和复制流量。 |
| 缺陷修复 | 修复 CVE-2022-24834 安全漏洞。 |  |  |  |
| 5.0.41 | LOW | 2023-07-21 | 功能优化 | 增强 TairSearch 的稳定性。 |
| 5.0.35 | LOW | 2023-06-12 | 新特性 | TairSearch 支持 Okapi BM25 相似度算法。 |
| 5.0.34 | LOW | 2023-05-22 | 功能优化 | 提升无感扩缩容的稳定性。 |
| 5.0.33 | LOW | 2023-04-23 | 新特性 | T
