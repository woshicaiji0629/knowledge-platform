## TR.MAX

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.MAX key |
| 时间复杂度 | O(1) |
| 命令描述 | 获取 Roaring Bitmap 中 bit 值为 1 的最大偏移量，不存在时返回-1。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 |
| 返回值 | 执行成功： 返回最后一个 bit 值为 1 的偏移量，格式为 Integer（整数）。 返回-1，表示 key 不存在或者该 Roaring Bitmap 中不存在值为 1 的 bit。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.MAX foo 返回示例： 6 |
