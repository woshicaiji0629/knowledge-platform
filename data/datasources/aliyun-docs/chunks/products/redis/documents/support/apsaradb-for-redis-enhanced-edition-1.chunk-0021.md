nable 参数，控制 TairTS 中 Skey 的过期行为，默认为 yes，表示当 Skey 中所有数据点都过期时会删除 Skey。 增强稳定性。 |
| 24.6.1.1 | LOW | 2024-07-09 | 功能优化 | 增强 TairSearch 的稳定性。 |
| 24.6.1.0 | LOW | 2024-07-05 | 新特性 | TairDoc 支持 JSON.MERGE 命令。 |
| 功能优化 | 增强 TairVector 的稳定性。 |  |  |  |
| 24.6.0.0 | LOW | 2024-07-02 | 功能优化 | 优化在突发大流量场景下主备节点同步的稳定性。 |
| 24.5.1.0 | MEDIUM | 2024-06-06 | 功能优化 | 取消 COMMAND GETKEYS 命令的使用限制。 优化 TairVector 中 FLAT 向量索引的内存使用，减少小索引的内存浪费。 优化 TairVector 中 Within、多条件 Condition 等倒排索引，并新增 TVS.KNNSEARCHFIELD 、 TVS.MINDEXKNNSEARCHFIELD 命令。 在 TairSearch 的 TFT.MSEARCH 命令根据索引字段排序时，返回的 aux_info 中新增了 field_type 字段。 |
| 缺陷修复 | 修复 TairVector 的写入性能问题，该问题由 24.3.2.2 引入（从 24.3.2.2 版本起，TairVector 的写入性能开始回退），建议升级到该版本及以上。 修复 TairSearch 的数个问题，优化稳定性。 |  |  |  |
| 24.5.0.0 | MEDIUM | 2024-05-22 | 功能优化 | 优化主备模式下跨 Slot 命令的同步能力。 优化了大实例的后台 BGREWRITE 的速度。 INFO 命令中返回了 Per command 的 CPU、QPS、流量信息。 |
| 缺陷修复 | 增强稳定性。 |  |  |  |
| 24.4.1.0 | MEDIUM | 2024-04-22 | 功能优化 | 支持 DTS 任务重启后同步点位任意回退，若实例需要长期配置 DTS 任务，建议升级到该版本。 |
| 24.4.0.0 | MEDIUM | 2024-04-16 | 功能优化 | 优化基础数据结构的内存占用，在少量复杂结构元素时降低内存占用。 优化 TairVector 全文检索、标量检索组合的检索性能。 与 TairVector 单 Index 检索一样，多 Index 检索支持返回非向量字段。 |
| 缺陷修复 | 增强稳定性。 |  |  |  |
| 24.3.2.2 | MEDIUM | 2024-03-21 | 功能优
