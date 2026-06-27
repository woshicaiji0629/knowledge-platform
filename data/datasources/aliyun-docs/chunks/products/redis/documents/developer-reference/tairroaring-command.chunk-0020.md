## TR.OPTIMIZE

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.OPTIMIZE key |
| 时间复杂度 | O(M) |
| 命令描述 | 优化 Roaring Bitmap 的存储空间。如果目标对象相对较大，且创建后以只读操作为主，可以主动执行此命令。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 |
| 返回值 | 执行成功：返回 OK。 若 key 不存在：返回 nil 。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.OPTIMIZE foo 返回示例： OK |
