## BF.RESERVE

| 类别 | 说明 |
| --- | --- |
| 语法 | BF.RESERVE key error_rate capacity |
| 时间复杂度 | O(1) |
| 命令描述 | 创建一个大小为 capacity，错误率为 error_rate 的空的 TairBloom。 |
| 选项 | Key ：Key 名称（TairBloom 数据结构），用于指定作为命令调用对象的 TairBloom。 error_rate ：期望的错误率（False Positive Rate），该值必须介于 0 和 1 之间。该值越小，精度越高，TairBloom 的内存占用量越大，CPU 使用率越高。 capacity ：TairBloom 的初始容量，即期望添加到 TairBloom 中的元素的个数。 当实际添加的元素个数超过该值时，TairBloom 将通过增加 Bloom Filter 的层数完成自动扩容，该过程会导致查询性能下降。每增加一层，就可能需要遍历多层 Bloom Filter 来完成查询。因此，如果对性能非常的敏感，需要在使用前充分评估要添加到 TairBloom 的元素个数，避免发生导致层数增加的扩容操作。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： BF.RESERVE BFKEY 0.01 100 返回示例： OK |
