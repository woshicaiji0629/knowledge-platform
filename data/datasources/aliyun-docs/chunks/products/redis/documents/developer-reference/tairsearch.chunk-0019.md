## TFT.MADDDOC

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.MADDDOC index document doc_id [document1 doc_id1] ... |
| 命令描述 | 向索引中插入多个文档（document），每个文档必须指定文档 ID（doc_id）。若某个文档写入失败（例如写入的文档内容与定义的格式不符），则该命令的所有文档均不会写入。 |
| 选项 | index ：待操作的索引名称。 document ：插入的文档，JSON 格式，插入的值需与该字段定义的数据类型一致。 说明 若索引通过 _source 的 includes 参数配置了仅保存部分字段，则在插入或更新文档时仅保存 includes 中配置的字段。 doc_id ：指定文档 ID，doc_id 的格式为任意字符串。 |
| 返回值 | 执行成功：返回 OK。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.MADDDOC idx:product '{"product_id":"test1"}' 00011 '{"product_id":"test2"}' 00012 返回示例： OK |
