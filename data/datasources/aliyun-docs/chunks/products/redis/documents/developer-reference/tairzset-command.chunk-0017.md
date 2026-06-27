## EXZREVRANGEBYLEX

| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREVRANGEBYLEX key max min [LIMIT offset count] |
| 时间复杂度 | O(log(N)+M)，其中，N 表示 TairZset 中元素的数量，M 表示返回的元素的数量。 说明 当 M 为常量时（例如使用 LIMIT 选项指定总是返回前 10 个元素时），可将该公式看作 O(log(N))。 |
| 命令描述 | 为确保元素按照字典序排列，当 Key 中所有元素分数相同时，则该命令返回存储在 Key 中介于 max 和 min 之间的元素。 说明 除排序方式相反外，本命令和 [EXZRANGEBYLEX](tairzset-command.md) 用法相同，注意本命令中 max 在前。 |
| 选项 | min 、 max ：分别表示成员名称的最小值和最大值（字符串形式），需指定字符的区间，例如 开区间：在值的前面增加半角圆括号，例如 (a 。 闭区间：在值的前面增加方括号，例如 [a 说明 正负无穷大分别为 + 和 - 。 LIMIT offset count ：指定返回结果的数量及区间，如果 count 为负数，则返回从 offset 开始的所有元素。 说明 如果 offset 较大，则需要遍历整个 Key 以定位到 offset 元素，然后才能返回元素，即会增加时间复杂度。 |
| 返回值 | 返回元素名称在指定范围内的元素列表。 |
| 命令示例 | 命令示例： EXZREVRANGEBYLEX zzz [b [a 返回示例： 1) "abc" 2) "aba" |
