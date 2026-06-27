## TFT.ADDDOC

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.ADDDOC index document [WITH_ID doc_id] |
| 命令描述 | 向索引中插入一个文档（document），可通过 WITH_ID 指定该文档在索引内的唯一 ID（doc_id），若 doc_id 已存在，则更新并覆盖原文档。若不指定 WITH_ID （默认），则自动生成 doc_id。 |
| 选项 | index ：待操作的索引名称。 document ：插入的文档，JSON 格式，插入的值需与该字段定义的数据类型一致。 说明 若索引通过 _source 的 includes 参数配置了仅保存部分字段，则在插入或更新文档时仅保存 includes 中配置的字段。 WITH_ID doc_id ：是否指定文档 ID，如需指定文档 ID 需输入 doc_id 值，doc_id 的格式为任意字符串。 |
| 返回值 | 执行成功：返回文档 ID，格式为 JSON。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.ADDDOC idx:product '{"product_id":"product test"}' WITH_ID 00001 返回示例： {"id":"00001"} 数组的添加示例： TFT.ADDDOC idx:product '{"product_id":["an","2","3df"]}' WITH_ID 00001 |
