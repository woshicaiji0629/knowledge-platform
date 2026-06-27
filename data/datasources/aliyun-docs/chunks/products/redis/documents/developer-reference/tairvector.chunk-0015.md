## TVS.SCANINDEX

| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.SCANINDEX cursor [MATCH pattern ] [COUNT count ] |
| 时间复杂度 | O(N)，N 为 Tair 实例中向量索引数量。 |
| 命令描述 | 扫描 Tair 实例中所有符合条件的向量索引。 |
| 选项 | cursor ：指定本次扫描的游标，从 0 开始。 pattern ：模式匹配。 count ：指定本次扫描的数量，默认为 10，但无法保证每次迭代都返回精准的元素数量。 |
| 返回值 | 执行成功，返回一个数组： 第一个元素：下次查询的游标，若已扫描完成，则返回 0。 第二个元素：本次查询的向量索引（ index_name ）名称。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.SCANINDEX 0 返回示例： 1) "0" 2) 1) "index_name1" 2) "index_name0" 3) "index_name2" 4) "index_name3" 带 Pattern 的查询示例： TVS.SCANINDEX 0 MATCH **name[0|1] 返回示例： 1) "0" 2) 1) "index_name1" 2) "index_name0" |
