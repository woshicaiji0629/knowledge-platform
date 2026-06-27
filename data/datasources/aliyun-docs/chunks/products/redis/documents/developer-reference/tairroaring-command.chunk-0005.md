-command.md) | TR.BITOPCARD operation key [key1 key2 ... keyN] | 对 Roaring Bitmap 执行集合运算操作，支持 AND 、 OR 、 XOR 、 NOT 和 DIFF 集合运算类型。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 | V2 新增 |  |
| [TR.OPTIMIZE](tairroaring-command.md) | TR.OPTIMIZE key | 优化 Roaring Bitmap 的存储空间。如果目标对象相对较大，且创建后以只读操作为主，可以主动执行此命令。 | - |  |
| 读操作 | [TR.GETBIT](tairroaring-command.md) | TR.GETBIT key offset | 获取 Roaring Bitmap 中指定偏移量（offset）的 bit 值。 | - |
| [TR.GETBITS](tairroaring-command.md) | TR.GETBITS key offset [offset1 offset2 ... offsetN] | 获取 Roaring Bitmap 中指定偏移量（offset）的 bit 值，支持查询多个值。 | V2 新增 |  |
| [TR.BITCOUNT](tairroaring-command.md) | TR.BITCOUNT key [start end] | 获取 Roaring Bitmap 中指定区间（偏移量）bit 值为 1 的数量。 | V2 更新，向前兼容。 |  |
| [TR.BITPOS](tairroaring-command.md) | TR.BITPOS <key> <value> [count] | 获取第 count 个 bit 值为 1 或者 0 的偏移量，count 为可选参数，默认为 1（表示从前向后计数的第一个）。 | V2 更新，向前兼容。 |  |
| [TR.SCAN](tairroaring-command.md) | TR.SCAN key start_offset [COUNT count] | 从 Roaring Bitmap 中指定偏移量（start_offset）开始向后扫描，返回若干（count）个 bit 值为 1 的偏移量，返回的游标（cursor）为 Roaring Bitmap 对应的 offset。 说明 在迭代过程中被添加、被删除的元素的扫描结果存在不确定性，即可能被返回，也可能不会。 | V2 新增 |  |
| [TR.RANGE](tairroaring-command.md) | TR.RANGE key start end | 获取 Roaring Bitmap 指定
