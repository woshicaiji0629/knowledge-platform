## EXHEXISTS

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHEXISTS key field |
| 时间复杂度 | O(1) |
| 命令描述 | 查询 key 指定的 TairHash 中是否存在对应的 field。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | key 不存在或者 field 不存在：0。 field 存在：1。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHEXISTS myhash field1 返回示例： (integer) 1 |
