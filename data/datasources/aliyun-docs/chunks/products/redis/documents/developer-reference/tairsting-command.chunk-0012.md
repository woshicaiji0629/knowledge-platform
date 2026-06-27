## EXCAD

| 类别 | 说明 |
| --- | --- |
| 语法 | EXCAD key version |
| 时间复杂度 | O(1) |
| 命令描述 | 当目标 key 的 version 值与指定的 version 相等时，则删除 Key。 |
| 选项 | Key ：TairString 的 key，用于指定作为命令调用对象的 TairString。 version ：用于跟 key 的现有 version 值比较的值。 |
| 返回值 | 执行成功：1。 执行失败：0。 若 key 不存在：-1。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXSET foo bar 命令。 命令示例： EXCAD foo 1 返回示例： (integer) 1 |

该文章对您有帮助吗？
反馈
