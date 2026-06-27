## EXGET

| 类别 | 说明 |
| --- | --- |
| 语法 | EXGET key |
| 时间复杂度 | O(1) |
| 命令描述 | 获取 TairString 的 value 和 version。 |
| 选项 | Key ：TairString 的 key，用于指定作为命令调用对象的 TairString。 |
| 返回值 | 执行成功：value 与 version。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXGET foo 返回示例： 1) "bar" 2) (integer) 1 |
