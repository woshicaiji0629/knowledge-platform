| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [EXZADD](tairzset-command.md) | EXZADD key [NX|XX] [CH] [INCR] score member [score member ...] | 将指定的分数与成员信息存储到 TairZset 结构的 Key 中，支持指定多个分数与成员。 说明 如需实现多维度的排序，各维度的分数之间使用井号（#）分隔，例如 111#222#121 ，且要求该 Key 中所有成员的分数格式必须相同。 |
| [EXZINCRBY](tairzset-command.md) | EXZINCRBY key increment member | 为 Key（TairZset 数据结构）中的成员增加分数， increment 为要增加的分数值。 |
| [EXZSCORE](tairzset-command.md) | EXZSCORE key member | 返回存储在 Key（TairZset 数据结构）中成员的分数，如果 Key 或 Key 中的成员不存在，系统会返回 nil。 |
| [EXZRANGE](tairzset-command.md) | EXZRANGE key min max [WITHSCORES] | 返回存储在 Key（TairZset 数据结构）中指定范围的元素。 |
| [EXZREVRANGE](tairzset-command.md) | EXZREVRANGE key min max [WITHSCORES] | 返回存储在 Key（TairZset 数据结构）中指定范围内的元素，元素按分值从高到低的顺序排列，按字典序降序排列分数相同的元素。 说明 除排序方式相反外，本命令和 [EXZRANGE](tairzset-command.md) 用法相似。 |
| [EXZRANGEBYSCORE](tairzset-command.md) | EXZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count] | 返回存储在 Key（TairZset 数据结构）中，分数大于等于 min 且小于等于 max 值的所有元素，返回元素按分数从低到高排列，分数相同的元素按照字典顺序返回。 |
| [EXZREVRANGEBYSCORE](tairzset-command.md) | EXZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count] | 返回存储在 Key（TairZset 数据结构）中，分数大于等于 min 且小于等于 max 值的所有元素。和 TairZset 中元素默认排序相反，该命令返回元
