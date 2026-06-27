## EXHSETVER

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHSETVER key field version |
| 时间复杂度 | O(1) |
| 命令描述 | 设置 key 指定的 TairHash 中一个 field 的版本号。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | TairHash 或者 field 不存在：0。 设置成功：1。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHSETVER myhash field1 3 返回示例： (integer) 1 |
