## BF.INSERT

| 类别 | 说明 |
| --- | --- |
| 语法 | BF.INSERT key [CAPACITY cap ] [ERROR error ] [NOCREATE] ITEMS item [ item ...] |
| 时间复杂度 | O(log N) ，其中 N 是 TairBloom 的层数。 |
| 命令描述 | 在 Key 指定的 TairBloom 中一次性添加多个元素，添加时可以指定大小和错误率，且可以控制在 TairBloom 不存在的时候是否自动创建。 |
| 选项 | Key ：Key 名称（TairBloom 数据结构），用于指定作为命令调用对象的 TairBloom。 capacity ：TairBloom 的初始容量，即期望添加到 TairBloom 中元素的个数，当 TairBloom 已经存在时该值将被忽略。 当实际添加的元素个数超过该值时，TairBloom 将进行自动的扩容。 error_rate ：期望的错误率（False Positive Rate），该值必须介于 0 和 1 之间。该值越小，精度越高，TairBloom 的内存占用量越大，CPU 使用率越高。 NOCREATE ：设置该选项后，当指定的 TairBloom 不存在的时候不要自动创建该 TairBloom。该参数不能与 CAPACITY 和 ERROR 同时设置。 item ：需要添加的元素，可设置多个。 |
| 返回值 | 1：表示该元素之前一定不存在，并往 TairBloom 中添加该元素。 0：表示该元素可能已存在，所以不会进行添加或更新操作。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： BF.INSERT bfkey1 CAPACITY 10000 ERROR 0.001 ITEMS item1 item2 item3 返回示例： (integer) 1 (integer) 1 (integer) 1 |
