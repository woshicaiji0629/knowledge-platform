## TR.BITCOUNT

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.BITCOUNT key [start end] |
| 时间复杂度 | O(M) |
| 命令描述 | 获取 Roaring Bitmap 中指定区间（偏移量）bit 值为 1 的数量。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 start ：起始偏移量（包含该值），取值范围为 0 ~ 2^32。 end ：结束偏移量（包含该值），取值范围为 0 ~ 2^32。 |
| 返回值 | 执行成功：返回 Roaring Bitmap 中值为 1 的 bit 位数量，格式为 Integer（整数）。 若 key 不存在：返回 0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.BITCOUNT foo 4 9 返回示例： (integer) 3 |
