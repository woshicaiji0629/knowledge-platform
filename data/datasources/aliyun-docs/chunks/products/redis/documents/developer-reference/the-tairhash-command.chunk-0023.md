## EXHMGETWITHVER

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHMGETWITHVER key field [field ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 同时获取 key 指定的 TairHash 多个 field 的值和版本。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | key 不存在：nil。 key 存在且查询的所有 field 都存在：返回一个数组，数组的每一个元素对应一个 field 的 value 和 version。 key 存在且查询的 field 中有不存在的：返回一个数组，数组的每一个元素对应一个 field 的 value 和 version，不存在的 field 对应的元素显示为 nil。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXHMSET myhash field1 10 field2 var1 命令。 命令示例： EXHMGETWITHVER myhash field1 field2 返回示例： 1) 1) "10" 2) (integer) 1 2) 1) "var1" 2) (integer) 1 |
