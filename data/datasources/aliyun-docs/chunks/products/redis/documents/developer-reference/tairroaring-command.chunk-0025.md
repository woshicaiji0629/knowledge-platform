## TR.SCAN

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.SCAN key start_offset [COUNT count] |
| 时间复杂度 | O(C) |
| 命令描述 | 从 Roaring Bitmap 中指定偏移量（start_offset）开始向后扫描，返回若干（count）个 bit 值为 1 的偏移量，返回的游标（cursor）为 Roaring Bitmap 对应的 offset。 说明 在迭代过程中被添加、被删除的元素的扫描结果存在不确定性，即可能被返回，也可能不会。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 start_offset ：起始偏移量（包含该值）。 COUNT ：查询的数量（默认为 10）。 |
| 返回值 | 执行成功，返回具有两个元素的数组： 第一个元素：下次查询的 start_offset，若该 key 已扫描完成，则返回 0。 第二个元素：本次查询的目标偏移量。 说明 若 key 不存在，返回 0 与空元素组成的数组。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.SCAN foo 0 COUNT 2 返回示例： 1) (integer) 3 2) 1) (integer) 0 2) (integer) 2 |
