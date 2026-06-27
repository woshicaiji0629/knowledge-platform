| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [TFT.CREATEINDEX](tairsearch.md) | TFT.CREATEINDEX index mappings settings | 创建索引（index）并添加映射（mappings），映射语法类似 [ES](https://www.elastic.co/guide/en/elasticsearch/reference/8.0/explicit-mapping.html) [语法](https://www.elastic.co/guide/en/elasticsearch/reference/8.0/explicit-mapping.html) 。在添加索引文档前，必须先创建索引。 |
| [TFT.UPDATEINDEX](tairsearch.md) | TFT.UPDATEINDEX index mappings settings | 向指定的索引中新增 properties 字段，或修改索引设置。 |
| [TFT.GETINDEX](tairsearch.md) | TFT.GETINDEX index | 获取索引的映射内容。 |
| [TFT.ADDDOC](tairsearch.md) | TFT.ADDDOC index document [WITH_ID doc_id] | 向索引中插入一个文档（document），可通过 WITH_ID 指定该文档在索引内的唯一 ID（doc_id），若 doc_id 已存在，则更新并覆盖原文档。若不指定 WITH_ID （默认），则自动生成 doc_id。 |
| [TFT.MADDDOC](tairsearch.md) | TFT.MADDDOC index document doc_id [document1 doc_id1] ... | 向索引中插入多个文档（document），每个文档必须指定文档 ID（doc_id）。若某个文档写入失败（例如写入的文档内容与定义的格式不符），则该命令的所有文档均不会写入。 |
| [TFT.UPDATEDOCFIELD](tairsearch.md) | TFT.UPDATEDOCFIELD index doc_id document | 更新索引中 doc_id 指定的文档，若更新的字段为 mapping 指定的索引字段时，该字段更新的内容需与 mapping 指定的类型一致；若非索引字段，支持更新任意字段类型的内容。 说明 若更新的字段已存在，则更新原文档，若字段不存在，则新增该字段。若指定的文档不存在，该命令支持自动创建文档，此时效果等同于 TFT.ADDDOC。 |
| [TFT.DELDOCFIELD](tairsearch.md) | TFT.DE
