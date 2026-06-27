## TVS.SCAN

| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.SCAN index_name cursor [MATCH pattern ] [COUNT count ] [FILTER filter_string] [VECTOR vector] [MAX_DIST max_distance] |
| 时间复杂度 | O(N)，N 为该向量索引中 Key 的数量。 |
| 命令描述 | 在指定向量索引中，扫描符合条件的数据记录（ key ）。 |
| 选项 | index_name ：向量索引名称。 cursor ：指定本次扫描的游标，从 0 开始。 pattern ：模式匹配。 count ：指定本次扫描的数量，默认为 10，但无法保证每次迭代都返回精准的元素数量。 filter_string ：过滤条件。 支持+-*/<>!=()&&||等操作符，暂不支持比较字符串之间的大小。如需输入字符串，请输入转义字符（\），例如 create_time > 1663637425 && location == \"Hangzhou\"。 操作符两侧必须用空格隔开，例如"creation_time > 1735"。 不支持 flag == true 类型的比较，即不支持 true、false 布尔类型，可以替换为 flag == \"true\" ，当成字符串传递即可。 vector ：查询向量，需要配合 max_distance 参数使用。 max_distance ：最大距离限制，必须配合 vector 参数使用。填写这两个参数后，返回结果与 vector 参数的距离将小于 max_distance 参数。 |
| 返回值 | 执行成功，返回一个数组： 第一个元素：下次查询的游标，若已扫描完成，则返回 0。 第二个元素：本次查询的数据记录（ key ）名称。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.SCAN index_name0 0 返回示例： 1) "0" 2) 1) "key0" 2) "keyV" |
