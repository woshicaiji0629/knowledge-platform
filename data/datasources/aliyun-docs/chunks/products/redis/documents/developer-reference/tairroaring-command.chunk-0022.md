## TR.GETBITS

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.GETBITS key offset [offset1 offset2 ... offsetN] |
| 时间复杂度 | O(C) |
| 命令描述 | 获取 Roaring Bitmap 中指定偏移量（offset）的 bit 值，支持查询多个值。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 offset ：待查询的偏移量。 |
| 返回值 | 执行成功：返回对应 bit 的值。 若 key 不存在：返回空数组。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.GETBITS foo 3 4 6 8 返回示例： 1) (integer) 1 2) (integer) 1 3) (integer) 1 4) (integer) 0 |
