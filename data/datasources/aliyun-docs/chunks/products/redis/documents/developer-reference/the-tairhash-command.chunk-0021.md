## EXHGETWITHVER

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHGETWITHVER key field |
| 时间复杂度 | O(1) |
| 命令描述 | 同时获取 key 指定的 TairHash 一个 field 的值和版本，如果 TairHash 不存在或者 field 不存在，则返回 nil。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | field 存在且操作成功：field 对应的值和版本。 key 不存在或者 field 不存在：nil。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHGETWITHVER myhash field1 返回示例： 1) "19.235" 2) (integer) 5 |
