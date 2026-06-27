## TFT.DELSUG

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.DELSUG index text [text] ... |
| 命令描述 | 在指定索引中，删除自动补全的文本，支持删除多个文本。 |
| 选项 | index ：待查询的索引名称。 text ：待删除的文本，需指定完整、正确的文本。 |
| 返回值 | 执行成功：返回成功删除的文本数量。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.DELSUG idx:redis 'redis is a memory database' 'redis cluster' 返回示例： (integer) 2 |
