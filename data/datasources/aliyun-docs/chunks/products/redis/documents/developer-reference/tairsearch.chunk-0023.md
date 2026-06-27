## TFT.INCRFLOATDOCFIELD

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.INCRFLOATDOCFIELD index doc_id field increment |
| 命令描述 | 向索引中 doc_id 指定文档的指定字段增加浮点数值（increment），支持指定 increment 为负数，支持指定的字段类型为 double 类型。 说明 若指定的文档不存在，该命令支持自动创建文档，初始化字段的值为 0，并增加指定的 increment。若指定的字段不存在（例如被 _source 过滤的字段），则操作失败。 |
| 选项 | index ：待操作的索引名称。 doc_id ：指定文档 ID。 field ：待操作的字段，支持的字段类型 double 类型，且不支持数组类型的字段。 increment ：待增加操作的值，可以指定该值为负数实现相减，数据类型为双精度浮点型（double）。 |
| 返回值 | 执行成功：返回执行操作后字段的数值。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.INCRFLOATDOCFIELD idx:product 00011 stock 299.6 返回示例： "299.6" |
