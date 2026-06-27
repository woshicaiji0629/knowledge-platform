索引，并提供先标量后向量的 KNN 检索特性。 |
| 缺陷修复 | 修复 GETDEL 命令异常情况下可能会导致实例崩溃的问题。 修复 XINFO STREAM 命令返回的结果中 last-entry 信息错误的问题。 修复 TairVector 的若干个问题，优化稳定性。 |  |  |  |
| 23.12.2.0 | LOW | 2023-12-26 | 新特性 | 支持半同步模式（ semisync ），您可以通过 #no_loose_tsync-repl-mode 参数进行控制。当前为 POC 版本，在生产环境中请谨慎开启。 |
| 23.12.1.2 | MEDIUM | 2023-12-21 | 功能优化 | 优化部分场景下的写性能，推荐升级。 TairSearch 支持 EXPAINSCORE 命令。 |
| 缺陷修复 | 合并 Redis 社区中有关 Lua 脚本的多个 CVE 修复。 修复 TairSearch、TairVector 的若干问题。 优化若干个稳定性问题，推荐升级。 |  |  |  |
| 23.8.1.2 | MEDIUM | 2023-08-22 | 功能优化 | 降低实例空闲时的 CPU 使用率，提升实例基础性能。 标准化 CloudDBA 中的 CPU 使用率指标。 主备复制流量将在 INFO STATS 中单独显示。 |
| 缺陷修复 | 修复 TairVector 的若干问题。 |  |  |  |
| 23.8.0.0 | MEDIUM | 2023-08-03 | 新特性 | 全面支持 TLS 加密连接。 TairVector 支持对 Index 中的 key 级别设置 TTL，支持对指定 Key 列表进行向量近邻查询，支持全文检索，可以实现向量检索与全文检索组合的混合检索。 |
| 功能优化 | 优化整体性能，增强稳定性。 TairZset 支持 EXZRANKBYSCORE 命令。 TairDoc 的接口行为与当前 TairDOC 官网文档对齐。 优化 GETBIT 、 BITPOS 、 BITCOUNT 等命令性能。 |  |  |  |
| 缺陷修复 | 修复 TairSearch 和 TairVector 的若干问题。 |  |  |  |
| 6.2.8.4 | MEDIUM | 2023-07-13 | 缺陷修复 | 修复 TairVector 中 Filter 低概率导致实例崩溃的问题。 |
| 6.2.8.3 | MEDIUM | 2023-07-12 | 功能优化 | 优化 TairVector 中 Filter 的限制，缩短执行时间。 |
| 6.2.8.2 | MEDIUM | 2023-07-04 | 功能优化 | 优化 TairVector HNSW 索引垃圾自动回收的稳定性。
