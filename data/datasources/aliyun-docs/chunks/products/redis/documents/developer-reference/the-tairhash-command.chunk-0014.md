## EXHEXPIRE

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHEXPIRE key field seconds [VER | ABS version] |
| 时间复杂度 | O(1) |
| 命令描述 | 在 key 指定的 TairHash 中为一个 field 设置相对过期时间，单位为秒。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 seconds ：相对过期时间，单位为秒。 VER ：版本号。 如果 field 存在，和当前版本号做比较： 如果相等，继续操作，且版本号加 1。 如果不相等，返回异常。 如果 field 不存在或者 field 当前版本为 0，忽略传入的版本号并继续操作，成功后版本号变为 1。 ABS ：绝对版本号，不论 field 是否存在，可以在插入 field 时设置为本参数所指定的版本号。 |
| 返回值 | field 存在且设置成功：1。 field 不存在：0。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHEXPIRE myhash field1 100 返回示例： (integer) 1 |
