## BF.ADD

| 类别 | 说明 |
| --- | --- |
| 语法 | BF.ADD key item |
| 时间复杂度 | O(log N) ，其中 N 是 TairBloom 的层数。 |
| 命令描述 | 在 Key 指定的 TairBloom 中添加一个元素。 说明 若目标 Key 不存在，Tair 会自动创建一个 TairBloom，创建 TairBloom 的默认容量（capacity）为 100，错误率（error_rate）为 0.01。 |
| 选项 | Key ：Key 名称（TairBloom 数据结构），用于指定作为命令调用对象的 TairBloom。 item ：需要添加到 TairBloom 的元素。 |
| 返回值 | 1：表示该元素之前一定不存在，并往 TairBloom 中添加该元素。 0：表示该元素可能已存在，所以不会进行添加或更新操作。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： BF.ADD BFKEY item1 返回示例： (integer) 1 |
