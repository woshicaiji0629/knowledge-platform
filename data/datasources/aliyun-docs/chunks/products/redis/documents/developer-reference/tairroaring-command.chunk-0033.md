## TR.CONTAINS

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.CONTAINS key1 key2 |
| 时间复杂度 | O(M) |
| 命令描述 | 计算 key2 所对应的 Roaring Bitmap 是否包含 key1 所对应的 Roaring Bitmap（即 key1 是否为 key2 的子集），若包含则返回 1，否则返回 0。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 |
| 返回值 | 执行成功： 返回 1，表示 key2 包含 key1，即 key1 是 key2 的子集。 返回 0，表示 key2 不包含 key1，即 key1 不是 key2 的子集。 其他情况返回相应的异常信息。 |
| 示例 | 提前执行 TR.SETBITS fooM 1 2 3 10 、 TR.SETBITS foom 1 2 命令。 命令示例： TR.CONTAINS foom fooM 返回示例： (integer) 1 |
