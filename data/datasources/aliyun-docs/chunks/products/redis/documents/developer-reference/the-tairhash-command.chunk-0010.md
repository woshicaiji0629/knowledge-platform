## EXHMSET

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHMSET key field value [field value ...] |
| 时间复杂度 | O(N) |
| 命令描述 | 同时向 key 指定的 TairHash 中插入多个 field，如果 TairHash 不存在则自动创建一个，如果 field 已经存在则覆盖其值。 说明 创建 Key 后，您可以通过 EXHPEXPIREAT 、 EXHPEXPIRE 、 EXHEXPIREAT 或 EXHEXPIRE 命令设置 field 的过期时间，您也可以通过 EXPIRE 或 EXPIREAT 命令设置 Key 的过期时间。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 value ：field 对应的值，一个 field 只能有一个 value。 |
| 返回值 | 成功：OK。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHMSET myhash field1 val1 field2 val2 返回示例： OK |
