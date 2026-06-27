## TR.BITPOS

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.BITPOS <key> <value> [count] |
| 时间复杂度 | O(C) |
| 命令描述 | 获取第 count 个 bit 值为 1 或者 0 的偏移量，count 为可选参数，默认为 1（表示从前向后计数的第一个）。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 value ：待查找 bit 值（1 或者 0）。 count ：查找第几位，负数表示从末尾向前计数。 |
| 返回值 | 执行成功：返回目标 bit 的偏移量（offset）。 若 key 不存在：返回-1。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.BITPOS foo 1 -1 返回示例： (integer) 6 |
