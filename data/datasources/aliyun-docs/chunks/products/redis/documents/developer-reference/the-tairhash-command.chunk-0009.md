## EXHGET

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHGET key field |
| 时间复杂度 | O(1) |
| 命令描述 | 获取 key 指定的 TairHash 中一个 field 的值，如果 TairHash 不存在或者 field 不存在，则返回 nil。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | field 存在且操作成功：field 对应的值。 key 不存在或者 field 不存在：nil。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXHSET myhash field1 val 命令。 命令示例： EXHGET myhash field1 返回示例： "val" |
