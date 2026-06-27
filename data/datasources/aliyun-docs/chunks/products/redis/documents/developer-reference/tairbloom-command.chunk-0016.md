## BF.INFO

| 类别 | 说明 |
| --- | --- |
| 语法 | BF.INFO key |
| 时间复杂度 | O(log N) ，其中 N 是 TairBloom 的层数。 |
| 命令描述 | 查看 Key 指定的 TairBloom 内部信息，如当前层数和每一层的元素个数、错误率等。 |
| 选项 | Key ：Key 名称（TairBloom 数据结构），用于指定作为命令调用对象的 TairBloom。 |
| 返回值 | 执行成功将返回 TairBloom 信息。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： BF.INFO bk1 返回示例： 1) "total_items:6,num_blooms:2" 2) "bytes:4 bits:32 hashes:7 hashwidth:64 capacity:3 items:3 error_ratio:0.01" 3) "bytes:16 bits:128 hashes:9 hashwidth:64 capacity:10 items:3 error_ratio:0.0025" BF.INFO 返回参数说明： total_items 表示总元素数量、num_blooms 表示总 Bloom Filter 层数。 每层 Bloom Filter 的信息： bytes：占用字节数。 bits：占用 bit 位数，bits = bytes * 8。 hashes：Hash 函数数量。 hashwidth：Hash 函数宽度。 capacity：容量。 items：元素数量。 error_ratio：错误率。 |

该文章对您有帮助吗？
反馈
