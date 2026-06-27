## EXZREVRANK

| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREVRANK key member |
| 时间复杂度 | O(log(N)) |
| 命令描述 | 返回存储在 Key（TairZset 数据结构）中的成员的级别。返回结果按照分数从高到低排列。 级别（或索引）从 0 开始计数，即分数最高的成员的级别为 0。 说明 除排序规则相反外，本命令和 [EXZRANK](tairzset-command.md) 用法类似。 |
| 选项 | 无 |
| 返回值 | 当 Key 中存在指定的成员，则返回成员的级别（整数）。 当 Key 或 Key 中的成员不存在，则返回 nil。 |
| 命令示例 | 命令示例： EXZREVRANK testkey b 返回示例： (integer) 1 |
