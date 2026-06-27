## TR.APPENDBITARRAY

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.APPENDBITARRAY key offset bitarray |
| 时间复杂度 | O(C) |
| 命令描述 | 将由连续的 0 或 1 组成的 bit 数组（bitarray）插入到 Roaring Bitmap 中指定偏移量（offset）之后的位置，并覆盖原有数据。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 offset ：指定的起始偏移量（不包含该值），取值范围为-1 ~ 2^32。 bitarray ：待添加的 bit 数组，将覆盖原有数据，由连续的 0 或 1，取值范围为 0 ~ 2^32。 说明 指定的 offset 与添加的 bitarray 的总长度不能超过 2^32，否则会操作失败。 |
| 返回值 | 执行成功：返回本次命令成功将 bit 值设置为 1 的数量。 其他情况返回相应的异常信息。 |
| 示例 | 提前执行 TR.SETBITS foo 0 。 命令示例： TR.APPENDBITARRAY foo 1 1101 返回示例： (integer) 4 此时，Roaring Bitmap foo 为“101101”。 |
