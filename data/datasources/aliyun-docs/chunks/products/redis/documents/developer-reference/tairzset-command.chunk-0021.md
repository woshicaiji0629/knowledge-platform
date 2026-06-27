## EXZREMRANGEBYLEX

| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREMRANGEBYLEX key min max |
| 时间复杂度 | O(log(N)+M)，其中，N 为 TairZset 中元素的数量，M 为该操作移除的元素的数量。 |
| 命令描述 | 为确保元素按照字典序排列，当 Key 中所有元素分数相同时，则该命令移除存储在 Key 中介于 max 和 min 之间的元素。 说明 若使用相同的 min 和 max 参数值执行该命令和 [EXZRANGEBYLEX](tairzset-command.md) 命令，则该命令移除的元素与 EXZRANGEBYLEX 命令返回的元素相同。 |
| 选项 | min 、 max ：分别表示成员名称的最小值和最大值（字符串形式），需指定字符的区间，例如 开区间：在值的前面增加半角圆括号，例如 (a 。 闭区间：在值的前面增加方括号，例如 [a |
| 返回值 | 被移除的元素的数量。 |
| 命令示例 | 命令示例： EXZREMRANGEBYLEX [a [b 返回示例： (integer) 2 |
