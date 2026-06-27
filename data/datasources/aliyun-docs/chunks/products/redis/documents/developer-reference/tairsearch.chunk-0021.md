## TFT.DELDOCFIELD

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.DELDOCFIELD index doc_id field [field1 field2 ...] |
| 命令描述 | 删除索引中 doc_id 指定文档的指定字段，若该字段为索引字段，会同时在索引中删除该字段的信息。 说明 若指定的字段不存在（例如被 _source 过滤的字段），则操作失败。 |
| 选项 | index ：待操作的索引名称。 doc_id ：指定文档 ID。 field ：待删除的字段。 |
| 返回值 | 执行成功：返回成功删除的字段数量。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.DELDOCFIELD idx:product 00011 product_group 返回示例： (integer) 1 |
