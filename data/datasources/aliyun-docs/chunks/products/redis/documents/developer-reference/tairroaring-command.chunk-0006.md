itmap 对应的 offset。 说明 在迭代过程中被添加、被删除的元素的扫描结果存在不确定性，即可能被返回，也可能不会。 | V2 新增 |  |
| [TR.RANGE](tairroaring-command.md) | TR.RANGE key start end | 获取 Roaring Bitmap 指定区间中 bit 值为 1 的偏移量。 | V1 的 TR.RANGEINTARRAY 命令，V2 重命名为 TR.RANGE。 |  |
| [TR.RANGEBITARRAY](tairroaring-command.md) | TR.RANGEBITARRAY key start end | 获取 Roaring Bitmap 指定区间中所有 bit 值（0、1）组成的字符串。 | V2 新增 |  |
| [TR.MIN](tairroaring-command.md) | TR.MIN key | 获取 Roaring Bitmap 中 bit 值为 1 的最小偏移量（首个），不存在时返回-1。 | - |  |
| [TR.MAX](tairroaring-command.md) | TR.MAX key | 获取 Roaring Bitmap 中 bit 值为 1 的最大偏移量，不存在时返回-1。 | - |  |
| [TR.STAT](tairroaring-command.md) | TR.STAT key [JSON] | 获取 Roaring Bitmap 的统计信息，包括各种容器的数量以及内存使用状况等信息。 | V2 新增 |  |
| [TR.JACCARD](tairroaring-command.md) | TR.JACCARD key1 key2 | 获取两个 Roaring Bitmap 之间的 Jaccard 相似系数，Jaccard 系数值越大，Roaring Bitmap 的相似度越高。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 | V2.2 新增 |  |
| [TR.CONTAINS](tairroaring-command.md) | TR.CONTAINS key1 key2 | 计算 key2 所对应的 Roaring Bitmap 是否包含 key1 所对应的 Roaring Bitmap（即 key1 是否为 key2 的子集），若包含则返回 1，否则返回 0。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 | V2.2 新增 |  |
| [TR.RANK](tairroaring-command.md) | TR.RANK key offset | 获取 Roaring Bitmap 中从 offset 为 0 到指定 offset 区间内（
