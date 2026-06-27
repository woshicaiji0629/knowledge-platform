## EXZCARD

| 类别 | 说明 |
| --- | --- |
| 语法 | EXZCARD key |
| 时间复杂度 | O(1) |
| 命令描述 | 返回存储在 Key（TairZset 数据结构）中的基数（即元素的个数）。 |
| 选项 | 无 |
| 返回值 | 返回 Key 中的元素的数量，如果 Key 不存在，则返回 0。 |
| 命令示例 | 命令示例： EXZCARD testkey 返回示例： (integer) 2 |
