## EXZREMRANGEBYSCORE

| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREMRANGEBYSCORE key min max |
| 时间复杂度 | O(log(N)+M)，其中，N 为 TairZset 中元素的数量，M 为待移除的元素的数量。 |
| 命令描述 | 移除存储在 Key（TairZset 数据结构）中，分数大于等于 min 且小于等于 max 值的元素。 |
| 选项 | min 和 max 分别表示最小分数和最大分数，如 Key 中的元素采用了多维度的分数，各维度的分数之间使用井号（#）分隔。 说明 在不确定 Key 中元素的最高分和最低分的情况下，如果想要移除 Key 中分数大于等于或小于等于某一特定值的元素，请将 min 和 max 分别设置为负无穷大（ -inf ）和正无穷大（ +inf ）。 默认数据范围为闭区间，如需指定开区间，则在分数范围前添加半角圆括号，例如 EXZREMRANGEBYSCORE (1 5 表示删除分数大于 1 且小于等于 5 的元素。 |
| 返回值 | 返回被移除的元素的数量。 |
| 命令示例 | 命令示例： EXZREMRANGEBYSCORE testkey 3#2#4 6#6#6 返回示例： (integer) 1 |
