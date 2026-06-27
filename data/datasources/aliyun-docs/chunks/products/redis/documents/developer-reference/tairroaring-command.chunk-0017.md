## TR.SETBITARRAY

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.SETBITARRAY key value |
| 时间复杂度 | O(C) |
| 命令描述 | 根据传入的 bit（由 0 和 1 组成的字符串），创建对应的 Roaring Bitmap。若目标 Key 已存在则会重置（覆盖）原有数据。 说明 在 TairRoaring V2 版本中，建议使用 [TR.APPENDBITARRAY](tairroaring-command.md) 代替该命令。 |
| 选项 | key ：Key 名称（TairRoaring 数据结构）。 value ：由 0 和 1 构成的字符串，即需要设置的 bit 数组。 |
| 返回值 | 执行成功：返回 OK 。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： tr.setbitarray foo 10101001 返回示例： OK |
