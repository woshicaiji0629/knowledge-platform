## TR.SETBIT

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.SETBIT key offset value |
| 时间复杂度 | O(1) |
| 命令描述 | 设置 Roaring Bitmap 中指定偏移量（offset）的 bit 值（1 或者 0），并返回该 bit 位之前的值，Roaring Bitmap 的偏移量（offset）从 0 开始。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 offset ：整型数字，表示待设置 bit 的偏移量，取值范围为 0 ~ 2^32。 value ：待设置的 bit 值，可以设置 1 或者 0。 |
| 返回值 | 执行成功：返回 0 或 1，表示 bit 位之前的值。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.SETBIT foo 0 1 返回示例： (integer) 0 |
