## EXZREVRANGEBYSCORE

| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count] |
| 时间复杂度 | O(log(N)+M) ，其中，N 表示 TairZset 中元素的数量，M 表示返回的元素的数量。 说明 当 M 为常量时（比如使用 LIMIT 选项指定总是返回前 10 个元素时），可将该公式看作 O(log(N))。 |
| 命令描述 | 返回存储在 Key（TairZset 数据结构）中，分数大于等于 min 且小于等于 max 值的所有元素。和 TairZset 中元素默认排序相反，该命令返回元素按照分数从高到低排列，分数相同的元素按照逆字典序排列。 说明 除排序方式相反以外，本命令和 [EXZRANGEBYSCORE](tairzset-command.md) 用法相似，注意本命令中 max 在前。 |
| 选项 | min 、 max ：分别表示最小分数和最大分数，如 Key 中的元素采用了多维度的分数，各维度的分数之间使用井号（#）分隔。 说明 在不确定 Key 中元素的最高分和最低分的情况下，如果想要查询 Key 中分数大于等于或小于等于某一特定值的元素，请将 min 和 max 分别设置为负无穷大（ -inf ）和正无穷大（ +inf ）。 默认数据范围为闭区间，如需指定开区间，则在分数范围前添加半角圆括号，例如 (1 5 表示返回分数大于 1 且小于等于 5 的元素。 WITHSCORES ：返回值中包含元素的分数。 LIMIT offset count ：指定返回结果的数量及区间，如果 count 为负数，则返回从 offset 开始的所有元素。 说明 如果 offset 较大，则需要遍历整个 Key 以定位到 offset 元素，然后才能返回元素，即会增加时间复杂度。 |
| 返回值 | 返回指定分数范围内的元素列表，如果使用了 WITHSCORES 选项，则返回结果中包含元素的分数。 |
| 命令示例 | 命令示例： EXZREVRANGEBYSCORE testkey 6#6#6 0#0#0 WITHSCORES 返回示例： 1) "a" 2) "3#2#4" 3) "b" 4) "1#0#2" |
