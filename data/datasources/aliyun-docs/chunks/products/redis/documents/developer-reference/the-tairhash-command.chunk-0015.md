## EXHPTTL

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHPTTL key field |
| 时间复杂度 | O(1) |
| 命令描述 | 查看 key 指定的 TairHash 中一个 field 的剩余过期时间，结果精确到毫秒。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | field 存在但是没有设置过期时间：-1。 key 不存在：-2。 field 不存在：-3。 field 存在且设置了过期时间：过期时间，单位为毫秒。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXHSET myhash field1 val1 EX 100 命令。 命令示例： EXHPTTL myhash field1 返回示例： (integer) 97213 |
