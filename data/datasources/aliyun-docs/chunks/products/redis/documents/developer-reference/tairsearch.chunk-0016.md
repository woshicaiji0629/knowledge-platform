## TFT.UPDATEINDEX

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.UPDATEINDEX index mappings settings |
| 命令描述 | 向指定的索引中新增 properties 字段，或修改索引设置。 |
| 选项 | index ：待操作的索引名称。 mappings ：映射内容，仅输入新增的 properties 字段（无需输入 dynamic 、 _source 等信息），且新增的 properties 字段不能与原有字段冲突，否则会新增失败。 settings ：修改索引设置。仅支持修改 queries_cache 、 compress_doc 和 index 参数，其中 index 参数仅支持修改 BM25 算法中 k1 、 b 的值。 说明 mappings 和 settings 的语法请参见 [TFT.CREATEINDEX](tairsearch.md) 。 |
| 返回值 | 执行成功：返回 OK。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.UPDATEINDEX idx:product '{"mappings":{"properties":{"product_group":{"type":"text","analyzer":"chinese"}}}}' 返回示例： OK |
