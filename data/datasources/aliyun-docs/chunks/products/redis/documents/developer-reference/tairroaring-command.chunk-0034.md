## TR.RANK

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.RANK key offset |
| 时间复杂度 | O(M) |
| 命令描述 | 获取 Roaring Bitmap 中从 offset 为 0 到指定 offset 区间内（包含该值），bit 值为 1 的数量。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 offset ：指定 bit 的 offset 位，取值为 INT（整型数字）。 |
| 返回值 | 执行成功：目标区间 bit 值为 1 的数量。 其他情况返回相应的异常信息。 |
| 示例 | 提前执行 TR.SETBITS fooM 1 2 3 10 。 命令示例： TR.RANK fooM 10 返回示例： (integer) 4 |
