## EXSETVER

| 类别 | 说明 |
| --- | --- |
| 语法 | EXSETVER key version |
| 时间复杂度 | O(1) |
| 命令描述 | 设置目标 key 的 version。 |
| 选项 | Key ：TairString 的 key，用于指定作为命令调用对象的 TairString。 version ：需要设置的版本号。 |
| 返回值 | 执行成功：1。 若 key 不存在：0。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXSETVER foo 2 返回示例： (integer) 1 |
