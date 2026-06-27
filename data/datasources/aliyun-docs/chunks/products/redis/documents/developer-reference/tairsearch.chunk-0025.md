## TFT.EXISTS

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.EXISTS index doc_id |
| 命令描述 | 查询索引中指定 doc_id 的文档是否存在。 |
| 选项 | index ：待查询的索引名称。 doc_id ：指定文档 ID。 |
| 返回值 | 执行成功： 若文档存在，返回 1。 若索引或文档不存在，返回 0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.EXISTS idx:product 00011 返回示例： (integer) 1 |
