| 类别 | 说明 |
| --- | --- |
| 语法 | TR.STAT key [JSON] |
| 时间复杂度 | O(M) |
| 命令描述 | 获取 Roaring Bitmap 的统计信息，包括各种容器的数量以及内存使用状况等信息。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 JSON ：若指定 JSON，则以 JSON 格式返回统计信息。 |
| 返回值 | 执行成功：返回 Redis 的统计信息（bulk string），说明如下。 "{\"cardinality\":3, # 元素总数量 \"number_of_containers\":1, # TairRoaring 容器总数（Roaring Bitmap 概念） \"max_value\":6, # 最大元素值 \"min_value\":3, # 最小元素值 \"sum_value\":13, \"array_container\":{ # array 容器数量（Roaring Bitmap 概念） \"number_of_containers\":1, \"container_cardinality\":3, \"container_allocated_bytes\":6}, \"bitset_container\":{ # bitset 容器数量（Roaring Bitmap 概念） \"number_of_containers\":0, \"container_cardinality\":0, \"container_allocated_bytes\":0}, \"run_container\":{ # RLE 容器数量（Roaring Bitmap 概念） \"number_of_containers\":0, \"container_cardinality\":0, \"container_allocated_bytes\":0}}" 若 key 不存在：返回 nil 。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.STAT foo JSON 返回示例： "{\"cardinality\":4,\"number_of_containers\":1,\"max_value\":5,\"min_value\":0,\"sum_value\":10,\"array_container\":{\"number_of_containers\":1,\"container_cardinality\":4,\"container_allocated_bytes\":8},\"bitset_container\":{\"number_of_containers\":0,\"container_cardinality\":0,\
