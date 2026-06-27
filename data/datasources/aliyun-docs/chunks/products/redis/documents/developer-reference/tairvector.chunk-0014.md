## TVS.DELINDEX

| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.DELINDEX index_name |
| 时间复杂度 | O(N)，N 为该向量索引中 Key 的数量。 |
| 命令描述 | 删除指定的向量索引及该索引内的所有数据。 |
| 选项 | index_name ：向量索引名称。 |
| 返回值 | 执行成功：删除向量索引，并返回 1。 若指定索引不存在，返回 0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.DELINDEX index_name0 返回示例： (integer) 1 |
