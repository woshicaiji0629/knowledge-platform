## TR.FLIPRANGE

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.FLIPRANGE key start end |
| 时间复杂度 | O(C) |
| 命令描述 | 对 Roaring Bitmap 中指定区间（偏移量）的 bit 值执行位反转（1 反转为 0；0 反转为 1）。若指定 key 不存在，则自动创建目标 key，并以空 Roaring Bitmap 对指定区间的 bit 值执行位反转。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 start ：起始偏移量（包含该值），取值范围为 0 ~ 2^32。 end ：结束偏移量（包含该值），取值范围为 0 ~ 2^32。 |
| 返回值 | 执行成功：返回本次命令成功将 bit 值设置为 1 的数量。 若 key 不存在：自动创建目标 key，并以空 Roaring Bitmap 对指定区间的 bit 值执行位反转，返回本次命令成功将 bit 值设置为 1 的数量。 其他情况返回相应的异常信息。 |
| 示例 | 提前执行 TR.SETBITS foo 0 2 3 5 。 命令示例： TR.FLIPRANGE foo 0 5 返回示例： (integer) 2 此时，Roaring Bitmap foo 为“01001”。 |
