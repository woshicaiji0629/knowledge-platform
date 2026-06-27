## TR.SETRANGE

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.SETRANGE key start end |
| 时间复杂度 | O(C) |
| 命令描述 | 设置 Roaring Bitmap 中指定区间（偏移量）的 bit 值为 1。 例如执行 TR.SETRANGE foo 1 3 ，将创建 foo 为"0111"。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 start ：起始偏移量（包含该值），取值范围为 0 ~ 2^32。 end ：结束偏移量（包含该值），取值范围为 0 ~ 2^32。 |
| 返回值 | 执行成功：返回本次命令成功将 bit 值设置为 1 的数量。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.SETRANGE foo 1 3 返回示例： (integer) 3 |
