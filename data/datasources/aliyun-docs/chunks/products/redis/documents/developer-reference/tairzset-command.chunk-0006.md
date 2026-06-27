NGEBYLEX](tairzset-command.md) | EXZREMRANGEBYLEX key min max | 为确保元素按照字典序排列，当 Key 中所有元素分数相同时，则该命令移除存储在 Key 中介于 max 和 min 之间的元素。 说明 若使用相同的 min 和 max 参数值执行该命令和 [EXZRANGEBYLEX](tairzset-command.md) 命令，则该命令移除的元素与 EXZRANGEBYLEX 命令返回的元素相同。 |
| [EXZCARD](tairzset-command.md) | EXZCARD key | 返回存储在 Key（TairZset 数据结构）中的基数（即元素的个数）。 |
| [EXZRANK](tairzset-command.md) | EXZRANK key member | 返回存储在 Key（TairZset 数据结构）中的成员的级别，按照分数由低到高排列。 级别（或索引）从 0 开始计数，即分数最低的成员的级别为 0。 |
| [EXZREVRANK](tairzset-command.md) | EXZREVRANK key member | 返回存储在 Key（TairZset 数据结构）中的成员的级别。返回结果按照分数从高到低排列。 级别（或索引）从 0 开始计数，即分数最高的成员的级别为 0。 说明 除排序规则相反外，本命令和 [EXZRANK](tairzset-command.md) 用法类似。 |
| [EXZCOUNT](tairzset-command.md) | EXZCOUNT key min max | 返回存储在 Key（TairZset 数据结构）中，分数介于 min 和 max 之间的元素的个数。 |
| [EXZLEXCOUNT](tairzset-command.md) | EXZLEXCOUNT key min max | 为确保元素按照字典序排列，若 Key 中所有元素分数相同，则该命令返回存储在 Key，值介于 min 和 max 之间的元素的数量。 |
| [EXZRANKBYSCORE](tairzset-command.md) | EXZRANKBYSCORE key score | 计算指定的分数在 Key（TairZset 数据结构）中按照分数从低到高排序的排名位置。级别（或索引）从 0 开始计数，即分数最低的成员的级别为 0。 说明 若指定的分数不存在，则返回该分数在 Key（TairZset 数据结构）中的预计排名；若指定的分数已存在，Tair 会默认将指定的分数排在已存在的分数之前。 |
| [EXZREVRANKBYSCORE](tairzset-command.md) | EXZREVRANKBYSCORE key
