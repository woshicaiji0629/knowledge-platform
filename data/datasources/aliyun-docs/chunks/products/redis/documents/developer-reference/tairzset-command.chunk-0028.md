## EXZREVRANKBYSCORE

| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREVRANKBYSCORE key score |
| 时间复杂度 | O(log(N)) |
| 命令描述 | 计算指定的分数在 Key（TairZset 数据结构）中按照分数从高到低排序的排名位置。级别（或索引）从 0 开始计数，即分数最高的成员的级别为 0。 说明 若指定的分数不存在，则返回该分数在 Key（TairZset 数据结构）中的预计排名；若指定的分数已存在，Tair 会默认将指定的分数排在已存在的分数之后。 |
| 选项 | 无 |
| 返回值 | 返回指定分数在 Key 中的排名。 |
| 命令示例 | 命令示例： EXZREVRANKBYSCORE testkey 2#0#2 返回示例： (integer) 1 |

该文章对您有帮助吗？
反馈
