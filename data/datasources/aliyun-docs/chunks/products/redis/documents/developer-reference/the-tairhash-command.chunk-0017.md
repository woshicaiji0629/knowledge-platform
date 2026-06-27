## EXHVER

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHVER key field |
| 时间复杂度 | O(1) |
| 命令描述 | 查看 key 指定的 TairHash 中一个 field 的当前版本号。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | key 不存在：-1。 field 不存在：-2。 查询成功：field 的版本号。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHVER myhash field1 返回示例： (integer) 1 |
