## TFT.UPDATEDOCFIELD

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.UPDATEDOCFIELD index doc_id document |
| 命令描述 | 更新索引中 doc_id 指定的文档，若更新的字段为 mapping 指定的索引字段时，该字段更新的内容需与 mapping 指定的类型一致；若非索引字段，支持更新任意字段类型的内容。 说明 若更新的字段已存在，则更新原文档，若字段不存在，则新增该字段。若指定的文档不存在，该命令支持自动创建文档，此时效果等同于 TFT.ADDDOC。 |
| 选项 | index ：待操作的索引名称。 doc_id ：指定文档 ID。 document ：更新的文档内容，JSON 格式。 说明 若索引通过 _source 的 includes 参数配置了仅保存部分字段，则在插入或更新文档时仅保存 includes 中配置的字段。 |
| 返回值 | 执行成功：返回 OK。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.UPDATEDOCFIELD idx:product 00011 '{"product_id":"test8","product_group":"BOOK"}' 返回示例： OK |
