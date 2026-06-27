## TR.RANGEBITARRAY

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.RANGEBITARRAY key start end |
| 时间复杂度 | O(C) |
| 命令描述 | 获取 Roaring Bitmap 指定区间中所有 bit 值（0、1）组成的字符串。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 start ：起始的偏移量（包含该值）。 end ：结束的偏移量（包含该值）。 |
| 返回值 | 执行成功：返回 bit 值为 1 的偏移量。 若 key 不存在：返回 nil 。 其他情况返回相应的异常信息。 |
| 示例 | 提前执行 TR.SETBITS foo 0 2 3 5 。 命令示例： TR.RANGEBITARRAY foo 0 5 返回示例： "101101" |
