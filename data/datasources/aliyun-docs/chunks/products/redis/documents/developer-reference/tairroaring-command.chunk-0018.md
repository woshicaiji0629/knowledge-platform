## TR.BITOP

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.BITOP destkey operation key [key1 key2 ... keyN] |
| 时间复杂度 | O(C * M) |
| 命令描述 | 对 Roaring Bitmap 执行集合运算操作，计算结果存储在 destkey 中，支持 AND 、 OR 、 XOR 、 NOT 和 DIFF 集合运算类型。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 |
| 选项 | destkey ：集合运算结果所存储的目标 Key（TairRoaring 数据结构）。 operation ：集合运算类型，取值：AND（表示与）、OR（表示或）、XOR（表示异或）、NOT（表示非）、DIFF（表示差）。 说明 NOT 仅支持操作 1 个对象。 DIFF 仅支持计算 2 个对象的差集，请注意计算差集对象的运算顺序，例如 TR.BITOP result DIFF key1 key2 是计算 key1 关于 key2 的差集（key1 - key2）。 key ：Key 名称（TairRoaring 数据结构），可传入多个 Key。 |
| 返回值 | 执行成功：返回操作运算结果中 bit 值为 1 的数量，格式为 Integer（整数）。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.BITOP result OR foo bar 返回示例： (integer) 6 |
