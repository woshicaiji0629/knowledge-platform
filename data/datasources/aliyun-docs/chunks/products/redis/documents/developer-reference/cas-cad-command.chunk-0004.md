## CAD

| 类别 | 说明 |
| --- | --- |
| 语法 | CAD key value |
| 时间复杂度 | O(1) |
| 命令描述 | CAD（Compare And Delete），查看指定 Value 值是否与目标 Key 的 Value 相等，若相等则删除该 Key，不相等则不删除。 说明 该命令仅适用于操作 Redis String 类型的数据，如需对 TairString 做相同的操作，请使用 EXCAD。 |
| 选项 | Key ：目标 Key，String 类型。 value ：指定 Value，用于跟现有 Key 的 Value 进行比较。 |
| 返回值 | 执行成功：1 执行失败：0 若 Key 不存在：-1 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 SET foo bar 命令。 命令示例： CAD foo bar 返回示例： (integer) 1 执行成功，则 foo Key 被删除，若此时执行 GET foo ，将返回 (nil) 。 |

该文章对您有帮助吗？
反馈
