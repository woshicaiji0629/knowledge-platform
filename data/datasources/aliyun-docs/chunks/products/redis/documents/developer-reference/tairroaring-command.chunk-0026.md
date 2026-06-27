## TR.RANGE

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.RANGE key start end |
| 时间复杂度 | O(C) |
| 命令描述 | 获取 Roaring Bitmap 指定区间中 bit 值为 1 的偏移量。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 start ：起始的偏移量（包含该值）。 end ：结束的偏移量（包含该值）。 |
| 返回值 | 执行成功：返回 bit 值为 1 的偏移量。 若 key 不存在：返回空数组。 其他情况返回相应的异常信息。 |
| 示例 | 提前执行 TR.SETBITS foo 0 2 3 5 。 命令示例： TR.RANGE foo 0 5 返回示例： 1) (integer) 0 2) (integer) 2 3) (integer) 3 4) (integer) 5 |
