mapping 指定的类型一致；若非索引字段，支持更新任意字段类型的内容。 说明 若更新的字段已存在，则更新原文档，若字段不存在，则新增该字段。若指定的文档不存在，该命令支持自动创建文档，此时效果等同于 TFT.ADDDOC。 |
| [TFT.DELDOCFIELD](tairsearch.md) | TFT.DELDOCFIELD index doc_id field [field1 field2 ...] | 删除索引中 doc_id 指定文档的指定字段，若该字段为索引字段，会同时在索引中删除该字段的信息。 说明 若指定的字段不存在（例如被 _source 过滤的字段），则操作失败。 |
| [TFT.INCRLONGDOCFIELD](tairsearch.md) | TFT.INCRLONGDOCFIELD index doc_id field increment | 向索引中 doc_id 指定文档的指定字段增加整数值（increment），支持指定 increment 为负数，支持指定的字段类型为 long 或 int 类型。 说明 若指定的文档不存在，该命令支持自动创建文档，初始化字段的值为 0，并增加指定的 increment。若指定的字段不存在（例如被 _source 过滤的字段），则操作失败。 |
| [TFT.INCRFLOATDOCFIELD](tairsearch.md) | TFT.INCRFLOATDOCFIELD index doc_id field increment | 向索引中 doc_id 指定文档的指定字段增加浮点数值（increment），支持指定 increment 为负数，支持指定的字段类型为 double 类型。 说明 若指定的文档不存在，该命令支持自动创建文档，初始化字段的值为 0，并增加指定的 increment。若指定的字段不存在（例如被 _source 过滤的字段），则操作失败。 |
| [TFT.GETDOC](tairsearch.md) | TFT.GETDOC index doc_id | 获取索引中指定 doc_id 的文档内容。 |
| [TFT.EXISTS](tairsearch.md) | TFT.EXISTS index doc_id | 查询索引中指定 doc_id 的文档是否存在。 |
| [TFT.DOCNUM](tairsearch.md) | TFT.DOCNUM index | 获取索引中的文档数量。 |
| [TFT.SCANDOCID](tairsearch.md) | TFT.SCANDOCID index cursor [MATCH *value*] [COUNT count] | 获取索引中所有的 doc_id。 |
| [TFT.DELDOC](tair
