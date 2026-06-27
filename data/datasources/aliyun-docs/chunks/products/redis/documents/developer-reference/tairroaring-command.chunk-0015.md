## TR.APPENDINTARRAY

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.APPENDINTARRAY key value [value1 value2 ... valueN] |
| 时间复杂度 | O(C) |
| 命令描述 | 设置 Roaring Bitmap 中指定偏移量（offset）的 bit 值为 1，支持传入多个值。 说明 在 TairRoaring V2 版本中，建议使用 [TR.SETBITS](tairroaring-command.md) 代替该命令。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 value ：整型数字，表示待设置的 bit 位，取值范围为 0 ~ 4294967296。 |
| 返回值 | 执行成功：返回 OK。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.APPENDINTARRAY foo 9 10 返回示例： OK |
