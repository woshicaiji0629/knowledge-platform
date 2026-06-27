mmand.md) | EXZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count] | 返回存储在 Key（TairZset 数据结构）中，分数大于等于 min 且小于等于 max 值的所有元素。和 TairZset 中元素默认排序相反，该命令返回元素按照分数从高到低排列，分数相同的元素按照逆字典序排列。 说明 除排序方式相反外，本命令和 [EXZRANGEBYSCORE](tairzset-command.md) 用法相似，注意本命令中 max 在前。 |
| [EXZRANGEBYLEX](tairzset-command.md) | EXZRANGEBYLEX key min max [LIMIT offset count] | 为确保元素按照字典序排列，当 Key 中所有元素分数相同时，则该命令返回存储在 Key 中介于 min 和 max 值之间的元素。 |
| [EXZREVRANGEBYLEX](tairzset-command.md) | EXZREVRANGEBYLEX key max min [LIMIT offset count] | 为确保元素按照字典序排列，当 Key 中所有元素分数相同时，则该命令返回存储在 Key 中介于 max 和 min 之间的元素。 说明 除排序方式相反外，本命令和 [EXZRANGEBYLEX](tairzset-command.md) 用法相同，注意本命令中 max 在前。 |
| [EXZREM](tairzset-command.md) | EXZREM key member [member ...] | 移除存储 Key 中的指定成员，如果指定成员不存在，则忽略。 |
| [EXZREMRANGEBYSCORE](tairzset-command.md) | EXZREMRANGEBYSCORE key min max | 移除存储在 Key（TairZset 数据结构）中，分数大于等于 min 且小于等于 max 值的元素。 |
| [EXZREMRANGEBYRANK](tairzset-command.md) | EXZREMRANGEBYRANK key start stop | 移除存储在 Key（TairZset 数据结构）中，级别介于 start 和 stop 之间的元素。 |
| [EXZREMRANGEBYLEX](tairzset-command.md) | EXZREMRANGEBYLEX key min max | 为确保元素按照字典序排列，当 Key 中所有元素分数相同时，则该命令移除存储在 Key 中介于 max 和 min 之间的元素。 说明 若使用相同的 min 和 max 参数值执行该命令和 [
