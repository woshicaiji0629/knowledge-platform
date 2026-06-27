## EXZREM

| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREM key member [member ...] |
| 时间复杂度 | O(M*log(N))，其中，N 为 TairZset 中元素的数量，M 为待移除的元素的数量。 |
| 命令描述 | 移除存储 Key 中的指定成员，如果指定成员不存在，则忽略。 说明 如果指定的 Key 存在，但其数据结构不是 TairZset，系统将返回错误。 |
| 选项 | 无 |
| 返回值 | 返回 Key 中被移除的成员数量，不包含不存在的成员。 |
| 命令示例 | 命令示例： EXZREM testkey a 返回示例： (integer) 1 |
