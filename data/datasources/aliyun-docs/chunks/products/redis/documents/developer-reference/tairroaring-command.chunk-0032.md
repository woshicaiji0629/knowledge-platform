## TR.JACCARD

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.JACCARD key1 key2 |
| 时间复杂度 | O(M) |
| 命令描述 | 获取两个 Roaring Bitmap 之间的 Jaccard 相似系数，Jaccard 系数值越大，Roaring Bitmap 的相似度越高。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 |
| 返回值 | 执行成功：返回 Jaccard 相似系数（Double 类型）。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.JACCARD foo1 foo2 返回示例： "0.20000000000000001" |
