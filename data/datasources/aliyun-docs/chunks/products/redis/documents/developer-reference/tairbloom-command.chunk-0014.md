## BF.MEXISTS

| 类别 | 说明 |
| --- | --- |
| 语法 | BF.MEXISTS key item [ item ...] |
| 时间复杂度 | O(log N) ，其中 N 是 TairBloom 的层数。 |
| 命令描述 | 同时检查多个元素是否存在于 Key 指定的 TairBloom 中。 |
| 选项 | Key ：Key 名称（TairBloom 数据结构），用于指定作为命令调用对象的 TairBloom。 item ：需要查询的元素，可设置多个。 |
| 返回值 | 0：表示该元素一定不存在。 1：表示该元素可能存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： BF.MEXISTS BFKEY item1 item5 返回示例： (integer) 1 (integer) 0 |
