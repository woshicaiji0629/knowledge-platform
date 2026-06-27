## TR.SETINTARRAY

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.SETINTARRAY key value [value1 value2 ... valueN] |
| 时间复杂度 | O(C) |
| 命令描述 | 根据传入的整型数组来设置对应的 Roaring Bitmap，若目标 Key 已存在则会重置（覆盖）原有数据。 说明 在 TairRoaring V2 版本中，建议使用 [TR.SETBITS](tairroaring-command.md) 代替该命令。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 value ：整型数字，表示待设置的 bit 位。 |
| 返回值 | 执行成功：返回 OK。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.SETINTARRAY foo 2 4 5 6 返回示例： OK |
