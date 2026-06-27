## EXZREMRANGEBYRANK

| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREMRANGEBYRANK key start stop |
| 时间复杂度 | O(log(N)+M)，其中，N 为 TairZset 中元素的数量，M 为该操作移除的元素的数量。 |
| 命令描述 | 移除存储在 Key（TairZset 数据结构）中，级别介于 start 和 stop 之间的元素。 |
| 选项 | start 和 stop 均为基于零的索引值，其中，0 代表分数最低的元素。 当索引值为负数，代表从最高分数元素开始的偏移量，例如-1 为分数最高的元素，-2 为分数第二高的元素，依此类推。 |
| 返回值 | 被移除的元素的数量。 |
| 命令示例 | 命令示例： EXZREMRANGEBYRANK testkey 0 1EXZREVRANGEBYSCORE 返回示例： (integer) 1 |
