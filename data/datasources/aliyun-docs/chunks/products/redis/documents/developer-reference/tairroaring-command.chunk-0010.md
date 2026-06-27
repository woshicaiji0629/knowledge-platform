## TR.SETBITS

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.SETBITS key offset [offset1 offset2 ... offsetN] |
| 时间复杂度 | O(C) |
| 命令描述 | 设置 Roaring Bitmap 中指定偏移量（offset）的 bit 值为 1，支持传入多个值。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 offset ：整型数字，表示待设置 bit 的偏移量，取值范围为 0 ~ 2^32。 |
| 返回值 | 执行成功：返回更新后 Roaring Bitmap 中 bit 值为 1 的数量。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.SETBITS foo 9 10 返回示例： (integer) 5 |
