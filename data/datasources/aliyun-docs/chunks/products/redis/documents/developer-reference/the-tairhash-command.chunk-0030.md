## EXHSCAN

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHSCAN key op subkey [MATCH pattern] [COUNT count] |
| 时间复杂度 | 每次调用时是 O(1)，遍历整个 TairHash 时是 O(N)。 |
| 命令描述 | 扫描 Key 指定的 TairHash。 说明 仅内存型实例支持该命令。 |
| 选项 | key ：TairHash 的 Key，用于指定作为命令调用对象的 TairHash。 op ：用于定位扫描的起点，可选值如下。 > ：表示从第一个大于 subkey 的 field 开始。 >= ：表示从第一个大于等于 subkey 的 field 开始。 < ：表示从第一个小于 subkey 的 field 开始。 <= ：表示从第一个小于等于 subkey 的 field 开始。 == ：表示从第一个等于 subkey 的 field 开始。 ^ ：表示从第一个 field 开始。 $ ：表示从最后一个 field 开始。 subkey ：用于与 op 选项搭配，设置扫描起始位置，当 op 为^或$时该值将被忽略。 MATCH ：用于过滤扫描结果，根据 MATCH 指定的 pattern 对 subkey 进行正则过滤。 COUNT ：用于规定单次扫描 field 的个数（默认为 10）。 说明 COUNT 仅表示每次扫描 TairHash 的 field 的个数，不代表最终一定会返回 COUNT 个 field 结果集，结果集的大小还要根据 TairHash 中当前 field 个数和是否指定 MATCH 进行过滤而定。 |
| 返回值 | Key 不存在：返回一个空数组。 Key 存在：返回一个具有两个元素的数组： 第一个元素：下一次扫描的起始 field，如果该 Key 已扫描完成，则该元素为空。 第二个元素：本次扫描结果，包含 field 和 value。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXHMSET myhashkey field1 val1 field2 val2 field3 val3 field4 val4 field5 val5 命令。 命令示例： EXHSCAN myhashkey ^ xx COUNT 3 返回示例： 1) "field4" 2) 1) "field1" 2) "val1" 3) "field2" 4) "val2" 5) "field3" 6) "val3" |
