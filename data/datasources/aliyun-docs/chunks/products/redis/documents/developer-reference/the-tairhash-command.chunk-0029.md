## EXHGETALL

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHGETALL key |
| 时间复杂度 | O(N) |
| 命令描述 | 获取 key 指定的 TairHash 中所有 field 及其 value。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 |
| 返回值 | key 不存在：返回一个空数组。 key 存在：返回一个数组，数组的每个元素对应 TairHash 中的一对 field 和 value。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXHMSET myhash field1 10 field2 var1 命令。 命令示例： EXHGETALL myhash 返回示例： 1) "field1" 2) "10" 3) "field2" 4) "var1" |
