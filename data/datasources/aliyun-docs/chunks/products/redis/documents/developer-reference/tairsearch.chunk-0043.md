## TFT.ADDSUG

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.ADDSUG index text weight [text weight] ... |
| 命令描述 | 在指定索引中，添加自动补全的文本及对应权重，支持添加多个文本。 |
| 选项 | index ：待操作的索引名称。 text ：自动补全文本。 weight ：对应文本的计分权重，范围为正整数。 |
| 返回值 | 执行成功：返回成功添加的文档数量。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.ADDSUG idx:redis 'redis is a memory database' 3 'redis cluster' 10 返回示例： (integer) 2 |
