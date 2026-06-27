员的级别为 0。 说明 若指定的分数不存在，则返回该分数在 Key（TairZset 数据结构）中的预计排名；若指定的分数已存在，Tair 会默认将指定的分数排在已存在的分数之前。 |
| [EXZREVRANKBYSCORE](tairzset-command.md) | EXZREVRANKBYSCORE key score | 计算指定的分数在 Key（TairZset 数据结构）中按照分数从高到低排序的排名位置。级别（或索引）从 0 开始计数，即分数最高的成员的级别为 0。 说明 若指定的分数不存在，则返回该分数在 Key（TairZset 数据结构）中的预计排名；若指定的分数已存在，Tair 会默认将指定的分数排在已存在的分数之后。 |
| [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairZset 数据。 |
