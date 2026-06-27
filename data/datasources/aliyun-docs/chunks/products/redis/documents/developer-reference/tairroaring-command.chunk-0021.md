## TR.GETBIT

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.GETBIT key offset |
| 时间复杂度 | O(1) |
| 命令描述 | 获取 Roaring Bitmap 中指定偏移量（offset）的 bit 值。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 offset ：待查询的偏移量。 |
| 返回值 | 执行成功：返回 0 或 1，表示 bit 位的值。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.GETBIT foo 0 返回示例： (integer) 1 |
